#スキップ
import pytest
class TestCalculation(object):

    @pytest.mark.skip(reason='理由を書く')
    def test_1(self):
        print('test1')

    @pytest.mark.skipif(False, reason='理由を書く')
    def test_2(self):
        print('test2')