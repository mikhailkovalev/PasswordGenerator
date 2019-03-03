import os.path
from setuptools import setup, find_packages


def read(filename):
    try:
        return open(os.path.join(
            os.path.dirname(__file__),
            filename
        )).read()
    except IOError:
        return ''


setup(
    name='password-generator',
    version='0.1',
    description=read('DESCRIPTION'),
    long_description=read('README'),
    url='https://github.com/mikhailkovalev/PasswordGenerator.git',
    author='Mikhail Kovalev',
    author_email='mixon271@gmail.com',
    license='None',
    packages=find_packages(),
    zip_safe=False
)
