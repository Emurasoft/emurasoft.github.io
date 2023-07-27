# NoWrapList 集合

NoWrapList 集合提供一個集合的 [NoWrapItem 對象](../no_wrap_item/index)。

## 屬性

|     |     |
| --- | --- |
|[Count](count) | 檢索項目的總數。 |
|[Item](item) | 為指定索引檢索 [NoWrapItem 對象](../no_wrap_item/index)。 |

## 方法

|     |     |
| --- | --- |
|[Add](add) | 添加一個項目。 |
|[Remove](remove) | 刪除一個項目。 |

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

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:maxdepth: 1
add
count
item
remove
```
