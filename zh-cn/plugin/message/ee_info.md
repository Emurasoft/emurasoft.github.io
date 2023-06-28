# EE\_INFO

检索或设置用于 EmEditor 的信息参数之一的值。你能明确地发送该消息或用
[Editor\_Info](../macro/editor_info)， [Editor\_DocInfo](../macro/editor_docinfo)，或 [Editor\_DocInfoEx](../macro/editor_docinfoex) 内联函数。

EE\_INFO

wParam = (WPARAM)(int)nCmd;

lParam = (LPARAM)lParam;

or

EE\_INFO

wParam = MAKEWPARAM(nCmd, iDoc+1);

lParam = (LPARAM)lParam;

## 参数

_nCmd_

> 指定要检索或设置的参数。这个参数可以是下面表格中所列的值之一。
>
> | nCmd | 含义 | lParam | 返回值 |
> | --- | --- | --- | --- |
> | EI\_GET\_ENCODE | 检索要保存文件的编码方式。 | 不使用。 | (int)nCP<br> 编码方式。 |
> | EI\_SET\_ENCODE | 设置一个保存文件的编码方式。 | (UINT)nCP<br> 指定一个以 CODEPAGE\_ 为开始值的编码方式。 | 不使用。 |
> | EI\_GET\_SIGNATURE | 检索是否要给 Unicode/UTF-8 文件签名。 | 不使用。 | (BOOL)bSignature<br> TRUE，签名。 |
> | EI\_SET\_SIGNATURE | 设置是否要给 Unicode/UTF-8 文件签名。 | (BOOL)bSignature<br> TRUE，签名。 | 不使用。 |
> | EI\_GET\_FONT\_CHARSET | 检索一个要显示的字符集。 | 不使用。 | (int)nCharset<br> 字符集。 |
> | EI\_SET\_FONT\_CHARSET | 设置要一个要显示的字符集。 | (int)nCharset<br> 指定一个以 CHARSET\_ 为开始值的字符集。 | 不使用。 |
> | EI\_GET\_FONT\_CP | 检索所使用的字体显示的代码页。 | 不使用。 | (UINT)nCP<br> 该代码页。 |
> | EI\_GET\_INPUT\_CP | 检索所使用的输入语言的代码页。 | 不使用。 | (UINT)nCP<br> 该代码页。 |
> | EI\_GET\_SHOW\_TAG | 检索是否显示被高亮的标签。 | 不使用。 | (BOOL)bShowTag<br> TRUE 表示高亮标签。 |
> | EI\_SET\_SHOW\_TAG | 设置是否显示被高亮的标签。 | (BOOL)bShowTag<br> TRUE 表示高亮标签。 | 不使用。 |
> | EI\_GET\_FILE\_NAMEA | 用字节检索当前打开的文件名。 | (LPSTR)szFileName<br> 指定一个指针指向缓冲区来检索文件名。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_FILE\_NAME\_EX | 用 Unicode 检索当前打开的文件名。 | (STRING\_BUF\*)pStringBuf<br> 指定一个指针指向检索文件名的 [STRING\_BUF](../structure/string_buf) 结构。 | 不使用。 |
> | EI\_GET\_FILE\_NAMEW | 检索当前打开的文件名，用 Unicode 表示。 | (LPSTR)szFileName<br> 指定一个指针指向缓冲区来检索文件名。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_SET\_FILE\_NAMEW | 重命名当前打开的文件名。如果文档没有标题，则重命名文档标题而不保存文件。 | (LPCWSTR)pszName<br> 指定新名称。 | (HRESULT)hr<br>如果失败则返回负值。 |
> | EI\_IS\_PROPORTIONAL\_FONT | 检索是否显示的字体是成比例的。 | 不使用。 | (BOOL)bProportionalFont |
> | EI\_GET\_NEXT\_BOOKMARK | 查找下一个书签位置。 | (int)yLine<br> 指定一个要搜索的起始逻辑行位置。-1 会从文档开始处搜索。 | (int)yLine<br> 返回被搜索的逻辑行。-1 会被返回如果没有被查找到任何匹配结果的话。 |
> | EI\_GET\_HILITE\_FIND | 检索被搜索的字符串是否被高亮。 | 不使用。 | (BOOL)bShowFindHilite |
> | EI\_SET\_HILITE\_FIND | 设置被搜索的字符串是否被高亮。 | (BOOL)bShowFindHilite | 不使用。 |
> | EI\_GET\_APP\_VERSIONA | 检索版本名称为一个 ANSI　字符串。 | (LPSTR)szVersionName<br> 指定一个指针指向一个缓冲区来检索版本字符串。缓存区必须是 MAX\_PATH 字符长度包括终止空字符。 | 不使用。 |
> | EI\_GET\_APP\_VERSIONW | 检索版本名称为一个 Unicode 字符串。 | (LPWSTR)szVersionName<br> 指定一个指针指向一个缓冲区来检索版本字符串。缓存区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_READ\_ONLY | 检索文档是否为只读模式。 | 不使用。 | (BOOL)bReadOnly |
> | EI\_IS\_WINDOW\_COMBINED | 检索窗口是否被合并。 | 不使用。 | (BOOL)bCombined |
> | EI\_WINDOW\_COMBINE | 设置窗口是否被合并。 | (BOOL)bCombined<br> 合并窗口如果是 TRUE，或分隔窗口如果是 FALSE。 | 不使用。 |
> | EI\_IS\_UNDO\_COMBINED | 检索一个被插入的字符串是否能被立即撤消。 | 不使用。 | (BOOL)bCombined |
> | EI\_GET\_DOC\_COUNT | 检索在当前框架窗口中打开文档的数目 (仅适用于 EmEditor 5.00 或之后的版本)。 | 不使用。 | (int)nCount<br> 返回打开文档数。 |
> | EI\_INDEX\_TO\_DOC | 把一个文档索引转换为文档句柄(仅适用于 EmEditor 5.00 或之后的版本)。 | 指定从零开始的文档索引。 | (HEEDOC)hDoc<br> 返回文档的句柄。 |
> | EI\_DOC\_TO\_INDEX | 把一个文档句柄转换为文档索引。 | 指定文档的句柄。 | (int)nIndex<br> 返回从零开始的文档索引。 |
> | EI\_ZORDER\_TO\_DOC | 把一个文档的叠置顺序 (z-order) 转换为一个文档句柄。 | 指定从零开始的文档叠置顺序。 | (HEEDOC)hDoc<br> 返回句柄到该文档中。 |
> | EI\_DOC\_TO\_ZORDER | 把一个文档句柄转换为一个文档的叠置顺序 (z-order)。 | 为该文档指定句柄。 | (int)nZOrder<br> 返回从零开始的文档叠置顺序。 |
> | EI\_GET\_ACTIVE\_INDEX | 检索活动文档的索引。 | 不使用。 | (int)nIndex<br> 返回从零开始的文档叠置顺序。 |
> | EI\_SET\_ACTIVE\_INDEX | 激活一个文档。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
> | EI\_GET\_FULL\_TITLEA | 在 ANSI 字符串中，检索文档的完整标题。 | (LPSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_FULL\_TITLEW | 在 Unicode 字符串中，检索文档的完整标题。 | (LPWSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_SHORT\_TITLEA | 在 ANSI 字符串中，检索文档的简略标题。 | (LPSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_SHORT\_TITLEW | 在 Unicode 字符串中，检索文档的简略标题。 | (LPWSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_SAVE\_AS\_TITLEA | 检索文档的完整标题，除了星号 (\*) 所表示的在 ANSI 字符串中的修改。 | (LPSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_GET\_SAVE\_AS\_TITLEW | 检索文档的完整标题，除了星号 (\*) 所表示的在 Unicode 字符串中的修改。 | (LPWSTR)szTitle<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_MOVE\_ORDER | 改变文档标签页顺序。 | 指定从零开始的目标标签页索引。 | 不使用。 |
> | EI\_CLOSE\_DOC | 关闭文档。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
> | EI\_SAVE\_DOC | 保存文档。如果文档未命名，会出现 **另存为** 对话框。 | 不使用。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。当文档未命名时，在 **另存为** 对话框中选择“取消”，也会返回 FALSE。 |
> | EI\_GET\_CURRENT\_FOLDER | 检索当前运作的文件夹。 | (LPWSTR)szDir<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | 不使用。 |
> | EI\_IS\_LARGE\_DOC | 检索标志来指出文档是否很大。 | 不使用。 | (BOOL)bLarge<br> 返回 TRUE 如果文档很大。否则的话，返回 FALSE。 |
> | EI\_USE\_INI | 检索是否用 INI 文件，而不是注册表。 | 不使用。 | (BOOL)bIni<br> 返回 TRUE 如果用 INI 文件，或 FALSE 如果用注册表。 |
> | EI\_GET\_LANGUAGE | 检索当前为用户界面选取的语言。 | (LPWSTR)szFolder<br> 指定要检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长度，包括终止空字符。 | (UINT)nLangID<br> 返回当前被选取的语言 ID。 |
> | EI\_COMBINE\_HISTORY | 指定是否要合并上一变更与下一变更，让它们一起作为一个撤消记录。 | (BOOL)bCombine<br> 合并的话，返回 TRUE。 | 不使用。 |
> | EI\_GET\_BAR\_TEXT\_COLOR | 检索自定义分栏的文本颜色。 | 不使用。 | (COLORREF)clrText<br> 返回文本颜色的 RGB 值。 |
> | EI\_GET\_BAR\_BACK\_COLOR | 检索自定义分栏的背景颜色。 | 不使用。 | (COLORREF)clrBack<br> 返回背景颜色的 RGB 值。 |
> | EI\_GET\_RETURN\_TYPE | 检索当前行的换行方式。如果当前行是文档的最后一行，并且没有换行，那就检索前一行的换行方式。 | (UINT\_PTR)yLogicalLine<br> 指定逻辑行的索引。 | (int)nReturnType<br> 返回 RETURN\_METHOD\_BOTH，RETURN\_METHOD\_CR\_ONLY，或 RETURN\_METHOD\_LF\_ONLY。 |
> | EI\_GET\_ACTIVE\_DOC | 检索活动文档的句柄。 | 不使用。 | (HEEDOC)hDoc<br> 返回该文档的句柄。 |
> | EI\_SET\_ACTIVE\_DOC | 激活一个文档。 | (HEEDOC)hDoc<br>指定要被激活文档的句柄。 | (BOOL)bSuccess<br> 如果成功，返回 TRUE；如果不成功，返回 FALSE。 |
> | EI\_GET\_SYNC\_SESSION | 检索文档的时段 ID，如果文档在比较或同步滚动模式中。 | 不使用。 | (int)nSessionID<br> 返回时段 ID，如果文档在比较或同步滚动模式中。返回 0，如果文档是标准模式。 |
> | EI\_GET\_LOC\_DLL\_INSTANCE | 检索本地化资源 DLL 实例的句柄。 | 不使用。 | (HINSTANCE)hinstLoc<br> 返回本地化资源 DLL 实例的句柄。 |
> | EI\_GET\_RES\_DLL\_INSTANCE | 检索资源 DLL 实例的句柄。 | 不使用。 | (HINSTANCE)hinstRes<br> 返回资源 DLL 实例的句柄。 |
> | EI\_GET\_CMD\_LIST\_SIZE | 检索指定多项菜单命令中可用的项目数。 | 多项菜单命令 ID 的第一个项目。T | (int)nCount<br>返回可用的项目数。 |
> | EI\_GET\_DISCARD\_UNDO | 检索标志，指出是否要 EmEditor 丢弃撤消信息来提高替换，插入或删除的速度。 | 不使用。 | (BOOL)bDiscardUndo<br>返回标志。 |
> | EI\_SET\_DISCARD\_UNDO | 设置标志，指出是否要 EmEditor 丢弃撤消信息来来提高替换，插入或删除的速度。 | (BOOL)bDiscardUndo<br>The flag. | 不使用。 |
> | EI\_GET\_HEADING\_LINES | 检索标题的行数（非滚动区域）。 | 不使用。 | (int)nHeadingLines |
> | EI\_SET\_HEADING\_LINES | 设置标题的行数（非滚动区域）。 | (int)nHeadingLines | 不使用。 |
> | EI\_GET\_NARROWING\_TOP | 检索仅编辑选定区域的首行（y 坐标）。-1 表示未设置仅编辑选定区域。 | 不使用。 | (int)nNarrowingTop |
> | EI\_SET\_NARROWING\_TOP | 设置仅编辑选定区域的首行（y 坐标）。-1 表示未设置仅编辑选定区域。 | (int)nNarrowingTop | 不使用。 |
> | EI\_GET\_NARROWING\_BOTTOM | 检索仅编辑选定区域的末行（y 坐标）。-1 表示未设置仅编辑选定区域。 | 不使用。 | (int)nNarrowingBottom |
> | EI\_SET\_NARROWING\_BOTTOM | 设置仅编辑选定区域的末行（y 坐标）。-1 表示未设置仅编辑选定区域。 | (int)nNarrowingBottom | 不使用。 |
> | EI\_SET\_HILITE\_FILTER | 使用上次使用的查找信息设置筛选。仅允许使用激活的文档。 | 不使用。 | 不使用。 |
> | EI\_GET\_CSV | 检索当前 CSV 模式的索引，如果不是 CSV 模式，则返回 -1。 | 不使用。 | (int)iCSV |
> | EI\_GET\_PRINT\_PAGES | 检索当前指定打印的页数。仅允许激活的文档。 | (BOOL)bSelOnly<br>指定是否仅计算选取区域的页数。 | (int)nPages |
> | EI\_GET\_COMBINE\_HISTORY | 检索能显示是否要在撤消记录中把下个变更与上一个变更合并为一个的标志。 | 不使用。 | (BOOL)bCombine |
> | EI\_GET\_CELL\_MODE | 检索标志，显示选择模式是否是单元格选择模式。 | 不使用。 | (BOOL)bCellMode |
> | EI\_SET\_CELL\_MODE | 设置标志，显示选择模式是否是单元格选择模式。 | (BOOL)bCellMode | 不使用。 |
> | EI\_GET\_UNTITLED | 检索显示文档是否未命名的标志。 | 不使用。 | (BOOL)bUntitled |
> | EI\_GET\_DPI | 检索当前监视器的 DPI 值。 | 不使用。 | (long)nDPI |
> | EI\_GET\_FILTER\_VISIBLE\_LINES\_ABOVE | 检索用筛选器匹配的行以上的可见行数。 | 不使用。 | (long)nLines |
> | EI\_SET\_FILTER\_VISIBLE\_LINES\_ABOVE | 设置用筛选器匹配的行以上的可见行数。 | (long)nLines | 不使用。 |
> | EI\_GET\_FILTER\_VISIBLE\_LINES\_BELOW | 检索用筛选器匹配的行以下的可见行数。 | 不使用。 | (long)nLines |
> | EI\_SET\_FILTER\_VISIBLE\_LINES\_BELOW | 设置用筛选器匹配的行以下的可见行数。 | (long)nLines | 不使用。 |
> | EI\_GET\_DPI\_OPTIONS | 检索与荧幕相关的选项。目前只支持 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED。当设置 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED 时，EmEditor 会在 DPI 变更时调整窗口的大小。 | 不使用。 | (long)nFlags |
> | EI\_SET\_DPI\_OPTIONS | 设置与荧幕相关的选项。目前只支持 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED。当设置 DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED 时，EmEditor 会在 DPI 变更时调整窗口的大小。 | (long)nFlags | 不使用。 |
> | EI\_GET\_REGISTERED\_NAME | 检索注册名称，显示在“关于”对话框中。 如果产品未注册，将检索空字符串。 | (LPWSTR)szName<br>指定要检索字符串的缓冲区。 缓冲区必须为 MAX\_REG\_NAME 字符长度，包括终止 NULL 字符。 | 不使用。 |
> | EI\_VALIDATE\_CSV | 验证CSV文档和输出错误，并可选择地调整分隔符位置。 | (int)nFlags<br>你可以指定 VALIDATE\_ADJUST\_COLUMNS，VALIDATE\_QUIET，VALIDATE\_ADJUST\_VISIBLE\_ONLY，VALIDATE\_DETECT\_NL，VALIDATE\_DONT\_CLEAR\_OUTPUT，VALIDATE\_QUIET\_IF\_NO\_ERROR，VALIDATE\_ADJUST\_ENLARGE\_ONLY，VALIDATE\_DETECT\_CSV 和 VALIDATE\_ASYNC 的组合。 | (int)nResults<br>返回值是 CSV\_ADJUSTED，CSV\_NL\_EMBEDDED，CSV\_ABORT，CSV\_INVALID\_QUOTES，CSV\_INCONSISTENT\_COLUMNS，CSV\_NOT\_CSV，CSV\_ASYNC\_SUCCESS 和 CSV\_ASYNC\_RUNNING 的组合。返回值为 0 表示没有错误。 |
> | EI\_GET\_CLIENT\_RECT\_NO\_BARS | 检索编辑器视图的坐标，不包括滚动条和迷你地图占用的区域。 | (RECT\*)pRect | 如果成功，返回 TRUE；如果失败，返回 FALSE。 |
> | EI\_REFRESH\_COMMON\_SETTINGS | 加载常用设置并刷新 EmEditor 窗口。 | 不使用。 | 不使用。 |
> | EI\_GET\_NEWLINE\_CODE | 检索文档中使用的换行字符码。 | 不使用。 | 返回 FLAG\_CR\_AND\_LF，FLAG\_CR\_ONLY，FLAG\_LF\_ONLY，或 FLAG\_NEWLINE\_MIXED。 |
> | EI\_GET\_MEMORY\_SIZE | 检索文档中使用的内存大小。可以在 **自定义** 对话框的 [**高级** 页面](../../dlg/customize/advanced/index) 上的 **内存大小** 文本框中指定默认值。 | 不使用。 | 返回内存大小。 |
> | EI\_SET\_MEMORY\_SIZE | 设置文档中使用的内存大小。可以在 **自定义** 对话框的 [**高级** 页面](../../dlg/customize/advanced/index) 上的 **内存大小** 文本框中指定默认值。 | (long)nBits<br>指定所需的内存大小。 | 返回新的内存大小。如果文档已经使用大于指定大小的内存大小，则此值可能会大于指定的大小。 |
> | EI\_GET\_BOOKMARK\_COUNT | 检索文档中的书签数。 | 不使用。 | 返回文档中的书签数。 |
> | EI\_SYNC\_NOW | 触发 EmEditor 立即同步。 | (UINT)nFlags<br>你可以指定 SYNC\_FLAG\_SEND，SYNC\_FLAG\_RECEIVE，SYNC\_FLAG\_FORCE，和 SYNC\_FLAG\_REFRESH\_UI 的组合。 | 不使用。 |
> | EI\_GET\_CHAR\_TYPE | 检索字符类型。 | (LPCWSTR)pch | 返回字符类型。它可以是下列类型之一：<br>CHAR\_NULL，CHAR\_SPACE，CHAR\_MARK，CHAR\_ALPHANUMERIC，CHAR\_KANA ，CHAR\_KANA\_MARK ，CHAR\_DB\_SPACE，CHAR\_DB\_MARK，CHAR\_DB\_ALPHANUMERIC，CHAR\_DB\_HIRA，CHAR\_DB\_KATA，CHAR\_DB\_KANJI，CHAR\_DB\_KANA\_MARK，CHAR\_SECOND\_DB，CHAR\_HANGUL，CHAR\_DB\_HANGUL。 |
> | EI\_FILE\_POS\_TO\_LOGICAL | 将文件位置转换为逻辑位置。 | (FILE\_POS\_INFO\*)pFilePosInfo | 不使用。 |
> | EI\_LOGICAL\_TO\_FILE\_POS | 将逻辑位置转换为文件位置。 | (FILE\_POS\_INFO\*)pFilePosInfo | 不使用。 |
> | EI\_CELL\_TO\_LOGICAL | 将单元格位置转换为逻辑位置。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 不使用。 |
> | EI\_LOGICAL\_TO\_CELL | 将逻辑位置转换为单元格位置。 | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | 不使用。 |
> | EI\_IS\_VERY\_DARK | 检查系统是否支持暗模式，如果支持，则检查用户是否选择了非常暗模式。 | 不使用。 | 如果用户选择了非常暗模式，则返回 TRUE；否则，返回FALSE；如果系统不支持暗模式，则返回 NOT\_SUPPORTED。 |
> | EI\_WM\_INITDIALOG | 在对话框过程中的 WM\_INITDIALOG 消息内调用，以支持非常暗的模式。 | (HWND)hWnd | 不使用。 |
> | EI\_WM\_CTLCOLOR | 在对话框过程中的 WM\_CTLCOLORDLG，WM\_CTLCOLORSTATIC，WM\_CTLCOLOREDIT，WM\_CTLCOLORBTN，以及 WM\_CTLCOLORLISTBOX 消息内调用，以支持非常暗的模式。 | (WPARAM)wParam<br>您可以转发传递 WM\_CTLCOLORxxx 消息。 | 如果选择了非常暗模式，则返回画笔。您必须将此值传递给对话框过程的返回值。 |
> | EI\_WM\_THEMECHANGED | 在对话框过程中的 WM\_THEMECHANGED 消息内调用，以支持非常暗模式。 | (HWND)hWnd | 不使用。 |
> | EI\_INIT\_LISTVIEW | 初始化一个列表视图控件以支持非常暗模式。 | (HWND)hWnd | 不使用。 |
> | EI\_GET\_VIEW\_FONT | 检索当前选择的编辑器字体的句柄。 | 不使用。 | (HFONT)hFont |
> | EI\_GET\_HIDE\_QUOTES | 检索一个标志，该标志指示在 CSV 单元格选择模式下是否启用了“隐藏引号”视图。 | 不使用。 | (BOOL)bHideQuotes |
> | EI\_SET\_HIDE\_QUOTES | 设置一个标志，该标志指示在 CSV单元格选择模式下是否启用了“隐藏引号”视图。 | (BOOL)bHideQuotes | 不使用。 |
> | EI\_ENABLE\_WM\_CHAR | 内部使用。 | 不使用。 | 内部使用。 |
> | EI\_GET\_SYNC | 检索同步文件夹的路径。 | (LPWSTR)szDir<br>指定用于检索字符串的缓冲区。缓冲区必须是 MAX\_PATH 字符长，包括终止的 NULL 字符。 | 返回包括 SYNC\_SETTINGS\_SEND 和 SYNC\_SETTINGS\_RECEIVE 的值的组合。 |
> | EI\_GET\_SPLIT | 检索拆分状态。 | 不使用。 | 返回以下值之一：SPLIT\_NONE，SPLIT\_HORZ，SPLIT\_VERT，SPLIT\_BOTH，SPLIT\_2\_HORZ，或 SPLIT\_2\_VERT。 |
> | EI\_GET\_SUM | 检索所选内容中包含的数字的总和以及次数。 | (SUM\_INFO\*)pSumInfo | 如果成功返回 TRUE，如果失败则返回 FALSE。 |
> | EI\_GET\_CONFIG | 检索选取的配置名称。 | 指定指向缓冲区的指针以检索配置名称。缓冲区的长度必须为 MAX\_CONFIG\_NAME 指定的字符，包括终止 NULL 字符。 | 不使用。 |
> | EI\_SET\_CONFIG | 对指定配置的更改。 | 指定一个配置名称。 | (BOOL)bSuccess |
> | EI\_SAVE\_FILE | 保存一个文档。 | 指定完整的文件路径名称。 | (BOOL)bSuccess |
> | EI\_INDEX\_TO\_DOC\_REAL | 将文档索引转换为文档句柄。与 EI\_INDEX\_TO\_DOC 不同，此命令计算在拆分窗口中唯一的单个文档。 | 指定从零开始的文档索引。 | (HEEDOC)hDoc<br>返回文档的句柄。 |
> | EI\_DOC\_TO\_INDEX\_REAL | 将文档索引转换为文档句柄。与 EI\_INDEX\_TO\_DOC 不同，此命令计算在拆分窗口中唯一的单个文档。 | 指定文档的句柄。 | (int)nIndex<br>返回从零开始的文档索引。 |
> | EI\_GET\_TITLE | 检索当前文档的标题。 | (STRING\_BUF\*)pStringBuf<br> 指定指针指向一个检索标题的 [STRING\_BUF](../structure/string_buf) 结构。 | 不使用。 |
> | EI\_SET\_TITLE | 设置当前文档的标题。标题可能包含由换行符 (\\n) 分隔的长标题和短标题。 | (LPCWSTR)pszTitle<br> 指定一个新标题。 | (HRESULT)hr<br>如果失败，则返回负值。 |

_iDoc_

> 指定目标文档的索引。应当在 wParam 参数的高字处指定一个以 1 为基准的索引。如果 wParam 参数的高字处指定了 0，那么当前活动的文档就会成为目标文档。根据不同的 nCmd 而定，这个参数也有可能不被使用。如果是这个情况，那么 wParam 的高字一定是 0。

_lParam_

> 取决于指定的参数。

## 返回值

> 取决于指定的参数。

## 支持版本

> 支持 EmEditor 3.00 或之后的版本。 然而，iDoc 参数仅在 EmEditor 5.00 或之后的版本上支持。