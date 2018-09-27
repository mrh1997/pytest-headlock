import pytest
from headlock.testsetup import TestSetup, CModule


TEST_INVALID_TESTSETUP = False


@CModule('file_ok.c')
class TSOk(TestSetup):
    pass

@CModule('file_ok.c', FUNCNAME="func2", RET_VAL=456)
class TS2Ok(TestSetup):
    pass

@pytest.fixture
def ts():
    with TSOk() as ts:
        yield ts

@pytest.fixture
def ts_err():
    with TSErr() as ts:
        yield ts


def test_writeCMakeFileOk():
    with TSOk() as ts:
        assert ts.func() == 123

def test_writeCMakeFile2Ok():
    with TSOk() as ts, TS2Ok() as ts2:
        assert ts.func() == 123
        assert ts2.func2() == 456


@pytest.mark.xfail
def test_writeCMakeFileErr(ts):
    @CModule('file_err.c')
    class TSErr(TestSetup):
        pass
