from setuptools import find_packages, setup

setup(
    name='alemanpyutils',
    packages=find_packages(),
    version='0.0.2',
    description='alemanpyutils',
    author='Alejandro Alemán',
    license='',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests'


)

