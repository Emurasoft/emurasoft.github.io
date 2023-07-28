# InsertDate 方法 (Selection 對象)

插入目前的時間和日期。

## 

### \[JavaScript\]

```
document.selection.InsertDate( nFlags );
```

### \[VBScript\]

```
document.selection.InsertDate [ nFlags ]
```

## 參數

_nFlags_

指定一個下列值的組合:

|     |     |
| --- | --- |
| eeDateTimeDate | 指定時間，后跟一個空白，然后日期。 |
| eeDateDateTime | 指定日期，后跟一個空白，然后時間。 |

## 備注

用於時間與日期的格式能在 Windows 上被組態，通過到 **控制面板** 中的 **區域語言選項** 上，然后選擇 **日期與時間**。

## 版本

支持 EmEditor 4.00 或之後的版本。
