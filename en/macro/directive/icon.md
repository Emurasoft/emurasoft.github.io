# \#icon directive (Script Directives)

Specifies the icon to use the toolbar button. This directive must be specified at the first lines of the script above the main code.

#icon = " _filename_", _index_

## Parameters

_filename_

> Specifies the file extracting icon with the relative paths from the current macro file or the complete paths. If the paths are omitted, specify the title of the file in which the current macro file exists.

_index_

> If multiple icons exist in the specified file, specify the index that you use. 0 would be selected if the specifying was omitted.

## Examples

Use the icon of calculator (calc.exe)

#icon = "C:\\WINDOWS\\system32\\calc.exe",0

## Version

Supported on EmEditor Professional Version 7.00 or later.
