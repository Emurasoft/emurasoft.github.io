# Q. 當我在巨集中使用某種 JavaScript 方法時，會顯示「物件不支援此屬性或方法」的錯誤。為什么？

EmEditor 中沒有目前的 JavaScript/ECMAScript 中的許多新方法。EmEditor 巨集使用 JScript 5.8（相當於 Internet Explorer 8.0），因此 EmEditor 巨集不支持 JScript 5.8 之後引入的新方法。另一方面，取代運算式使用 Chakra（相當於 Microsoft Edge Legacy），並且最多支持到 ECMAScript 5.1，因此不支持 ECMAScript 5.1 之後引入的新方法。請檢查您要使用的方法是否滿足所需的版本。
