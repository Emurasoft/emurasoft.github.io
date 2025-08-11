# Highlight (1) page

The **Highlight (1)** page allows you to set properties related to highlight
(1).

## Enable Keyword Highlight check box

If this is checked, EmEditor will highlight specified keywords.

## Enable Keyword Highlight drop-down list box

Specifies the type of keywords to be highlighted. Select one of the following options.

|     |     |
| --- | --- |
| **Only User-Defined Strings** | Only highlights the strings specified in the User-Defined Strings list box. |
| **Only Default Keywords** | Only highlights default configuration keywords. |
| **Both User-Defined Strings and Default Keywords** | Highlights both user-defined strings and default configuration keywords. |

## User-Defined Strings list box

List of highlighted strings. Clicking the check box will change the color.
These numbers correspond to the highlight colors specified on the
[**Display** page](../display/index).

## Add button

Click this button to add a new item to the list.

## Delete button

Click this button to delete the selected item from the list.

## Add Default button

Click this button to add default keywords to the list.

## Whole Word Only check box

Highlight the selected string only if the whole word is the string.

## Highlight Right Side check box

Highlight the selected word and the right of the word on the
line only up to the word wrapped position.

## Highlight Right All check box

Highlight the selected word and everything to the right of the word on the
line up to the window border (if no wrap or wrap by window is selected) or specified width or page width.

## Match Case check box

Highlight the selected word only if the case matches.

## Inside Tag Only check box

Highlight the string only if the string is inside a tag.

## Regular Expression check box

Highlight the selected string using a regular expression.

## Color drop-down list box

Specifies the color to highlight the selected string.

## Begin Tag text box

The beginning character of the tag. You can set each string to be highlighted
only if it exists inside the tag.

## End Tag text box

The end character of the tag. You can set each string to be highlighted only
if it exists inside the tag.

## Import button

Import highlighted strings from CSV or ESY type file. The CSV file contents are organized
as string, **Color**, **Whole Word Only**, **Highlight**
**Right Side**, **Match Case**, and **Inside Tag Only**. The ESY file syntax can be found at the following page.

**See Also**

- [To Create a New Syntax File](../../../howto/customize/syntax_file)

## Export button

Export highlighted strings to CSV or ESY type file. The CSV file contents are organized as
string, **Color**, **Whole Word Only**, **Highlight**
**Right Side**, **Match Case**, and **Inside Tag Only**. The ESY file syntax can be found at the following page.

**See Also**

- [To Create a New Syntax File](../../../howto/customize/syntax_file)

## Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

## Tips

When Regular Expression is enabled, you can add these special directives to conditionally apply a highlight based on the formatting at the start of the match. Place the directive at the very beginning of your pattern.

- `(?#_text_c==n)` Apply the highlight only if the current text (foreground) color is n.
- `(?#_text_c!=n)` Apply the highlight only if the current text (foreground) color is not n.
- `(?#_back_c==n)` Apply the highlight only if the current background color is n.
- `(?#_back_c!=n)` Apply the highlight only if the current background color is not n.
- `(?#_font_s==n)` Apply the highlight only if the current font style is n.
- `(?#_font_s!=n)` Apply the highlight only if the current font style is not n.

Here, n is an integer ID defined in plugin.h (for example, 0 = SMART_COLOR_NORMAL, 17 = SMART_COLOR_HILITE_4, etc.).

Example: instead of `%%.*$`, use `(?#_text_c!=17)%%.*$` to highlight lines that start with `%%` only if they don’t already use color 17 (SMART_COLOR_HILITE_4).
