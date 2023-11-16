# Macro Temporary Options dialog box

This dialog box appears when the
[**Run with Temporary Options** command](../../cmd/macros/macro_run_options) is selected.

## Macro text box

Specifies the macro file name to run. If the current macro has been recorded and unsaved, this text box shows "(Untitled)".

## ... button

Click this button to display the **Open** dialog box where you can select a macro file to run.

## ▼ button

Click this button to display the default macro, the (Clipboard) option and the list of **My Macros**.

## Set this as the default macro check box

If this is checked, the selected macro will be set as the default macro.

## Set Repeat Count check box and text box

Specifies the number of times the macro repeats.

## Stop if Search Fails check box

If this box is checked, the macro will be stopped when finding or replacing a string
fails. It is useful when you want to repeat a macro that finds or replaces a
string.

## Suppress redraw check box

If this box is checked, the macro starts with "Redraw = false". EmEditor will suppress redraw of changes until "Redraw = true" or the end of macro is reached.

## Run the macro against each opened document check box

If this box is checked, you can specify files to open before running the macro. The macro will be run immediately after each specified file is opened. If the **Repeat Count** is specified, the macro will be repeated for each opened file.

## Name list box

Specifies the files to open if the **Run the macro against each opened document** check box is set.

## Add button

Adds an item to the list.

## Delete button

Deletes the selected items from the list.

## Save and close each document after running the macro check box

If this is checked, each opened file will be saved and closed after running the macro.

## Save options check box

If this is checked, the settings will be saved.

