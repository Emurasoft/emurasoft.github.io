# 事件

|     |     |
| --- | --- |
| EVENT\_CARET\_MOVED | 光标位置被移动。 |
| EVENT\_CHANGE | 文本被更改。 |
| EVENT\_CHAR | 插入一个字符。LOWORD (lParam) 表示插入的 Unicode 字符代码。 |
| EVENT\_CLOSE | 在关闭 EmEditor 之前或该插件被释放前立即调用。一个插件应该释放资源，并使 DLL 文件可以被删除。 [OnEvents 函数](../exports/index) 的第一个参数 hwnd 会是 NULL。这个事件不代表该插件实际上会被释放。 |
| EVENT\_CLOSE\_FRAME | 当关闭一个 EmEditor 框架窗口时被调用（支持 EmEditor 5.00 或之后的版本）。 |
| EVENT\_CONFIG\_CHANGED | 当前配置属性被更改。 |
| EVENT\_CREATE | 在 启动 EmEditor 或该插件被加载时立即调用。LOWORD(lParam) 代表该插件本身的命令 ID。 |
| EVENT\_CREATE\_FRAME | 当新建一个 EmEditor 框架窗口时被调用。这个事件在启用或禁用标签页时也会被调用。LOWORD(lParam) 代表该插件本身的命令 ID（支持 EmEditor 5.00 或之后的版本）。 |
| EVENT\_CUSTOM\_BAR\_CLOSED | 当关闭一个自定义分栏时被调用。EmEditor 调用 DestroyWindow() 到客户端窗口上，当一个自定义分栏被关闭。lParam 代表一个指针指向 [CUSTOM\_BAR\_CLOSED\_INFO 结构](../structure/custom_bar_close_info)（支持 EmEditor 6.00 或之后的版本）。 |
| EVENT\_CUSTOM\_BAR\_CLOSING | 当关闭一个自定义分栏时被调用。lParam 代表存储个指针到 [CUSTOM\_BAR\_CLOSED\_INFO 结构](../structure/custom_bar_close_info) 中（支持 EmEditor 6.00 或之后的版本）。 |
| EVENT\_DOC\_CLOSE | 当一个文档要被关闭时被调用。lParam 代表存储一个处理 (HEEDOC) 到正在关闭的文档中（支持 EmEditor 5.00 或之后的版本）。 |
| EVENT\_DOC\_SEL\_CHANGED | 当一个活动的文档发生更改时被调用（支持 EmEditor 5.00 或之后的版本）。 |
| EVENT\_DROPPED | 一个文件被拖放到 EmEditor 框架窗口中。 |
| EVENT\_FILE\_OPENED | 打开一个文件。 |
| EVENT\_HISTORY | 每次更改文本时被调用。lParam 代表存储一个指针到 HISTORY\_INFO 结构中。 |
| EVENT\_IDLE | 当闲置时调用。（支持 EmEditor 6.00 或之后的版本）。 |
| EVENT\_KILL\_FOCUS | 失去焦点。 |
| EVENT\_LANGUAGE | 更改 UI 语言。 |
| EVENT\_MODIFIED | 修改状态被改变。 |
| EVENT\_SAVING | 文档要被保存时。lParam 代表存储一个处理 (HEEDOC) 到正被保存的文档中（支持 EmEditor 8.00 或之后的版本）。 |
| EVENT\_SCROLL | 滚动栏位置被更改。 |
| EVENT\_SEL\_CHANGED | 文本的选区被更改。 |
| EVENT\_SET\_FOCUS | 焦点已被设定。 |
| EVENT\_TAB\_MOVED | 当移动一个标签页时被调用。 |
| EVENT\_TEMP\_SAVING | 当用户正要保存一个临时文档时被调用。该插件负责保存文件。lParam 代表存储一个指针到 [TEMP\_INFO 结构](../structure/temp_info) 中。 |
| EVENT\_TOOLBAR\_CLOSED | 当关闭一个自定义工具栏时被调用。与 EVENT\_CUSTOM\_BAR\_CLOSED 消息不同，EmEditor 不毁坏客户端窗口。lParam 代表存储一个指针到 [TOOLBAR\_INFO 结构](../structure/toolbar_info) 中（支持 EmEditor 7.00 或之后的版本）。 |
| EVENT\_TOOLBAR\_SHOW | 当显示或隐藏一个自定义工具栏时被调用 （即当 RBBS\_HIDDEN 样式被切换时）。lParam 代表存储一个指针到 [TOOLBAR\_INFO 结构](../structure/toolbar_info) 中 （支持 EmEditor 7.00 或之后的版本）。 |
| EVENT\_UI\_CHANGED | 调用当 UI 变更时。<br> changed. lParam 代表下列标志的组合: <br> UI\_CHANGED\_LANGUAGE 以及 UI\_CHANGED\_TOOLBARS。 |

通过 [OnEvents](../exports/index) 函数，这些事件被用作 nEvents 参数。

这些常数在头文件 (plugin.h) 中被定义。
