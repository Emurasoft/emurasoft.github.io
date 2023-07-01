# Compare Method (Editor Object)

Compares two open documents.

#### \[JavaScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] );

#### \[VBScript\]

_n_ = editor. **Compare**( _nFlags_, _strDocument1_, _strDocument2_\[, _strResultFileName_\] )

## Parameters

_nFlags_

You can specify a combination of the following values.

|     |     |
| --- | --- |
| eeCompareGenerateReport | Generates a report file. A file path must be specified in strResultFileName. |
| eeCompareOpenReport | Opens the report file. eeCompareGenerateReport must also be specified. |
| eeCompareQuality1 | Fastest method that that searches nearby lines. |
| eeCompareQuality2 | Faster method. |
| eeCompareQuality3 | Medium speed. |
| eeCompareQuality4 | More precise method. |
| eeCompareQuality5 | Most precise method that searches the entire file (up to a certain limit). |
| eeCompareQuick | Quickly compares, and will not highlight differences. This flag cannot be combined with other options except eeCompareQuiet. |
| eeCompareQuiet | Does not display any output messages. |
| eeCompareReport3Col | Outputs report in a 3 column format. |
| eeCompareReportDiffOnly | Reports non-identical lines only. |
| eeCompareReset | Resets comparison or synchronized scrolling mode and clears comparison results. |
| eeCompareResetAfter | Resets comparison or synchronized scrolling mode and clears comparison results after comparison and report generation. eeCompareGenerateReport must also be specified. |
| eeCompareRestorePos | Restores window positions when finished. |
| eeCompareSplitVert | Splits the window vertically to display documents. |
| eeCompareSwitchNoWrap | Switches to no wrap. |
| eeCompareSyncCaret | Synchronizes cursor positions. |
| eeCompareSyncScrollHorz | Synchronizes horizontal scrolling. |
| eeCompareSyncScrollOnly | Show compared documents without highlighting differences. |
| eeCompareSyncScrollVert | Synchronizes vertical scrolling. |
| eeCompareTileHorz | Tiles documents horizontally. |
| eeCompareTileVert | Tiles documents vertically. |
| eeIgnoreCases | Ignores case. |
| eeIgnoreComments | Ignores text marked as a comment by the configuration. |
| eeIgnoreEmbeddedSpaces | Ignores spaces within the first and last non-whitespace characters within a line. |
| eeIgnoreEncodings | Ignores encoding difference. |
| eeIgnoreLeadSpaces | Ignores spaces before the first non-whitespace character within a line. |
| eeIgnoreNewlines | Ignores differences in newline characters. |
| eeIgnoreTrailingSpaces | Ignores spaces after the last non-whitespace characters within a line. |

_strDocument1_

Specifies the string to identify the first document. This value can be a file name, file name with the full path, or a colon (:) followed by the index of the document in the current group. For
example, "filename.csv", "C:\\data\\filename.csv" (in case of JavaScript, "C:\\\data\\\filename.csv"), or ":2". If both strDocument1 and strDocument2 are empty strings, EmEditor chooses most recently used documents.

_strDocument2_

Specifies the string to identify the second document. The format of this value is the same as strDocument1.

_strResultFileName_

If this parameter is specified and eeCompareGenerateReport is specified, EmEditor saves a comparison report to this path, including the name.

## Return Values

The return value is one of the following values.

|     |     |
| --- | --- |
| eeDiff | Two documents are NOT identical. |
| eeMatched | Two documents are identical. |
| eeMatchedIgnored | Two documents are identical except for ignored places. |

## Version

Supported on EmEditor Professional Version 17.7 or later.
