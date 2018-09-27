import pytest
from headlock.testsetup import TestSetup
from pytest_headlock import testsetup_fixture


class TS(TestSetup):
    def func(self, param):
        raise NotImplementedError()

ts = testsetup_fixture(TS)

def test_testsetupFixture_onSuccess_ok(ts):
    assert isinstance(ts, TS)

def test_testsetupFixture_hasTypeProperty():
    ts = testsetup_fixture(TS)
    assert ts.type is TS
