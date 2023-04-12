import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = lib_folder + '/requirements.txt'
install_requires = [] # Here we'll get: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()



setuptools.setup(
    name="auxiliary_functions",
    version="0.1.0",
    author="Olavo Barros",
    author_email="olavo.barros@ufv.br",
    description="Lib with auxiliary functions for general proposes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Olavo-B/BDD_random_forest.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires
)