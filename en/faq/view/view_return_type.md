# Q. How can I find the return type (e.g. CR, LF, CR+LF) for each line?

If you set the **Character Code at Cursor** checkbox in the **Status** tab of the **Customize** dialog box, and when the cursor is at end of any line, you will see **0D+0A** (CR+LF) or **0D** (CR only) or **0A** (LF only). You
can also check the **Show CR and LF with Different Marks** in the **Marks** tab of Properties to distinguish the return types. Since each line can have different return types in EmEditor, this is how EmEditor displays the return types for each
line.
