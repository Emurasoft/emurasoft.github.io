# GetFastViewDiffPath メソッド (Editor オブジェクト)

指定するファイルの高速ビュー モードの差分ファイルのパスを取得します。

## 

### \[JavaScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile );
```

### \[VBScript\]

```
strDiffPath = editor.GetFastViewDiffPath( strFile )
```

## パラメータ

_strFile_

ファイルのパスを指定します。

## 戻り値

高速ビュー モードでファイルの編集内容や行の位置を保存する差分ファイルのパスを返します。ファイルの差分ファイルが見つからない場合は、[\[差分を保存\] コマンド](../../cmd/file/fast_view_save_diff)が差分ファイルを保存するパスを返すため、返されたファイルが存在しない場合があります。

## 解説

差分ファイルは、EmEditor のローカル アプリケーション データ フォルダー内の **FastView** フォルダーに保存されます。詳細は、[高速ビュー モードで巨大ファイルを開いて編集する](../../howto/file/file_fast_view)を参照してください。

## 例

### \[JavaScript\]

```
sDiff = editor.GetFastViewDiffPath( document.FullName );
fso = new ActiveXObject( "Scripting.FileSystemObject" );
if( fso.FileExists( sDiff ) )  alert( "差分ファイルが存在します: " + sDiff );
```

### \[VBScript\]

```
sDiff = editor.GetFastViewDiffPath( document.FullName )
Set fso = CreateObject( "Scripting.FileSystemObject" )
If fso.FileExists( sDiff ) Then alert( "差分ファイルが存在します: " & sDiff )
```

## バージョン

EmEditor Professional Version 26.4 以上で利用できます。
