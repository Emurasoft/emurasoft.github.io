# Export メソッド ()

コレクションを TSV ファイルにエクスポートします。

#### \[JavaScript\]

list. **Export**( _strFileName_ );

#### \[VBScript\]

list. **Export** _strFileName_

## パラメータ

_strFileName_

TSV ファイルの完全パスを含むファイル名を指定します。

## 例

#### \[JavaScript\]

var filters = document.filters;

if( filters.Count > 0 ) {

filters.Export( "E:\\\Test\\\filter.tsv" );

}

#### \[VBScript\]

Set filters = document.filters

If filters.Count > 0 Then

filters.Export "E:\\Test\\filter.tsv"

End If

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。
