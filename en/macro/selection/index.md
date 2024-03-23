# Selection Object

## Properties

|     |     |
| --- | --- |
| **[Average](average)** | Retrieves the average of the numbers contained in the selection. |
| **[Count](selection_count)** | Retrieves the number of selections in the current document. |
| **[IsActiveEndGreater](selection_isactiveendgreater)** | Indicates whether the active point is equal to the bottom point. |
| **[IsEmpty](selection_isempty)** | Indicates whether the active point is equal to the anchor point. |
| **[Mode](selection_mode)** | Sets or retrieves a flag indicating the selection mode. |
| **[OverwriteMode](selection_overwritemode)** | Sets or retrieves a flag indicating the overwrite or insert mode. |
| **[Sum](sum)** | Retrieves the sum of the numbers contained in the selection. |
| **[Text](selection_text)** | Retrieves the selected text, or inserts a string at the cursor position. |

## Methods

|     |     |
| --- | --- |
| **[BatchFind](batch_find)** | Searches for multiple strings. |
| **[BatchReplace](batch_replace)** | Replaces multiple strings. |
| **[ChangeCase](selection_changecase)** | Changes the case of the selected text. |
| **[ChangeWidth](selection_changewidth)** | Changes the width of the selected text. |
| **[CharLeft](selection_charleft)** | Moves the cursor the specified number of characters to the left. |
| **[CharRight](selection_charright)** | Moves the cursor the specified number of characters to the right. |
| **[ClearBookmark](selection_clearbookmark)** | Clears a bookmark on the current line. |
| **[Collapse](selection_collapse)** | Collapses the selection to the active point. |
| **[Copy](selection_copy)** | Copies the selection to the Clipboard. |
| **[CopyLink](selection_copylink)** | Copies the hyperlink at the cursor to the Clipboard. |
| **[Cut](selection_cut)** | Moves the selected text to the Clipboard. |
| **[Delete](selection_delete)** | Deletes the contents of the selection. |
| **[DeleteLeft](selection_deleteleft)** | Deletes the contents of the selection, or the specified number of characters to the left of the cursor. |
| **[DestructiveInsert](selection_destructiveinsert)** | Inserts text, overwriting the existing text. |
| **[DuplicateLine](selection_duplicateline)** | Duplicates the current line. |
| **[EndOfDocument](selection_endofdocument)** | Moves the cursor to the end of the document. |
| **[EndOfLine](selection_endofline)** | Moves the cursor to the end of the current line. |
| [**ExtractFrequent**](extract_frequent) | Extracts frequently used strings into a new document. |
| **[Find](selection_find)** | Searches for the specified string. |
| **[FindRepeat](selection_findrepeat)** | Repeats the previous search for the same string. |
| **[Format](selection_format)** | Inserts or deletes newline characters in the selection. |
| **[GetActivePointX](selection_getactivepointx)** | Returns the column number of the cursor position. |
| **[GetActivePointY](selection_getactivepointy)** | Returns the line number of the cursor position. |
| **[GetAnchorPointX](selection_getanchorpointx)** | Returns the column number of the origin point of the selection. |
| **[GetAnchorPointY](selection_getanchorpointy)** | Returns the line number of the origin point of the selection. |
| **[GetBottomPointX](selection_getbottompointx)** | Returns the column number of the bottom of the selection. |
| **[GetBottomPointY](selection_getbottompointy)** | Returns the line number of the bottom of the selection. |
| **[GetTopPointX](selection_gettoppointx)** | Returns the column number of the top of the selection. |
| **[GetTopPointY](selection_gettoppointy)** | Returns the line number of the top of the selection. |
| **[GoToBrace](selection_gotobrace)** | Moves the cursor to the corresponding bracket / brace. |
| **[Indent](selection_indent)** | Indents the selected lines by the specified number of indentation levels. |
| **[InsertDate](selection_insertdate)** | Inserts the current time and date. |
| **[InsertFromFile](selection_insertfromfile)** | Inserts the contents of the specified file at the cursor position. |
| **[LineDown](selection_linedown)** | Moves the cursor down a specified number of lines. |
| **[LineOpen](selection_lineopen)** | Inserts an empty line between two lines. |
| **[LineUp](selection_lineup)** | Moves the cursor up a specified number of lines. |
| **[NewLine](selection_newline)** | Inserts the specified number of newline characters at the cursor. |
| **[NextBookmark](selection_nextbookmark)** | Moves to the next bookmark in the document. |
| **[OpenLink](selection_openlink)** | Opens the hyperlink at the cursor. |
| **[PageDown](selection_pagedown)** | Moves the cursor the specified number of pages down in the document. |
| **[PageUp](selection_pageup)** | Moves the cursor the specified number of pages up in the document. |
| **[Paste](selection_paste)** | Inserts the Clipboard contents at the cursor. |
| **[PreviousBookmark](selection_previousbookmark)** | Moves to the previous bookmark in the document. |
| **[Replace](selection_replace)** | Replaces a string in the document. |
| **[SelectAll](selection_selectall)** | Selects the entire document. |
| **[SelectColumn](select_column)** | Selects specified columns in a CSV mode. |
| **[SelectLine](selection_selectline)** | Selects a line at the cursor. |
| **[SelectWord](selection_selectword)** | Selects an entire word at the cursor. |
| **[SetActivePoint](selection_setactivepoint)** | Moves the cursor position and optionally extends the selection. |
| **[SetAnchorPoint](selection_setanchorpoint)** | Sets the origin point of the selection. |
| **[SetBookmark](selection_setbookmark)** | Sets a bookmark at the cursor position. |
| **[Sort](sort)** | Sorts or removes duplicate split strings in the selection. |
| **[StartOfDocument](selection_startofdocument)** | Moves the cursor to the start of the document. |
| **[StartOfLine](selection_startofline)** | Moves the cursor to the start of the line. |
| **[Tabify](selection_tabify)** | Converts spaces to tabs in the selection. |
| **[TagJump](selection_tagjump)** | Jumps to a tag at the cursor. |
| **[UnIndent](selection_unindent)** | Removes indents from the selected text by the specified number of indentation levels. |
| **[Untabify](selection_untabify)** | Converts tabs to spaces in the selection. |
| **[WordLeft](selection_wordleft)** | Moves the cursor the specified number of words to the left. |
| **[WordRight](selection_wordright)** | Moves the cursor the specified number of words to the right. |

