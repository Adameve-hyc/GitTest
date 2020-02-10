import pytest

from data.raad_data import read_yaml


class TestSum():

    @pytest.mark.parametrize('a,b,c', read_yaml())
    def test_sum(self,a,b,c):
        assert a + b == c
