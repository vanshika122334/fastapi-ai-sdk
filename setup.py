"""Setup configuration for fastapi-ai-sdk package."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fastapi-ai-sdk",
    version="0.1.0",
    author="Arif Dogan",
    author_email="me@arif.sh",
    description="FastAPI helper library for Vercel AI SDK backend implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doganarif/fastapi-ai-sdk",
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Framework :: FastAPI",
        "Typing :: Typed",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.115.0",
        "pydantic>=2.9.0",
        "typing-extensions>=4.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.0",
            "pytest-asyncio>=0.24.0",
            "pytest-cov>=5.0.0",
            "black>=24.10.0",
            "isort>=5.13.0",
            "flake8>=7.1.0",
            "mypy>=1.13.0",
            "httpx>=0.27.0",
            "uvicorn>=0.32.0",
            "ruff>=0.7.0",
        ],
        "examples": [
            "uvicorn>=0.32.0",
            "python-multipart>=0.0.12",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/doganarif/fastapi-ai-sdk/issues",
        "Source": "https://github.com/doganarif/fastapi-ai-sdk",
    },
    keywords="fastapi vercel ai sdk streaming sse llm",
)
