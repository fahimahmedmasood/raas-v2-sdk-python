from setuptools import setup, find_packages

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='raas',
    version='2.2.0',
    description='With this RESTful API you can integrate a global reward or incentive program into your app or platform. If you have any questions or if you\'d like to receive your own credentials, please contact us at devsupport@tangocard.com.',
    long_description=long_description,
    author='APIMatic SDK Generator',
    author_email='support@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'jsonpickle>=0.7.1, <1.0',
        'cachecontrol>=0.11.7, <1.0'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)
