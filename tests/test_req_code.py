import pytest
from unittest.mock import patch
from src.req_code import call_api

class TestPatchTest(object):
    def test_call_api(self):
        # どこにパッチを指定するかを記述
        # 下記の場合、mainモジュールのrequests.getメソッドに設定
        with patch('src.req_code.requests.get') as mocked_get:
            # 上記requests.getの返り値の「OK」値を設定
            mocked_get.return_value.ok = True
            # 上記requests.getの返り値の「text」値を設定
            mocked_get.return_value.text = 'success'

            # patchで設定した（この場合、request.get）の引数をチェック
            # 下記で指定した引数でなければ、NGを表示
            # mocked_get.assert_called_with('https://zero-cheese.com/')
            # 自作関数を実行した結果、戻り値テスト
            # assert call_api() == 'success'

            # 新たに値を設定する際は、値をリセットする
            # mocked_get.reset_mock()
            # mocked_get.return_value.ok = False
            # mocked_get.return_value.text = 'No Site'
            # assert call_api() == 'No Site'