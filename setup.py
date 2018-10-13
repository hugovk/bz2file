from distutils.core import setup

with open("README.rst") as f:
    readme = f.read()

setup(
    name="bz2file",
    version="0.98",
    description="Read and write bzip2-compressed files.",
    long_description=readme,
    author="Nadeem Vawda",
    author_email="nadeem.vawda@gmail.com",
    url="https://github.com/nvawda/bz2file",
    py_modules=["bz2file"],
    license="Apache License, Version 2.0",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Compression",
    ],
)
