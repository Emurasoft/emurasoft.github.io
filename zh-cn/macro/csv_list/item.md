# Item 属性 (CsvList 集合)

检索指定索引的 [**Csv** 对象](../csv/index)。

## 

### \[JavaScript\]

```
doc = editor.CsvList.Item( Index );
```

### \[VBScript\]

```
doc = editor.CsvList.Item( Index )
```

## 示例

_Index_

将 Csv 对象的索引指定为基于 1 的整数。

## Examples

### \[JavaScript\]

```
alert( "第一个 Csv 对象的名称：" + editor.CsvList.Item(1).Name );
```

### \[VBScript\]

```
alert "第一个 Csv 对象的名称：" & editor.CsvList.Item(1).Name
```

## 版本

支持 EmEditor 19.4 或之后的版本。
