# Flags 屬性

設定或檢索旗標。

該值必須為零或以下值的組合。

|     |     |
| --- | --- |
| eeFuzzyIgnoreCombining | 忽略組合字元，例如讀音符號、dakuten（日文中的濁點）和 handakuten（日文中的半濁點）。 |
| eeFuzzyIgnoreEmoji | 忽略表情符號（emoji）序列。 |
| eeFuzzyIgnoreKanaSize | 忽略大假名和小假名之間的區別。 |
| eeFuzzyIgnoreKanaType | 忽略平假名與片假名字元之間的區別。 |
| eeFuzzyIgnoreVS | 忽略 Variation Selector。 |
| eeFuzzyIgnoreWidth | 忽略忽略半形和全形字元的區別。全形形式是中文和日文腳本中使用的獨特格式。 |

#### \[JavaScript\]

_n_ = obj. **Flags**;

obj. **Flags** = _n_;

#### \[VBScript\]

_n_ = obj. **Flags**;

obj. **Flags** = _n_;

## 版本

支持 EmEditor Professional Version 22.0 或之後的版本。