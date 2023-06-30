# getData メソッド ()

クリップボードからデータを取得します。

#### \[JavaScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, \[ _iPos_ \] );

#### \[VBScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, \[ _iPos_ \] )

## パラメータ

_sDataFormat_

取得するクリップボードのフォーマットを文字列で指定します。次の文字列を指定することができます。

|     |     |
| --- | --- |
| Text | テキストのフォーマットを指定します。 |
| LineText | 行テキストのフォーマットを指定します。 |
| BoxText | 箱型テキストのフォーマットを指定します。 |
| html | HTML のフォーマットを指定します。 |

_iPos_

任意指定。古いクリップボードのデータを取得したい場合は、クリップボード履歴の位置を指定します。これに -1 を指定するか、または省略すると、現在のデータが取得されます。 _sDataFormat_ に "html" を指定した場合は、この値には -1 または 0 を指定する必要があります。

## 例

#### \[JavaScript\]

str = clipboardData.getData("Text");

#### \[VBScript\]

str = clipboardData.getData("Text")

次のマクロはクリップボード履歴を表示し、項目を選択するとそのテキストを挿入します。

#### \[JavaScript\]

menu = CreatePopupMenu();

i = 0;

do {

str = clipboardData.getData("text", i);

if( str.length == 0 ) break;

str = str.substr( 0, 40 )

menu.Add( str, i + 100 );

i++;

} while( 1 );

result = menu.Track( 0 );

if( result != 0 ) {

s = clipboardData.getData("text", result - 100);

document.write( s );

}

次のマクロはクリップボードの中身を HTML フォーマットとして貼り付けます。

#### \[JavaScript\]

str = clipboardData.getData("html");

document.selection.Text = str;

## バージョン

EmEditor Professional Version 5.00 以上で利用できます。