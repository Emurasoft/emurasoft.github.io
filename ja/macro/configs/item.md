# Item プロパティ

指定するインデックスの設定の [Config オブジェクト](../config/index) を取得します。

#### \[JavaScript\]

_cfg_ = editor.Configs. **Item**( _Index_ );

#### \[VBScript\]

_cfg_ = editor.Configs. **Item**( _Index_ )

## パラメータ

_Index_

設定のインデックスを 1 を基底とする整数で指定します。

## 例

#### \[JavaScript\]

alert( "最初の設定の名前: " + editor.Configs.Item(1).Name );

#### \[VBScript\]

alert "最初の設定の名前: " & editor.Configs.Item(1).Name

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。