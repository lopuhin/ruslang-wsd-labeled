import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='rl_wsd_labeled',
    version='0.1.1',
    license='MIT',
    packages=['rl_wsd_labeled'],
    url='https://github.com/lopuhin/ruslang-wsd-labeled/',
    include_package_data=True,
    author='Konstantin Lopuhin',
    author_email='kostia.lopuhin@gmail.com',
    description='Labeled contexts of Russian polysemous words',
    long_description=read('README.rst'),
    zip_safe=False,
    package_data={
        'rl_wsd_labeled': [
            '*/*/*.txt',
            '*/*/*.json',
        ],
    },
)
