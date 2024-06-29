from setuptools import setup

setup(
    name="anime",
    version="1.1",
    description="Glimpse of Anime through the terminal",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libanime"],
    scripts=["anime"], 
    package_data={"libanime": ["content/*"]},  
)
