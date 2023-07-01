# Find in Files (Tutorial)

To find a string in files, add the eighth line to our tutorial macro:

#### \[JavaScript\]

document.selection.Text = "EmEditor supports macros.";

document.selection.NewLine();

document.selection.Text = "\\tEmEditor is a text editor.";

document.selection.CharLeft( false, 12 );

document.selection.DeleteLeft( 15 );

document.selection.CharRight( true, 9 );

document.selection.ChangeCase( eeCaseUpperCase );

if( document.selection.Find( "Em", eeFindPrevious ) )  alert( "Found!"
);

#### \[VBScript\]

document.selection.Text = "EmEditor supports macros."

document.selection.NewLine

document.selection.Text = Chr(9) & "EmEditor is a text editor."

document.selection.CharLeft False, 12

document.selection.DeleteLeft 15

document.selection.CharRight True, 9

document.selection.ChangeCase eeCaseLowerCase

If document.selection.Find( "Em", eeFindPrevious ) Then alert "Found!"

Save the above macro and run it in a new EmEditor Window. Now "Em" is searched and
a message box with the text "Found!" is displayed.

The first argument of the [Find Method](../selection/selection_find) specifies
a string to search for and the second argument specifies a flag to tell it how to search.
In this example, the second argument takes eeFindPrevious and searches backward from the current cursor position
to the top of the file.
The [Find Method](../selection/selection_find) returns 1 if the search string is found. Otherwise, 0 is returned.
In this example, the search string is found and 1 is returned, so the Then clause,
that is [alert Method](../window/window_alert), is executed.
The [alert Method](../window/window_alert) displays a simple message box with a OK button and the string of
the argument. In our tutorial, it displays the text "Found!".

The second argument of the [Find Method](../selection/selection_find)
allows you to specify a variety of flags. See the argument explanations of the
[Find Method](../selection/selection_find) for more details.

Normally, the execution of a macro is not terminated when the search string is not found. There is an exception, however.
If you execute a macro with the **Stop if Search Fails** check box selected in the **Run with Temporary Options** command
under the **Macro** menu, the execution of the macro is terminated when the search string is not found.
This **Run with Temporary Options** lets you perform searches in flexible ways. For example, if you want to repeat
an operation, such as search and replace, and you don't know how many times the operation will occur,
you can have the search terminate upon the failure of the search, without modifying the macro,
by specifying the number of operations to repeat in greater numbers than you think you need.

If you want to terminate the execution of a macro upon the failure of the search
without using the **Run with Temporary Options** command, then you need to modify the macro.
That is, when the [Find Method](../selection/selection_find) return 0, you terminate the macro.
The following code will do it:

#### \[JavaScript\]

if( !document.selection.Find( "xx", eeFindPrevious ) )  throw new
Error("Cannot find xx");

#### \[VBScript\]

If Not document.selection.Find( "xx", eeFindPrevious )  Then Err.Raise
vbObjectError + 1, "Find Error", "Cannot find xx"

Also, if you use [FindRepeat Method](../selection/selection_findrepeat),
you can search again for the string that you have previously searched for, and you can search for the word
where the cursor is positioned on.
If you specify the flags of [FindRepeat Method](../selection/selection_findrepeat) as follows,
it performs searches, which has the corresponding keyboard commands shortcuts.

|     |     |
| --- | --- |
| eeFindRepeatNext | Search again forward from the current cursor position for the string that you have previously searched for. Equivalent to F3. |
| eeFindRepeatPrevious | Search again backward from the current cursor position for the string that you have previously searched for. Equivalent to Shift + F3. |
| eeFindRepeatNext + eeFindRepeatWord | Search forward from the current cursor position for the selected string <br> or the word at the cursor. Equivalent to CTRL + F3. |
| eeFindRepeatPrevious + eeFindRepeatWord | Search backward from the current cursor position for the selected string <br> or the word at the cursor. Equivalent to CTRL + SHIFT + F3. |

## Next Topic:
