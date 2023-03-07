#テスト全体で開始前、開始後に1度だけ実行されるコード
#「setup_class」が全体開始前、「teardown_class」が全体終了時に実行されま
from src.add_function import add

class TestCalculation(object):
    @classmethod
    def setup_class(cls):
        print('開始前に実行')

    @classmethod
    def teardown_class(cls):
        print('終了時に実行')

    def test1(self):
        assert add(10, 5) == 15

    def test2(self):
        assert add(10, -1) == 9