# Item 屬性 (CsvList 集合)

檢索指定索引的 [Csv 對象](../csv/index)。

## 

### \[JavaScript\]

```
doc = editor.CsvList.Item( Index );
```

### \[VBScript\]

```
doc = editor.CsvList.Item( Index )
```

## 範例

_Index_

將 Csv 對象的索引指定為基於 1 的整數。

## Examples

### \[JavaScript\]

```
alert( "第一個 Csv 對象的名稱：" + editor.CsvList.Item(1).Name );
```

### \[VBScript\]

```
alert "第一個 Csv 對象的名稱：" & editor.CsvList.Item(1).Name
```

## 版本

支持 EmEditor 19.4 或之後的版本。
