# Record Macro

To record a macro, select the [**Start/Stop Macro Record** command](../../cmd/macros/quick_macro_record).
The mouse pointer should then turn into a video camera icon, indicating that
macro recording is active.
In this state, you can record most operations in EmEditor.
Let's start our tutorial by typing the following text:

"EmEditor supports macros."

After typing the text, select the [**Start/Stop Macro Record** command](../../cmd/macros/quick_macro_record) again.
The video camera icon should return to the original Windows mouse pointer.

We have now recorded the insertion of the text "EmEditor supports macros _."_ into EmEditor.

We call this a "temporary macro" since it has not yet been saved to a file
(it is temporarily saved in the Windows Registry). You can execute the temporary
macro by selecting the
[**Run Macro** command](../../cmd/macros/quick_macro_run). The temporary macro is stored until a new operation is recorded in the macro, and can be executed as many times as you want. When you exit EmEditor and reopen it later, the
temporary macro will still be available.

A temporary macro provides a quick, convenient way of automating tasks.
If you want to record and execute multiple macros, however, you need to save the macro
(see **[Save Macro](tutorial_save)**).

## Tips

EmEditor can record most operations involving keystrokes and mouse pointer movements.

## Next Topic: