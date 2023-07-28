# \#status 指令 (脚本指令)

指定当前宏的状态（是否启用宏以及是否勾选）应该模拟由 ID 指定的命令。 宏菜单以及宏工具栏根据这个指定的命令状态更新宏状态。 此指令必须在脚本的第一行，即主代码上面指定。

#status = _id_

## 参数

_id_

指定用于查询状态的命令 ID 的整数值。 此值等同于 QueryStatusByID 方法的 _nID_ 参数。

## 示例

该宏模拟自动复制命令 (ID = 3979)。当启用自动复制功能时，会选中宏菜单和工具栏上的按钮。当关闭自动复制功能时，不会选中宏菜单和工具栏上的按钮。

### \[JavaScript\]

```
```

#status = 3979

editor.ExecuteCommandByID(3979);   // 3979 = EEID\_AUTO\_COPY

## 

### \[VBScript\]

```
```

#status = 3979

editor.ExecuteCommandByID 3979   ' 3979 = EEID\_AUTO\_COPY

## 版本

支持 EmEditor Professional Version 16.4 或之后的版本。
