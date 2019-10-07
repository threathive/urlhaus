import codecs
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def get_version():
    return re.search(r"""__version__\s+=\s+(?P<quote>['"])(?P<version>.+?)(?P=quote)""", open('urlhaus/__init__.py').read()).group('version')


setup(name             = "urlhaus",
      version          = get_version(),
      author           = "Adam",
      author_email     = "adam@threathive.com",
      url              = "https://github.com/threathive/urlhaus",
      description      = "Simple api client for urlhaus.",
      long_description = codecs.open("README.md", encoding="utf-8").read(),
      install_requires = [
      ],
      extras_require = {
      },

      packages         = ['urlhaus'],
      classifiers      = [
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.5",
      ]
)


