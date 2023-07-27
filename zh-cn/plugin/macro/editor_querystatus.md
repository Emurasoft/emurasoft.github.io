# Editor\_QueryStatus

查询命令的状态，无论命令是否被启用，也不管命令是否处于被选中的状态。你能直接用该内联函数或明确地发送 [EE\_QUERY\_STATUS](../message/ee_query_status) 消息。

Editor\_QueryStatus( HWND hwnd, UINT nCmdID, BOOL\* pbChecked );

## 参数

_hwnd_

指定 EmEditor 视图或框架的窗口句柄。

_nCmdID_

状态被查询的命令的标识符。请参考
[命令 ID](../cmdid/index)。

_pbChecked_

指针指向一个接收勾选状态的变量（TRUE 表示所选命令已被选中，FALSE 则表示所选命令没有被勾选）。

## 返回值

如果命令被启用，返回值就不是零。如果命令没有被启用，返回值是零。
