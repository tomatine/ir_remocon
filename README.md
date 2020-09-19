
# ir_remocon
raspberry piとBit Trade One社製の[USB赤外線リモコンアドバンス](https://bit-trade-one.co.jp/product/module/adir01p/)を使い、discordから家電を遠隔操作するためのコードです。
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">よっしゃ <a href="https://t.co/gkRBkPILc9">pic.twitter.com/gkRBkPILc9</a></p>&mdash; とまちん (@tomatine86) <a href="https://twitter.com/tomatine86/status/1305607212094484480?ref_src=twsrc%5Etfw">September 14, 2020</a></blockquote>
IFTTTを使ってgooglehomeとdiscordを連携させることで音声操作もできます
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">音声でもいける <a href="https://t.co/jBoDFgIgdS">pic.twitter.com/jBoDFgIgdS</a></p>&mdash; とまちん (@tomatine86) <a href="https://twitter.com/tomatine86/status/1305607815319363585?ref_src=twsrc%5Etfw">September 14, 2020</a></blockquote>

## Dependency
- python3.8+
- libusb-1.0.0
- libusb-1.0.0-dev
- [mojimoji](https://pypi.org/project/mojimoji/)
- [discord.py](https://pypi.org/project/discord.py/)
- [bto_ir_advanced_cmd](https://github.com/Drunkar/bto_ir_advanced_cmd)

## Setup
raspberry piと[USB赤外線リモコンアドバンス](https://bit-trade-one.co.jp/product/module/adir01p/)、USB-A to miniBケーブルを用意し、繋ぎます。
raspberry piにgit cloneします。
```
$ git clone https://github.com/tomatine/ir_remocon
$ git clone https://github.com/Drunkar/bto_ir_advanced_cmd.git
```
bto_ir_advancedを動かすためのライブラリをインストールし、bto_ir_advancedをmakeします。
```
$ sudo apt install libusb-1.0.0
$ sudo apt install libusb-1.0.0-dev
$ cd bto_ir_advanced_cmd
$ make
$ sudo make install
```
これでコマンドラインからbto_ir_advancedを使えます。
まず、送信したい赤外線のデータを受信し、ファイルに書き込みます。
```
$ bto_advanced_USBIR_cmd -r         # (生データ)受信開始
$ bto_advanced_USBIR_cmd -s         # (生データ)受信停止
$ bto_advanced_USBIR_cmd -g | tee data.txt  # 生データ取得
```
pythonモジュールをインストールします
```
$ pip install mojimoji discord.py
```
discordbotの設定をします。長くなるので、[Discord Botアカウント初期設定ガイド for Developer](https://qiita.com/1ntegrale9/items/cb285053f2fa5d0cccdf)を参考にして下さい。アクセストークンを環境変数discord_homebot_tokenに登録します。
```
$ echo export discord_homebot_token=`your_token` >> ~/.profile
```
bto_advanced_cmdを使って記録したデータファイルの名前をdiscord_homebot.pyの22行目～27行目で変数に指定します。初期状態ではエアコンのオンオフとライトの調整が設定されています。

## Usage
```
$ python discord_homebot.py
```
でdiscordbotが起動します。  
bashから直接送信したい場合は、
```
$ python send_ir.py data.txt
```
で送信できます。  
タイマー機能ですが、現状1回しか設定できず、上書きすると以前のものは消えます。  
bashからタイマーを設定するには、
```
$ python set_timer.txt [hour]  [minute]
```
でできます。

## License
MIT

## References
[Pythonで実用Discord Bot(discordpy解説)](https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f)  
[エアコンを外出先から遠隔操作(by MQTT)](https://qiita.com/Kaz-su/items/93ec120b4bb90de7da2b)  
[#1【RaspberryPiとGoogle Homeでスマートホーム化】赤外線モジュール動作確認 | ネタの杜](https://netanomori.net/2019/04/15/1%E3%80%90raspberrypi%E3%81%A8google-home%E3%81%A7%E3%82%B9%E3%83%9E%E3%83%BC%E3%83%88%E3%83%9B%E3%83%BC%E3%83%A0%E5%8C%96%E3%80%91%E8%B5%A4%E5%A4%96%E7%B7%9A%E3%83%A2%E3%82%B8%E3%83%A5%E3%83%BC/)  