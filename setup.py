from setuptools import setup, find_packages
import os

LONG_DESCRIPTION = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    author="Omar Quraishi",
    author_email="https://github.com/omarquraishi95/HelloWorldDjango",
    maintainer='Omar Quraishi',
    maintainer_email='https://github.com/omarquraishi95/HelloWorldDjango',
    name='helloworld',
    version='0.1',
    description='Week 6 Django helloworld Assignment ',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/omarquraishi95/HelloWorldDjango',
    license='GPL',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django==1.10.5',
    ],
    packages=find_packages(exclude=["project","project.*"]),
    include_package_data=True,
    zip_safe = False
)
