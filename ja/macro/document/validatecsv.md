# ValidateCsv メソッド (Document オブジェクト)

CSV文書の正当性を確認してエラーを出力し、オプションにより区切り位置を調節します。

## 

### \[JavaScript\]

```
nResults = document.ValidateCsv( nFlags );
```

### \[VBScript\]

```
nResults = document.ValidateCsv( nFlags )
```

## パラメータ

_nFlags_

次の値の組み合わせを指定します。省略すると、フラグを何も指定しないことになります。

|     |     |
| --- | --- |
| eeValidateAdjustColumns | 区切り位置を調節します。 |
| eeValidateAdjustEnlargeOnly | eeValidateAdjustColumns と組み合わせて指定することにより、列の幅を狭くすることはできませんが広くすることはできます。 |
| eeValidateAdjustVisibleOnly | eeValidateAdjustColumns と組み合わせて指定することにより、表示されている行のみの区切り位置を調節します。 |
| eeValidateDetectNL | 改行コードを検出し2重引用符の内側で見つけた場合はセルの中に埋め込みます。このフラグは、定義されたCSVフォーマットが \[2重引用符の内の改行コードを許可\] オプションが有効な場合にのみ意味があります。 |
| eeValidateDontClearOutput | 使用されません。 |
| eeValidateQuiet | アウトプット バーに情報やエラーを表示しません。 |
| eeValidateQuietIfNoError | エラーが無い場合、アウトプット バーに情報を表示しません。 |

## 戻り値

戻り値は、次の値の組み合わせになります。戻り値が 0 の場合エラーが無いことを意味します。

|     |     |
| --- | --- |
| eeCsvAbort | 操作はユーザーにより中止されました。 |
| eeCsvAdjusted | 区切り位置は調節されました。 |
| eeCsvInconsistentColumns | 一致しない列数を検出しました。 |
| eeCsvInvalidQuotes | 不正な2重引用符を検出しました。 |
| eeCsvNLEmbedded | 改行コードがセルに埋め込まれました。 |
| eeCsvNotCsv | CSVモードが選択されていません。 |

## 例

### \[JavaScript\]

```
nResults = document.ValidateCsv( eeValidateQuiet );
if( nResults != 0 ) {
    if( nResults & eeCsvAbort ) {
        alert( "The operation was aborted by the user." );
    }
    if( nResults & eeCsvAdjusted ) {
        alert( "Separator positions were adjusted." );
    }
    if( nResults & eeCsvInconsistentColumns ) {
        alert( "The inconsistent number of columns was detected." );
    }
    if( nResults & eeCsvInvalidQuotes ) {
        alert( "An invalid quotation mark was detected." );
    }
    if( nResults & eeCsvNLEmbedded ) {
        alert( "A newline code was embedded into a cell." );
    }
    if( nResults & eeCsvNotCsv ) {
        alert( "A CSV mode was not selected." );
    }
}
else {
    alert( "There were no errors" );
}
```

### \[VBScript\]

```
nResults = document.ValidateCsv( eeValidateQuiet )
If nResults <> 0 Then
If nResults And eeCsvAbort Then
alert( "操作はユーザーにより中止されました。" )
End If
If nResults And eeCsvAdjusted Then
alert( "区切り位置は調節されました。" )
End If
If nResults And eeCsvInconsistentColumns Then
alert( "一致しない列数を検出しました。" )
End If
If nResults And eeCsvInvalidQuotes Then
alert( "不正な2重引用符を検出しました。" )
End If
If nResults & eeCsvNLEmbedded Then
alert( "改行コードがセルに埋め込まれました。" )
End If
If nResults & eeCsvNotCsv Then
alert( "CSVモードが選択されていません。" )
End If
Else
alert( "エラーが見つかりませんでした。" )
End If
```

## バージョン

EmEditor Professional Version 17.2 以上で利用できます。
