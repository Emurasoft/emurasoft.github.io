# 批处理替换全部和多项替换全部之间的区别

**批处理替换全部** 一次在整个文档中搜索一个字符串，并按搜索字符串的数量重复此过程。 **多项替换全部** 同时搜索所有搜索字符串。这个区别会导致不同的结果，如果搜索/替换字符串配对包含如下示例：

1 → 5

2 → 4

4 → 2

5 → 1

并且如果源文档是：

\[1,2,3,4,5\]

在这个情况下，如果用 **批处理替换全部**，EmEditor 会先把整个文档中的 1 替换为 5，然后再将 2 替换为 4。这样，源文档会变为：

\[5,4,3,4,5\]

接下来，当它将 4 替换为 2 时，请注意它将替换两个 4（第二个和第四个数字）。最后，当它将 5 替换为 1 时，它将替换两个 5（第一个和最后一个数字）。因此，结果将是：

\[1,2,3,2,1\]

如果使用新的 **多项替换全部**，EmEditor 将同时替换所有字符串。因此，结果将是：

\[5,4,3,2,1\]

**多项替换全部** 的执行速度会比 **批处理替换全部** 快很多。在我们的测试中， **多项替换全部** 的速度比 **批处理替换全部** 快 6310 倍，当搜索/替换配对有 100 万个时。（请参考 [Version 21.7](../../history/v21_7) 中的测试结果）。

**多项替换全部** 不支持正则表达式，数字范围，或包含换行的字符串。
