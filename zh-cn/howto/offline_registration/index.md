# 离线注册

使用[产品注册对话框](../../dlg/regist/index)进行注册需要互联网连接。

如果您在在线注册过程中遇到错误信息“请求错误：发送请求的 URL… 找不到这样的主机。”，请确保您的防火墙允许 `EmEditor.exe` 通过端口 80 和 443 访问 `support.emeditor.com`。

如果您想在没有互联网连接的情况下注册 EmEditor，可以使用离线注册功能。离线注册要求 EmEditor 版本 24.3.0 或更高。

离线注册在注册过程中使用授权文件。授权文件通过电子邮件发送给客户。请按照以下步骤，使用离线授权注册 EmEditor。

1. 使用[联系表单](https://zh-cn.emeditor.com/support/#contact)请求授权文件。在表单中，请使用您在 [Emurasoft 用户中心](https://support.emeditor.com/)使用的电子邮件地址。包括您的注册密钥或 [Stripe 订阅 ID](https://support.emeditor.com/en/account/subscriptions)。
2. 我们将通过电子邮件回复您的请求，邮件中附有授权文件。将授权文件下载到本地磁盘中一个不需要管理员权限访问的文件夹中。
3. 如果您尚未安装 EmEditor，请安装 EmEditor。安装时无需添加 [`REGKEY`](https://www.emeditor.com/faq/installation-faq/how-can-i-install-emeditor-without-displaying-dialog-boxes/) 选项。
4. 如果您已经注册了 EmEditor，请使用[注册信息](../../dlg/registration_info/index)取消注册。
5. 关闭 EmEditor。使用[命令行选项](https://www.emeditor.org/zh-cn/howto/file/file_commandline.html#options) `/ol "licenseFilePath"`，其中 `licenseFilePath` 是授权文件的绝对路径。以下是命令示例。
```
EmEditor.exe /ol "C:\Users\Example\emeditorLicenseFile-a7PT7Au3TOelfK1w.txt"
```

6. 打开 EmEditor 并查看[注册信息](../../dlg/registration_info/index)，确认离线注册是否成功。授权文件现在可以删除，因为不再需要用它激活 EmEditor。

## 技术信息

关于离线注册的内部细节可以[在这里](https://www.emeditor.com/general/new-validation-system-explained/)查看。
