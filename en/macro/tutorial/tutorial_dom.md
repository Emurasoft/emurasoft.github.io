# Specifications of Macro (Document Object Model) (Tutorial)

In the specifications of the EmEditor macro Document Object Model (DOM), **[Window Object](../window/index)**
is the current scope. In other words, properties and methods without explicit scope refer
to the current **[Window Object](../window/index)**.
For example, the first _document_ is the **[document Property](../window/window_document)** of the Window
Object,
which applies to scripts used for web browsers. For those who are familiar with web browser scripting,
the following code might look more familiar:

## 

### \[JavaScript\]

```
document.write("EmEditor supports macros.");
```

### \[VBScript\]

```
document.write "EmEditor supports macros."
```
Either of the above examples produces the same result; the behaviors of[Text Property](../selection/selection_text) and that of[write Method](../document/document_write) are identical.
You can use multiple objects in EmEditor macros. We designed the macros this way to achieve Object-Oriented Programming
(OOP)
as well as to allow extensibility and to accommodate future enhancements of the macros,
such as manipulating multiple windows and documents in a single macro.
You can use the following objects in EmEditor macros:
-[Window Object](../window/index) \-
becomes the default scope, and thus, there is no need to specify object names.
It provides methods and properties of Windows user interfaces. The[document \
Property](../window/windowdocument) allows you to use properties and methods of[Document Object](../document/index)
for the current document. Also, the[editor \
Property](../window/windoweditor) allows you to access[Editor Object](../editor/index).
-[Document Object](../document/index) \-
provides methods and properties for opened documents,
which applies to elements of the overall document and includes details about a file, such as the file name of the document,
the setup name, and the read-only status. Furthermore, the[selection \
Property](../document/documentselection) allows you to use[Selection \
Object](../selection/index) for the current Selection Range and cursor location.
-[Selection Object](../selection/index) \-
provides methods and properties for the current Selection Range and cursor location.
It provides many methods and properties, such as Selection Change in Selection Range,
character conversion, cursor movement, search, and replace.
-[Editor Object](../editor/index) \- EmEditor
provides methods and properties for overall EmEditor application. For example,
it provides the path and version of EmEditor executables, and methods and properties used in opening new or
specified files.
