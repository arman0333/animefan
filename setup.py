from setuptools import setup, find_packages

setup(
    name='anime-cli',
    version='1.0.0',
    description='A CLI tool for anime quotes and ASCII art',
    author='Arman Sethi',
    author_email='armansethi64@gmail.com',
    url='https://github.com/yourusername/anime-cli',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',    
        'pyfiglet',
    ],
    entry_points={
        'console_scripts': [
        'anime-cli=libanime:_init_.py'
        ],
    },
)
