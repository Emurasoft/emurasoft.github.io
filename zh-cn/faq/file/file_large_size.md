# Q. 怎么能加速打开一个大文件呢？

一些配置会降低程序运行的速度。请检查以下几点:

- 点击工具 菜单下的[当前配置属性](../../dlg/properties/index)，点选 [常规 页面](../../dlg/properties/general/index)。
如果
“自动换行”下拉
列表框中不是“不换行”，那就可能降低 EmEditor 的运行速度，因为 EmEditor 要计算哪里要换行。所以当您要打开大文件时，请选择“不换行”或 [不换行 命令](../../cmd/view/wrap_none).
