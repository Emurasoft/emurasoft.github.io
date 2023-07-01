# Editor\_GetAttr

クリップボード履歴にある特定の位置のテキストを消去します。このインライン関数を使うか、または [EE\_GET\_ATTR](../message/ee_get_attr) メッセージを直接送ることができます。

Editor\_GetAttr( HWND hwnd, ATTR\_INFO\* pAI );

## パラメータ

_pAI_

> [ATTR\_INFO](../structure/attr_info) 構造体へポインタします。

## 戻り値

> 成功すると TRUEを、失敗すると FALSEを返します。

## バージョン

> Version 9.00 以上で利用できます。
