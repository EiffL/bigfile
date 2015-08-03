
from bigfile import BigFile
from bigfile import BigBlock
import tempfile
import numpy
import shutil
from numpy.testing import assert_equal

dtypes = [
    'i4', 
    'u4', 
    'u8', 
    'f4', 
    'f8', 
    ('f4', 1),
    ('f4', 2), 
]

def test_create():
    fname = tempfile.mkdtemp()
    x = BigFile(fname, create=True)
    for d in dtypes:
        d = numpy.dtype(d)
        numpy.random.seed(1234)

        # test creating
        with x.create(d.str, Nfile=1, dtype=d, size=128) as b:
            shape = [ b.size ] + list(d.shape)
            data = numpy.random.uniform(99999, size=shape)
            b.write(0, data)

        with x[d.str] as b:
            assert_equal(b[:], data.astype(d.base))

        # test writing with an offset
        with x[d.str] as b:
            b.write(1, data[0:1])
            assert_equal(b[1:2], data[0:1].astype(d.base))

    assert set(x.blocks) == set([numpy.dtype(d).str for d in dtypes])
    shutil.rmtree(fname)