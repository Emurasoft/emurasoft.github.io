# Item 属性 (DisplayList 集合)

为指定索引检索 [DisplayItem 对象](../display_item/index)。

## 

### \[JavaScript\]

```
item = list.Item( Index );
```

### \[VBScript\]

```
item = list.Item( Index )
```

## 参数

_Index_

指定以 1 为基准的整数为项目的索引。

如果对象是一个颜色列表，项目会是下列值之一。

|     |     |
| --- | --- |
| eeColorNormal | 一般 |
| eeColorSelection | 选取 |
| eeColorCurrentLine | 当前行 |
| eeColorQuote | 引用行 |
| eeColorURL | URL |
| eeColorMailTo | 邮箱地址 |
| eeColorTag | 包括“在文件中查找”结果的超链接的标签 |
| eeColorSingleQuotes | 带单引号 '...' 的字符串 |
| eeColorDoubleQuotes | 带双引号 "..." 的字符串 |
| eeColorComment | 注释 |
| eeColorScript | 脚本 |
| eeColorBraces | 匹配的圆括号/方括号 |
| eeColorInsideTag | HTML/XML 标签 |
| eeColorHighlight1 | 高亮 (1) |
| eeColorHighlight2 | 高亮 (2) |
| eeColorHighlight3 | 高亮 (3) |
| eeColorHighlight4 | 高亮 (4) |
| eeColorHighlight5 | 高亮 (5) |
| eeColorHighlight6 | 高亮 (6) |
| eeColorHighlight7 | 高亮 (7) |
| eeColorHighlight8 | 高亮 (8) |
| eeColorHighlight9 | 高亮 (9) |
| eeColorHighlight10 | 高亮 (10) |
| eeColorReturn | 换行符，制表符，EOF |
| eeColorCursorLine | 水平/垂直行 |
| eeColorPageBreak | 分页符/仅编辑选定区域 |
| eeColorLineNumbers | 行号 (数字) |
| eeColorRuler | 标尺/列标题 (数字) |
| eeColorOutside | 超出区域 |
| eeColorCompareChange | 比较 \- 变更的行 |
| eeColorCompareChar | 比较 \- 变更的字符 |
| eeColorCompareAdded | 比较 \- 新增 |
| eeColorCompareDeleted | 比较 \- 删除 |
| eeColorCompareBlank | 比较 \- 空白 |
| eeColorSpell | 错误拼写 |
| eeColorUnicode | Unicode 字符 |
| eeColorVerticalSel | 垂直选择框架 |
| eeColorHexSel | 十六进制显示选取框架 |
| eeColorIndentGuides | 缩进参考线 |
| eeColorHorzGrid | 水平网格 |
| eeColorOutline | 大纲 |
| eeColorLineNumberLines | 行号 (线) |
| eeColorRulerLines | 标尺/列标题 (线) |
| eeColorVerticalSeparator | 垂直分隔符 |
| eeColorHtmlCharRef | HTML 字符引用 |
| eeColorUcn | 通用字符名称/百分比编码 |
| eeColorAutoMarker | 自动标记 |
| eeColorMarker1 | 标记 (1) |
| eeColorMarker2 | 标记 (2) |
| eeColorMarker3 | 标记 (3) |
| eeColorMarker4 | 标记 (4) |
| eeColorMarker5 | 标记 (5) |
| eeColorMarker6 | 标记 (6) |
| eeColorMarker7 | 标记 (7) |
| eeColorMarker8 | 标记 (8) |
| eeColorMarker9 | 标记 (9) |
| eeColorMarker10 | 标记 (10) |
| eeColorMatchingTag | 匹配标记 |
| eeColorBookmark | 添加书签行 |
| eeColorUserDefinedGuides | 用户自定义参考线 |
| eeColorIndicatorModified | 垂直标记 \- 更改过的行 |
| eeColorIndicatorSaved | 垂直标记 \- 变更已保存的行 |
| eeColorIndicatorBookmark | 垂直标记 \- 书签 |
| eeColorMarkerModified | 滚动条标记 \- 更改过的行 |
| eeColorMarkerSaved | 滚动条标记 \- 变更已保存的行 |
| eeColorMarkerBookmark | 滚动条标记 \- 书签 |
| eeColorMarkerFound | 滚动条标记 \- 已找到 |
| eeColorMarkerCursor | 滚动条标记 \- 光标位置 |
| eeColorMarkerCompareChange | 滚动条标记 \- 比较变更项 |
| eeColorMarkerCompareAdded | 滚动条标记 \- 比较新增项 |
| eeColorMarkerCompareDeleted | 滚动条标记 \- 比较删除项 |
| eeColorHeadings | 标题 |
| eeColorSearchSel | 搜索范围 |
| eeColorFilter | 筛选内容 |
| eeColorLinkUrlVisited | URL (访问过的) |
| eeColorLinkIdVisited | 邮件地址 (访问过的) |
| eeColorLinkTagVisited | “在文件中查找”结果中的超链接 (访问过的) |
| eeColorCellText | CSV 单元格所选文本 |
| eeColorCellBorder | CSV 单元格选择框架 |
| eeColorFilterSeparator | 筛选分隔符 |
| eeColorMinimapBackground | 迷你地图背景 |
| eeColorMinimapView | 迷你地图视图 |
| eeColorLinkIpv4 | IPv4 地址 |
| eeColorLinkIpv4Visited | IPv4 地址 (已访问) |
| eeColorLinkIpv6 | IPv6 地址 |
| eeColorLinkIpv6Visited | IPv6 地址 (已访问) |
| eeColorHexColor | 十六进制颜色 \- #ff0080 |
| eeColorRgbColor | RGB 颜色 - rgb(255,0,128) |
| eeColorLineNumberHovered | 行号 (悬停) |
| eeColorRulerHovered | 标尺/列标题 (悬停) |
| eeColorLineNumberSel | 行号 (选取的行) |
| eeColorRulerSel | 标尺/列标题 (选取的列) |
| eeColorLineNumberCurr | 行号 (选区) |
| eeColorRulerCurr | 标尺/列标题 (选区) |
| eeColorOpenFilter | 开启筛选 |
| eeColorMultiSelection | 有多选区的行 |
| eeColorValidatorError | 语法检查错误 |
| eeColorValidatorWarning | 语法检查警告 |
| eeColorValidatorMessage | 语法检查消息 |
| eeColorEvenLines | 偶数行 |
| eeColorInvalidCharacters | 警告字符 |

如果对象是一个搜索列表，项目指定进行搜索的次数。

## 版本

支持 EmEditor 7.00 或之后的版本。
