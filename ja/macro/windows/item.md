# Item プロパティ

指定するインデックスのウィンドウの Window オブジェクトを取得します。

#### \[JavaScript\]

_wnd_ = shell.windows. **Item**( _Index_ );

#### \[VBScript\]

_wnd_ = shell.windows. **Item**( _Index_ )

## パラメータ

_Index_

ウィンドウのインデックスを 1 を基底とする整数で指定します。

## 例

#### \[JavaScript\]

alert( "最初のウィンドウの名前: " + shell.windows.Item(1).Caption );

#### \[VBScript\]

alert "最初のウィンドウの名前: " & shell.windows.Item(1).Caption

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。