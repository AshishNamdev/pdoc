import pdoc.extract
import pdoc.doc

import tutils


def test_simple():
    with tutils.tdir():
        m = pdoc.extract.extract_module("./modules/one.py")
        sm = pdoc.doc.Module(m, allsubmodules=True)
        assert(sm)