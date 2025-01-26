import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Gautam-102203061",
    version="1.0.0",
    description="TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making method that ranks alternatives based on their closeness to the ideal solution.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/uditvashisht/saral-square",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "square=square.__main__:main",
        ]
    },
)