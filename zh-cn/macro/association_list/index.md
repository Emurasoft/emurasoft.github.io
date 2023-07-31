# AssociationList 集合

AssociationList 集合提供 [AssociationItem 对象](../association_item/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索项目的数目。 |
| **[Item](item)** | 为指定索引检索 [AssociationItem 对象](../association_item/index)。 |

## 方法

|     |     |
| --- | --- |
| **[Add](add)** | 添加一个项目。 |
| **[Remove](remove)** | 删除一个项目。 |

## 示例

### \[JavaScript\]

```
list = new Enumerator( document.Config.Association.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.Association.List
alert item.Name
Next
```

## 版本

支持 EmEditor 7.00 至 EmEditor 14.3 的版本。


```{toctree}
:hidden:
:maxdepth: 1
add
count
item
remove
```
