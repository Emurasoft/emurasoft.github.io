# FindWindow メソッド (Shell オブジェクト)

クラス名またはウィンドウ タイトルでトップ レベルの [Window オブジェクト](../window/index) を検索します。

## 

### \[JavaScript\]

```
wnd = shell.FindWindow( strClass, strCaption );
```

### \[VBScript\]

```
wnd = shell.FindWindow( strClass, strCaption )
```

## パラメータ

_strClass_

ウィンドウのクラス名を指定します。このパラメータが空なら、すべてのクラス名が一致します。

_strCaption_

ウィンドウ名 （タイトル） を指定します。 このパラメータが空なら、すべてのウィンドウ名が一致します。

## 例

### \[JavaScript\]

```
wnd = shell.FindWindow( "", "Calculator" );
wnd.SetForeground();
```

### \[VBScript\]

```
wnd = shell.FindWindow( "", "Calculator" )
wnd.SetForeground
```

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。
