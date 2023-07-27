# Editor\_Free

指定するプラグインを開放します。このインライン関数を使うか、または [EE\_FREE](../message/ee_free)
メッセージを直接送ることができます。通常、EmEditorのプラグイン設定ダイアログで使用されます。

Editor\_Free( HWND hwnd, ATOM atom );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_atom_

プラグインのファイル名のアトムを指定します。

## 戻り値

プラグインの開放に成功したら TRUE を返します。失敗すると FALSE を返します。
