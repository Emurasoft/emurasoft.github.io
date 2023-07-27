# Editor\_DoIdle

ツール バー、タイトル、タブなどの表示更新を行います。このインライン関数を使うか、または [EE\_DO\_IDLE](../message/ee_do_idle) メッセージを直接送ることができます。

void Editor\_DoIdle( HWND hwnd, BOOL bResetTab );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウハンドルを指定します。

_bReset_

タブをリセットします。

## 戻り値

戻り値は利用されません。

## バージョン

Version 5.00 以上で利用できます。
