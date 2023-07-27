# 运行宏 (�̳�)

当保存一个宏文件，宏变为默认宏文件，并且，会在下次你选择 [运行宏 命令](../../cmd/macros/quick_macro_run) 时被加载。如果你打开宏 的下拉菜单，你会看到运行 命令的右边出现了"tutorial.jsee" 或 "tutorial.vbee"。另外，如果你把鼠标指针放在「运行宏」 按钮上，你会看到"运行宏 tutorial.jsee" 或 "运行宏 tutorial.vbee"的提示。总之，当要选择宏执行命令时所出现的宏文件名是默认的宏。EmEditor 保存默认宏直到它记录一个新的宏，或选择或保存另一个宏。当您退出 EmEditor 后，再重新打开它，默认的宏保持不变。

现在选择 [新建文本 命令](../../cmd/file/file_new) 来显示一个新的 EmEditor 窗口。然后选择 [运行宏 命令](../../cmd/macros/quick_macro_run)。之前录制的宏会被显示:

"EmEditor supports macros _."_

你想运行该宏几次都可以。

记住，当你录制或选择另一个宏时，你便替换了默认宏，这样你就不能执行上面所显示的之前保存的宏。在这种情况下，你可以用下面的任一方法来运行之前被录制的宏:

1. 点击 [选择宏 命令](../../cmd/macros/macro_select)。在弹出的
In the resulting打开文件 对话框中，选择一个你想要运行的宏文件（在这个教程中，我们选择 tutorial.jsee 或 tutorial.vbee）。然后，通过之前所描述的步骤运行该宏。
2. 点击菜单上的宏。宏 的下拉菜单中包括了已被保存的宏的列表。让我们把该列表称为"我的宏"。你能通过从列表中选择一个来运行指定的宏（在这个教程中，我们选择 tutorial.jsee 或 tutorial.vbee）。

默认情况下，EmEditor 会自动添加已经被录制或选取的宏到我的宏 中。如果你不想要宏被自动添加到我的宏 中，请选择 [自定义宏 命令](../../cmd/macros/customize_macro)。
在 [自定义宏 对话框](../../dlg/macro_customize/index) 的 [选项 页面](../../dlg/macro_customize/options/index) 上，点击清除对 [自定义宏 对话框](../../dlg/macro_customize/index) 上的当保存或选择新的宏时将该宏添加至“我的宏”。 复选框的勾选。这个动作会关闭该功能，这样宏就不会自动被添加到我的宏 中当你保存或选取一个宏时。

同样，如果你想要删除一个宏文件，从 [自定义宏 对话框](../../dlg/macro_customize/index) 中 [我的宏 页面](../../dlg/macro_customize/my_macros/index) 上选择你想要删除的宏文件的名称。然后点击「删除」 按钮。另外，该页面还能让你变更宏文件在宏 下拉菜单中显示的顺序。

如果你想要用键盘上的一个快捷键运行宏，你可以通过 [所有配置属性 命令](../../cmd/tools/all_prop) 或 [当前配置属性 命令](../../cmd/tools/customize) 中的 [键盘 页面](../../dlg/properties/keyboard/index) 给宏分配一个快捷键。

## 下一主题:
