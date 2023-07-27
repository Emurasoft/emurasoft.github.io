# Configs 集合

Configs 集合提供 [Config 對象](../config/index) 的集合。

## 屬性

|     |     |
| --- | --- |
|[Count](count) | 檢索組態的數目。 |
|[Item](item) | 為指定索引的組態檢索 [Config 對象](../config/index)。 |

## 示例

### \[JavaScript\]

```
cfgs = new Enumerator( editor.Configs );
for( ; !cfgs.atEnd(); cfgs.moveNext() ){
cfg = cfgs.item();
alert( cfg.Name );
}
```

### \[VBScript\]

```
For Each cfg In editor.Configs
alert cfg.Name
Next
```

## 版本

支持 EmEditor 7.00 或之後的版本。


```{toctree}
:maxdepth: 1
count
item
```
