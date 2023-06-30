# prompt メソッド ()

文字列を入力するためのダイアログ ボックスを表示します。

#### \[JavaScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_);

#### \[VBScript\]

_strAnswer_ = **prompt**( _strMessage, strDefault, flags_ )

## パラメータ

_strMessage_

表示する文字列を指定します。

_strDefault_

テキスト ボックスに既定で表示される文字列を指定します。

_flags_

省略可能。次の値のいずれかを指定します。省略すると 0 を指定することになります。

|     |     |
| --- | --- |
| 0 | 1行テキスト ボックスを表示します。 |
| eePromptMultiline | 複数行のテキスト ボックスを表示します。 |

## 戻り値

\[OK\] ボタンを選択した場合は、テキスト ボックスに入力された文字列を返します。\[キャンセル\] ボタンを選択した場合は、空の文字列を返します。

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。