from setuptools import setup

setup(
    name="perceptive",
    version="1.1",
    description="perceptive of life througth the terminal ",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libperceptive"],
    scripts="perceptive",
    package_data={"libperceptive": ["content/*"]},
)