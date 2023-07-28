# 录制宏 (教程)

要录制一个宏，选择 [开始/停止宏录制 命令](../../cmd/macros/quick_macro_record)。
鼠标指针会变为一个摄像机图标，表示宏录制开启。在这个状态下，你能在 EmEditor 中录制大部分的操作。让我们通过输入下列文字开始教程:

"EmEditor supports macros."

在输入文本后，再次选择 [开始/停止宏录制 命令](../../cmd/macros/quick_macro_record)。
摄像机图标会变回原来的 Windows 鼠标指针。

我们已经录制了插入 _"EmEditor supports macros."_ 文本到 EmEditor 中。

我们把这个称为一个 "临时宏" 因为还没有保存这个宏（它只是被临时地保存在 Windows 注册表中）。你能执行该临时宏通过选择
[运行宏 命令](../../cmd/macros/quick_macro_run)。临时宏会一直被程序储存直到录制一个新的宏操作为止，并且你想执行几次都可以。当你退出 EmEditor 后再重新打开它，临时宏仍然可用。

一个临时宏可提供一种快捷、方便的自动化任务的方式。如果你想要录制并执行多个宏，你需要保存宏
(请查看[保存宏](tutorial_save))。

## 提示

EmEditor 能记录包括键盘和鼠标指针移动的大多数操作。

## 下一主题:
