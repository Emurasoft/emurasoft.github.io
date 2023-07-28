# OutputBar 对象

## 属性

|     |     |
| --- | --- |
| **[CurrentDirectory](current_directory)** | 为输出栏设置当前目录。 |
| **[Visible](visible)** | 显示或隐藏输出栏。 |
| **[Text](text)** | 在输出栏中检索整个文本。 |

## 方法

|     |     |
| --- | --- |
| **[Clear](clear)** | 清除输出栏的内容。 |
| **[SetFocus](set_focus)** | 把键盘焦点设置到输出栏上。 |
| **[write](write)** | 追加一个字符串到输出栏上。 |
| **[writeln](writeln)** | 追加一个字符串和一个新行到输出栏上。 |

## 示例

### \[JavaScript\]

```
OutputBar.Clear();
OutputBar.writeln( "Hello!" );
OutputBar.Visible = true;
OutputBar.SetFocus();
```

### \[VBScript\]

```
OutputBar.Clear
OutputBar.writeln "Hello!"
OutputBar.Visible = True
OutputBar.SetFocus
```

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:maxdepth: 1
clear
current_directory
set_focus
text
visible
write
writeln
```
