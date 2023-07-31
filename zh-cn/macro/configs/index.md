# Configs 集合

Configs 集合提供 [**Config** 对象](../config/index) 的集合。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索配置的数目。 |
| **[Item](item)** | 为指定索引的配置检索 [**Config** 对象](../config/index)。 |

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

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:hidden:
:maxdepth: 1
count
item
```
