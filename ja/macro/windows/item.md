# Item プロパティ (Windows コレクション)

指定するインデックスのウィンドウの Window オブジェクトを取得します。

## 

### \[JavaScript\]

```
wnd = shell.windows.Item( Index );
```

### \[VBScript\]

```
wnd = shell.windows.Item( Index )
```

## パラメータ

_Index_

ウィンドウのインデックスを 1 を基底とする整数で指定します。

## 例

### \[JavaScript\]

```
alert( "最初のウィンドウの名前: " + shell.windows.Item(1).Caption );
```

### \[VBScript\]

```
alert "最初のウィンドウの名前: " & shell.windows.Item(1).Caption
```

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
