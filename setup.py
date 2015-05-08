from distutils.core import setup

version = '0.4.4'

long_description = ''
try:
    with open('README.md') as readme:
        # load long_description into memory
        long_description = readme.read()
        # save README (no extension) for pypi
        with open('README', 'w') as myfile:
            myfile.write(long_description)
except IOError:
    with open('README') as readme:
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

