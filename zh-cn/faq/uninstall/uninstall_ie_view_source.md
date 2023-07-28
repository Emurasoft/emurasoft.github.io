# Q. 在我卸载 EmEditor 之后，当我在IE浏览器上的上下文菜单中选择“查看源”后，为什么源代码不显示在记事本中？

一些比较早版本的 EmEditor 不能够完全卸载注册信息。您需要右击 **「开始」** 菜单选择 **“运行”**，然后输入“RegEdit.exe”，在点击「确定」键来启用注册表编辑器。请在注册表编辑器中搜索 HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\View Source Editor，然后删除该项。
