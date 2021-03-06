"""
Build tnseq_yeast.
"""

from setuptools import setup

# requirements = [line.strip() for line in open('requirements.txt')]

setup(
    name = 'tnseq_yeast',
    version = '0.3', #versioneer.get_version(),
    author = 'Jim Chu',
    author_email = 'biojxz@163.com',
    url = 'https://tnseq_yeast.readthedocs.io/',
    description = 'trim adapters from high-throughput sequencing reads',
    license = 'MIT',
    #cmdclass = cmdclass,
    #ext_modules = extensions,
    packages = ['tnseq_yeast', 'tnseq_yeast.scripts'],
    scripts = ['bin/tnseqy'],
    install_requires=[
        'cutadapt>=1.10',
        'PyYAML>=3.11',
        'numpy>=1.9.1',
        'pandas>=0.17.1',
        'pyfaidx>=0.2.7',
        'click>=2.0',
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)
