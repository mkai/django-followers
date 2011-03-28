from setuptools import setup

setup(name='django-simple-follower',
      version='0.1',
      description="Simple Django follower/ following implementation taken and adapted from ericflo's starkthedark project.",
      long_description="",
      author='Markus Kaiserswerth',
      author_email='mkai@sensun.org',
      license='GPL',
      packages=['simple_follower'],
      zip_safe=False,
      install_requires=['django'],
)
