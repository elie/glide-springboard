#!/usr/bin/env python


from setuptools import setup

setup(name='Glide Springboard',
      version='1.1',
      description='Springboard themes for Glide.',
      author='Elie Schoppik',
      author_email='eschoppik@gmail.com',
      url='https://github.com/elie/glide-springboard',
      packages=['glide_springboard'],
      install_requires=["glide"],
      include_package_data=True,
     )
