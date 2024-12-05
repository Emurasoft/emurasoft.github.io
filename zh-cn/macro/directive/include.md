# \#include 指令 (脚本指令)

指定要包括的文件。该指令必须在脚本的第一行，即主代码上面指定。

#include "_filename_"

## 参数

_filename_

用从当前宏文件的相对路径或完整路径上指定要包括的文件。如果路径被省略，指定当前的宏文件所在的文件的标题。

## 示例

包括文件 library.jsee

#include "library.jsee"

## 版本

支持 EmEditor 7.00 or latere
