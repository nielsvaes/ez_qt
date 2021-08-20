from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ez_qt',
    version='1.1.2',
    packages=['ez_qt'],
    url='https://www.github.com/nielsvaes/ez_qt',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Niels Vaes',
    author_email='nielsvaes@gmail.com',
    description='Helper functions and classes to work with PySide2/PyQt5'
)
