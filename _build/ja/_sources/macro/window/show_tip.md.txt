# ShowTip メソッド

ツールチップを表示します。

#### \[JavaScript\]

**ShowTip**( _strTip_, _flags_ );

#### \[VBScript\]

**ShowTip** _strTip_, _flags_

## パラメータ

_strTip_

ツールチップに表示するテキストを指定します。テキストの長さは 3,999 文字を超えることができません。文字列には、次の形式を使用して、クリック可能なテキストを含めることができます: "<a href="url">clickable text</a>"

_flags_

次の値の組み合わせを指定します。

|     |     |
| --- | --- |
| SHOW\_TIP\_ACTIVE\_STRING | マウス ポインターがポイントされているアクティブな文字列にツールチップを表示します。 |
| SHOW\_TIP\_CURRENT\_CARET | キャレット位置にツールチップを表示します。 |
| SHOW\_TIP\_CURRENT\_MOUSE | マウス ポインター位置にツールチップを表示します。 |
| SHOW\_TIP\_HIDE | 既にツールチップが表示されている場合、非表示にします。 |

## バージョン

EmEditor Professional Version 16.9 以上で利用できます。