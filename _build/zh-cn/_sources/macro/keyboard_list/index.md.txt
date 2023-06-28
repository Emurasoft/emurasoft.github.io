# KeyboardList 集合

KeyboardList 集合提供了 [KeyboardItem 对象](../keyboard_item/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索项目的总数。 |
| **[Item](item)** | 为指导索引检索 [KeyboardItem 对象](../keyboard_item/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一个项目。 |
| **[Remove](remove)** | 删除一个项目。 |

## 示例

#### \[JavaScript\]

list = new Enumerator( document.Config.Keyboard.List );

for( ; !list.atEnd(); list.moveNext() ){

item = list.item();

alert( item.Key );

}

#### \[VBScript\]

For Each item In document.Config.Keyboard.List

alert item.Key

Next

## 版本

支持 EmEditor 7.00 或之后的版本。

```{toctree}
:maxdepth: 1
add
count
item
remove
```
