# Character Check page

The **Character Check** page allows you to set properties related to character check.

### Check before savings check box

If this is checked, EmEditor checks if the document contains specified warning characters immediately before being saved.

### Warn invisible characters check box

Click this check box to warn invisible characters. An invisible character is any of the following:

`
SOFT HYPHEN (0x00ad), ARABIC LETTER MARK (0x061c), MONGOLIAN VOWEL SEPARATOR (0x180e), ZERO WIDTH SPACE (0x200b), ZERO WIDTH NON-JOINER (0x200c), ZERO WIDTH JOINER (0x200d), LEFT-TO-RIGHT MARK (0x200e), RIGHT-TO-LEFT MARK (0x200f), LEFT-TO-RIGHT EMBEDDING (0x202a), RIGHT-TO-LEFT EMBEDDING (0x202b), POP DIRECTIONAL FORMATTING (0x202c), LEFT-TO-RIGHT OVERRIDE (0x202d), RIGHT-TO-LEFT OVERRIDE (0x202e), WORD JOINER (0x2060), FUNCTION APPLICATION (0x2061), INVISIBLE TIMES (0x2062), INVISIBLE SEPARATOR (0x2063), INVISIBLE PLUS (0x2064), LEFT-TO-RIGHT ISOLATE (0x2066), RIGHT-TO-LEFT ISOLATE (0x2067), FIRST STRONG ISOLATE (0x2068), POP DIRECTIONAL ISOLATE (0x2069), INHIBIT SYMMETRIC SWAPPING (0x206a), ACTIVATE SYMMETRIC SWAPPING (0x206b), INHIBIT ARABIC FORM SHAPING (0x206c), ACTIVATE ARABIC FORM SHAPING (0x206d), NATIONAL DIGIT SHAPES (0x206e), NOMINAL DIGIT SHAPES (0x206f), ZERO WIDTH NO-BREAK SPACE (0xfeff), INTERLINEAR ANNOTATION ANCHOR (0xfff9), INTERLINEAR ANNOTATION SEPARATOR (0xfffa), INTERLINEAR ANNOTATION TERMINATOR (0xfffb), OBJECT REPLACEMENT CHARACTER (0xfffc)
`

### Warn control characters check box

Click this check box to warn control characters. A control character has a code point of either (1) less than or equal to `0x1f`, but is not carriage return, line feed, or tab, or (2) in the range `[0x7f, 0x9f]`.

### Warn surrogate characters check box

Click this check box to warn surrogate characters.

### Warn characters in specified ranges check box

Click this check box to warn characters in specified ranges.

### Warn characters outside of specified ranges check box

Click this check box to warn characters outside of specified ranges.

### Add button

[**Character Range** dialog box](char_range/index) will be displayed and will allow you to add specified range to the list.

### Delete button

Removes the selected range from the list.

### Character ranges list box

Lists the user-defined character ranges. Double-clicking on an item in the list will allow you to edit the selected range.

### Reset button

Resets to default settings. The
[**Reset** dialog box](../reset/index) will be displayed
and will allow you to copy from another configuration.

You can also move to the following dialog box from this page.

(Select **Add**
button)


```{toctree}
:maxdepth: 1
char_range/index
```
