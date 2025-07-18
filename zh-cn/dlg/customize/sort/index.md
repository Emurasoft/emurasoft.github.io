# “排序”页面

排序页面让你能自定义与排序功能相关的设定。

## “快速二进制比较”复选框

如果勾选该选项，快速二进制比较会被用来排序。当该选项被勾选时，区域设置信息会被忽略。

## “平稳排序”复选框

勾选该选项会启用平稳排序。平稳排序维护记录的相对顺序，但通常较慢。

## “忽略大小写”复选框

如果该选项被勾选了，大小写会被忽略。

## “不区分平假名与片假名字符”复选框

如果该选项被勾选了，相应的平假名与片假名字符相等。

## “忽略不占位的组合字符，例如变音符号、dakuten（日文中的浊点）和 handakuten（日文中的半浊点）”复选框

如果该选项被勾选了，EmEditor 会忽略不占位的组合字符，例如变音符号、dakuten（日文中的浊点）和 handakuten（日文中的半浊点）。

## “忽略符号”复选框

如果该选项被勾选了，符号会被忽略。

## “不区分半角与全角字符”复选框

如果该选项被勾选了，半角与全角字符之间的差异会被忽略。全角形式是一种用于中文和日文脚本中的独特格式。

## “将标点符号视为符号”复选框

连字符和撇号被视为正常字符。 这在默认情况下是关闭的，以确保按字母排序时包含连字符或撇号的单词是匹配的。

## “将数字视为序号”复选框

如果该选项被勾选了，即使选择 **字母升序** 或 **字母降序** 命令，数字也会作为序号被排序。例如，"2" 会排在 "10" 之前。

## “对数字进行排序时忽略开头的非数字字符”复选框

如果该选项被勾选了，排序时前导非数字字符会被忽略。

## “当按长度排序时，将全角字符作为 2 个字符排序”复选框

如果该选项被勾选了，当选择 **按文本长度从短到长** 或 **从长到短** 命令时，全角字符会被视为 2 个字符。

## “比较 CSV 文档单元格中未加引号的字符串”复选框

比较 CSV 文档单元格中未加引号的字符串。 例如，当单元格字符串是 _"a""b"_ 时，要比较的实际字符串将是 _a"b_。

## “当存在垂直选择或多重选择时，仅检查选取的字符串”复选框

当存在垂直选择或多重选择时，仅用选取的字符串来排序。

## “按出现次数对相同的字符串进行分组”复选框

如果该选项被勾选了，EmEditor 会按出现次数对相同的字符串进行分组。

## “允许数字分组”复选框

允许对数字进行数字分组。数字分组字符取决于“区域设置”下拉列表框中指定的区域。此选项会影响状态栏上所显示的总和和平均值以及搜索、筛选和排序命令的数字范围表达式。

## “区域设置”下拉列表框

指定用于排序的区域设置。

## “使用默认的日期格式”下拉列表框

指定应使用从当前区域设置派生的日期格式。如果未设置此选项，则应在下面的下拉列表框中指定日期和/或时间格式。

## 「重置」按钮

重置为默认设置。

