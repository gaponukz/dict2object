import setuptools

with open("README.md", "r") as out:
	long_description = out.read()

setuptools.setup(
	name="dict2object-gaponukz",
	version="0.0.2",
	author="Eugene Gaponyuk",
	author_email="gaponukz54@gmail.com",
	description="Convert dict to (js)object",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/gaponukz/dict2object",
	packages=setuptools.find_packages(),
    
	classifiers=[
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.8',
)