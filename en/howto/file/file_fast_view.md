# To Open and Edit Huge Files in Fast View Mode

Fast View mode opens a huge file almost instantly, without loading it into memory. EmEditor finds the lines in the background and reads only the lines on the screen. Your edits are kept separately, and the file does not change until you save it.

## To Open a File in Fast View Mode

- Open a file that is larger than the **Minimum file size to enable Fast View mode** (4,096 MB by default), which is set on the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box. The file opens in Fast View mode automatically, and a notification appears. To never open files in Fast View mode automatically, set the size to **0**.
- To switch the current document between the normal mode and Fast View mode, select the [**Fast View** command](../../cmd/edit/fast_view) on the **Edit** menu, or double-click **FAST** on the status bar. You can also select the **Fast View mode** check box in the [**Large File Controller**](../../cmd/view/large_file_bar) and click **Apply**.
- A file that has a diff file (see below) always opens in Fast View mode, even if it is smaller than the minimum file size.

While a document is in Fast View mode, **FAST** appears on the status bar, and a lightning bolt icon appears on the document tab. Untitled documents cannot be switched to Fast View mode.

You can jump to the end of a file as soon as it starts opening, while EmEditor is still finding the lines. Line numbers appear once all the lines are found.

## What You Can Do in Fast View Mode

