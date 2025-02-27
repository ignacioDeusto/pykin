from setuptools import setup, find_packages

# read the contents of your README file
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    lines = f.readlines()

# remove images from README
lines = [x for x in lines if ".png" not in x]
long_description = "".join(lines)

setup(
    name="pykin",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "numpy",
        "matplotlib",
        "trimesh[easy]",
        "pyglet",
        "tqdm",
        "pyyaml",
        "python-fcl",
        "Pillow",
    ],
    eager_resources=["*"],
    include_package_data=True,
    python_requires=">=3",
    description="Robotics Kinematics Library",
    author="Daejong Jin, Youngtaek Hong, Juhan Park",
    url="https://github.com/jdj2261/pykin.git",
    download_url="https://github.com/jdj2261/pykin/archive/refs/heads/main.zip",
    author_email="wlseoeo@gmail.com",
    version="1.6.0" ,
    long_description=long_description,
    long_description_content_type="text/markdown",
)

# python setup.py sdist bdist_wheel
# twine upload --skip-existing dist/*
