# Item Property (DisplayList Collection)

Retrieves the [DisplayItem object](../display_item/index) for the specified index.

#### \[JavaScript\]

_item_ =
list. **Item**( _Index_ );

#### \[VBScript\]

_item_ =
list. **Item**( _Index_ )

## Parameters

_Index_

Specifies the index of the item as a one-based integer.

If the object is a color list, it should be one of the following values.

|     |     |
| --- | --- |
| eeColorNormal | General |
| eeColorSelection | Selection |
| eeColorCurrentLine | Current Line |
| eeColorQuote | Quoted Line |
| eeColorURL | URLs |
| eeColorMailTo | Mail addresses |
| eeColorTag | Tags including Find in Files hyperlinks |
| eeColorSingleQuotes | String enclosed by single quotation marks '...' |
| eeColorDoubleQuotes | String enclosed by double quotation marks "..." |
| eeColorComment | Comments |
| eeColorScript | Script |
| eeColorBraces | Matched parentheses/brackets |
| eeColorInsideTag | HTML/XML Tags |
| eeColorHighlight1 | Highlight (1) |
| eeColorHighlight2 | Highlight (2) |
| eeColorHighlight3 | Highlight (3) |
| eeColorHighlight4 | Highlight (4) |
| eeColorHighlight5 | Highlight (5) |
| eeColorHighlight6 | Highlight (6) |
| eeColorHighlight7 | Highlight (7) |
| eeColorHighlight8 | Highlight (8) |
| eeColorHighlight9 | Highlight (9) |
| eeColorHighlight10 | Highlight (10) |
| eeColorReturn | Newline Characters, tabs, EOF |
| eeColorCursorLine | Horizontal/vertical lines |
| eeColorPageBreak | Page break marks/Narrowing |
| eeColorLineNumbers | Line numbers (digits) |
| eeColorRuler | Ruler/Column header (digits) |
| eeColorOutside | Outside of regions |
| eeColorCompareChange | Compare - Changed lines |
| eeColorCompareChar | Compare - Changed characters |
| eeColorCompareAdded | Compare - Added |
| eeColorCompareDeleted | Compare - Deleted |
| eeColorCompareBlank | Compare - Blank |
| eeColorSpell | Incorrect spelling |
| eeColorUnicode | Unicode characters |
| eeColorVerticalSel | Vertical selection frame |
| eeColorHexSel | Hexadecimal view selection frame |
| eeColorIndentGuides | Indent guides |
| eeColorHorzGrid | Horizontal grid |
| eeColorOutline | Outline |
| eeColorLineNumberLines | Line Numbers (lines) |
| eeColorRulerLines | Ruler/Column header (lines) |
| eeColorVerticalSeparator | Vertical Separator |
| eeColorHtmlCharRef | HTML Character Reference |
| eeColorUcn | Universal Character Names/Percent-encoding |
| eeColorAutoMarker | Auto Marker |
| eeColorMarker1 | Marker (1) |
| eeColorMarker2 | Marker (2) |
| eeColorMarker3 | Marker (3) |
| eeColorMarker4 | Marker (4) |
| eeColorMarker5 | Marker (5) |
| eeColorMarker6 | Marker (6) |
| eeColorMarker7 | Marker (7) |
| eeColorMarker8 | Marker (8) |
| eeColorMarker9 | Marker (9) |
| eeColorMarker10 | Marker (10) |
| eeColorMatchingTag | Matching Tag |
| eeColorBookmark | Bookmarked Lines |
| eeColorUserDefinedGuides | User-Defined Guides |
| eeColorIndicatorModified | Vertical Indicator - Changed Lines |
| eeColorIndicatorSaved | Vertical Indicator - Saved Lines |
| eeColorIndicatorBookmark | Vertical Indicator - Bookmarks |
| eeColorMarkerModified | Scroll Bar Marker - Changed Lines |
| eeColorMarkerSaved | Scroll Bar Marker - Saved Lines |
| eeColorMarkerBookmark | Scroll Bar Marker - Bookmarks |
| eeColorMarkerFound | Scroll Bar Marker - Found |
| eeColorMarkerCursor | Scroll Bar Marker - Cursor Position |
| eeColorMarkerCompareChange | Scroll Bar Marker - Compare Changed |
| eeColorMarkerCompareAdded | Scroll Bar Marker - Compare Added |
| eeColorMarkerCompareDeleted | Scroll Bar Marker - Compare Deleted |
| eeColorHeadings | Headings |
| eeColorSearchSel | Search Range |
| eeColorFilter | Filter |
| eeColorLinkUrlVisited | URLs (visited) |
| eeColorLinkIdVisited | Mail addresses (visited) |
| eeColorLinkTagVisited | Find in Files hyperlinks (visited) |
| eeColorCellText | CSV cell selected text |
| eeColorCellBorder | CSV cell selection frame |
| eeColorFilterSeparator | Filter separator |
| eeColorMinimapBackground | Minimap background |
| eeColorMinimapView | Minimap view |
| eeColorLinkIpv4 | IPv4 addresses |
| eeColorLinkIpv4Visited | IPv4 addresses (visited) |
| eeColorLinkIpv6 | IPv6 addresses |
| eeColorLinkIpv6Visited | IPv6 addresses (visited) |
| eeColorHexColor | Hexadecimal colors - #ff0080 |
| eeColorRgbColor | RGB colors - rgb(255,0,128) |
| eeColorLineNumberHovered | Line numbers (hovered) |
| eeColorRulerHovered | Ruler/Column header (hovered) |
| eeColorLineNumberSel | Line numbers (line selected) |
| eeColorRulerSel | Ruler/Column header (column selected) |
| eeColorLineNumberCurr | Line numbers (selected) |
| eeColorRulerCurr | Ruler/Column header (selected) |
| eeColorOpenFilter | Open Filter |
| eeColorMultiSelection | Lines with Multiple Selections |
| eeColorValidatorError | Syntax Check Errors |
| eeColorValidatorWarning | Syntax Check Warnings |
| eeColorValidatorMessage | Syntax Check Messages |
| eeColorEvenLines | Even Lines |
| eeColorInvalidCharacters | Warning Characters |

If the object is a search list, it specifies a number of times the search has been made.

## Version

Supported on EmEditor Professional Version 7.00 or later.