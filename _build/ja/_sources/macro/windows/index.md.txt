# Windows コレクション

Windows コレクションは、ウィンドウ ( [Window オブジェクト](../window/index)) のコレクションを提供します。

## プロパティ

|     |     |
| --- | --- |
| [Count](count) | ウィンドウの数を取得します。 |
| [Item](item) | 指定するインデックスのウィンドウの Window オブジェクトを取得します。 |

## 例

#### \[JavaScript\]

wnds = new Enumerator( shell.windows );

for( ; !wnds .atEnd(); wnds.moveNext() ){

wnd = wnds.item();

if( wnd.Caption == "Calculator" ){

alert( "Found Calculator window" );

break;

}

}

#### \[VBScript\]

For Each wnd In shell.windows

If wnd.Caption = "Calculator" Then

alert "Found Calculator window"

Exit For

End If

Next

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。

```{toctree}
:maxdepth: 1
count
item
```
