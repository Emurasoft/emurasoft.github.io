# Configs コレクション

Configs コレクションは、設定 ( [Config オブジェクト](../config/index)) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| [Count](count) | 設定の数を取得します。 |
| [Item](item) | 指定するインデックスの設定の [Config オブジェクト](../config/index) を取得します。 |

## 例

#### \[JavaScript\]

cfgs = new Enumerator( editor.Configs );

for( ; !cfgs.atEnd(); cfgs.moveNext() ){

cfg = cfgs.item();

alert( cfg.Name );

}

#### \[VBScript\]

For Each cfg In editor.Configs

alert cfg.Name

Next

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。


```{toctree}
:maxdepth: 1
count
item
```
