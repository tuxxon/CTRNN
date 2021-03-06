from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='CTRNN',
    version='1.0',
    description='A package that implements Continuous Time Recurrent Neural Networks',
    long_description=readme,
    author='Madhavun Candadai',
    author_email='madvncv@gmail.com',
    url='https://github.com/madvn/CTRNN',
    license=license,
    packages=['CTRNN'],
    install_requires=['numpy','scipy']
)
