import os
from setuptools import setup, find_packages

def read_requirements():
    filepath = os.path.join("requirements", "requirements.in")
    with open(filepath, "r") as file:
        return file.read().splitlines()

setup(
    name="fastapi_class_views",
    version="0.1.0",
    packages=find_packages(),
    install_requires=read_requirements(),
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