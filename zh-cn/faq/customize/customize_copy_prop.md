# Q. 怎么把配置属性中的设定复制到另一台电脑上？

如果您使用的是EmEditor v5 或v5后的版本，你可以到“工具”菜单下的“导入和导出”中，根据自己的需求选择导出当前设置的方式，然后在另一台电脑上导入设置。

对于EmEditor v5 之前的版本，您需要用注册表编辑器(Regedit.exe)把HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3 项写入一个文件中，把这个文件复制到另一台电脑上，然后通过注册表编辑器读取文件。 您可能需要通过手动在 **“属性”** 中来变更文件夹名称。
