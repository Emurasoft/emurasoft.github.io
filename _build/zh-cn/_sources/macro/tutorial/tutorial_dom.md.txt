# 宏的规格（文档对象模型）

在 EmEditor 宏文档对象模型 (DOM) 的规格中，In the specifications of the EmEditor macro Document 对象 Model (DOM), **[Window 对象](../window/index)** 是当前的范围。换句话说，没有明确的范围的属性和方法指的都是当前的 **[Window 对象](../window/index)**。
例如，第一个 _document_ 是 Window 对象的 **[document 属性](../window/window_document)**，适用于网页浏览器的脚本。对于熟悉网页浏览器脚本的用户，下面的代码可能会比较眼熟:

#### \[JavaScript\]

document.write("EmEditor supports macros.");

#### \[VBScript\]

document.write "EmEditor supports macros."

上面任一脚本都会产生同样的结果； **[Text 属性](../selection/selection_text)** 以及 **[write 方法](../document/document_write)** 的行为是一致的。

在 EmEditor 宏中，你能用多个对象。我们这样设计宏是为了达到面向对象的编程 (OOP) 以及允许程序的扩展性并能适应增强的宏，例如在一个宏中操纵多个窗口和文档。

你能在 EmEditor 宏中用下列的对象:

- **[Window 对象](../window/index)** \-

变为默认范围，这样，不需要指定对象名称。它会提供 Windows 用户界面的方法与属性。比如， [**document**\
**属性**](../window/window_document) 让你能把 **[Document 对象](../document/index)** 的属性与方法用于当前文档。同样， **[editor \**
**属性](../window/window_editor)** 让你能访问 **[Editor 对象](../editor/index)**。

- **[Document 对象](../document/index)** \-
为打开的文档提供方法和属性，应用于整个文档中的所有元素，包括文件中的细节部分，例如文档的文件名，安装名，还有只读状态。而且， **[selection \**
**属性](../document/document_selection)** 让你能把 **[Selection \**
**对象](../selection/index)** 用于当前选区范围 (Selection Range) 以及光标位置。

- **[Selection 对象](../selection/index)** \-
为当前选区范围 (Selection Range) 以及光标位置提供方法和属性。它提供许多方法和属性。例如在选区范围内的选取变更 (Selection Change)，字符转换，光标移动，搜索以及替换。

- **[Editor 对象](../editor/index)** \- EmEditor
EmEditor 为整个应用程序所提供的方法和属性。例如，它提供 EmEditor 可执行的文件的路径和版本，以及用于打开新或指定文件的方法和属性。

## 下一主题: