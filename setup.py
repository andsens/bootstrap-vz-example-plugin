from setuptools import setup
from setuptools import find_packages
import os.path


def find_version(path):
	import re
	version_file = open(path).read()
	version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
	if version_match:
		return version_match.group(1)
	raise RuntimeError("Unable to find version string.")

setup(name='example-plugin',
      version=find_version(os.path.join(os.path.dirname(__file__), 'example/__init__.py')),
      packages=find_packages(),
      include_package_data=True,
      entry_points={'bootstrapvz.plugins': ['example = example']},
      install_requires=['bootstrap-vz >= 0.9.5'],
      license='Apache License, Version 2.0',
      description='An example plugin for bootstrap-vz',
      long_description='''This package showcases the external plugin architecture for bootstrap-vz''',
      author='Anders Ingemann',
      author_email='anders@ingemann.de',
      url='http://www.github.com/andsens/bootstrap-vz-example-plugin',
      )
