from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qt_ez',
    version='1.0',
    packages=['ez_qt'],
    url='www.github.com/nielsvaes/ez_qt',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    author='Niels Vaes',
    author_email='nielsvaes@gmail.com',
    description='Helper functions and classes to work with PySide2/PyQt5'
)