# Save Details dialog box

This dialog box appears when theSaving button
on the [File page](../index) of Configuration Properties is selected.

## Prompt when Saving Unicode as ANSI check box

When saving a file as an encoding other than Unicode, Unicode big endian, or
UTF-8, prompts if the document contains Unicode characters which cannot be
converted to the specified encoding.

## Save Unicode as HTML/XML Character Reference check box

If this box is checked, any Unicode character that cannot be converted to the
destination code page will be encoded as a numeric entity code such as &#10070;.

## Use Named Entity Reference check box

If this box is checked, any Unicode character that cannot be converted to the
destination code page will be encoded as the named entity code such as &copy;.
This option is available only when Internet Explorer 5.0 or later is installed.

## Save Tabs as Spaces check box

Convert tabs to spaces when saving documents.

## Insert Returns when Saving check box

Insert returns at wrap points when saving documents.

## Delete Empty Files when Saving check box

Delete the file if the document is empty.

## Always Enable Saving check box

Enable the [Save command](../../../../cmd/file/file_save) even
if the document is not modified.

## Delete Spaces at End of Lines check box

Delete spaces at end of lines when saving documents. Even if this option is enabled, extra spaces at the cursor line will not be affected when a file is being saved. However, they will be deleted when a file is being saved and closed at the same time.

## Except for Line at Cursor check box

## Automatically Name Untitled Document check box

If this is checked, when an untitled document is being saved, the first line of the document will be used to name the file.

## Prompt before Deleting an Old File when Renaming check box

If this is checked, EmEditor will display a dialogue box to prompt user before deleting the old file when renaming.

## Encoding drop-down list box

Select an encoding method when saving the file.

## Add a Unicode Signature (BOM) check box

When saving the file as Unicode, Unicode big endian or UTF-8, add the Byte
Order Mark (BOM) signature to the file.

## Newline Character drop-down list box

Specify how to save returns.No Change will not change the return
styles.CR+LF (Windows) will change all returns to CR plus LF pairs.CR only (Macintosh) will change all returns to CRs.LF only (Unix)
will change returns to LFs. Generally, Windows uses CR+LF for all returns.
Macintosh uses CRs only, and Unix uses LFs only.

## Reset button

Resets to default settings. The
[Reset dialog box](../../reset/index) will be displayed
and will allow you to copy from another configuration.

