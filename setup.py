import setuptools


with open('README.md') as fp:
    long_description = fp.read()


setuptools.setup(
    name='django_injector',
    version='0.0.1',
    author='Tiemo Kieft',
    author_email='pypi@isogram.nl',
    description='Integrate injector with Django',
    long_description=long_description,
    url='https://github.com/blubber/django_injector',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)
