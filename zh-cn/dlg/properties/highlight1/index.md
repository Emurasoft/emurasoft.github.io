# “高亮（1）”页面

**高亮（1）** 页面让你能设置与高亮（1）相关的属性。

## “启用关键词高亮”复选框

如果勾选了该复选框，EmEditor 会启用关键词高亮。

## “启用关键词高亮”下拉列表框

指定要高亮的关键词类型。你可以从下列的几个选项中选择。

|     |     |
| --- | --- |
| **仅用户定义的字符串** | 仅高亮在“用户定义的字符串”列表框中指定的字符串。 |
| **仅默认关键词** | 仅高亮默认配置关键词。 |
| **用户定义的字符串和默认关键词** | 高亮用户定义的字符串和默认配置关键词。 |

## “用户定义的字符串”列表框

用户自定义的要高亮的字符串列表。单击字符串前面的复选框会改变高亮颜色。复选框中的数字分别与在 [**显示** 页面](../display/index) 中指定的高亮颜色相对应。

## 「添加」按钮

点击该按钮添加一个新的条目到列表中。

## 「删除」按钮

点击该按钮从列表中删除被选取的条目。

## 「添加默认」按钮

点击该按钮添加默认关键词到列表中。

## “全词匹配时高亮”复选框

高亮被选取的字符串仅当整个词都符合时。

## “高亮单词及其右侧文本”复选框

高亮被选取的单词以及单词的右边直到单词所在行换行位置处。

## “高亮单词及其右侧区域”复选框

高亮被选取的单词以及单词的右侧直到窗口边框（如果按窗口换行或不换行被选取的话），或者到被指定的宽度或页面宽度处。

## “区分大小写”

高亮被选取的单词只有当大小写都符合时。

## “仅在标记内”复选框

高亮字符串只有当字符串在一个标记内时。

## “正则表达式”复选框

用正则表达式高亮被选取的字符串。

## “颜色”列表框

指定要高亮显示所选字符串的颜色。

## “开始标记”文本框

标记的开头字符。你能设置每个要被高亮的字符串只有当它在标记内时。

## “结束标记”文本框

标记的结尾字符。你能设置每个要被高亮的字符串只有当它在标记内时。

## 「导入」按钮

从 CSV 或 ESY 文件中导入被高亮的字符串。CSV 文件内容按字符串， **颜色**， **全词匹配**， **高亮右边**， **区分大小写**，还有 **仅在标记内** 整理。有关ESY 文件语法可以参考下面的页面。

**请参考**

- [创建一个新的语法文件](../../../howto/customize/syntax_file)

## 「导出」按钮

导出高亮的字符串到 CSV 或 ESY 文件中。CSV 文件内容按字符串， **颜色**， **全词匹配**， **高亮右边**， **区分大小写**，还有 **仅在标记内** 整理。有关ESY 文件语法可以参考下面的页面。

**请参考**

- [创建一个新的语法文件](../../../howto/customize/syntax_file)

## 「重置」按钮

重置为默认设定。会显示 [**重置** 对话框](../reset/index) 并让你能从另一个配置复制设定。

