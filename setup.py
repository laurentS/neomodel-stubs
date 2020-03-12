from distutils.core import setup

setup(
    name="neomodel-stubs",
    author="Laurent Savaete <laurent@where.tf>",
    version="0.1.0",
    package_data={"neomodel-stubs": ["*.pyi"]},
    packages=["neomodel-stubs"]
)
