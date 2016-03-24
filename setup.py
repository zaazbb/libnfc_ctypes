from distutils.core import setup
import libzbar
setup(
    name='libnfc',
    description='Python ctypes libnfc wrapper',
    provides=['zbar'],
    requires=[],
    long_description=
    """
    This package is a python ctypes wrapper for the libnfc api 
    """,
    version=libzbar.version,
    packages=['libnfc'],
    package_dir={'libnfc': './libnfc'},
    url='https://github.com/zaazbb/libnfc_ctypes',
    author='zaazbb',
    author_email='zaazbb@163.com',
    platforms='Linux',
    license='GNU Library or Lesser General Public License (LGPL)'
)
