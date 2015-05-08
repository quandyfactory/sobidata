from distutils.core import setup

version = '0.4.1'

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name = 'sobidata',
    version = version,
    description = 'Downloads your Social Bicycles route data.',
    long_description = long_description,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'LICENCE.txt',
    url = 'https://github.com/quandyfactory/sobidata',
    py_modules = ['sobidata'],
    install_requires = [
        'dicttoxml',
        'openpyxl',
        'requests'
    ],
    download_url = 'https://pypi.python.org/packages/source/s/sobidata/sobidata-%s.tar.gz?raw=true' % (version),
    platforms='Cross-platform',
    classifiers=[
      'Programming Language :: Python',
    ],
)

