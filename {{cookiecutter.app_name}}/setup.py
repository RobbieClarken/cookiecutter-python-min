from setuptools import setup
import re

with open('{{cookiecutter.app_name}}/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='{{cookiecutter.app_name}}',
    version=version,
    description='{{cookiecutter.description}}',
    long_desciption=readme,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license='MIT',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    packages=['{{cookiecutter.app_name}}'],
    install_requires=[],
    entry_points={'console_scripts': []},
)
