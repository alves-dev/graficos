from setuptools import setup
from constants import VERSION_GRAPHICS

setup(name='graficos',
      version=VERSION_GRAPHICS,
      description='Geração de graficos',
      url='https://github.com/alves-dev/graficos',
      author='Igor Moreira',
      author_email='alvesmoreiraigor@gmail.com',
      license='MIT',
      packages=['files', 'graphics', 'main', 'my_time', 'netflix', 'validations', 'utility'],
      zip_safe=False)
