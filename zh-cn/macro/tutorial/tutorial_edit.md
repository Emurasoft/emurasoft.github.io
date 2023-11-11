# 编辑宏 (教程)

EmEditor 会自动把最后的宏作为默认宏。所有，如果要编辑默认宏，选择 [**编辑宏** 命令](../../cmd/macros/macro_edit) 即可。默认的宏会在一个新的 EmEditor 窗口中被打开。如果你想要打开非默认的宏文件，执行 [**选择宏** 命令](../../cmd/macros/macro_select)，然后选择你想要编辑的宏。这个动作会把你所选取的宏设为默认。然后，你便能通过选择 [**编辑宏** 命令](../../cmd/macros/macro_edit) 来编辑该宏。在这个教程中，我们会编辑 tutorial.jsee 或 tutorial.vbee。当打开这两个文件中的一个时，会分别出现下列文本:

## 

### \[JavaScript\]

```
document.selection.Text="EmEditor supports macros.";
```

### \[VBScript\]

```
document.selection.Text="EmEditor supports macros."
```
上面的代码用[Text 属性](../selection/selection_text) 告诉 EmEditor 在当前光标位置处插入 "EmEditor supports macros." 文本。
