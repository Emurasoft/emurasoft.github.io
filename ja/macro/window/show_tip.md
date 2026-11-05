# ShowTip メソッド (Window オブジェクト)

ツール チップを表示します。

## 

### \[JavaScript\]

```
ShowTip( strTip, flags );
```

### \[VBScript\]

```
ShowTip strTip, flags
```

## パラメーター

_strTip_

ツール チップに表示するテキストを指定します。テキストの長さは 3,999 文字を超えることができません。文字列には、次の形式を使用して、クリック可能なテキストを含めることができます: "<a href="url">clickable text</a>"

_flags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| SHOW\_TIP\_ACTIVE\_STRING | マウス ポインターがポイントされているアクティブな文字列にツール チップを表示します。 |
| SHOW\_TIP\_CURRENT\_CARET | キャレット位置にツール チップを表示します。 |
| SHOW\_TIP\_CURRENT\_MOUSE | マウス ポインター位置にツール チップを表示します。 |
| SHOW\_TIP\_HIDE | 既にツール チップが表示されている場合、非表示にします。 |

## バージョン

EmEditor Professional Version 16.9 以上で利用できます。
