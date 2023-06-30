# Join メソッド ()

SQL においての JOIN 操作と同様な方法を使って、2個の CSV 文書を結合して新規文書を作成します。

#### \[JavaScript\]

_n_ = editor. **Join**( _nFlags_, _strDocument1_, _strColumn1_, _strDocument2_, _strColumn2_, _strSelect_ );

#### \[VBScript\]

_n_ = editor. **Join**( _nFlags_, _strDocument1_, _strColumn1_, _strDocument2_, _strColumn2_, _strSelect_ )

## パラメータ

_nFlags_

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeJoinUniqueKey1 | 第1文書の指定した列には一意キーが含まれます。 |
| eeJoinUniqueKey2 | 第2文書の指定した列には一意キーが含まれます。 |
| eeJoinIncludeAll1 | 第1文書のすべての行が出力に含まれます。第1文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
| eeJoinIncludeAll2 | 第2文書のすべての行が出力に含まれます。第2文書にマッチしない行が存在する場合、出力文書には空のセルが含まれます。 |
| eeJoinMatchCase | 大文字と小文字を区別します。 |
| eeJoinSimpleMerge | キーを使用しないで、単純に結合します。これを指定した場合、 _strColumn1_ と _StrColumn2_ パラメータは無視されます。 |
| eeJoinIgnoreHeadings1 | 第1文書のヘディングを無視します。第1文書のヘディングは、結合された文書に残ります。 |
| eeJoinIgnoreHeadings2 | 第2文書のヘディングを無視します。 |
| eeJoinContain | Key1 は Key2 を含みます。 |
| eeJoinStartWith | Key1 は Key2 から始まります。 |
| eeJoinEndWith | Key1 は Key2 で終わります。 |
| eeJoinMatchSplitBoth | 両方の分割文字列が一致します。 |
| eeJoinMatchSplitOne | Key1 は 分割した Key2 に一致します。 |
| eeJoinFuzzy | あいまい一致を使用します。このフラグは、eeJoinEndWith、eeJoinMatchSplitBoth、または eeJoinMatchSplitOne と共に指定することはできません。このフラグを使用すると動作が遅くなります。 |
| eeJoinSwap | eeJoinContain、eeJoinStatWith、または eeJoinEndWith と共に指定されている場合、Key1 と Key2 を入れ替えます。 |

_strDocument1_

第1文書を特定する文字列を指定します。この値は、ファイル名、完全パスの付いたファイル名、またはコロン (:) で始まる現在のグループ内の文書のインデックスになります。例えば、"filename.csv"、"C:\\data\\filename.csv" (JavaScript の場合は、"C:\\\data\\\filename.csv") 、または ":2" と指定することができます。

_strColumn1_

第1文書のキー列を特定する文字列を指定します。この値は、列の最初の行、コロン (:) で始まる列のインデックス、または数値範囲になります。例えば、"first\_name"、":5"、"1-5"、"2-" と指定することができます。

_strDocument2_

第1文書を特定する文字列を指定します。この値のフォーマットは strDocument1 と同じです。

_strColumn2_

第1文書のキー列を特定する文字列を指定します。この値のフォーマットは strColumn1 と同じです。

_strSelect_

出力文書にどの列を選択するかを示す文字列を指定します。例えば、"file1.csv>column1,file2.csv>column2" と指定することができます。前の列と連結するには「,」の代わりに「+」を、最初の空でない値を使用するには「,」の代わりに「\|」を使用します。

## 戻り値

戻り値は、出力文書の行数になります。

## バージョン

EmEditor Professional Version 14.8 以上で利用できます。