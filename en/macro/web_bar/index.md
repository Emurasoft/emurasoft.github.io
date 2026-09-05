# WebBar Object

## Properties

|     |     |
| --- | --- |
| **[scrollX](scrollx)** | Returns the horizontal position of the scroll bar. |
| **[scrollY](scrolly)** | Returns the vertical position of the scroll bar. |
| **[Visible](visible)** | Shows or hides the Web Browser. |

## Methods

|     |     |
| --- | --- |
| **[Open](open)** | Opens a web site of the specified URL. |
| **[scrollBy](scrollby)** | Scrolls the window by the specified relative amount. |
| **[scrollTo](scrollto)** | Scrolls the window to the specified position. |
| **[SetFocus](set_focus)** | Sets the keyboard focus to the Web Browser. |

## Examples

### \[JavaScript\]

```
WebBar.Open( "https://www.emeditor.com/" );
WebBar.SetFocus();
```

### \[VBScript\]

```
WebBar.Open "https://www.emeditor.com/"
WebBar.SetFocus
```

## Version

Supported on EmEditor Professional Version 23.0 or later.


```{toctree}
:hidden:
:maxdepth: 1
scrollx
scrolly
visible
open
scrollby
scrollto
set_focus
```
