from setuptools import find_packages, setup
setup(
    name='mlwlib',
    packages=find_packages(),
    version='0.1.0',
    description='MLW functions library',
    author='SAG',
    license='MIT',
    install_requires=["pandas"],
    test_suite='tests',
)