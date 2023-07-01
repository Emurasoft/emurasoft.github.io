# Regex 對象

## 屬性

|     |     |
| --- | --- |
| [Engine](engine) | 設置會檢索規則運算式引擎類型。 |
| [Global](global) | 設置或檢索全域標幟。 |
| [IgnoreCase](ignore_case) | 設置或檢索是否規則運算式忽略大小寫。 |
| [OnlyWord](only_word) | 設置或檢索是否規則運算式僅符合整個單字。 |
| [Pattern](pattern) | 設置或檢索規則運算式模式。 |
| [SeparateCrLf](separate_cr_lf) | 設置或檢索規則運算式是否分開處理 CR 以及 LF。 |

## 方法

|     |     |
| --- | --- |
| [Find](find) | 用規則運算式搜尋指定的字串并返回一個 Match 對象如果發現符合。 |
| [Replace](replace) | 用規則運算式搜尋指定的字串，并用指定的字串取代。 |
| [Test](test) | 測試規則運算式是否與指定字串成功符合。 |

## 版本

支持 EmEditor Professional Version 15.9 或之後的版本。


```{toctree}
:maxdepth: 1
engine
find
fuzzy
global
ignore_case
only_word
pattern
replace
separate_cr_lf
test
```
