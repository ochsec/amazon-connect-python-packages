from setuptools import setup, find_packages

setup(
    name='connect-packages',
    version='1.0.0',
    author='Christopher Ochsenreither',
    author_email='cochsenreither@protonmail.com',
    description='Packages for Amazon Connect scripts and lambdas',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ochsec/amazon-connect-python-packages',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'pg8000',
        'dotenv'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',  # Target audience
        'License :: OSI Approved :: MIT License',  # License
        'Programming Language :: Python :: 3',  # Supported Python versions
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6',  # Minimum version requirement of Python
)