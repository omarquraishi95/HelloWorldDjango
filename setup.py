#Setup Python File
from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),


setup(
    author="Omar Quraishi",
    author_email="https://github.com/omarquraishi95/HelloWorldDjango",
    maintainer='Omar Quraishi',
    maintainer_email='https://github.com/omarquraishi95/HelloWorldDjango',
    name='HelloWorld',
    version='0.1',
    description='Week 6 Django HelloWorld Assignment ',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/omarquraishi95/HelloWorldDjango',
    license='GPL',
    platforms=['OS Independent'],
    install_requires=[
        'Django==1.10.5',
    ],
    packages=find_packages(exclude=["project","project.*"]),
    include_package_data=True,
    zip_safe = False
)
