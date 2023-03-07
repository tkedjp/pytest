#それぞれのテスト前後で決まったコードを実行

class TestCalculation(object):

    # 各テストの開始前に実行
    def setup_method(self, method):
        print('テスト開始前')

    # 各テストの開始後に実行
    def teardown_method(self, method):
        print('テスト開始後')

    def test_1(self):
        print('test1')

    def test_2(self):
        print('test2')