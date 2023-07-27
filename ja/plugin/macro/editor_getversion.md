# Editor\_GetVersion

バージョン番号を返します。このインライン関数を使うか、または [EE\_GET\_VERSION メッセージ](../message/ee_get_version) を直接送ることができます。

Editor\_GetVersion( HWND hwnd );

Editor\_GetVersionEx( HWND hwnd, int\* pnProductType );

## パラメータ

_hwnd_

EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pnProductType_

製品タイプを取得する int 変数へのポインタを指定します。次のうちいずれかの値になります。

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## 戻り値

バージョン番号に 1000 を乗じた値を返します。
