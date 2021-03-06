from setuptools import setup

setup(name='myPyPkg',
      version='0.1.3',
      description='A minimalistic python package',
      url='http://github.com/Accio/2017-11-pythonPackaging',
      author='Jitao David Zhang',
      author_email='davidvonpku@gmail.com',
      license='GPL-3',
      packages=['myPyPkg'],
      scripts=['bin/joke.py', 'bin/pythagorean.py'],
      zip_safe=False)
