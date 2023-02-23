from src import code3

def get_json_data_mock(id):
    return{'name':'太郎'}

# monkeypathcの3つの引数
# 1のcode3はmockに差し替えたい関数のモジュール
# 2のget_json_dataはmockに差し替えたい関数名の文字列
# 3のget_json_data_mockは実際に置き換えるmockの関数
def test_get_user_names(monkeypatch):
    monkeypatch.setattr(
        code3, 'get_json_data', get_json_data_mock)
    result = code3.get_user_names(['001'])

    assert list(result.keys()) == ['001']
    assert list(result.values()) == ['太郎']