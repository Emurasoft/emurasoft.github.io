# Q. 我想要在命令提示符中用一个外部工具编译已打开的文件，但是在编译完成后如何能让命令提示符窗口保持开启？

选择“外部工具”子菜单下的 [**“自定义工具”** 命令](../../cmd/tools/customize_tools)，点击 **「新建」** 按钮并在 **“命令”** 文本框中输入"cmd.exe"，然后在 **“参数”** 文本框中输入 _"_/k "filename" $(Path)"。
