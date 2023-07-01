# Q. 当我在宏中使用某种 JavaScript 方法时，会显示“对象不支持此属性或方法”的错误。为什么？

EmEditor 中没有当前 JavaScript/ECMAScript 中的许多新方法。EmEditor 宏使用 JScript 5.8（相当于 Internet Explorer 8.0），因此 EmEditor 宏不支持 JScript 5.8 之后引入的新方法。另一方面，替换表达式使用 Chakra（相当于 Microsoft Edge Legacy），并且最多支持到 ECMAScript 5.1，因此不支持 ECMAScript 5.1 之后引入的新方法。请检查您要使用的方法是否满足所需的版本。
