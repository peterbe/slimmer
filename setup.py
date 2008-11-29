from setuptools import setup, find_packages
import sys, os

import slimmer
version = slimmer.__version__ # hate repeating myself

README = os.path.join(os.path.dirname(__file__), 'README.txt')
long_description = open(README).read().strip() + "\n\n"


setup(name='slimmer',
      version=version,
      description="HTML,XHTML,CSS,JavaScript optimizer",
      long_description=long_description,
      keywords='slimmer optimizer optimiser whitespace',
      author='Peter Bengtsson',
      author_email='peter@fry-it.com',
      url='http://www.fry-it.com',
      download_url='http://pypi.python.org/pypi/slimmer/',
      license='Python',
      classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],      
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      test_suite='slimmer.tests',
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
