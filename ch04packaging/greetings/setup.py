
from setuptools import setup, find_packages

setup(
    name = "Greetings",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    scripts = ['scripts/greet'],
    install_requires = ['argparse']
)