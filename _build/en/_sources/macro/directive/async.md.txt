# \#async directive

Specifies whether the macro should be run asynchronously (as a separate thread). This directive must be specified at the first lines of the script above the main code.

#async = "off" (or "on")

## Parameters

"off" (or "on")

> The macro will be not run asynchronously if "off" is specified, otherwise it will be run asynchronously. The default depends on the way a macro is run. If a macro is run at a specified event, the default is off. If a macro specified by the Snippets plug-in, the macro is always run synchronously. Otherwise, the default is specified in the [**Options** page](../../dlg/macro_customize/options/index) of the **Customize Macros** dialog box.

## Examples

Do not run the macro asynchronously.

#async = "off"

## Version

Supported on EmEditor Professional Version 20.8.