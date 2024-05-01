from setuptools import setup, find_packages

setup(
    name='nmfspalettepy',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy', 'matplotlib'
    ],
    author='Michael Akridge',
    description='NMFS color palettes handling library in Python'
)
