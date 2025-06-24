# EE\_GET\_VERSION

バージョン番号を返します。このメッセージを直接送るか、または [Editor\_GetVersion インライン関数](../macro/editor_getversion) を使うことができます。

```
EE_GET_VERSION
wParam = pnProductType;
lParam = 0;
```

## パラメータ

_pnProductType_

製品タイプを取得する int 変数へのポインタを指定します。次のうちいずれかの値になります。

|     |     |
| --- | --- |
| VERSION\_PRO | EmEditor Professional |
| VERSION\_STD | EmEditor Standard |

## 戻り値

バージョン番号に 10000 を乗じた値を返します。例えば、バージョン番号が 25.1.907 の場合、返り値は 251907 になります。
