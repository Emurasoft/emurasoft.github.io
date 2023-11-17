# getData Method (clipboardData Object)

Retrieves the data in the specified format from the Clipboard.

## 

### \[JavaScript\]

```
sData = clipboardData.getData( sDataFormat, iPos );
```

### \[VBScript\]

```
sData = clipboardData.getData( sDataFormat, iPos )
```

## Parameters

_sDataFormat_

String that specifies one or more of the following data format values.

|     |     |
| --- | --- |
| Text | Specifies the text format. |
| LineText | Specifies the line text format. |
| BoxText | Specifies the box text format. |
| html | Specifies the HTML format. |

_iPos_

Optional. Specifies the position in the Clipboard history if you want to retrieve older clipboard data. If this is -1 or omitted, the current data is retrieved. This value must be 0 or -1 if "html" is specified in the _sDataFormat_ parameter.

## Examples

### \[JavaScript\]

```
str = clipboardData.getData("Text");
```

### \[VBScript\]

```
str = clipboardData.getData("Text")
```

The following macro displays the clipboard history, and selecting an item will insert that text.


### \[JavaScript\]

```
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
```

The following macro pastes the clipboard contents as HTML format.

### \[JavaScript\]

```
str = clipboardData.getData("html");
document.selection.Text = str;
```

## Version

Supported on EmEditor Professional Version 5.00 or later.
