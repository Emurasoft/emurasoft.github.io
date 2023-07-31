# DroppedFiles 集合

DroppedFiles 集合在一個框架視窗中提供拖放的檔案名稱的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索被拖放的檔案的數目。 |
| **[Item](item)** | 檢索指定索引下的被拖放的檔案名稱。 |

## 示例

### \[JavaScript\]

```
files = new Enumerator( DroppedFiles );
for( ; !files.atEnd(); files.moveNext() ){
alert( files.item() );
}
```

### \[VBScript\]

```
For Each str In DroppedFiles
alert str
Next
```

## 版本

支持 EmEditor 8.00 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
