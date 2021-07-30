from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name="helloworld",
    version="0.0.1.dev0",
    description="Hello World command line.",
    author="A.suzuki",
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        "console_scripts": [
            "helloworld-cli=helloworld.main:main",
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ]
)
