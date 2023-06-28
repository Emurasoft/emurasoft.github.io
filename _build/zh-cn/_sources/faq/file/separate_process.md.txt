# Q. EmEditor 被指定为另一个应用程序的外部文本编辑器。为什么在 EmEditor 中做的改变没有在这个应用程序中显现出来？

如果 EmEditor 被设定为另一个应用程序(例如邮件客户端)的外部文本编辑器，并且这个应用程序监控着 EmEditor 的操作，这个程序很有可能不会反映用 EmEditor 保存并修改的内容。要解决这个问题，请用 [/sp (分离)选项](../../howto/file/file_commandline)
在单独的进程中启动 EmEditor (具体操作方式是: 右击Windows「开始」菜单－>点击“运行”－>输入”emeditor /sp”)。要注意的是在这种情况下，每一个 EmEditor 窗口都会作为单独的群组显示。