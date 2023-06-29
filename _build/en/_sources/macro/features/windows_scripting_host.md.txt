# Windows Scripting Host

EmEditor macros are based on the Windows Scripting Host (WSH) engine, so you
can use various Windows Component Object Model (COM) objects. For
example, you can perform regular expression searches using the RegExp object,
manipulate files using the FileSystemObject object, create a short-cut,
manipulate the Windows Registry using the WshShell object, or work with
networking functions using the WshNetwork object. Additionally, you can create
and execute a macro that utilizes an external application that supports
Automation (such as Word and Excel) to copy a document created in
EmEditor, then paste into, and print it from the external application.