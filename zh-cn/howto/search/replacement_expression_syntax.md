# 替换表达式语法

当用正则表达式或数字范围取代时，可以用替换表达式。

下列表达式是可用于 **替换** 对话框以及 **在文件中替换** 对话框中的 **替换为** 文本框内。

| | |
| --- | --- |
| \\0 | 把整个正则表达式作为指定为向后引用。 |
| \\1 - \\9 | 指定一个向后引用 \- 一个向后引用是上一个被匹配的子表达式的引用。引用的内容是与子表达式相匹配的内容，而不是表达式本身。一个向后引用由转义符 "\\" 加一个 "1" 到 "9" 的数字组成。"\\1" 指的是第一个子表达式，"\\2" 是第 2 个，以此类推。 |
| $10, $11, $12, ... | 表示超过 9 个的向后引用。相当于 \\k<10>，\\k<11>，\\k<12>，...。 |
| \\k<name> | 表示一个已命名的向后引用。已命名的向后引用是用以下形式引用之前匹配的已命名的捕获组：(?<name>expression)。如果 "name" 是一个数字，则它表示一个已编号的向后引用，相当于 \\1，\\2，\\3，...。 |
| \\n | 一个换行符。 |
| \\r | 在 **在文件中替换** 表示一个回车符。请参考 [指定换行符](search_nl)。 |
| \\t | 一个 tab。 |
| \\L | 强制所有后续替换字符要小写。 |
| \\U | 强制所有后续替换字符要大写。 |
| \\H | 强制所有后续替换字符要是半角字符。 |
| \\F | 强制所有后续替换字符要是全角字符。 |
| \\Nc | 强制使用 [Unicode 标准化表单 C（规范组成）](../../cmd/edit/unicode_norm_fc) 转换所有后续替换字符。 |
| \\Nd | 强制使用 [Unicode 标准化表单 D（规范分解）](../../cmd/edit/unicode_norm_fd) 转换所有后续替换字符。 |
| \\NC | 强制使用 [Unicode 标准化表单 KC（兼容性组成）](../../cmd/edit/unicode_norm_fkc) 转换所有后续替换字符。 |
| \\ND | 强制使用 [Unicode 标准化表单 KD（兼容性分解）](../../cmd/edit/unicode_norm_fkd) 转换所有后续替换字符。 |
| \\E | 关闭之前的 \\L，\\U，\\F，\\H，\\Nc，\\Nd，\\NC，或 \\ND。 |
| \\J | 指定表达式使用 JavaScript。\\J 必须放在替换表达式的开头。可以与反向引用结合使用。还可以在脚本中使用 **cell** 函数。例如，<table><tbody><tr><th>替换表达式</th><th>含义</th></tr><tr><td>\J&quot;\0&quot;+&quot;abc&quot;</td><td>合并匹配字符串与&quot;abc&quot;</td></tr><tr><td>\J&quot;\0&quot;.substr(0,5);</td><td>返回匹配字符串的前5个字符</td></tr><tr><td>\J\0*100;</td><td>将匹配的数字乘以100</td></tr><tr><td>\JparseFloat(\0).toFixed(2);</td><td>将匹配的数字四舍五入到小数点后2位</td></tr><tr><td>\Jcell(-1)</td><td>返回位于匹配单元格左侧相邻单元格中的文本</td></tr><tr><td>\JparseFloat(cell(-1))+parseFloat(cell(-2))</td><td>返回左侧两个相邻单元格的总和</td></tr></tbody></table>
| \\V | 与 \\J 相同，只是 \\V 使用 **V8 JavaScript** 引擎而不是 **Chakra** 引擎。 |
| \\D | 如果 [**数字范围表达式**](number_range_syntax) 的日期/时间类型用于匹配字符串，则此表达式可以指定日期格式。它可以与 **\\T** 结合使用。 [查看可用的日、月、年格式图片。](https://docs.microsoft.com/en-us/windows/win32/intl/day--month--year--and-era-format-pictures) 例如，如果匹配的日期/时间是 "2022-03-31 21:30":（示例的语言环境是英语（美国））<table><tbody><tr><th>替换表达式</th><th>结果</th></tr><tr><td>\DM/d/yyyy</td><td>3/31/2022</td></tr><tr><td>\DMMMM,d,yyyy</td><td>March31,2022</td></tr><tr><td>\D'month='M'day='d\THH:mm</td><td>month=3day=3121:30</td></tr></tbody></table>
| \\T | 如果 [**数字范围表达式**](number_range_syntax) 的日期/时间类型用于匹配字符串，则此表达式可以指定时间格式。它可以与 **\\D** 结合使用。 [查看可用小时、分钟 , 和第二种格式的图片。](https://docs.microsoft.com/en-us/windows/win32/intl/hour--minute--and-second-format-pictures) 例如，如果匹配的日期/时间是   "2022-03-31 21:30":（示例的语言环境是英语（美国））<table><tbody><tr><th>替换表达式</th><th>结果</th></tr><tr><td>\DM/d/yyyy</td><td>3/31/2022</td></tr><tr><td>\DMMMM,d,yyyy</td><td>March31,2022</td></tr><tr><td>\D'month='M'day='d\THH:mm</td><td>month=3day=3121:30</td></tr></tbody></table>
| (?Ntrue\_expression:false\_expression) | 如果匹配子表达式 N，则评估 true\_expression 并将其发送到输出，否则评估 false\_expression 并将其发送到输出。例如，(?1foo:bar)，如果匹配子表达式 \\1，会用 foo替换每个匹配，反之则用 bar。另外，您也可以用这种方式写该表达式：(?{1}foo:bar) |
| $(Path) | 文件路径。 |
| $(Dir) | 文件目录。 |
| $(Filename) | 不带扩展名的文件名。 |
| $(FilenameEx) | 带扩展名的文件名。 |
| $(Ext) | 扩展名。 |
| $(Lines) | 行数（不能用于 **在文件中替换**）。 |
| $(CsvColumns) | CSV 列数（不能用于 **在文件中替换**）。 |

## cell 函数 (beta)

如果指定了 **\\J**，则可以在 JavaScript 中使用 **cell** 函数。此函数检索指定 CSV 单元格中的文本。

### 

#### \[JavaScript\]

```
str =cell( iColumn [, yLine [, flags ] ] );
```

### 参数

_iColumn_

指定要检索的文本的列的索引，以从当前位置出发的相对位置表示，除非在 _flags_ 中指定了 8。

_yLine_

指定要检索的文本的行号，以从当前位置出发的相对位置表示，除非在 _flags_ 中指定了 8。 如果省略，则指定 0。

_flags_

指定以下值的组合。0，1 和 2 不能一起使用。如果省略，则指定 1。

|     |     |
| --- | --- |
| 0 | 返回的文本可以不包括包围的双引号或分隔符。 |
| 1 | 返回的文本可以包括包围的双引号但不包括分隔符。 |
| 2 | 返回的文本可以包括包围的双引号和分隔符。 |
| 8 | _iColumn_ 和 _yLine_ 参数以 1 为基础的绝对值表示。 |

## 注意

EmEditor 中没有当前 JavaScript/ECMAScript 中的许多新方法。替换表达式使用 Chakra（相当于 Microsoft Edge Legacy），并且最多支持到 ECMAScript 5.1，因此不支持 ECMAScript 5.1 之后引入的新方法。

## 请同样参考

- [正则表达式语法](search_regexp_syntax)
