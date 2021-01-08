
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ez-utils',
    version='1.0.0',
    packages=['tangle'],
    url='https://www.github.com/nielsvaes/ez_utils',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Niels Vaes',
    author_email='nielsvaes@gmail.com',
    description='Some super simple one-liners to do common Python tasks'
)
