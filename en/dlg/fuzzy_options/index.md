# Fuzzy Matching Options dialog box

This dialog box appears when the
**...** button is clicked in the **Find**, **Replace**, **Find in Files**, **Replace in Files**, **Advanced Filter**, or **Join CSV** dialog box.

## Similarity slider

Specifies the similarity in percentage. For instance, if you specify 75%, and if the search string is 4 characters long, 3 out of 4 characters must be equal in order to match. You may set this 100% if any of the following options is set. For instance, if you only want to ignore diacritics, you should set this 100% and set the **Ignore nonspacing combining characters, such as diacritics, dakuten, and handakuten** check box.

## Max edit distance

<!-- cspell:disable-next-line -->
Specifies the max [edit distance](https://en.wikipedia.org/wiki/Edit_distance) that a matched string can have. `fuzzx maching` and `fuzzy matching` are 2 edit distance apart.

## Ignore nonspacing combining characters, such as diacritics, dakuten, and handakuten check box

If this is checked, nonspacing combining characters, such as diacritics, dakuten, and handakuten, are ignored. For instance, é (U+00E9) and e (U+0065) will not be differentiated.

## Do not differentiate between a half-width and a full-width characters check box

If this is checked, the difference between half-width and full-width characters is ignored. For instance, A (U+0041) and Ａ (U+FF21) will not be differentiated.

## Do not differentiate between Hiragana and Katakana characters check box

If this is checked, corresponding Hiragana and Katakana characters compare as equal. For instance, あ (U+3042) and ア (U+30A2) will not be differentiated.

## Do not differentiate between small and large kana characters check box

If this is checked, corresponding small and large kana characters compare as equal. For instance, あ (U+3042) and ぁ (U+3041) will not be differentiated.

## Ignore Unicode Variation Selector characters check box

If this is checked, Unicode Variation Selector characters are ignored. For instance, 辻 (U+8FBB) and 辻󠄀 (U+8FBB U+E0100) will not be differentiated.

## Ignore Emoji sequences check box

If this is checked, Emoji sequences are ignored except the first code value of the sequences. For instance, 👨‍🦰 (red hair man, U+1F468 U+200D U+1F9B0) and 👨‍🦳 (white hair man, U+1F468 U+200D U+1F9B3) will not be differentiated.

## Add button

[**String/Character Range** dialog box](str_char_range/index) will be displayed and will allow you to add a string or character range to the list.

## Delete button

Removes the selected range from the list.

## String/Character ranges list box

Lists the user-defined strings and character ranges. Double-clicking on an item in the list will allow you to edit the selected string or character range.


```{toctree}
:maxdepth: 1
str_char_range/index
```
