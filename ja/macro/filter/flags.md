# Flags プロパティ (Filter �I�u�W�F�N�g)

次の値を組み合わせて指定します。

|     |     |
| --- | --- |
| eeFindLogicalOr | 複数レベルのフィルターの場合、以前のレベルに論理和 (論理 OR) でフィルターを実行します。 |
| eeFindNegative | フィルター ツール バーを表示して指定する文字列に一致する行を除外します。 |
| eeFindReplaceCase | 大文字と小文字を区別して検索します。 |
| eeFindReplaceEscSeq | 文字列をエスケープ シーケンスで指定します。eeFindReplaceRegExp と組み合わせて指定できません。 |
| eeFindReplaceOnlyWord | 単語のみを検索します。 |
| eeFindReplaceRegExp | 文字列を正規表現で指定します。eeFindReplaceEscSeq と組み合わせて指定できません。 |

## 

### \[JavaScript\]

```
flag = item.Flags;
item.Flags = flags;
```

### \[VBScript\]

```
n = item.Flags
item.Flags = n
```

## バージョン

EmEditor Professional Version 16.0 以上で利用できます。
