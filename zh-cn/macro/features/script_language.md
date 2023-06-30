# 支持 JavaScript 或 VBScript (����)

EmEditor 把 JavaScript 或 VBScript 作为它的宏语言，所以对于熟悉 HTML 或 Windows 脚本编写的用户，编写宏并不困难。对于不熟悉这些脚本语言的用户，EmEditor 也能让你轻松地编辑宏。EmEditor 能录制键盘动作，并把它保存到一个能随时加载的宏文件中。通过 JavaScript 或 VBScript，你还能轻松地检查代码出错的部分。例如，在 JavaScript 中，你能用下列语句来排查错误:

try { ... } catch(e) { ... }

当存在一个错误，例如无法打开文件，try-catch 语句会允许脚本继续执行，而不是强制终止它。