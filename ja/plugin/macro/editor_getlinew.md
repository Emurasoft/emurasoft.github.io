# Editor\_GetLineW

指定する行のUnicodeテキストを取得します。このインライン関数を使うか、または [EE\_GET\_LINEW](../message/ee_get_linew) メッセージを直接送ることができます。

Editor\_GetLineW( HWND hwnd, GET\_LINE\_INFO\* pGetLineInfo, LPWSTR szString );

Editor\_GetLineW( HWND hwnd, HEEDOC hDoc, UINT\_PTR yLine, LPWSTR pBuf, UINT\_PTR cchBuf, UINT flags, BYTE byteCrLf )

## パラメータ

_hwnd_

> EmEditor ビューまたはフレームのウィンドウ ハンドルを指定します。

_pGetLineInfo_

> [GET\_LINE\_INFO 構造体](../structure/get_line_info) へのポインタを指定します。

_szString_

> テキストを取得するバッファへのポインタを指定します。

_hDoc_

> 対象となる文書へのハンドルを指定します。NULL を指定すると、現在アクティブな文書を対象とします。

_yLine_

> 取得したいテキストの行番号を指定します。

_pBuf_

> テキストを取得するバッファへのポインタを指定します。

_cchBuf_

> _pBuf_ パラメータで、テキストを取得するバッファに格納することができる文字列の文字数を終端 Null
> 文字を含めて指定します。 0 を指定すると、バッファに必要な文字数を返すように指定することになります。

_flags_

> 下位ワードは、次のフラグの組み合わせを指定します。
>
> | 定数 | 説明 |
> | --- | --- |
> | FLAG\_LOGICAL | _yLine_ フィールドを論理座標で指定します |
> | FLAG\_WITH\_CRLF | 結果のテキストに改行コードを追加します |
> | FLAG\_GET\_CRLF\_BYTE | byteCrLf フィールドに改行コードを示すフラグを入れるように指示します。FLAG\_LOGICAL と共に指定する必要があります。 |
>
> 上位ワードは、操作対象のドキュメントのインデックスを指定します。 _flags_ の上位ワードには、1 を基底とするインデックスを指定します。 _flags_ の上位ワードに 0 を指定すると、現在アクティブなドキュメントが操作対象になります。

_byteCrLf_

> 指定する行の改行コードを示すフラグを取得します。このフィールドは、 _flags_ フィールドに FLAG\_LOGICAL と FLAG\_GET\_CRLF\_BYTE の両方を指定した場合にのみ使用されます。次のいずれかの値になります。
>
> | 定数 | 説明 |
> | --- | --- |
> | 0 | CR+LF またはファイルの最後。 |
> | FLAG\_CR\_ONLY | CR のみ。 |
> | FLAG\_LF\_ONLY | LF のみ。 |

## 戻り値

> _cchBuf_ に 0 を指定した場合、バッファに必要なサイズを文字単位で返します。 _cchBuf_
> が 0 以外の場合は利用されません。
