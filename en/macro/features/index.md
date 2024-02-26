# Features

EmEditor Professional allows you to create functionally-rich macros using JavaScript or VBScript.
Features of the macros include:

```{toctree}
:maxdepth: 1
can_script_all
keystroke_mouse
macro_ide
script_language
separate_design
windows_scripting_host
```

## Notes

To utilize many of the new methods in modern JavaScript/ECMAScript, please opt for the V8 engine. To activate V8, set the **Use V8 as JavaScript engine** checkbox found on the [**Options** page](../../dlg/macro_customize/options) in **Customize Macros** dialog box, or insert **[#language](../directive/language) = "V8"** at the start of your macro.

Without selecting V8, EmEditor macros will run on JScript 5.8, which corresponds to Internet Explorer 8.0, meaning that methods introduced after JScript 5.8 will not be supported in EmEditor macros. Ensure the methods you intend to use are compatible with the version requirements.