#mockの使い方
import requests

# requestで外部のシステムにidをパラメーターにしてリクエストを送る
# jsonメソッドを呼び出して関数の戻り値にする
def get_json_data(id):
    res = requests.get('http://xxxx', params={'id':id})
    res_json = res.json()
    return res_json

#get_user_nameという関数
#引数で受け取ったidのリストから，idに対するユーザーネームのデータを取得する
#キーがidで，バリューがusernameの辞書を作成して返す

def get_user_names(user_ids):
    user_names = {}
    for id in user_ids:
        json_data = get_json_data(id)
        user_names[id] = json_data['name']
    return user_names