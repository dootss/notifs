from setuptools import setup, find_packages

setup(
    name='notifs',
    version='0.1.0',
    description='Customizable notification system for terminal output',
    author='doot',
    author_email='doot@waifu.club',
    packages=find_packages(),
    install_requires=[
        'colorama',
    ],
)
