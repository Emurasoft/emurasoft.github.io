# getData 方法

從剪貼簿上用指定的格式檢索數據。

#### \[JavaScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ );

#### \[VBScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ )

## 參數

_sDataFormat_

指定一個或多個下列數據格式值的字符串。

|     |     |
| --- | --- |
| Text | 指定文本格式。 |
| LineText | 指定行文本格式。 |
| BoxText | 指定框文本格式。 |
| html | 指定 HTML 格式。 |

_iPos_

可選項。在剪貼簿記錄中指定位置如果您想要檢索舊的剪貼簿記錄。如果該參數值是 -1 或被省略，當前數據會被檢索。該值必須是 0 或 -1 如果 "html" 被指定為 _sDataFormat_ 參數。

## 示例

#### \[JavaScript\]

str = clipboardData.getData("Text");

#### \[VBScript\]

str = clipboardData.getData("Text")

下列巨集顯示剪貼簿記錄，并且選擇一個項目會插入該文本內容。

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

下列巨集把剪貼簿內容粘貼為 HTML 格式。

#### \[JavaScript\]

str = clipboardData.getData("html");

document.selection.Text = str;

## 版本

支持 EmEditor 5.00 或之後的版本。