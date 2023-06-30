# FindWindow メソッド ()

クラス名またはウィンドウ タイトルで子の [Window オブジェクト](index) を検索します。

#### \[JavaScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ );

#### \[VBScript\]

wndChild = wnd. **FindWindow**( _strClass_, _strCaption_ )

## パラメータ

_strClass_

ウィンドウのクラス名を指定します。このパラメータが空なら、すべてのクラス名が一致します。

_strCaption_

ウィンドウ名 （タイトル） を指定します。 このパラメータが空なら、すべてのウィンドウ名が一致します。

## 例

#### \[JavaScript\]

wnd = FindWindow( "EmEditorView", "" );

alert( wnd.Caption );

#### \[VBScript\]

wnd = FindWindow( "EmEditorView", "" )

alert wnd.Caption

## バージョン

EmEditor Professional Version 7.00 以上で利用できます。