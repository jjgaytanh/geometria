from setuptools import setup, find_packages

def module_path():
    import sys
    import os
    if (hasattr(sys, "frozen")):
        return os.path.dirname(sys.executable)
    if os.path.dirname(__file__) == "":
        return "."
    return os.path.dirname(__file__)

dir_path = module_path()
long_description_file = dir_path + "/README.md"
setup(name='geometria',
    version='1.3',
    url=None,
    license=None,
    author='Juan Jose Gaytan Hernandez Magro',
    author_email='juan.jose.gaytan@tec.mx',
    description='This library has classes that represent geometric shapes (prepared for educational purposes).',
    packages=find_packages(exclude=['tests']),
    long_description=open(long_description_file).read())
