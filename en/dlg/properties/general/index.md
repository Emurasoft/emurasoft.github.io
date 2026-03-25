# General page

The **General** page allows you to set properties related to basic operations.

## Wrap by drop-down list box

Specifies how lines should wrap. Select one of the following options.

|     |     |
| --- | --- |
| **No wrap** | Does not wrap lines. |
| **Specified characters** | Wraps by a specified length of characters (in bytes). The length of characters can be specified at **Normal line margin** text box or **Quote Line Margin** text box. |
| **Window width** | Wraps according to the window width. If the window resizes, the wrapped position will resize. |
| **Page width** | Wraps according to the printed page width. |

## Display line and column numbers as drop-down list box

Specifies how line numbers and column position should be displayed. Select one of the following options.

|     |     |
| --- | --- |
| **Display coordinates** | Line numbers and column positions are counted as displayed. If a line wraps, the wrapped position is counted. The column position will be restored to one at the wrapped position. A full-width character is counted as two. It can be called a word-processor-like display. |
| **Logical coordinates** (full-width characters as 2 columns) | Line numbers and column positions are counted by real logical lines. Lines numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as two columns. A tab character is counted as one character. |
| **Logical coordinates** (full-width characters as 1 column) | Line numbers and column positions are counted by real logical lines. Line numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as one column. A tab character is counted as one character. |
| **Logical with tab** (full-width characters as 2 columns) | Line numbers and column positions are counted by real logical lines. Line numbers and column positions do not depend on how lines are wrapped. A full-width character is counted as two columns. A tab character is counted as if it were replaced by spaces. |

## Normal line margin text box

The length of lines in bytes that do not begin with quote characters when **Wrapped by** **Specified characters** is selected.

## Quoted line margin text box

The length of lines in bytes that begins with quote characters when **Wrapped by specified characters** is selected.

## Quote character text box

Specifies a quote character that EmEditor uses for the **Quoted line margin** text box. It is also used by the [**Copy in Quotes** command](../../../cmd/edit/edit_copy_prefix).

## Show line numbers checkbox

Shows line numbers on the left side of the window. To print line numbers when printing, you will need to check the **Print Line Numbers** checkbox on the **Print** page.

## Show ruler checkbox

Shows the ruler on the top of the window.

## Show zero-based line/column numbers checkbox

Shows zero-based line numbers and column numbers instead of one-based numbers. This option does NOT alter macro or plug-in behaviors.

## Run input method editor checkbox

Runs an Input Method Editor (IME) when running EmEditor.

## No space at the left edge of the window checkbox

Does not display a space along the left edge of the EmEditor window when line numbers are not displayed.

## Show page numbers checkbox

Displays page numbers. Page break lines will be drawn, and page numbers will be displayed in the status bar to show in which page the cursor is located. If line numbers are displayed, the line numbers are based from the top of each page. Page numbers might not be displayed if a printer is unavailable.

## Allow inserting control characters checkbox

If this box is checked, you can insert a control character by typing CTRL + an alphabetical key, or CTRL + SHIFT+ an alphabetical key, as long as it is not configured elsewhere as a shortcut key. If this box is not checked, you cannot insert a control character in this way.

## Preserve newline characters on the clipboard checkbox

If this box is checked, the newline characters will be preserved when you copy and paste text. For instance, the LF only returns will be copied and pasted to another location with LF only returns.

## Always paste as the system default encoding checkbox

If this box is checked, text is pasted from the Clipboard not as Unicode, but always as the [system default encoding](../../../glossary/systemdefaultencoding). This option is sometimes useful when you want to copy text from other applications that have a problem converting text from the [system default encoding](../../../glossary/systemdefaultencoding) to Unicode.

## Enable virtual space checkbox

When this is checked, the cursor can move beyond the end of each line, and spaces are inserted when a character is inserted beyond the end of each line.

## Tab/Indent button

Press this button to display the [**Tab/Indent** dialog box](indent/index) to specify **Auto Indent** settings.

## Reset button

Resets to default settings. The [**Reset** dialog box](../reset/index) will be displayed and will allow you to copy from another configuration.

You can also move to the following dialog box from this page.

[**Tab/Indent** Dialog Box](indent/index) (Select the **Tab/Indent** button)

```{toctree}
:maxdepth: 1
:hidden:
indent/index
```
