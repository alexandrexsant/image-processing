from setuptools import setup find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

 setus(
name=" image processing”,
version="0.0.1",
author="Alexandre”,
description="Image Processing Package using Skimage",
long_description=page_description,
long_description_content_type="text/markdown",
url="https://github.con/alexandrexsant/image-processing-package”
packages=find_packages(),
install_requires=-requirements,
python_requires= '>=3.5',
)  
 