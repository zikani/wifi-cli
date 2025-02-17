from setuptools import setup, find_packages

setup(
    name='wifi_manager',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'scapy',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'wifi-cli=cli.cli:main',
        ],
    },
    python_requires='>=3.6',
    package_data={
        'wifi_manager': ['config.json'],
    },
    include_package_data=True,
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI tool for managing Wi-Fi connections on Windows',
    url='https://github.com/zikani/wifi-cli',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
)
