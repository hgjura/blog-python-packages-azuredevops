import pytest

import mdw.databricks as db

def test_hi():
    s = db.hi()
    assert isinstance(s, str)

