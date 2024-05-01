from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nmfspalettepy',
    version='0.1.4',
    description='NMFS color palettes handling library',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    packages=['nmfspalettepy'],
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    author='Michael Akridge'
)

