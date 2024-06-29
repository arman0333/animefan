from setuptools import setup, find_packages

setup(
    name="anime",
    version="1.1",
    description="Glimpse of Anime through the terminal",
    long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    author="Arman Sethi",  
    author_email="armansethi64@gmail.com",  
    url="https://github.com/arman0333/anime-cli", 
    license="MIT",
    packages=find_packages(),  
    install_requires=[
        'click',  
    ],
    entry_points={
        'console_scripts': [
            'anime=libanime.cli:main', 
        ],
    },
    package_data={
        "libanime": ["content/*"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
