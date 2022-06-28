from setuptools import find_packages, setup
setup(
    name='mlwlib',
    packages=find_packages(),
    version='1.0.0',
    description='MLW functions library',
    author='Software AG',
    install_requires=["pandas"],
    test_suite='tests',
)