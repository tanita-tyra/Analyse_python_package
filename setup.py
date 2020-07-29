from setuptools import setup, find_packages

setup(
    name = 'Analyse_python_package',
    version = '0.1',
    packages = find_packages(),
    license = 'MIT',
    description = 'EDSA Analyse Python Package ',
    longer_description = open('README.md') .read(),
    install_requires = ['numpy','pandas'],
    url = 'https://github.com/<username>/<package-name>',
    author = 'Tanita Lakram',
    author_email = 'lakramtanita9@gmail.com'
)

