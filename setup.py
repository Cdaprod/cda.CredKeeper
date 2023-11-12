from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='CredKeeper',
    version='1.0.0',
    author='David Cannan',
    author_email='Cdaprod@Cdaprod.dev',
    description='A Python package for managing various credentials securely, with API access.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/CredKeeper',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi>=0.68.0',
        'pydantic>=1.8.2',
        'sqlalchemy>=1.4.22',
        'cryptography',
        'httpx',
        # Add any additional packages needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)