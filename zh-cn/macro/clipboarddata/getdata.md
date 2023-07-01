# getData 方法 (clipboardData ����)

从剪贴板上用指定的格式检索数据。

#### \[JavaScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ );

#### \[VBScript\]

_sData_ = clipboardData. **getData**( _sDataFormat_, _iPos_ )

## 参数

_sDataFormat_

指定一个或多个下列数据格式值的字符串。

|     |     |
| --- | --- |
| Text | 指定文本格式。 |
| LineText | 指定行文本格式。 |
| BoxText | 指定框文本格式。 |
| html | 指定 HTML 格式。 |

_iPos_

可选项。在剪贴板记录中指定位置如果你想要检索旧的剪贴板记录。如果该参数值是 -1 或被省略，当前数据会被检索。该值必须是 0 或 -1 如果 "html" 被指定为 _sDataFormat_ 参数。

## 示例

#### \[JavaScript\]

str = clipboardData.getData("Text");

#### \[VBScript\]

str = clipboardData.getData("Text")

下列宏显示剪贴板记录；选择一个项目会插入该文本内容。

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

下列宏把剪贴板内容粘贴为 HTML 格式。

#### \[JavaScript\]

str = clipboardData.getData("html");

document.selection.Text = str;

## 版本

支持 EmEditor 5.00 或之后的版本。
