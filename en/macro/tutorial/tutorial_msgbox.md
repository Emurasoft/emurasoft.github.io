# Display a Message Box (Tutorial)

To display simple text in a message box, you can use [alert \
Method](../window/window_alert) or [confirm Method](../window/window_confirm).
However, these methods can only display three buttons: YES, NO, and CANCEL.
To display more complex text in a message box, use Popup Method of WshShell Object.

The following example code displays the text Continue? and then YES, NO, and CANCEL buttons.
The variable n is assigned the value 6 if YES button is selected, 7 if NO button is selected, or 2 if CANCEL button is selected.

#### \[JavaScript (JScript)\]

WshShell = new ActiveXObject( "WScript.Shell" );

n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 );

#### \[VBScript\]

Set WshShell = CreateObject( "WScript.Shell" )

n = WshShell.Popup( "Continue?", 0, "EmEditor", 3 )

## References

)
