# Matches Collection

Matches collection provides a collection of [Match objects](../match/index) for regular expression search results. The collection consists of the first item as the whole matched item (backreference 0), and submatches (backreferences 1, 2, 3, ...).

## Properties

|     |     |
| --- | --- |
| **[Count](count)** | Retrieves the number of Match objects. |
| **[Item](item)** | Retrieves the Match object for the specified index. Item(0) returns the whole matched item (backreference 0), Item(1) returns backreference 1. |

## Version

Supported on EmEditor Professional Version 15.9 or later.

```{toctree}
:hidden:
:maxdepth: 1
count
item
```