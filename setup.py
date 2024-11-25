from setuptools import setup, find_packages

setup(
    name="fastapi_class_views",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pydantic",
    ],
    author="Your Name",
    author_email="mitubhatt670@gmail.com",
    description="A library for class-based views in FastAPI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fastapi_class_views",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)