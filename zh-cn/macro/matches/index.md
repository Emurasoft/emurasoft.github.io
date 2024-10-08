# Matches 集合

Matches 集合提供一集合的正则表达式搜索结果的 [Match 对象](../match/index)。该集合由作为完全匹配项的第一项 (向后引用 0)，以及子匹配项 (向后引用 1, 2, 3, ...) 构成。

## 属性

|     |     |
| --- | --- |
| **[Count](count)** | 检索 Match 对象的数目。 |
| **[Item](item)** | 按指定索引检索 Match 对象。Item(0) 返回完全匹配项 (向后引用 0), Item(1) 返回向后引用 1。 |

## 版本

支持 EmEditor Professional Version 15.9 或之后的版本。

```{toctree}
:hidden:
:maxdepth: 1
count
item
```