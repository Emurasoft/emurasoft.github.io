# Q. 当读取 Macintosh 文本文件时，一些字符无法正常显示。怎样才能正常地读取 Macintosh 文本文件呢？

Macintosh 与 Windows 系统使用的代码页稍有不同。在 Windows 2000/XP/2003/Vista 中，Macintosh 的代码页已经安装了，您能轻松地把 Macintosh 文本文件转换成Windows 文本文件。首先，在 **自定义** 对话框中选择 [**文件编码** 页面](../../dlg/customize/encodings/index.md)，点击 **「新建」** 按钮，然后选择一个 Macintosh 编码，例如“10001 (MAC – Japanese)”。再选择一个适当的字体类别，例如，Japanese(日文)。点击 **“确定”** 两次来关闭对话框。

接着，到 **文件** 下拉单中，选择 [**打开...** 命令](../../cmd/file/file_open)，
选择您要定义的编码，例如，从 **编码** 组合框中选择"10001 (MAC -
Japanese)"，接着选择一个您想要读取的 Macintosh 文件。

在 Windows 98/Me 中，没有安装 Macintosh
的代码页，所以您无法正常读取有特殊字符的 Macintosh 文件，因为 Windows 代码页无法读取这些文件。
