from setuptools import setup

setup(name='django-followers',
      version='0.21',
      description="Simple follow/ unfollow implementation for users, adapted from ericflo's starkthedark project.",
      long_description="",
      author='Markus Kaiserswerth',
      author_email='mkai@sensun.org',
      license='GPL',
      packages=['followers'],
      zip_safe=False,
      install_requires=['django'],
)
