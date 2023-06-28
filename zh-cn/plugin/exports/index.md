# 导出函数

|     |     |
| --- | --- |
| OnCommand( HWND hwnd ) | 插件已从菜单或工具栏中被选择。 |
| QueryStatus( HWND hwnd, LPBOOL pbChecked ) | 查询插件的状态，命令是否被启用以及插件是否在检查状态。 |
| OnEvents( HWND hwnd, UINT nEvent, LPARAM lParam ) | 当一个状态被改变时，可以用 [事件](../event/index) 参数调用该函数。 |
| GetMenuTextID() | 检索插件菜单条目文本的资源 ID。 |
| GetStatusMessageID() | 检索用 \\n 把工具栏上的提示文本与状态栏文本合并的资源 ID。 |
| GetBitmapID() | 获得显示在工具栏上的插件的位图资源 ID。 |
| PlugInProc( HWND hwnd, UINT nMsg, WPARAM wParam, LPARAM lParam ) | 用 [插件消息](../plugin_message/index) 来检索或设置设定。 |

这些导出函数必须通过这个顺序在一个 DEF 文件中定义。当你编译它们时，你需要选择 \_stdcall 作为调用方式。有关更多插件示例的信息，请访问 EmEditor 网站的资源库。
