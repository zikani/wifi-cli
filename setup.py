from setuptools import setup, find_packages

setup(
    name='wifi_manager',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # List dependencies here if any
    entry_points={
        'console_scripts': [
            'wifi-cli=cli.cli:main',  # This specifies the CLI entry point
        ],
    },
    python_requires='>=3.6',
)
