# \#language directive (Script Directives)

Specifies the scripting language to use. By specifying this, ActiveScript languages other than JavaScript and VBScript can be used. This directive must be specified at the first lines of the script above the main code.

#language = "ScriptName"

## Parameters

_ScriptName_

> Specifies the scripting language by its ProgID. The script engine must be installed before the script can be used.

## Examples

Inserts "Hello!" at the cursor position by using various script languages.

#### \[JavaScript (JScript)\]

#language = "JScript"

document.write( "Hello!" );

#### \[JavaScript (V8)\]

#language = "V8"

document.write( "Hello!" );

#### \[PerlScript\]

#language = "PerlScript"

$Window->document->write( 'Hello!' );

#### \[PHPScript\]

#language = "PHPScript"

$Window->document->write( "Hello!" );

#### \[Python\]

#language = "Python"

Window.document.write( 'Hello' );

#### \[RubyScript\]

#language = "RubyScript"

Window.document.write( "Hello!" );

#### \[VBScript\]

#language = "VBScript"

document.write "Hello!";

If you wish to use another language not listed above, run Registry Editor (regedit.exe) and search for the key {F0B7A1A2-9847-11CF-8F20-00805F2CD064}. If the searched key is under the desired script language, you can find the
ProgID for that language.

## Notes

If a scripting language other than JavaScript or VBScript is used, Macro constants (beginning with "ee") will not be defined. To use these constants, you must specify these constants as integer values. These values can be inspected, for instance,
by running the following line with JavaScript:

alert( eeEncodingSystemDefault );

These constant values might be changed in the future.

Macros cannot be recorded automatically with any scripting language except JavaScript and VBScript. How to write scripting languages other than JavaScript or VBScript is not supported.

## Version

Supported on EmEditor Professional Version 6.00 or later.
