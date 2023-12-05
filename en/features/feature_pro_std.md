---
orphan: true
---
# New features for both EmEditor Professional and EmEditor Standard

## New commands

- [Always on Top - On command](../cmd/window/window_always_top_on)
- [Always on Top - Off command](../cmd/window/window_always_top_off)

## Existing dialog boxes with new options

- [Customize dialog box](../dlg/customize/index)
- The
[File page](../dlg/properties/file/index) on
[Configuration Properties](../dlg/properties/index)

## Other new features

- You can cancel during the [**Find in** **Files** command](../cmd/search/grep).
- You can use multi-byte characters using regular expressions for the
[**Find in Files** command](../cmd/search/grep).
- Searching using a regular expression has become faster.
- Optimized how EmEditor searches other windows, and launching EmEditor has
become faster.
- Added a **Help** button to each
dialog box.
- Enhanced the Help with more details including **[Command Reference](../cmd/index)**
and **[Frequently Asked Questions](../faq/index)**.
- In Windows 2000/XP/2003, not only the core and some dialog boxes, but all
dialog boxes support Unicode.
- Added the /? switch to the **[Command Line Options](../howto/file/file_commandline)**.
- By default, an inserted string can be undone with only one
[**Undo** command](../cmd/edit/edit_undo). This behavior can be
restored to the previous behavior by clearing the
**Undo Character by Character (need to restart EmEditor)** check box
on the [**Advanced** page](../dlg/customize/advanced/index) of
the [**Customize** dialog box](../dlg/customize/index).
- Eliminated the Read Me file (emeditor.txt) and incorporated all the
information into help.
- Added the new plug-in messages [EE\_SET\_SEL\_TYPE](../plugin/message/ee_set_sel_type), [EE\_GET\_STATUSA](../plugin/message/ee_get_statusa),
[EE\_GET\_STATUSW](../plugin/message/ee_get_statusw),
[EE\_INSERT\_FILEA](../plugin/message/ee_insert_filea),
[EE\_INSERT\_FILEW](../plugin/message/ee_insert_filew),
[EE\_GET\_ANCHOR\_POS](../plugin/message/ee_get_anchor_pos),
[EE\_SET\_ANCHOR\_POS](../plugin/message/ee_set_anchor_pos), and
expanded the existing messages
[EE\_INSERT\_STRINGA](../plugin/message/ee_insert_stringa),
[EE\_INSERT\_STRINGW](../plugin/message/ee_insert_stringw),
[EE\_GET\_VERSION](../plugin/message/ee_get_version),
[EE\_INFO](../plugin/message/ee_info),
[EE\_SET\_CARET\_POS](../plugin/message/ee_set_caret_pos)
with new functions.
- **Prompt**, **Auto-Reload**, or **Keep Locked** options in the
**Changed**
**by Another Program** drop-down list box allows the read-only status of
EmEditor changed when the read-only attribute of the file is changed.
