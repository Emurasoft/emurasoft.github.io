# Q. 怎么变更安装文件夹？

默认设置下，安装新版 EmEditor 的文件夹与旧版的文件夹相同，如果是第一次安装的话，默认的安装文件夹是 %LocalAppData%\\Programs\\EmEditor（按每个用户安装 - “只为我”）或 Program Files\\EmEditor（按每台计算机安装 - ”每个人（所有用户）“）。如果要更改安装文件夹，请使用管理员权限打开命令提示符，然后用 NOSKIP 选项运行安装程序。

例如，如果 EmEditor 安装文件是 emed64\_18.9.3.msi，您想要把 EmEditor 安装到另一文件夹中，请运行以下命令：

msiexec /i emed64\_18.9.3.msi NOSKIP=1

这将使您有机会在安装过程中选择 "Custom"（自定义）按钮，允许您更改安装文件夹。

注意: 您不能更改安装文件夹如果 EmEditor 是按每个用户安装。要变更安装文件夹，您必须选择为所有用户安装 EmEditor 选项。

不同版本的 EmEditor 无法同时存在在一台电脑上。如果旧的版本已经安装了，您必须先卸载旧的版本，或安装新的版本到与旧版本相同的文件夹中。
