# EE\_INFO

Retrieves or sets the value of one of the information parameters used by
EmEditor. You can send this message explicitly or use the
[Editor\_Info](../macro/editor_info), [Editor\_DocInfo](../macro/editor_docinfo), or [Editor\_DocInfoEx](../macro/editor_docinfoex) inline functions.

```
EE_INFO
wParam = (WPARAM)(int)nCmd;
lParam = (LPARAM)lParam;
```

Or

```
EE_INFO
wParam = MAKEWPARAM(nCmd, iDoc+1);
lParam = (LPARAM)lParam;
```

## Parameters

_nCmd_

Specifies a parameter to retrieve or set. This parameter can be one of the values from the following table.

| nCmd | Meaning | lParam | Return Value |
| --- | --- | --- | --- |
| EI\_GET\_ENCODE | Retrieves the encoding method to save files. | Not used. | (int)nCP<br> The encoding method. |
| EI\_SET\_ENCODE | Sets an encoding method to save files. | (UINT)nCP<br> Specifies an encoding method, whose value begins by CODEPAGE\_. | Not used. |
| EI\_GET\_SIGNATURE | Retrieves whether to sign Unicode/UTF-8 files. | Not used. | (BOOL)bSignature<br> TRUE to sign. |
| EI\_SET\_SIGNATURE | Sets whether to sign Unicode/UTF-8 files. | (BOOL)bSignature<br> TRUE to sign. | Not used. |
| EI\_GET\_FONT\_CHARSET | Retrieves the character set to display. | Not used. | (int)nCharset<br> The character set. |
| EI\_SET\_FONT\_CHARSET | Sets a character set to display. | (int)nCharset<br> Specifies an character set whose value begins by CHARSET\_. | Not used. |
| EI\_GET\_FONT\_CP | Retrieves the code page used by the font to display. | Not used. | (UINT)nCP<br> The code page. |
| EI\_GET\_INPUT\_CP | Retrieves the code page used by the input languages. | Not used. | (UINT)nCP<br> The code page. |
| EI\_GET\_SHOW\_TAG | Retrieves whether to show the tag highlighted. | Not used. | (BOOL)bShowTag<br> TRUE to highlight the tag. |
| EI\_SET\_SHOW\_TAG | Sets whether to show the tag highlighted. | (BOOL)bShowTag<br> TRUE to highlight the tag. | Not used. |
| EI\_GET\_FILE\_NAMEA | Retrieves the file name currently opened, in bytes. | (LPSTR)szFileName<br> Specifies a pointer to a buffer to retrieve the file name. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_FILE\_NAME\_EX | Retrieves the file name currently opened, in Unicode. | (STRING\_BUF\*)pStringBuf<br> Specifies a pointer to a [STRING\_BUF](../structure/string_buf) structure that retrieves the file name. | Not used. |
| EI\_GET\_FILE\_NAMEW | Retrieves the file name currently opened, in Unicode. | (LPSTR)szFileName<br> Specifies a pointer to a buffer to retrieve the file name. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_SET\_FILE\_NAMEW | Renames the file name currently opened. If the document is untitled, renames the document title without saving the file. | (LPCWSTR)pszName<br> Specifies a new name. | (HRESULT)hr<br>Returns a negative value if failed. |
| EI\_IS\_PROPORTIONAL\_FONT | Retrieves whether the display font is proportional. | Not Used. | (BOOL)bProportionalFont |
| EI\_GET\_NEXT\_BOOKMARK | Finds the next book mark position. | (int)yLine<br> Specifies an initial logical line to search from. -1 will search from the beginning of the document. | (int)yLine<br> Returns the searched logical line. -1 will be returned if not found. |
| EI\_GET\_HILITE\_FIND | Retrieves whether searched strings are highlighted. | Not used. | (BOOL)bShowFindHilite |
| EI\_SET\_HILITE\_FIND | Sets whether searched strings are highlighted. | (BOOL)bShowFindHilite | Not used. |
| EI\_GET\_APP\_VERSIONA | Retrieves the version name as an ANSI string. | (LPSTR)szVersionName<br> Specifies a pointer to a buffer to retrieve the version string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_APP\_VERSIONW | Retrieves the version name as a Unicode string. | (LPWSTR)szVersionName<br> Specifies a pointer to a buffer to retrieve the version string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_READ\_ONLY | Retrieves whether the document is read-only. | Not used. | (BOOL)bReadOnly |
| EI\_IS\_WINDOW\_COMBINED | Retrieves whether the windows are combined. | Not used. | (BOOL)bCombined |
| EI\_WINDOW\_COMBINE | Sets whether the windows are combined. | (BOOL)bCombined<br> Combines the windows if TRUE, or separate the windows if FALSE. | Not used. |
| EI\_IS\_UNDO\_COMBINED | Retrieves whether an inserted string can be undone at once. | Not used. | (BOOL)bCombined |
| EI\_GET\_DOC\_COUNT | Retrieves the number of opened documents in the current frame window (EmEditor Professional 5.00 or later only). | Not used. | (int)nCount<br> Returns the number of documents. |
| EI\_INDEX\_TO\_DOC | Converts a document index to a document handle (EmEditor Professional 5.00 or later only). | Specifies the zero-based index of the document. | (HEEDOC)hDoc<br> Returns the handle to the document. |
| EI\_DOC\_TO\_INDEX | Converts a document handle to a document index. | Specifies the handle to the document. | (int)nIndex<br> Returns the zero-based index of the document. |
| EI\_ZORDER\_TO\_DOC | Converts a document z-order to a document handle. | Specifies the zero-based z-order of the document. | (HEEDOC)hDoc<br> Returns the handle to the document. |
| EI\_DOC\_TO\_ZORDER | Converts a document handle to a document z-order. | Specifies the handle to the document. | (int)nZOrder<br> Returns the zero-based z-order of the document. |
| EI\_GET\_ACTIVE\_INDEX | Retrieves the index of the active document. | Not used. | (int)nIndex<br> Returns the zero-based index of the document. |
| EI\_SET\_ACTIVE\_INDEX | Activates a document. | Not used. | (BOOL)bSuccess<br> Returns TRUE if succeeded, or FALSE if failed. |
| EI\_GET\_FULL\_TITLEA | Retrieves the full title of the document in ANSI string. | (LPSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_FULL\_TITLEW | Retrieves the full title of the document in Unicode string. | (LPWSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_SHORT\_TITLEA | Retrieves the short title of the document in ANSI string. | (LPSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_SHORT\_TITLEW | Retrieves the short title of the document in Unicode string. | (LPWSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_SAVE\_AS\_TITLEA | Retrieves the full title of the document except the asterisk (\*) indicating modification in ANSI string. | (LPSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_GET\_SAVE\_AS\_TITLEW | Retrieves the full title of the document except the asterisk (\*) indicating modification in Unicode string. | (LPWSTR)szTitle<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_MOVE\_ORDER | Moves the document tab order. | Specifies the zero-based index of the destination tab. | Not used. |
| EI\_CLOSE\_DOC | Closes the document. | Not used. | (BOOL)bSuccess<br> Returns TRUE if succeeded, or FALSE if failed. |
| EI\_SAVE\_DOC | Saves the document. If the document is untitled, the **Save As** dialog box will appear. | Not used. | (BOOL)bSuccess<br> Returns TRUE if succeeded, or FALSE if failed. Selecting Cancel in the **Save As** dialog box when the document is untitled will also return FALSE. |
| EI\_GET\_CURRENT\_FOLDER | Retrieves the current working folder. | (LPWSTR)szDir<br> Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Not used. |
| EI\_IS\_LARGE\_DOC | Retrieves the flag to indicate whether the document is very large. | Not used. | (BOOL)bLarge<br> Returns TRUE if the document is very large. Otherwise, it returns FALSE. |
| EI\_USE\_INI | Retrieves whether the INI files are used instead of the Registry. | Not used. | (BOOL)bIni<br> Returns TRUE if the INI files are used, or FALSE if the Registry is used. |
| EI\_GET\_LANGUAGE | Retrieves the currently selected language for the user interface. | (LPWSTR)szFolder<br> Specifies the buffer to retrieve the language folder. The buffer must be MAX\_PATH character long including the terminating NULL character. | (UINT)nLangID<br> Returns the currently selected language ID. |
| EI\_COMBINE\_HISTORY | Specifies whether to combine the next change with the previous change as one history for Undo. | (BOOL)bCombine<br> TRUE to combine. | Not used. |
| EI\_GET\_BAR\_TEXT\_COLOR | Retrieves the text color of custom bars. | Not used. | (COLORREF)clrText<br> Returns the RGB value of the text color. |
| EI\_GET\_BAR\_BACK\_COLOR | Retrieves the background color of custom bars. | Not used. | (COLORREF)clrBack<br> Returns the RGB value of the background color. |
| EI\_GET\_RETURN\_TYPE | Retrieves the return type of the current line. If the current line is the last line of the document and does not have a return, it retrieves the return type of the previous line. | (UINT\_PTR)yLogicalLine<br> Specifies the index of the logical line. | (int)nReturnType<br> Returns either RETURN\_METHOD\_BOTH, RETURN\_METHOD\_CR\_ONLY, or RETURN\_METHOD\_LF\_ONLY |
| EI\_GET\_ACTIVE\_DOC | Retrieves the handle to the active document. | Not used. | (HEEDOC)hDoc<br> Returns the handle to the document. |
| EI\_SET\_ACTIVE\_DOC | Activates a document. | (HEEDOC)hDoc<br>Specifies the handle to the document to be activated. | (BOOL)bSuccess<br> Returns TRUE if succeeded, or FALSE if failed. |
| EI\_GET\_SYNC\_SESSION | Retrieves the session ID of the document if the document is in comparison or synchronous scroll mode. | Not used. | (int)nSessionID<br> Returns the session ID if the document is in comparison or synchronous scroll mode. Returns 0 if the document is in normal mode. |
| EI\_GET\_LOC\_DLL\_INSTANCE | Retrieves the handle to the localized resource DLL instance. | Not used. | (HINSTANCE)hinstLoc<br> Returns the handle to the localized resource DLL instance. |
| EI\_GET\_RES\_DLL\_INSTANCE | Retrieves the handle to the resource DLL instance. | Not used. | (HINSTANCE)hinstRes<br> Returns the handle to the resource DLL instance. |
| EI\_GET\_CMD\_LIST\_SIZE | Retrieves the number of items available for the specified multiple-menu command | The first item of the multiple-menu command ID. | (int)nCount<br>Returns the number of items available. |
| EI\_GET\_DISCARD\_UNDO | Retrieves the flag to indicate whether EmEditor discards undo information to improve the speed of replace, insert or delete. | Not used. | (BOOL)bDiscardUndo<br>Returns the flag. |
| EI\_SET\_DISCARD\_UNDO | Sets the flag to indicate whether EmEditor discards undo information to improve the speed of replace, insert or delete. | (BOOL)bDiscardUndo<br>The flag. | Not used. |
| EI\_GET\_HEADING\_LINES | Retrieves the number of lines of the headings (non-scroll area). | Not used. | (int)nHeadingLines |
| EI\_SET\_HEADING\_LINES | Sets the number of lines of the headings (non-scroll area). | (int)nHeadingLines | Not used. |
| EI\_GET\_NARROWING\_TOP | Retrieves the top line (y-coordinate) of the narrowing. -1 means the narrowing is not set. | Not used. | (int)nNarrowingTop |
| EI\_SET\_NARROWING\_TOP | Sets the top line (y-coordinate) of the narrowing. -1 means the narrowing is not set. | (int)nNarrowingTop | Not used. |
| EI\_GET\_NARROWING\_BOTTOM | Retrieves the bottom line (y-coordinate) of the narrowing. -1 means the narrowing is not set. | Not used. | (int)nNarrowingBottom |
| EI\_SET\_NARROWING\_BOTTOM | Sets the bottom line (y-coordinate) of the narrowing. -1 means the narrowing is not set. | (int)nNarrowingBottom | Not used. |
| EI\_SET\_HILITE\_FILTER | Sets the filter using last used find information. Only the active document is allowed. | Not used. | Not used. |
| EI\_GET\_CSV | Retrieves the index of the current CSV mode, or -1 if it is not a CSV mode. | Not used. | (int)iCSV |
| EI\_GET\_PRINT\_PAGES | Retrieves the number of pages for the currently selected printer. Only the active document is allowed. | (BOOL)bSelOnly<br>Specifies whether only the selection is calculated to retrieve the number of pages. | (int)nPages. |
| EI\_GET\_COMBINE\_HISTORY | Retrieves the flag that shows whether to combine the next change with the previous change as one history for Undo. | Not used. | (BOOL)bCombine |
| EI\_GET\_CELL\_MODE | Retrieves the flag that shows whether the selection mode is cell selection mode. | Not used. | (BOOL)bCellMode |
| EI\_SET\_CELL\_MODE | Sets the flag that shows whether the selection mode is cell selection mode. | (BOOL)bCellMode | Not used. |
| EI\_GET\_UNTITLED | Retrieves the flag that shows whether the document is untitled. | Not used. | (BOOL)bUntitled |
| EI\_GET\_DPI | Retrieves the DPI value at the current monitor. | Not used. | (long)nDPI |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_ABOVE | Retrieves the number of visible lines above the matched lines by filters. | Not used. | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_ABOVE | Sets the number of visible lines above the matched lines by filters. | (long)nLines | Not used. |
| EI\_GET\_FILTER\_VISIBLE\_LINES\_BELOW | Retrieves the number of visible lines below the matched lines by filters. | Not used. | (long)nLines |
| EI\_SET\_FILTER\_VISIBLE\_LINES\_BELOW | Sets the number of visible lines below the matched lines by filters. | (long)nLines | Not used. |
| EI\_GET\_DPI\_OPTIONS | Retrieves the options related to the monitor. Currently, only DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED is supported. When DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED is set, EmEditor resizes the window when the DPI is changed. | Not used. | (long)nFlags |
| EI\_SET\_DPI\_OPTIONS | Sets the options related to the monitor. Currently, only DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED is supported. When DPI\_OPTIONS\_RESIZE\_WHEN\_DPI\_CHANGED is set, EmEditor resizes the window when the DPI is changed. | (long)nFlags | Not used. |
| EI\_GET\_REGISTERED\_NAME | Retrieves the registered name, which is displayed in the About dialog box. If the product is not registered, an empty string will be retrieved. | (LPWSTR)szName<br>Specifies the buffer to retrieve the string. The buffer must be MAX\_REG\_NAME character long including the terminating NULL character. | Not used. |
| EI\_VALIDATE\_CSV | Validates the CSV document and output errors, and optionally adjusts separator positions. | (int)nFlags<br>You may specify a combination of VALIDATE\_ADJUST\_COLUMNS, VALIDATE\_QUIET, VALIDATE\_ADJUST\_VISIBLE\_ONLY, VALIDATE\_DETECT\_NL, VALIDATE\_QUIET\_IF\_NO\_ERROR, VALIDATE\_ADJUST\_ENLARGE\_ONLY, VALIDATE\_DETECT\_CSV, and VALIDATE\_ASYNC. | (int)nResults<br>Return values are combination of CSV\_ADJUSTED, CSV\_NL\_EMBEDDED, CSV\_ABORT, CSV\_INVALID\_QUOTES, CSV\_INCONSISTENT\_COLUMNS, CSV\_NOT\_CSV, CSV\_ASYNC\_SUCCESS, and CSV\_ASYNC\_RUNNING. The return value of 0 means there were no errors. |
| EI\_GET\_CLIENT\_RECT\_NO\_BARS | Retrieves the coordinates of the editor view excluding the area occupied by scroll bars and the Minimap. | (RECT\*)pRect | Returns TRUE if succeeded, or FALSE if failed. |
| EI\_REFRESH\_COMMON\_SETTINGS | Loads common settings and refreshes the EmEditor window. | Not used. | Not used. |
| EI\_GET\_NEWLINE\_CODE | Retrieves the newline character code used in the document. | Not used. | Returns FLAG\_CR\_AND\_LF, FLAG\_CR\_ONLY, FLAG\_LF\_ONLY, or FLAG\_NEWLINE\_MIXED. |
| EI\_GET\_MEMORY\_SIZE | Retrieves the memory size used in the document. The default value can be specified in the **Memory Size** text box in the [**Advanced** page](../../dlg/customize/advanced/index) of the **Customize** dialog box. | Not used. | Returns the memory size. |
| EI\_SET\_MEMORY\_SIZE | Sets the memory size used in the document. The default value can be specified in the **Memory Size** text box in the [**Advanced** page](../../dlg/customize/advanced/index) of the **Customize** dialog box. | (long)nBits<br>Specifies the required memory size. | Returns the new memory size. This value may become greater than the specified size if the document already uses greater memory size than the specified size. |
| EI\_GET\_BOOKMARK\_COUNT | Retrieves the number of bookmarks in the document. | Not used. | Returns the number of bookmarks in the document. |
| EI\_SYNC\_NOW | Triggers EmEditor to sync now. | (UINT)nFlags<br>You may specify a combination of SYNC\_FLAG\_SEND, SYNC\_FLAG\_RECEIVE, SYNC\_FLAG\_FORCE, and SYNC\_FLAG\_REFRESH\_UI. | Not used. |
| EI\_GET\_CHAR\_TYPE | Retrieves the type of the character. | (LPCWSTR)pch | Returns the type of the character. It can be one of the following types:<br>CHAR\_NULL, CHAR\_SPACE, CHAR\_MARK, CHAR\_ALPHANUMERIC, CHAR\_KANA , CHAR\_KANA\_MARK , CHAR\_DB\_SPACE, CHAR\_DB\_MARK, CHAR\_DB\_ALPHANUMERIC, CHAR\_DB\_HIRA, CHAR\_DB\_KATA, CHAR\_DB\_KANJI, CHAR\_DB\_KANA\_MARK, CHAR\_SECOND\_DB, CHAR\_HANGUL, CHAR\_DB\_HANGUL. |
| EI\_FILE\_POS\_TO\_LOGICAL | Converts a file position to the logical position. | (FILE\_POS\_INFO\*)pFilePosInfo | Not used. |
| EI\_LOGICAL\_TO\_FILE\_POS | Converts a logical position to the file position. | (FILE\_POS\_INFO\*)pFilePosInfo | Not used. |
| EI\_CELL\_TO\_LOGICAL | Converts a cell position to the logical position. | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | Not used. |
| EI\_LOGICAL\_TO\_CELL | Converts a logical position to the cell position. | (CELL\_LOGICAL\_INFO\*)pCellLogicalInfo | Not used. |
| EI\_IS\_VERY\_DARK | Checks if the dark mode is supported in the system, and whether the user selects the very dark mode if supported. | Not used. | Returns TRUE if the user selects the very dark mode, FALSE if not, or NOT\_SUPPORTED if the dark mode is not supported in the system. |
| EI\_WM\_INITDIALOG | Called inside the WM\_INITDIALOG message in a dialog procedure to support the very dark mode. | (HWND)hWnd | Not used. |
| EI\_WM\_CTLCOLOR | Called inside the WM\_CTLCOLORDLG, WM\_CTLCOLORSTATIC, WM\_CTLCOLOREDIT, WM\_CTLCOLORBTN, and WM\_CTLCOLORLISTBOX messages in a dialog procedure to support the very dark mode. | (WPARAM)wParam<br>You may forward pass of the WM\_CTLCOLORxxx messages. | Returns a brush if the very dark mode is selected. You must pass this value to the dialog procedure return value. |
| EI\_WM\_THEMECHANGED | Called inside the WM\_THEMECHANGED message in a dialog procedure to support the very dark mode. | (HWND)hWnd | Not used. |
| EI\_INIT\_LISTVIEW | Initialize a listview control to support the very dark mode. | (HWND)hWnd | Not used. |
| EI\_GET\_VIEW\_FONT | Retrieves the handle to the currently selected editor font. | Not used. | (HFONT)hFont |
| EI\_GET\_HIDE\_QUOTES | Retrieves a flag indicating whether the Unquoted/Unescaped View is enabled in the CSV cell selection mode. | Not used. | (BOOL)bHideQuotes |
| EI\_SET\_HIDE\_QUOTES | Sets a flag indicating whether the Unquoted/Unescaped View is enabled in the CSV cell selection mode. | (BOOL)bHideQuotes | Not used. |
| EI\_ENABLE\_WM\_CHAR | Used internally. | Not used. | Used internally. |
| EI\_GET\_SYNC | Retrieves the path to the sync folder. | (LPWSTR)szDir<br>Specifies the buffer to retrieve the string. The buffer must be MAX\_PATH character long including the terminating NULL character. | Returns a combination of values including SYNC\_SETTINGS\_SEND and SYNC\_SETTINGS\_RECEIVE. |
| EI\_GET\_SPLIT | Retrieves the split status. | Not used. | Returns one of following values: SPLIT\_NONE, SPLIT\_HORZ, SPLIT\_VERT, SPLIT\_BOTH, SPLIT\_2\_HORZ, or SPLIT\_2\_VERT |
| EI\_GET\_SUM | Retrieves the sum and count of numbers contained in the selection. | (SUM\_INFO\*)pSumInfo | Returns TRUE if succeeded, or FALSE if failed. |
| EI\_GET\_CONFIG | Retrieves the selected configuration name. | Specifies a pointer to a buffer to retrieve the configuration name. The buffer must be MAX\_CONFIG\_NAME character long including the terminating NULL character. | Not used. |
| EI\_SET\_CONFIG | Changes to a specified configuration. | Specifies a configuration name. | (BOOL)bSuccess |
| EI\_SAVE\_FILE | Saves a document. | Specifies a full path file name. | (BOOL)bSuccess |
| EI\_INDEX\_TO\_DOC\_REAL | Converts a document index to a document handle. Unlike EI\_INDEX\_TO\_DOC, this command counts unique individual documents in a split window. | Specifies the zero-based index of the document. | (HEEDOC)hDoc<br>Returns the handle to the document. |
| EI\_DOC\_TO\_INDEX\_REAL | Converts a document handle to a document index. Unlike EI\_INDEX\_TO\_DOC, this command counts unique individual documents in a split window. | Specifies the handle to the document. | (int)nIndex<br>Returns the zero-based index of the document. |
| EI\_GET\_TITLE | Retrieves the title of the current document. | (STRING\_BUF\*)pStringBuf<br> Specifies a pointer to a [STRING\_BUF](../structure/string_buf) structure that retrieves the title. | Not used. |
| EI\_SET\_TITLE | Sets the title of the current document. The title may contain long and short titles separated by a linefeed (\\n). | (LPCWSTR)pszTitle<br> Specifies a new title. | (HRESULT)hr<br>Returns a negative value if failed. |
| EI\_SET\_WEB | Sets the flags of the Web Browser. | (UINT)nFlags<br> Specifies a new flag. | Not used. |
| EI\_OPEN\_WEB | Opens a website of the specified URL. | (LPCWSTR)pszURL<br> Specifies an URL. | (HRESULT)hWnd<br>Returns the window handle to the web view. |

_iDoc_

Specifies the index of the target document. A one-based index should be specified at the higher word of wParam. If 0 is specified at the higher word of wParam, the currently active document will
be targeted. This parameter may not be used depending on nCmd. In this case, the higher word of wParam must be 0.

_lParam_

Depends on the parameter specified.

## Return Values

Depends on the parameter specified.

## Version

Supported in EmEditor Professional Version 3.00 or later. However, the iDoc parameter is only supported on Version 5.00 or later.
