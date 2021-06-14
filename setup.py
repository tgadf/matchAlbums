from distutils.core import setup
import setuptools

setup(
  name = 'matchAlbums',
  py_modules = ['matchAlbums'],
  version = '0.0.1',
  description = 'A Python Wrapper To Parse Music Chart Data',
  long_description = open('README.md').read(),
  author = 'Thomas Gadfort',
  author_email = 'tgadfort@gmail.com',
  license = "MIT",
  url = 'https://github.com/tgadf/matchAlbums',
  keywords = ['music'],
  classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Utilities'
  ],
  install_requires=['utils==0.0.1'],
  dependency_links=[]
)
 
