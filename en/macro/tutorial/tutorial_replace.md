# Replace a String (Tutorial)

To replace a string in files, add the ninth and tenth line to our tutorial macro:

## \[JavaScript\]

```
document.selection.Text = "EmEditor supports macros.";
document.selection.NewLine();
document.selection.Text = "\\tEmEditor is a text editor.";
document.selection.CharLeft( false, 12 );
document.selection.DeleteLeft( 15 );
document.selection.CharRight( true, 9 );
document.selection.ChangeCase( eeCaseUpperCase );
if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);
n = document.selection.Replace( "editor", "######", eeReplaceAll );
alert( n + " strings found!" );
```

## \[VBScript\]

```
document.selection.Text = "EmEditor supports macros."
document.selection.NewLine
document.selection.Text = Chr(9) & "EmEditor is a text editor."
document.selection.CharLeft False, 12
document.selection.DeleteLeft 15
document.selection.CharRight True, 9
document.selection.ChangeCase eeCaseLowerCase
If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"
n = document.selection.Replace( "editor", "######", eeReplaceAll )
alert n & " strings found!"
```
Save the above macro and run it in a new EmEditor Window. Notice that two of the string "editor" has been
searched case-insensitively and replaced with the string "######", and then a message box with the text
" Two strings found!" is displayed.
The first argument of the [Replace Method](../selection/selection_replace)
specifies the string to search for, the second argument specifies the string to replace with, and the third argument
specifies a combination of flags. The method returns the number of strings that have been replaced.
If you specify eeReplaceAll in the third argument, the method will replace the string at once
and thus might return a number more than 1.
See the argument explanations of the [Replace Method](../selection/selection_replace) for more details on flags for the third argument.
Normally in the [Replace Method](../selection/selection_replace),
similar to the [Find Method](../selection/selection_find),
the execution of a macro is not terminated when the search string is not found. There is an exception, however.
If you execute a macro with the
Stop if Search Fails check box
selected by selecting the [Run with Temporary Options command](../../cmd/macros/macro_run_options) under the Macro menu
and bringing up the [Macro Temporary Options dialog box](../../dlg/macro_temp_options/index),
the execution of the macro is terminated when the search string is not found.
See [Find a String](tutorial_find) in our tutorial for more details.