- Scroll (including smooth scrolling), select text (including vertical and multiple selections), copy, jump, and use [**Filter**](../../cmd/edit/filter_word) and [**Narrowing**](../../cmd/edit/narrowing_toggle). While narrowing, editing and the commands that change the whole document affect only the narrowed lines.
- Display highlighted strings, comments, quoted strings, markers, bookmarks, the ruler, and the [**Marks**](../../cmd/view/view_marks).
- Find, count, replace, and extract text, including with regular expressions and text that spans lines. Many of the options of the **Find** dialog box, the **Find** toolbar, and the [**Advanced** dialog box](../../dlg/advanced/index) are available. {{profree}}
- Reload the file in a different encoding, [**Compare**](../../cmd/diff/index) documents, and run [external tools](../../cmd/external_tools/index), macros, plug-ins, and the commands on the [**AI** menu](../../cmd/ai/index). {{pro}}
- Use the CSV modes, including the [**Cell Selection Mode**](../../cmd/csv/csv_cell_mode). {{pro}}
- You can edit and use most of the commands that can change the document, including [**Undo**](../../cmd/edit/edit_undo)/[**Redo**](../../cmd/edit/edit_redo), the [**Insert**](../../cmd/insert/index), [**Convert**](../../cmd/convert/index), [**Sort**](../../cmd/sort/index), and [**CSV**](../../cmd/csv/index) menus, and macros and plug-ins. See [Limitations](#limitations) for the features that are not supported in Fast View mode.

You cannot edit a document if the file is read-only, is opened in Binary (Hexadecimal View), or is partly opened with the [**Large File Controller**](../../cmd/view/large_file_bar), while a filter is applied, or while documents are being compared. To stop editing, turn on [**Read Only**](../../cmd/edit/read_only). Commands that change many lines run on multiple threads. EmEditor keeps your edits in memory, and a message appears if they need more memory than is available. If this happens, save your edits or switch to the normal mode.

## To Save Edits

Saving a huge file can take a long time, so when you [**Save**](../../cmd/file/file_save) a document in Fast View mode, EmEditor asks how you want to save it:

- **Save and merge now** writes your changes into the file.
- **Save only my changes** saves your changes to a diff file and leaves the original file untouched. The next time you open the file, the changes are applied automatically. You can merge them into the file later by choosing **Save and merge now**.

If you select **Do not show this message again**, EmEditor remembers your choice. To change it later, use the **Prompt when saving a huge file in Fast View mode** and **Save only the changes to a diff file when saving a huge file in Fast View mode** options on the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box. [**Save As**](../../cmd/file/file_save_as) always writes the whole file, including your changes.

You can also use the following commands on the **File** \> **Diff** submenu of the [**All Commands**](../../cmd/tools/all_commands) menu:

- [**Save Diff**](../../cmd/file/fast_view_save_diff) saves your edits to the diff file.
- [**Load Diff**](../../cmd/file/fast_view_load_diff) applies the edits saved in the diff file.
- [**Discard Diff**](../../cmd/file/fast_view_discard_diff) discards your edits and deletes the diff file.

## Diff Files

A diff file stores your edits to a file and the positions of its lines, so that a huge file opens instantly the next time, without finding the lines again. Diff files are saved in the **FastView** folder in the EmEditor local application data folder, not next to the original files.

- When the **Save the line positions of huge files so they open instantly next time** option is on (the default), the line positions of a file larger than the minimum file size are saved once they are found, and again when the file is saved.
- If you rename or move the file outside EmEditor, its diff file still applies to it.
- A diff file cannot be applied if the file has changed since the diff file was saved, if the file is opened in a different encoding, or if the CSV setting that allows newlines in quoted cells is different.
- Diff files that contain only line positions are deleted automatically when their file changes size or has been missing for more than 30 days. Only the newest 100 of them are kept. Diff files that contain edits are never deleted automatically.
- To view and delete diff files, use the [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box.

Documents in Fast View mode are included in workspaces. When a workspace is saved, the line positions of each unmodified document are saved too, so the workspace opens without finding the lines again. Unsaved edits are saved in the workspace, and the document is restored as modified.

## Limitations

- Each document can have up to 100,000 bookmarks, and the vertical scroll bar shows up to 100,000 found string markers.
- The **Prompt if a null character is found** and **Prompt if an invalid character is found** options check only the beginning of the file. For details, see the [**File** page](../../dlg/properties/file/index) of the **Properties** dialog box.

The following features are not available in Fast View mode. To use them, switch to the normal mode.

- **File** menu: [**Verify**](../../cmd/file/file_verify), [**Print**](../../cmd/file/file_print), [**Print Now**](../../cmd/file/file_print_direct), and [**Print Preview**](../../cmd/file/print_preview).
- **Edit** menu: [**Find Matching Tag**](../../cmd/edit/next_tag), [**Matching Tag Extend**](../../cmd/edit/shift_next_tag), the **Markdown/HTML** submenu (including [**Markdown Design View**](../../cmd/edit/markdown_view)), [**Spelling**](../../cmd/edit/spell_toggle), and [**Syntax Check**](../../cmd/edit/csv_validate).
- **Insert** menu: [**AutoFill/AutoRepeat**](../../cmd/insert/auto_fill).
- **Convert** menu: [**Remove Newline Characters**](../../cmd/convert/delete_cr_wrap), [**Join Lines**](../../cmd/convert/join_lines), and the Base64, Markdown, and HTML conversions of **Encode/Decode Selection**.
- **Bookmarks** menu: [**Invert Bookmarks**](../../cmd/bookmarks/bookmark_invert) and [**Select Bookmarked Lines**](../../cmd/bookmarks/bookmark_select).
- **Search** menu: [**Find Next/Previous Warning Character/Unicode**](../../cmd/search/find_next_unicode) and [**Erase Unicode Highlight**](../../cmd/search/erase_unicode_hilite).
- **Find** dialog box and **Find** toolbar: **Incremental search**. With **Search all documents in the group**, **Select All** and **Extract** skip the Fast View documents other than the active document. (**Find Next**, **Count**, and **Bookmark** search all of them.)
- **Filter** toolbar: **Incremental Search** and **Block Multiline Changes**.
- **View** menu: the **Wrap** commands, the [**Syntax Checker**](../../cmd/view/toggle_validation_bar), the [**Outline Bar**](../../cmd/view/outline_bar) and [**Outline Guide**](../../cmd/view/outline_guide), the **Tab/Indent** options, [**Tag Links**](../../cmd/view/tag_links), [**Clear Markers for Saved Lines**](../../cmd/view/clear_saved_markers), and the [**Minimap**](../../cmd/window/minimap_toggle).
- **CSV** menu: [**Convert to Fixed Width Columns**](../../cmd/csv/convert_to_fixed_width), [**Flash Fill**](../../cmd/csv/flash_fill), [**Transpose**](../../cmd/csv/transpose), [**Pivot Table**](../../cmd/csv/pivot_table), [**Unpivot**](../../cmd/csv/unpivot), the **Separators** submenu, and **Convert**, [**Auto Add Separators**](../../cmd/csv/auto_add_separators), and **Truncate Unfit** on the **CSV Converter** bar.
- Macros: the **AutoFill**, **ConvertCsv**, **PivotTable**, and **Unpivot** methods of the **Document** object fail. {{pro}}

## See Also

- [**Fast View** command](../../cmd/edit/fast_view)
- [**Fast View** page](../../dlg/customize/fast_view/index) of the **Customize** dialog box
- [**FastView** property](../../macro/document/fast_view) of the **Document** object
