# General page

The **General** page allows you to set properties related to basic
operations.

## Wrap by drop-down list box

Specifies how lines should wrap. Select one of the following options.

|     |     |
| --- | --- |
| **No Wrap** | Does not wrap lines. |
| **Specified Characters** | Wraps by a specified length of characters (in bytes). The length of <br> characters can be specified at **Normal**<br>**Line Margin** text box or **Quote**<br>**Line Margin** text box. |
| **Window Width** | Wraps according to the window width. If the window resizes, the wrapped position will resize. |
| **Page Width** | Wraps according to the printed page width. |

## Line and Column Display as drop-down list box

Specifies how line numbers and column position should be displayed. Select
one of the following options.

|     |     |
| --- | --- |
| **Display Coordinates** | Line numbers and column positions are counted as displayed. If a line <br> wraps, the wrapped position is counted. The column position will be restored <br> to one at the wrapped position. A full-width character is counted as two. It <br> can be called a word-processor-like display. |
| **Logical Coord.** (Full-Width Char. as 2 Col.) | Line numbers and column positions are counted by real logical lines. <br> Lines numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as two columns. A tab character is counted as <br> one character. |
| **Logical Coord.**(Full-Width Char. as 1 Col.) | Line numbers and column positions are counted by real logical lines. <br> Line numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as one column. A tab character is counted as <br> one character. |
| **Logical w/Tab**(Full-Width Char. as 2 Col.) | Line numbers and column positions are counted by real logical lines. <br> Line numbers and column positions do not depend on how lines are wrapped. A <br> full-width character is counted as two columns. A tab character is counted as <br> if it were replaced by spaces. |

## Normal Line Margin text box

The length of lines in bytes that do not begin with quote characters when **Wrapped by**
**Specified Characters** is selected.

## Quoted Line Margin text box

The length of lines in bytes that begins with quote characters when **Wrapped by Specified**
**Characters** is selected.

## Quote Character text box

Quote character that EmEditor uses for the **Quoted Line**
**Margin** text box. It is also used by the
[**Quote** **Copy** command](../../../cmd/edit/edit_copy_prefix).

## Show Line Numbers check box

Shows line numbers on the left side of the window. To print line numbers when
printing, you will need to check the **Print Line Numbers** check box on the
**Print**
page.

## Show Ruler check box

Shows the ruler on the top of the window.

## Show Zero-based Line/Column Numbers check box

Shows zero-based line numbers and column numbers instead of one-based numbers. This option does NOT alter macro or plug-in behaviors.

## Run Input Method Editor check box

Runs an Input Method Editor (IME) when running EmEditor.

## No Space at Left Edge of Window check box

Does not display a space along the left edge of the EmEditor window when line
numbers are not displayed.

## Show Page Numbers check box

Displays page numbers. Page break lines will be drawn, and page numbers will be displayed in
the status bar to show in which page the cursor is located. If line numbers are
displayed, the line numbers are based from the top of each page. Page numbers
might not be displayed if a printer is unavailable.

## Allow Insert Control Character check box

If this box is checked, you can insert a control character by typing CTRL + an alphabetical
key, or CTRL + SHIFT+ an alphabetical key, as long as it is not configured elsewhere
as a shortcut key. If this box is not checked, you cannot insert a control character
in this way.

## Preserve Newline Characters on Clipboard check box

If this box is checked, the newline characters will be preserved when you copy and paste text.
For instance, the LF only returns will be copied and pasted to another location
with LF only returns.

## Always Paste as ANSI check box

If this box is checked, text is pasted from the Clipboard not as Unicode, but
always as the [system default encoding](../../../glossary/systemdefaultencoding). This option is sometimes useful when you want to copy text from
other applications that have a problem converting text from the
[system default encoding](../../../glossary/systemdefaultencoding)
to Unicode.

## Enable Virtual Space check box

When this is checked, the cursor can move beyond the end of each line, and spaces are inserted when a character is inserted beyond the end of each line.

## AI assisted writing check box

When this is checked, EmEditor will enable AI assisted writing. This option is enabled only if the **Enable AI** check box in the **AI** page of the **Customize** dialog box is set.

## Tab/Indent button

Press this button to display the [**Tab/Indent** dialog box](indent/index) to specify **Auto Indent** settings.

## Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

You can also move to the following dialog box from this page.

[**Tab/Indent** Dialog Box](indent/index) (Select the **Tab/Indent** button)

```{toctree}
:maxdepth: 1
:hidden:
indent/index
```