## Version

Supported on EmEditor Professional Version 4.00 or later.


```{toctree}
:hidden:
:maxdepth: 1
average
batch_find
batch_replace
extract_frequent
select_column
selection_changecase
selection_changewidth
selection_charleft
selection_charright
selection_clearbookmark
selection_collapse
selection_copy
selection_copylink
selection_count
selection_cut
selection_delete
selection_deleteleft
selection_destructiveinsert
selection_duplicateline
selection_endofdocument
selection_endofline
selection_find
selection_findrepeat
selection_format
selection_getactivepointx
selection_getactivepointy
selection_getanchorpointx
selection_getanchorpointy
selection_getbottompointx
selection_getbottompointy
selection_gettoppointx
selection_gettoppointy
selection_gotobrace
selection_indent
selection_insertdate
selection_insertfromfile
selection_isactiveendgreater
selection_isempty
selection_linedown
selection_lineopen
selection_lineup
selection_mode
selection_newline
selection_nextbookmark
selection_openlink
selection_overwritemode
selection_pagedown
selection_pageup
selection_paste
selection_previousbookmark
selection_replace
selection_selectall
selection_selectline
selection_selectword
selection_setactivepoint
selection_setanchorpoint
selection_setbookmark
selection_startofdocument
selection_startofline
selection_tabify
selection_tagjump
selection_text
selection_unindent
selection_untabify
selection_wordleft
selection_wordright
sort
sum
```
