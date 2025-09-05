from setuptools import setup, find_packages

setup(
    name="BLOGEN_AI",
    version="0.1.0",
    author="Vignesh R",
    author_email="mail2vikivignesh06@gmail.com",
    description="A Python library to generate blog posts from topics",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/VIGNESH-R-06/BLOGEN_AI",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv",
        "mistralai"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
