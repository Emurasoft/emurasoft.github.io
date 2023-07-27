# NoWrapList 集合

NoWrapList 集合提供一个集合的 [NoWrapItem 对象](../no_wrap_item/index)。

## 属性

|     |     |
| --- | --- |
|[Count](count) | 检索项目的总数。 |
|[Item](item) | 为指定索引检索 [NoWrapItem 对象](../no_wrap_item/index)。 |

## 方法

|     |     |
| --- | --- |
|[Add](add) | 添加一个项目。 |
|[Remove](remove) | 删除一个项目。 |

## 示例

### \[JavaScript\]

```
list = new Enumerator( document.Config.NoWrap.List );
for( ; !list.atEnd(); list.moveNext() ){
item = list.item();
alert( item.Name );
}
```

### \[VBScript\]

```
For Each item In document.Config.NoWrap.List
alert item.Name
Next
```

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:maxdepth: 1
add
count
item
remove
```
