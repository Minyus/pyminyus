from setuptools import find_packages, setup

import pyminyus

setup(name='pyminyus',
      version='0.0.1',
      author='Yusuke Minami',
	  license='MIT',
	  description='Python utility.',
	  url='https://github.com/Minyus/pyminyus',
      packages=find_packages(),
	  install_requires=[
      ],
	  keywords='minyus',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
      ])
