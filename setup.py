from setuptools import setup, find_packages



setup(
	    name='punch',
	    version='0.1',
	    packages=find_packages(),
	    install_requires=['selenium','argparse'],
	author='Ori Zerah',
	author_email='orizerahmc@gmail.com',
	description='Punch CLI',
	entry_points={
		'console_scripts': [
			'punch=punch.cli:main'
		]
	}
)

