import os
from distutils.core import setup

from setuptools import find_packages

setup(
    name='ebi_eva_internal_pyutils',
    scripts=[os.path.join(os.path.dirname(__file__), 'ebi_eva_internal_pyutils', 'archive_directory.py')],
    packages=find_packages(),
    version='0.1.0.dev0',
    license='Apache',
    description='EBI EVA - Python Utilities for internal use',
    url='https://github.com/EBIVariation/eva-internal-pyutils',
    keywords=['EBI', 'EVA', 'PYTHON', 'UTILITIES'],
    install_requires=['lxml', 'pymongo', 'pyyaml', 'retry', 'psycopg2-binary', 'ebi_eva_common_pyutils'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ]
)
