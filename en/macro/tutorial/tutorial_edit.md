# Edit Macro (Tutorial)

EmEditor automatically makes the last macro used the default macro. To edit the
default macro, select the
[**Edit Macro** command](../../cmd/macros/macro_edit).  The macro opens in a new EmEditor window. If
you wish to open a non-default macro, select the
[**Select Macro** command](../../cmd/macros/macro_select) and choose the macro
you wish to edit.  This action sets the macro to default. You can now edit the
macro by selecting the
[**Edit Macro** command](../../cmd/macros/macro_edit). In this tutorial, we will edit tutorial.jsee or
tutorial.vbee.
Upon opening one of the files, the following text should appear:

#### \[JavaScript\]

document.selection.Text="EmEditor supports macros.";

#### \[VBScript\]

document.selection.Text="EmEditor supports macros."

The above code uses the **[Text \**
**Property](../selection/selection_text)** and tells EmEditor to insert the text "EmEditor supports macros _."_
at the current cursor location.

## Next Topic:
