from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pyawabi",
    version="0.2",
    rust_extensions=[RustExtension("pyawabi.awabi", binding=Binding.PyO3)],
    packages=["pyawabi"],
    zip_safe=False,
)
