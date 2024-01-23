# 在文件中查找 (教程)

要在文件中查找，添加第八行到我们所示范的宏中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!");
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"
```
保存该宏并在一个新的 EmEditor 窗口中运行它。现在 "Em" 被搜索并且出现显示有 "Found!" 的消息框。
[Find 方法](../selection/selection_find) 的第一个参数指定一个要搜索的字符串；第二个参数指定要告知它如何搜索的标志。在这个例子中，第二个参数是 eeFindPrevious，即从当前光标位置向前搜索到该文件的顶部。
[Find 方法](../selection/selection_find) 返回 1 如果搜索字符串被找到。不然，则返回 0。在这个例子中，搜索字符串被找到，返回 1，因此执行 Then 子句，即 [alert 方法](../window/window_alert)。
[alert 方法](../window/window_alert) 显示一个简单的带有「OK」按钮的消息框以及该参数的字符串。在我们的示例中，它会显示文本 "Found!"。
[Find 方法](../selection/selection_find) 的第二个参数让你能指定一系列的标志。更多说明请详见 [Find 方法](../selection/selection_find)。
通常不会终止执行一个宏当没有找到搜索字符串。但是，有一个例外。如果你用宏 菜单下的使用临时选项运行 命令，并在弹出的对话框中勾选了搜索失败即停止 复选框，那么就会终止执行宏当没有找到搜索字符串时。
使用临时选项运行 让你能用更灵活的方式进行搜索。例如，如果你想要重复一个操作，比如搜索和替换，并且你不知道操作会发生几次，你可以不用修改宏，勾选搜索失败即停止 复选框，并输入一个比你认为你所需要的重复操作次数多的数字。
如果你想不用使用临时选项运行 命令就终止宏当搜索失败时，那么你需要修改该宏。即，当 [Find 方法](../selection/selection_find) 返回 0，你会终止该宏。下列的代码可以做到:

### \[JavaScript\]

```
if( !document.selection.Find( "xx", eeFindPrevious ) )  throw new
Error("Cannot find xx");
```

### \[VBScript\]

```
If Not document.selection.Find( "xx", eeFindPrevious )  Then Err.Raise
vbObjectError + 1, "Find Error", "Cannot find xx"
```

另外，如果你用 [FindRepeat 方法](../selection/selection_findrepeat)，你能再次搜索你之前搜索过的字符串，并且你能搜索光标所在位置的单词。
如果你如下指定了 [FindRepeat 方法](../selection/selection_findrepeat) 的标志，它会执行搜索，并有相对应的键盘快捷键。
|     |     |
| --- | --- |
| eeFindRepeatNext | 从光标位置向下再次搜索你之前搜索过的字符串。等同于 F3。 |
| eeFindRepeatPrevious | 从光标位置向上再次搜索你之前搜索过的字符串。等同于 Shift + F3。 |
| eeFindRepeatNext + eeFindRepeatWord | 从光标位置向下搜索被选取的字符串或光标处的单词。等同于 CTRL + F3。 |
| eeFindRepeatPrevious + eeFindRepeatWord | 从光标位置向上搜索被选取的字符串或光标处的单词。等同于 CTRL + SHIFT + F3。 |
