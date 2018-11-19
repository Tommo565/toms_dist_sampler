from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='toms-dist-sampler',
    version='0.1',
    description=(
        'A distribution sampler for Normal, Poisson and Binomial'
        'distributions'
    ),
    url='https://github.com/Tommo565/distribution-sampler',
    author='Flying Circus',
    author_email='tomewing1979@yahoo.co.uk',
    license='MIT',
    packages=['toms_dist_sampler'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License ::  MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Statistics :: Data Science',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
