# Paste Method (Selection Object)

Inserts the Clipboard contents at the cursor.

#### \[JavaScript\]

document.selection. **Paste**( _nFlags_ );

#### \[VBScript\]

document.selection. **Paste** _nFlags_

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeCopyUnicode | Pastes as Unicode (default). |
| eeCopyQuotes | Pastes in quotes. |
| eeCopyNL | Pastes with newline characters. |
| eeCopySystemDefault | Pastes as the [system default encoding](../../glossary/index). |

## Version

Supported on EmEditor Professional Version 4.00 or later.
