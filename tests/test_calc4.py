#fixture
#test(self, tmpdir)の第2引数がfixutre
#この第2引数の名前により、機能が変わる

class TestCalculation(object):

    def test(self, tmpdir):
        print(tmpdir)