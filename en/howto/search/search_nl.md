# To Specify Newline Characters

The following tables show how to specify newline characters.

## Find Dialog box, Replace dialog box - Find, Replace with

|     |     |
| --- | --- |
| Use Regular Expressions is on | \\n or \\r\\n (same meaning) |
| Use Regular Expressions is off (Use Escape Sequence) | \\n or \\r\\n (same meaning) |

## Find in Files dialog box, Replace in Files dialog box - Find

|     |     |
| --- | --- |
| Use Regular Expressions is on | \\r\\n, \\r, or \\n (depends on actual newline character) |
| Use Regular Expressions is off (Use Escape Sequence) | \\n or \\r\\n (same meaning) |

## Replace in Files dialog box - Replace with

|     |     |     |
| --- | --- | --- |
|  | Keep Modified Files Open is on | Keep Modified Files Open is off |
| Use Regular Expressions is on | \\r\\n, \\r, or \\n (depends on actual newline character) | \\r\\n, \\r, or \\n (depends on actual newline character) |
| Use Regular Expressions is off (Use Escape Sequence) | \\n or \\r\\n (same meaning) | \\r\\n, \\r, or \\n (depends on actual newline character) |

## Tips

- In case of "\\n or \\r\\n (same meaning)", you cannot search newline characters by
distinguishing CR+LF, CR only, and LF only.
- In case of "\\r\\n, \\r, or \\n (depends on actual newline character)", you
need to specify "\\r\\n" if the actual newline character is CR+LF, "\\r" if CR only, or
"\\n" if LF only. Usually CR+LF (\\r\\n) is used on Windows Operating Systems,
CR (\\r) is used on Macintosh, and LF (\\n) is used on Unix.