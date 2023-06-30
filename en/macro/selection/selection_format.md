# Format Method (Selection Object)

Inserts or deletes newline characters in the selection.

#### \[JavaScript\]

document.selection. **Format**( _nFlags_ );

#### \[VBScript\]

document.selection. **Format** _nFlags_

## Parameters

_nFlags_

Specifies a combination of the following values:

|     |     |
| --- | --- |
| eeFormatInsertNL | Inserts newline characters at wrapped positions in the selection. |
| eeFormatDeleteNL | Removes newline characters at wrapped positions in the selection. |
| eeFormatSplitLines | Splits lines by inserting newline characters and removing trailing spaces (EmEditor Professional Version 4.10 or later). |
| eeFormatJoinLines | Joins lines by removing newline characters and inserting spaces at the end of each line (EmEditor Professional Version 4.10 or later). |

## Version

Supported on EmEditor Professional Version 4.00 or later.