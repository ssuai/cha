from setuptools import setup, find_packages

setup(
    name="cha-parser",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pandas>=1.5.0"],
    author="ssuai",
    description="CLAN's CHA file parser",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ssuai/cha",
    license="MIT",
)

