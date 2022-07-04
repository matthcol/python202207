# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:29:07 2022

@author: Matthias
"""

import pytest

@pytest.fixture(params=[ [[1]], [[1,2],[3,4]] ])
def carre_nok(request):
    return request.param


def test_checkMagic_nok(carre_nok):
    assert len(carre_nok) == 1