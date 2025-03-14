#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="fib_Him10Agr_rs.py",
    version="0.1",
    rust_extensions=[RustExtension(
        ".src.lib.fib_rs",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["fib_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating Sysyem :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    zip_safe=False,
)