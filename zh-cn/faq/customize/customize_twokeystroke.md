# Q. 怎么定义两次按键的键盘快捷方式？

您可以通过整合用户菜单功能和键盘映射功能来定义两次按键的键盘快捷方式。通过定义用户菜单(1)，CTRL+K 已经被预先设置为第一个两次按键的键盘快捷方式。

一些系统预先定义的快捷键包括:

CTRL+K, K 切换书签

CTRL+K, N 当前文档中的下一个书签

CTRL+K, P 当前文档中的上一个书签

CTRL+K, L 清除当前文档中的所有书签

CTRL+K, C 注释选定内容

CTRL+K, U 取消注释选定内容

在这个列表中，在您按第二个键之前，可以按也可以不按CTRL键。例如，切换书签指令的快捷方式是先按CTRL键和K键，然后您可以再按一下K键，或再按一下CTRL键和K键。两种方式都可以。

添加新的两次按键的键盘快捷方式:

1\. 到帮助菜单下选择 **“键盘布局”**.

2\. 如果您想要所有 EmEditor 的配置都使用同样的快捷方式的话，点击工具栏上的 **「键盘布局设置」** 按钮，选择 **“所有配置”**（或取消选择“所有配置”如果您不想快捷方式通用的话）。

3\. 在列表中查找“用户菜单(2)”并双击符合条目。

4\. 在弹出的 **“配置属性”** 对话框中，输入一个快捷键到 **“按下新的快捷键”** 文本框中。例如， CTRL+;。

5\. 点击 **「分配」** 按钮，然后点击「确定」。

6\. 关闭“键盘布局”窗口。

7\. 在 **工具** 菜单下选择 **“自定义菜单”**。

8\. 在“需要定义的菜单列表”下选择“用户菜单(2)”。

9\. 点击 **「插入右边」** 按钮。

10\. 在弹出的 **“菜单属性”** 对话框中，选择一个要添加快捷键的命令。

11\. 在对话框中的 **“名称”** 文本框中，用 & 指定一个新的快捷键。

12\. 在 & 的右边输入字符，这个字符代表第二次要按的快捷键。

例如，如果您想要给 **“新建并粘贴”** 命令设置一个两次按键的快捷方式并把"N"设置为第二个快捷键，操作如下:

1\. 在“菜单属性”对话框中的“类别”组合框中，选择 **“文件”**。

2\. 在“命令”组合框中选择 **“新建并粘贴”**。

3\. 在 **“名称”** 文本框中输入: **&New and Paste**。

4\. 点击「确定」。

重复以上的步骤，您就可以给许多的命令设置快捷键。

在默认情况下，用户菜单会在按第一个键的1秒后出现。第二个快捷键在用户菜单出现之前有效。您可以到 **“自定义菜单”** 中移动 **“延时”** 滑块，让菜单出现的时间延长。
