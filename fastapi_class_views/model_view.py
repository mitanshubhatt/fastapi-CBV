from fastapi import Request, HTTPException
from pydantic import BaseModel
from fastapi_class_views.base_view import BaseView
from fastapi.responses import JSONResponse
from typing import Any, Type, List, Optional, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql.expression import and_


class ModelView(BaseView):
    model: Type[BaseModel] = None
    db_model: Any = None  # SQLAlchemy model for database queries
    db_session: Optional[AsyncSession] = None  # Database session for ORM queries

    def __init__(self, request: Request, response_class=JSONResponse, db_session: Optional[AsyncSession] = None):
        super().__init__(request, response_class)
        self.db_session = db_session
        if not self.model or not self.db_model:
            raise ValueError("ModelView must define both 'model' and 'db_model' attributes")

    async def serialize(self, data: Any) -> Any:
        """
        Serialize data to a dict. Handles both ORM objects and plain data.
        """
        if isinstance(data, list):
            return [self.model.from_orm(item).dict() for item in data]
        elif isinstance(data, self.db_model):
            return self.model.from_orm(data).dict()
        return data

    async def apply_filters(self, query, filters: Dict[str, Any]) -> Any:
        """
        Automatically apply filters to a SQLAlchemy query based on the incoming parameters.
        """
        filter_conditions = []
        for field, value in filters.items():
            if hasattr(self.db_model, field):
                db_field = getattr(self.db_model, field)
                filter_conditions.append(db_field == value)

        if filter_conditions:
            query = query.where(and_(*filter_conditions))
        return query

    async def get_queryset(self, filters: Dict[str, Any]) -> List[Any]:
        """
        Retrieve the base queryset and apply filters automatically.
        """
        query = select(self.db_model)
        query = await self.apply_filters(query, filters)

        async with self.db_session as session:
            result = await session.execute(query)
            return result.scalars().all()

    async def get_object(self, id: int, *args, **kwargs) -> Any:
        """
        Retrieve a single object by ID.
        """
        query = select(self.db_model).where(self.db_model.id == id)
        async with self.db_session as session:
            result = await session.execute(query)
            obj = result.scalar_one_or_none()
            if not obj:
                raise HTTPException(status_code=404, detail="Object not found")
            return obj

    async def get(self, *args, **kwargs):
        """
        Retrieve a filtered list of objects based on query parameters.
        """
        filters = dict(self.request.query_params)
        queryset = await self.get_queryset(filters)
        serialized_data = await self.serialize(queryset)
        return self.response_class(content=serialized_data)

    async def retrieve(self, id: int, *args, **kwargs):
        obj = await self.get_object(id, *args, **kwargs)
        serialized_data = await self.serialize(obj)
        return self.response_class(content=serialized_data)
