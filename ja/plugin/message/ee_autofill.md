# EE\_AUTOFILL

CSV 文書に対してオートフィル、またはフラッシュ フィルを実行します。このメッセージを直接送るか、または [Editor\_AutoFill](../macro/editor_autofill) インライン関数を使うことができます。

```
EE_AUTOFILL
wParam = 0;
lParam = (LPARAM) (AUTOFILL_INFO*) pInfo;
```

## パラメータ

_pInfo_

[AUTOFILL\_INFO 構造体](../structure/autofill_info) へのポインタを指定します。

## 戻り値

戻り値は、メッセージが成功すると、次の値の組み合わせになります。戻り値が 0 の場合、オートフィルまたはフラッシュ フィルの動作を完了するためのパターンが検出できなかったことを意味します。負の値はメッセージが失敗したことを意味します。

|     |     |
| --- | --- |
| FLAG\_FILL\_COPY | ソース範囲からターゲット範囲に値をコピーし、必要に応じて繰り返します。 |
| FLAG\_FILL\_SERIES | ソース範囲の値をターゲット範囲に連続する数値として適用します。 |
| FLAG\_FILL\_FLASH | フラッシュ フィルの動作を実行します。つまり、検出されたパターンに基づいて、ソース範囲の値をターゲット範囲に適用します。このフラグは垂直方向にのみ適用されます。 |

## バージョン

EmEditor Professional Version 17.5 以上で利用できます。
