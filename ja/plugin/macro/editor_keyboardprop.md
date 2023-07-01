# Editor\_KeyboardProp

指定したコマンド ID と設定のキーボード プロパティを表示します。このインライン関数を使うか、または
[EE\_KEYBOARD\_PROP メッセージ](../message/ee_keyboard_prop) を直接送ることができます。

Editor\_KeyboardProp( HWND hwnd, UINT nCmdID, LPCWSTR pszConfigName );

## パラメータ

_hwnd_

> EmEditorのビューかフレームのウィンドウ ハンドルを指定します。

_nCmdID_

> キーボード プロパティで最初に選択するコマンド ID を指定します。

_pszConfigName_

> EmEditor が表示するキーボード プロパティの設定を指定します。

## 戻り値

> 設定プロパティで OK を選択すると戻り値は TRUE を返します。キャンセルを選択すると戻り値は FALSE を返します。
