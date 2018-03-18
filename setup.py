from setuptools import setup, find_packages

setup(
    name='libdistrict',
    version='0.1.0',
    description='Library of common metrics used to evaluate district plans',
    author='PlanScore',
    author_email='info@planscore.org',
    url='https://github.com/PlanScore/libdistrict',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    test_suite='tests',
)
