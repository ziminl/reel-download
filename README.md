# reel-download
pip of reel download server



# Usage :

`from DownloadReels import host`



#comments for remind

# setup.py
> pip install setuptools

setup.py

```
import setuptools

with open("README.md", "r") as www:
    long_description = www.read()

setuptools.setup (
    name = '<name>',
    version = '<version>',
    license = '<license>',
    py_modules = ['<py_modules>'],
    description = '<description>',
    author = '<author>',
    author_email = '<author_email>',
    url = '<url>',
    packages = setuptools.find_packages(),
    classifiers = [        "Programming Language :: Python :: 3",
        "License :: MIT License"
    ],
)
```

# pack with wheel and upload 

register https://pypi.org/

> pip install wheel, twine
> apt install twine
> twine upload dist/<file>.whl

