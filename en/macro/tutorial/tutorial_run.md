# Run Macro (Tutorial)

When you save a macro file, the macro becomes the default macro file, and thus, will be loaded the next time
you select the [**Run Macro**command](../../cmd/macros/quick_macro_run). If you open the **Macros** menu, "tutorial.jsee" or "tutorial.vbee"
appears at the right-side of the **Run** command.
Also, if you place the mouse pointer on top of the **Run Macro** button,
"Run Macro tutorial.jsee" or "Run Macro tutorial.vbee" should
appear. In short, a macro file name that appears at the selection of the macro execution command is the default macro. EmEditor saves the default macro until it records a new macro, or selects or saves
another macro. When you exit EmEditor and reopen it, the default macro remains the same.

Now select the [**New Text** command](../../cmd/file/file_new) to display a new EmEditor window. Then select
the
[**Run Macro** command](../../cmd/macros/quick_macro_run). The previously recorded macro should be displayed:

"EmEditor supports macros _."_

You can run this macro as many times as you want.

Keep in mind that, when you record or select another macro, you are replacing the default macro with it, and thus,
you can't execute the macro that you've previously saved in the single operation shown above.
In this case, you can use either of the methods below to run a macro that has been previously recorded:

1. Click the [**Select Macro**command](../../cmd/macros/macro_select).
In the resulting **Open File** dialog box, select a macro file you want to run (in this tutorial,
tutorial.jsee or tutorial.vbee).
Run the macro by following the steps described earlier.

2. Select **Macros**. The **Macros** menu includes a list of macros that
have been saved. Let's call the list "My Macros". You can run a macro by
selecting one from the list (in this tutorial, tutorial.jsee or
tutorial.vbee).

By default, EmEditor automatically adds a macro that has been recorded or
selected to **My Macros**. If you don't want your macros automatically added
to **My Macros**, select the [**Customize Macros** command](../../cmd/macros/customize_macro).
In the [**Options** page](../../dlg/macro_customize/options/index) of the resulting
[**Customize Macros** dialog box](../../dlg/macro_customize/index),
click to clear the
**Add to My Macros when New Macro is Saved or Selected** check box. This
action turns off the feature and a macro won't automatically be added to **My Macros** when you save or select a macro.

Also, if you want to delete a macro file, select the name of the macro file you want to delete from
the [**My Macros**page](../../dlg/macro_customize/my_macros/index) in the [**Customize** **Macros** dialog box](../../dlg/macro_customize/index), then click the **Delete** button. This page also allows you to change the order of macro files
shown in the **Macros** menu.

If you want to run a macro from a shortcut key on your keyboard, you can assign
a shortcut key to the macro by selecting the
[**Keyboard** tab](../../dlg/properties/keyboard/index) from
the [**Properties for All Configurations**command](../../cmd/tools/all_prop) or the [**Properties for****Current Configuration**command](../../cmd/tools/customize).
