# Item プロパティ (Configs コレクション)

指定するインデックスの設定の [Config オブジェクト](../config/index) を取得します。

## 

### \[JavaScript\]

```
cfg = editor.Configs.Item( Index );
```

### \[VBScript\]

```
cfg = editor.Configs.Item( Index )
```

## パラメータ

_Index_

設定のインデックスを 1 を基底とする整数で指定します。

## 例

### \[JavaScript\]

```
alert( "最初の設定の名前: " + editor.Configs.Item(1).Name );
```

### \[VBScript\]

```
alert "最初の設定の名前: " & editor.Configs.Item(1).Name
```

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
