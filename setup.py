from setuptools import find_packages, setup

setup(name='pyminyus',
      version='0.0.2',
      author='Yusuke Minami',
	  author_email='contactme@minyus.github.com',
	  license='MIT',
	  description='Python utility.',
	  url='https://github.com/Minyus/pyminyus',
      packages=find_packages(),
	  install_requires=[
      ],
	  keywords='minyus',
	  zip_safe=False,
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent"
      ])
