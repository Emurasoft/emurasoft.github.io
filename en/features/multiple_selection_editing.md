# Multiple Selection Editing

The new version of EmEditor allows you to select multiple locations within a document. To make multiple selections, after making one selection, make another selection with the mouse while pressing the CTRL key. Alternatively, you can press the F8 key, move the cursor to extend the selection, press the F8 key again to finish the selection, move the cursor again to go to the next selection position, and repeat this procedure until you make all selections. Moreover, the **[Add Next Occurrence](../cmd/search/add_next_occurrence)** command (CTRL+R) will find the same text as the word at the cursor. The **[Add Next Next Occurrence](../cmd/search/add_next2_occurrence)** command will skip the next occurrence, but add the occurrence after the next one. The **[Select All Occurrences](../cmd/search/select_all_occurrences)** command (CTRL+SHIFT+A) will select all the occurrences.

After you make multiple selections, you can type new text to replace all the selections at once. Pressing the BACKSPACE key removes the last character in each selection. Moreover, you can use many conversion commands against the selections.

The **Find All** button was added to the **[Find](../dlg/find/index)** dialog box, which allows you to select all the occurrences.

Along with multiple selection editing, vertical selection editing has also been enhanced. For instance, pressing BACKSPACE with the zero-width vertical selection now removes the last character in each line. This allows you to remove the end portions of text in multiple lines more easily than ever!

The **[Switch Starting Point and Ending Point](../cmd/edit/switch_start_end_select)** command (SHIFT+F8) was also added in v13. Before the new version, you could move the ending point by pressing arrow keys while pressing the SHIFT key, but couldn't move the starting point. Now with the new version, you can move the cursor to the selection starting point by pressing SHIFT+F8, and then adjust the selection starting point.
