from setuptools import setup
import re

with open('{{cookiecutter.app_name}}/__init__.py', 'r') as f:
    version = re.search(r"__version__ = '(.*)'", f.read()).group(1)

setup(
    name='{{cookiecutter.app_name}}',
    version=version,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.app_name}}',
    packages=['{{cookiecutter.app_name}}'],
    install_requires=[
    ],
)
