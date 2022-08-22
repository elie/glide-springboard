#!/usr/bin/env python


from setuptools import setup

setup(
    name='Glide springboard',
    version='1.5.0',
    description='springboard themes for Glide.',
    author='Joel Burton',
    author_email='joel@joelburton.com',
    url='https://github.com/joelburton/glide-springboard',
    packages=['glide_springboard'],
    install_requires=["glide"],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'revealjs-springboard = glide_springboard',
            'handouts-springboard = glide_springboard',
        ],
    },
)
