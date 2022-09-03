from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'A package to help developers build front end user interfaces for machine learning models.'
LONG_DESCRIPTION = 'A package to help developers build front end user interfaces for machine learning models.'

# Setting up
setup(
    name="django-machine-learning-user-interface",
    version=VERSION,
    author="Phikolomzi Gugwana",
    author_email="<ggwphi001@myuct.ac.za>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'django', 'machine learning', 'user interface'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)