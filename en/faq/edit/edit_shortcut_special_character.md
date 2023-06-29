# Q. How can I assign a shortcut key to insert a special character?

Many shortcut keys are already assigned to insert many special characters by default. To see which keys are assigned, go to:

[Insert Special Characters](../../howto/edit/edit_special_char)

Any character can be assigned to your favorite shortcut key using a macro. For example, if you would like to insert ä with a shortcut key, write a macro (in this case, JavaScript):

document.selection.Text="ä";

and save this file as a file, for example, **InsertA.jsee**. Click **Select**... on the **Macros**, and select this file. Running this macro will insert this character. To assign a shortcut key to this macro, go to Configuration Properties, select
the Keyboard page, and then select My Macros from the Category drop-down list, and assign your favorite key to the macro.