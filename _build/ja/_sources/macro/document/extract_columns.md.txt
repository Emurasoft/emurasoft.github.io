# ExtractColumns メソッド

CSV 文書から指定する列を抽出して新規文書を作成します。

#### \[JavaScript\]

document. **ExtractColumns**( _strColumns_ );

#### \[VBScript\]

document. **ExtractColumns** _strColumns_

## パラメータ

_strColumns_

どの列を抽出するかを選択する文字列を指定します。この値はカンマで区切られた列の組み合わせになります。各列は、列の最初の行、またはコロン (:) で始まる列のインデックスになります。例えば、":1,:3" は、アクティブな文書の1列目3列目を出力します。"first\_name,last\_name" は、最初の行が "first\_name" または "last\_name" に一致する列を出力します。前の列と連結するには「,」の代わりに「+」を、最初の空でない値を使用するには「,」の代わりに「\|」を使用します。

## バージョン

EmEditor Professional Version 18.4 以上で利用できます。