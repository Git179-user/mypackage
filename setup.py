from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1.0",
    packages=find_packages(exclude=['tests*']),
    description= 'EDSA example python package',
    author="Charles Kyalo",
    author_email="kyalocharles179@gmail.com",
    url="https://github.com/Git179-user/mypackage",
    install_requires=[
        # List your dependencies here, e.g.:
        "numpy>=1.20.0",
        "pandas>=1.3.0",
    ],
    python_requires=">=3.6",
)



