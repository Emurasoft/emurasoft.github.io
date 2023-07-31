# KeyboardList 集合

KeyboardList 集合提供了 [KeyboardItem 對象](../keyboard_item/index) 的集合。

## 屬性

|     |     |
| --- | --- |
| **[Count](count)** | 檢索項目總數。 |
| **[Item](item)** | 為指導索引檢索 [KeyboardItem 對象](../keyboard_item/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一個項目。 |
| **[Remove](remove)** | 刪除一個項目。 |

## 示例

### \[JavaScript\]

```
list = new Enumerator( document.Config.Keyboard.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Key );
}
```

### \[VBScript\]

```
For Each item In document.Config.Keyboard.List
alert item.Key
Next
```

## 版本

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:hidden:
:maxdepth: 1
add
count
item
remove
```
