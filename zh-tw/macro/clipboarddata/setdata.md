# setData 方法 (clipboardData ��H)

以指定格式分配數據到剪貼簿上。

## 

### \[JavaScript\]

```
bSuccess = clipboardData.setData( sDataFormat, sData, iPos );
```

### \[VBScript\]

```
bSuccess = clipboardData.setData( sDataFormat, sData, iPos )
```

## 參數

_sDataFormat_

指定一個或多個下列數據格式值得字符串。

|     |     |
| --- | --- |
| Text | 指定文本格式。 |
| LineText | 指定行文本格式。 |
| BoxText | 指定框文本格式。 |

_sData_

把文本數據指定為字符串。

_iPos_

可選。指定剪貼簿記錄中的位置如果您想要設置更舊的剪貼簿數據。如果該值是零或被省略，會分配當前數據。

## 示例

### \[JavaScript\]

```
clipboardData.setData("Text", "Hello!");
```

### \[VBScript\]

```
clipboardData.setData "Text", "Hello!"
```

## 版本

支持 EmEditor 5.00 或之後的版本。
