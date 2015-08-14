import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-luoji-accounts',
    version='0.1.0',
    # packages=find_packages(),
    packages=['accounts', 'accounts.migrations', 'accounts.fixtures'],
    package_data={
        '': ['*.json'],
    },
    # include_package_data=True,
    license='BSD License',
    description='A general account app for projects.',
    long_description=README,
    url='https://github.com/hereischen/django-luoji-accounts',
    author='Haotong Chen',
    author_email='hereischen@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
