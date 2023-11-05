# EE\_KEYBOARD\_PROP

指定したコマンド ID と設定のキーボード プロパティを表示します。このメッセージを直接送るか、または [Editor\_keyboadProp インライン関数](../macro/editor_keyboardprop) を使うことができます。

```
EE_KEYBOARD_PROP
wParam = (WPARAM)(UINT)nCmdID;
lParam = (LPARAM)(LPCWSTR)pszConfigName;
```

## パラメータ

_nCmdID_

キーボード プロパティで最初に選択するコマンド ID を指定します。

_pszConfigName_

EmEditor が表示するキーボード プロパティの設定を指定します。

## 戻り値

設定プロパティで OK を選択すると戻り値は TRUE を返します。キャンセルを選択すると戻り値は FALSE を返します。

## バージョン

EmEditor Version 7.00 以上で利用できます。
