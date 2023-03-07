from src.add_function import add

# クラスを使わない方法
# def test_add():
#     assert add(10, 5) == 15

# クラスを使う方法
class TestAdd(object):
    def test_add(self):
        assert add(10, 5) == 15
