# Shell 对象

## 属性

|     |     |
| --- | --- |
| **[ForegroundWindow](foreground_window)** | 检索当前置前窗口。 |
| **[KeepRunning](keep_running)** | 检索或设置标志以在使用 V8 时继续运行宏。 |
| **[windows](windows)** | 返回顶层窗口集合。 |

## 方法

|     |     |
| --- | --- |
| [**CreateFolder**](create_folder) | 创建一个文件夹。 |
| [**DeleteFile**](delete_file) | 删除一个或多个指定的文件。 |
| [**DeleteFolder**](delete_folder) | 删除一个或多个指定的文件夹及其内容。 |
| [**FileExists**](file_exists) | 如果指定文件存在则返回 true；如果没有，则为 false。 |
| **[FindWindow](find_window)** | 通过一个类名和/或窗口标题查找顶层 Window 对象。 |
| [**FolderExists**](folder_exists) | 如果指定文件夹存在则返回 true；如果没有，则为 false。 |
| [**GetFileAttributes**](get_file_attributes) | 返回指定文件或文件夹的属性。 |
| [**Run**](run) | 在新进程中运行程序。 |
| **[SendKeys](send_keys)** | 发送一个或多个键击（或鼠标活动）到活动窗口中。 |
| [**SetFileAttributes**](set_file_attributes) | 设置指定文件或文件夹的属性。 |

## 版本

支持 EmEditor 7.00 或之后的版本。


```{toctree}
:hidden:
:maxdepth: 1
create_folder
delete_file
delete_folder
file_exists
find_window
folder_exists
foreground_window
get_file_attributes
run
send_keys
set_file_attributes
windows
```
