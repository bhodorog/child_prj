from setuptools import setup, find_packages

setup(
    name="child",
    version="0.1",
    install_requires=["requests >= 1.1.0", ],
    packages=find_packages(),
)

