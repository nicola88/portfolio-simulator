
from setuptools import setup, find_packages
from pfsim.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='pfsim',
    version=VERSION,
    description='Simulate an investment portfolio based on an asset allocation',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Nicola Moretto',
    author_email='nicolamoretto88@gmail.com',
    url='https://github.com/nicola88/portfolio-simulator',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'pfsim': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        pfsim = pfsim.main:main
    """,
)
