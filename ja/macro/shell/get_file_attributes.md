# GetFileAttributes メソッド

指定するファイルまたはフォルダの属性を返します。

#### \[JavaScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ );

#### \[VBScript\]

nAttr = shell. **GetFileAttributes**( _strFile_ )

## パラメータ

_strFile_

属性を取得するファイルまたはフォルダの完全パス。

## 例

#### \[JavaScript\]

nAttr = shell.GetFileAttributes( "C:\\\Test\\\file.txt" );

#### \[VBScript\]

nAttr = shell.GetFileAttributes( "C:\\Test\\file.txt" )

## 戻り値

次の値の組み合わせを返します。

|     |     |
| --- | --- |
| 値 | 説明 |
| 0 | 通常 |
| 1 | 書き換え禁止 |
| 2 | 隠しファイル |
| 4 | システム |
| 8 | ボリューム |
| 16 | ディレクトリ |
| 32 | アーカイブ |
| 1024 | エイリアス |
| 2048 | 圧縮 |

## バージョン

EmEditor Professional Version 22.1 以上で利用できます。