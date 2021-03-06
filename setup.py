from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
        Extension("bigfile.pyxbigfile", ["bigfile/pyxbigfile.pyx"],
            include_dirs = ["src/", numpy.get_include()])]

def find_version(path):
    import re
    # path shall be a plain ascii text file.
    s = open(path, 'rt').read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              s, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")

setup(
    name="bigfile",
    version=find_version("bigfile/version.py"),
    author="Yu Feng",
    author_email="rainwoodman@gmail.com",
    url="http://github.com/rainwoodman/bigfile",
    description="python binding of BigFile, a peta scale IO format",
    zip_safe = False,
    package_dir = {'bigfile': 'bigfile'},
    install_requires=['cython', 'numpy'],
    packages= ['bigfile', 'bigfile.tests'],
    requires=['numpy'],
    ext_modules = cythonize(extensions)
)
