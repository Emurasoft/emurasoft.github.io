# Flags Property (FuzzyOptions Object)

Sets or retrieves flags.

The value must be zero or a combination of the following values.

|     |     |
| --- | --- |
| eeFuzzyIgnoreCombining | combining haracters, such as diacritics, dakuten, and handakuten, are ignored. |
| eeFuzzyIgnoreEmoji | emoji sequences are ignored. |
| eeFuzzyIgnoreKanaSize | the difference between small and large kana characters is ignored. |
| eeFuzzyIgnoreKanaType | the difference between Hiragana and Katakana characters is ignored. |
| eeFuzzyIgnoreVS | Variation Selectors are ignored. |
| eeFuzzyIgnoreWidth | the difference between half-width and full-width characters is ignored. The full-width form is a formatting distinction used in Chinese and Japanese scripts. |

#### \[JavaScript\]

_n_ = obj. **Flags**;

obj. **Flags** = _n_;

#### \[VBScript\]

_n_ = obj. **Flags**;

obj. **Flags** = _n_;

## Version

Supported on EmEditor Professional Version 22.0 or later.
