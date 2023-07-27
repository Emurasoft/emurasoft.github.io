# 变更选取范围 (�̳�)

要更改选取范围，添加第六行到我们所示范的宏中:

## 

### \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
```

### \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
保存该宏并在一个新的 EmEditor 窗口中运行它。注意，"text edit" 部分会如下图所示被高亮显示:
text editor.
我们把 true 传递到CharRight 方法 的第一个参数中，这样就变更了光标位置并且改变了选取范围；你也可以当按住 SHIFT 键的同时按右箭头键来进行相同的操作。
同样，许多光标移动方法接收参数来变更选取范围（详见 [移动光标](tutorialmove)）。
更多变更选取范围的可用方法:
|     |     |
| --- | --- |
|[SelectAll](../selection/selectionselectall) | 选择整个文本。等同于 CTRL + A 键。 |
|[SelectLine](../selection/selectionselectline) | 选择光标所在处的行。 |
|[SelectWord](../selection/selectionselectword) | 选择光标位置处的整个单词。 |
|[Collapse](../selection/selectioncollapse) | 关闭当前选项。等同于 ESC 键。 |
你能用下列属性安装或检查选取范围的状态:
|     |     |
| --- | --- |
|[IsActiveEndGreater](../selection/selectionisactiveendgreater) | 显示活动点是否与选取范围的结尾部分匹配。 |
|[IsEmpty](../selection/selectionisempty) | 显示是否选取范围为空。 |
|[Mode](../selection/selectionmode) | 获取或安装选择类型（垂直选择，行选择等等）。 |
```

## 下一主题:
