# Options page

The **Options** page allows you to set options related to the **Macros** menu.

## Add to My Macros when New Macro is Saved or   Selected check box

If this box is checked, when a new macro is selected by the
[**Save Macro** command](../../../cmd/macros/macro_save) or the
[**Select Macro** command](../../../cmd/macros/macro_select), the
macro will be added to **My Macros**.

## Ask Macro Language when Editing New Recorded Macro check box

Displays a dialog box to select a macro language from JavaScript or VBScript
when selecting the **Edit Macro** command while a temporary macro is selected.

## Running one of My Macros will set it as the default macro check box

If this box is checked, when you select one of **My Macros** or press the shortcut key assigned to a macro, the selected macro will be set as the default macro.

## Run macros asynchronously by default check box

If this box is checked, EmEditor runs macros asynchronously if the [**#async** directive](../../../macro/directive/async) is not used.

## Use V8 as JavaScript engine check box

If this box is checked, EmEditor runs JavaScript macros using the V8 engine if the [**#language** directive](../../../macro/directive/language) is not used.

## Always open macros without a Unicode signature (BOM) as UTF-8 check box

If this box is checked, and if a macro file does not have a Unicode signature (BOM), EmEditor opens the file as UTF-8 without displaying a dialog box to select the encoding with which the file should be opened.

## Default language option

Specifies the default language for a macro. If the Clipboard is selected for the macro, this option selects the language of the macro in the Clipboard.

## Folder text box

Specifies the default folder for **My Macros**. When you select a macro by using
the [**Save Macro** command](../../../cmd/macros/macro_save) or the
[**Select Macro** command](../../../cmd/macros/macro_select), this
folder will be the default folder.

## ... button

Click this button to find the specified file.

## Reset button

Resets to default settings.

