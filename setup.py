from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openmanus",
    version="0.1.0",
    author="mannaandpoem and Mirai Team",
    author_email="Mirai@gmail.com",
    description="A versatile agent that can solve various tasks using multiple tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mirai-terminal",
    packages=find_packages(),
    install_requires=[
        "pydantic~=2.10.4",
        "openai~=1.58.1",
        "tenacity~=9.0.0",
        "pyyaml~=6.0.2",
        "loguru~=0.7.3",
        "numpy",
        "datasets~=3.2.0",
        "html2text~=2024.2.26",
        "gymnasium~=1.0.0",
        "pillow~=10.4.0",
        "browsergym~=0.13.3",
        "uvicorn~=0.34.0",
        "unidiff~=0.7.5",
        "browser-use~=0.1.40",
        "googlesearch-python~=1.3.0",
        "aiofiles~=24.1.0",
        "pydantic_core~=2.27.2",
        "colorama~=0.4.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "Skyai=main:main",
        ],
    },
)
