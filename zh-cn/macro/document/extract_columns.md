# ExtractColumns 方法 (Document 对象)

提取 CSV 文档中的指定列。

## 

### \[JavaScript\]

```
document.ExtractColumns( strColumns );
```

### \[VBScript\]

```
document.ExtractColumns strColumns
```

## 参数

_strColumns_

指定要包含在输出文档中的列的字符串。此值是以逗号分隔的列的组合。每列可以是列的第一行，也可以是冒号（：）后跟列的索引。 例如，“:1, :3”将输出活动文档的第一列和第三列。另外，“姓，名”将输出第一行与“姓”或“名”匹配的列。

## 版本

支持 EmEditor Professional 18.4 或之后的版本。
