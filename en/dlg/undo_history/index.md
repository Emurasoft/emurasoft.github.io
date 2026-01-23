# Undo/Redo History dialog box

This dialog box appears when the [**Undo/Redo History** command](../../cmd/edit/undo_history) is selected. You can jump to a particular action in the history, or export and import the undo/redo history.

## List

The Undo and Redo history for the current document is displayed in this list. Items below the selection represent the Redo actions, and items above the selection represent the Undo actions. You can click an item to jump to the particular action. The '#' mark on the left of the list means the saved action or the new document. Right-clicking will display the context menu where you can select all or copy selected item strings to the Clipboard.

## Undo button

Starts undoing the selected actions.

## Redo button

Starts redoing the selected actions.

## Undo All button

Starts undoing all the previous actions.

## Redo All button

Starts redoing all the previous actions.

## Import button

Imports a previously exported CSV file containing the Undo/Redo history. The current document must be identical to one from which the history was exported.

## Export button

Exports the Undo/Redo history into a CSV file. When you import the file next time, the document must be identical to the current document. If you would like to redo the same actions in the future by importing the history, you should **Undo All** before you export the history.

## Clear All button

Clicking this button clears all the actions in the Undo/Redo history.

