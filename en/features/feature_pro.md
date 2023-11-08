---
orphan: true
---
# New Features exclusive to EmEditor Professional

## New features

- [Powerful and functionally-rich macros](macro)
- [Replace in Files](replace_in_files)
- [Find in Files specifying an Encoding](grep)
- [Combine Windows](tab_features)

## New commands

- [Close All without Save command](../cmd/file/quit_all)
- [Tabify command](../cmd/convert/tabify)
- [Untabify command](../cmd/convert/untabify)
- [Increase Line Indent command](../cmd/convert/indent)
- [Decrease Line Indent command](../cmd/convert/unindent)
- [Comment command](../cmd/convert/edit_comment)
- [Uncomment command](../cmd/convert/edit_uncomment)
- [Insert Caron command](../cmd/insert/insert_caron)
- [Tabify All command](../cmd/edit/space_to_tab)
- [Move to Last Edited Position command](../cmd/edit/move_last_edit)
- [Next Bookmark in This \
Window command](../cmd/bookmarks/bookmark_next_within)
- [Previous Bookmark in This \
Window command](../cmd/bookmarks/bookmark_prev_within)
- [Replace in Files command](../cmd/search/replace_in_files)
- [Marks command](../cmd/view/view_marks)
- [Increase Font Size command](../cmd/view/increase_font_size)
- [Decrease Font Size command](../cmd/view/decrease_font_size)
- [Run Macro with Temporary \
Options command](../cmd/macros/macro_run_options)
- [Save Macro command](../cmd/macros/macro_save)
- [Edit Macro command](../cmd/macros/macro_edit)
- [Select Macro command](../cmd/macros/macro_select)
- [Select This Macro command](../cmd/macros/macro_select_this)
- [Customize Macros command](../cmd/macros/customize_macro)
- [Macro Reference command](../cmd/macros/macro_help)
- [Find Macro Keyword command](../cmd/macros/macro_help_word)
- [Run Macro command](../cmd/macros/macro1)
- [Combine Windows command](../cmd/window/window_combine)
- [Find Next Unicode command](../cmd/search/find_next_unicode)
- [Find Previous Unicode command](../cmd/search/find_prev_unicode)
- [Erase Unicode Highlight command](../cmd/search/erase_unicode_hilite)

## Existing commands with new features

- [Insert Acute command](../cmd/insert/insert_acute)
- [Insert Tilde command](../cmd/insert/insert_tilde)

## New dialog boxes

- [Replace in Files dialog box](../dlg/replace_in_files/index)
- [Macro Temporary Options dialog \
box](../dlg/macro_temp_options/index)
- [Customize Macros dialog box \
dialog box](../dlg/macro_customize/index)

## Existing dialog boxes with new options

- [Search dialog box](../dlg/find/index)
- [Replace dialog box](../dlg/replace/index)
- [Find in Files dialog box](../dlg/find_in_files/index)
- [Customize dialog box](../dlg/customize/index)
- [Customize Tray Icon dialog box](../dlg/tray/index)

## Toolbar new buttons

- ![](../images/filesaveexit.gif)[Save and Close command](../cmd/file/file_save_exit)
- ![](../images/saveexitall.gif)[Save and Close All command](../cmd/file/save_exit_all)
- ![](../images/nextparen.gif)[Find Matching Parenthesis/Bracket command](../cmd/edit/next_paren)
- ![](../images/duplicateline.gif)[Duplicate Line command](../cmd/insert/duplicate_line)
- ![](../images/insertcontrol.gif)[Insert Special Character \
command](../cmd/insert/insert_control)
- ![](../images/marks.gif)[Marks command](../cmd/view/view_marks)
- ![](../images/editcomment.gif)[Comment command](../cmd/convert/edit_comment)
- ![](../images/edituncomment.gif)[Uncomment command](../cmd/convert/edit_uncomment)
- ![](../images/indent.gif)[Increase Line Indent command](../cmd/convert/indent)
- ![](../images/unindent.gif)[Decrease Line Indent command](../cmd/convert/unindent)
- ![](../images/macrosave.gif)[Save Macro command](../cmd/macros/macro_save)
- ![](../images/macroedit.gif)[Edit Macro command](../cmd/macros/macro_edit)
- ![](../images/macroselect.gif)[Select Macro command](../cmd/macros/macro_select)
- ![](../images/windowsplithorzfix.gif)[Toggle Horizontal Split](../cmd/window/window_split_horz_toggle)
- ![](../images/windowcombine.gif)[Combine Windows command](../cmd/window/window_combine)
- ![](../images/increasefontsize.gif)[Increase Font Size command](../cmd/view/increase_font_size)
- ![](../images/decreasefontsize.gif)[Decrease Font Size command](../cmd/view/decrease_font_size)
- ![](../images/replaceinfiles.gif)[Replace in Files command](../cmd/search/replace_in_files)
- ![](../images/bookmarkprevwithin.gif)[Previous Bookmark in This \
Window command](../cmd/bookmarks/bookmark_prev_within)
- ![](../images/bookmarknextwithin.gif)[Next Bookmark in This Window \
command](../cmd/bookmarks/bookmark_next_within)

## Other new features

- The [**Find** command](../cmd/search/edit_find) can search for newline characters if
**A Regular Expression "." Can Match Newline Characters** check box
in the [**Search** page](../dlg/customize/search/index)
is checked. The number of newline characters to be matched can be customized in the
**Additional Lines to**
**Search for Regular Expressions** text box.
- Added the **Replace >>** button
on the [**Find** dialog box](../dlg/find/index) to jump to the
[**Replace** dialog box](../dlg/replace/index).
- Added the **\>**
**button**
on all the search dialog boxes to browse available regular
expressions.
- Added the **Display File Names Only** check box
in the [**Find in Files** dialog box](../dlg/find_in_files/index).
- Added the **Change Font for Find/Replace Drop-Down List** check box
and the **Change Font only if Character Set of Selected Font is not System Default**
check box in the [**Search** \
page](../dlg/customize/search/index) of the [**Customize** dialog \
box](../dlg/customize/index), which allows you to select conditions when the font for the
**Find/Replace** drop-down list should be adjusted to the current font.
- Added a shortcut key to display the **Tray Icon** menu. By default,
it is ALT + CTRL + N,
and you can customize it in the **Shortcut Key to Simulate Left Mouse Button** text box
in the [**Customize Tray Icon** dialog box](../dlg/tray/index).
- Added a shortcut key to launch an EmEditor window with the contents of
the focused edit box. The original edit box will be filled with EmEditor contents when the EmEditor
window closes. By default, it is ALT + CTRL + X, and you can customize it in the
**Shortcut**
**Key to Grab Text with EmEditor** text box
in the [**Customize Tray Icon** dialog box](../dlg/tray/index).
- When saving a file, and the prompt message "This document contains
characters in Unicode format ...
Continue?" appears, pressing the **Cancel** button jumps to characters
that
cannot be converted to the encoding for saving, and also highlights the
Unicode characters.
- Added new switches /bk, /eh, /fu, /fn, /ko, /mf, /rc, /rd, /ri,  and /rw to the
[Command Line Options](../howto/file/file_commandline).
- Replacement expressions including lowercase/uppercase
and half-width/full-width conversions.
- Optimized for the Pentium 4 CPU (can also run on other CPUs).
- Features will be added to EmEditor Professional in the future.
