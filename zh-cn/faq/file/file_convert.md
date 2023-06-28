# Q. 怎么用命令行转换文件编码？

您可以参考使用下列的命令行选项:

/cp Encoding --- 设定一个编码来打开文件。sets an encoding to open as.

/cps Encoding --- 设定一个编码来保存文件。

/sa "DestFile" --- 指定一个文件名来另存为在转换编码后。

/ss+ --- 用Unicode签名(BOM)来保存文件在转换编码后。

/ss- --- 不用Unicode签名(BOM)来保存文件在转换编码后。

例如，如果您想要把一个文件编码从Western European (iso-8859-1)转换为UTF-8，可以使用下面的语法:

emeditor.exe "windows1252.txt" /cp 1252 /cps 65001 /ss- /sa "utf8.txt"

又或者，如果您想要把一个文件，Chinese.txt，从简体中文(GB2312)转换成UTF-8，并且想把文件重命名为utf8Chinese，您可以使用如下所示的语法:

emeditor.exe “Chinese.txt” /cp 936 /cps 65001 /ss- /sa “utf8Chinese.txt”

请参考 [编码常数](../../macro/const/const_encoding) 查找编码。

请参考 [使用命令行选项](../../howto/file/file_commandline) 获取更多信息。