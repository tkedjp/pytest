from src import main

#pytest-mockをインストールすれば、fixtureでmockerが使えるようになる
#差し替えたい処理をpatchで指定してモックにする

def test_func_main(mocker):
    mocker.patch("src.main.func_hoge", return_value=[1, 2])
    print(main.func_main()) # [1, 2]