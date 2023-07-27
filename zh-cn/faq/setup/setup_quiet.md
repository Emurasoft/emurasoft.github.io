# Q. 怎么能不用显示对话框就安装 EmEditor？

在正常安装的情况下，你会看到屏幕显示对话框指示您完成一系列的安装步骤。但是，如果您想把 EmEditor 安装到公司，团体或个人使用的多台电脑中时，您可以用一个批处理文件或脚本文件让电脑自动完成安装并简化安装步骤。EmEditor 使用 Windows 安装程序来进行安装，所以如果你不想看到对话框的话就可以把它们都屏蔽掉。

假设 EmEditor 的安装文件是 emed64\_20.9.0.msi，请运行以下命令：

msiexec /i "(...path...)emed64\_20.9.0.msi" /passive MSIINSTALLPERUSER=1

这样，EmEditor 在安装时就不会出现任何对话框。如果您想更改默认设置的话，您也可以使用以下的这些选项：

|     |     |
| --- | --- |
| MSIINSTALLPERUSER=1 | 为当前用户指定按用户（即“只为我”）安装（v20.9 或更高版本的默认值）。 |
| MSIINSTALLPERUSER="" | 指定按每台计算机（即“所有用户”）安装（v20.8 或之前版本的默认设置）。 |
| NOCHECKUPDATES=1 | 禁用到 Internet 上查看最新版本 EmEditor 的功能。 |
| NOCONTEXTMENU=1 | 禁用添加一个快捷键到资源浏览器上的上下文菜单中。 |
| DESKTOP=1 | 启用添加一个快捷键到桌面。 |
| NOIEEDITOR=1 | 禁用把 EmEditor 添加至 IE 浏览器 HTML 编辑列表中。 |
| NOIEVIEW=1 | 禁用在 IE 浏览器中用 EmEditor 查看源代码的功能。 |
| NOPATH=1 | 禁止把到 EmEditor 的路径添加到 PATH 环境变量中。 |
| NOSHORTCUT=1 | 禁止添加一个快捷键到程序菜单中。 |
| NOTRAYICON=1 | 禁用托盘图标。 |
| NOTXT=1 | 禁用文本文件关联。 |
| REGNAME=name | 授权用户姓名。 |
| REGKEY=xxxxxx | 输入注册密钥。 |

如果您只想用注册密钥和授权者名字为当前用户安装 EmEditor，请运行下列命令：

msiexec /i "emed64\_20.9.0.msi" /q MSIINSTALLPERUSER=1 REGKEY=xxxxx REGNAME="John Doe"

如果您想用注册密钥和授权者名字为所有用户安装 EmEditor，请使用管理员权限运行命令：

msiexec /i "emed64\_20.9.0.msi" /q REGKEY=xxxxx REGNAME="John Doe"

Windows 安装程序还有许多别的选项。具体信息，请运行：

msiexec /?

来显示一系列可以操作的命令。

## 备注:

在 Windows Vista 或更新的系统上操作时，安装程序一定要在管理员特权上运行，来避免“用户帐户控制”提示。例如，如果您要在命令提示符上运行安装程序，您需要在按SHIFT键的同时右击命令提示符图标来打开命令提示符窗口，然后选择作为管理员运行 程序。此外，您必须指定MSIINSTALLPERUSER="" 才能为所有用户安装 EmEditor v20.9 或更高版本。要仅为当前用户安装 EmEditor v20.8 或更早版本，您必须指定MSIINSTALLPERUSER=1。
