from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest==7.4.0",
        "flask==3.0.0",
    ],
    entry_points={
        "console_scripts": [
            "my_project=my_project.main:main",
        ],
    },
)