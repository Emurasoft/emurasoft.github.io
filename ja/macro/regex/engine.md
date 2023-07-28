# Engine プロパティ (Regex オブジェクト)

正規表現エンジンの種類を設定または取得します。

この値は、以下のいずれかになります。

|     |     |
| --- | --- |
| 0 | 既定の正規表現エンジンを使用します。 |
| eeExFindRegexBoost | Boost.Regex を正規表現エンジンとして使用します。 |
| eeExFindRegexOnigmo | Onigmo を正規表現エンジンとして使用します。 |

## 

### \[JavaScript\]

```
n = reg.Engine;
reg.Engine = n;
```

### \[VBScript\]

```
n = reg.Engine;
reg.Engine = n;
```

## バージョン

EmEditor Professional Version 15.9 以上で利用できます。
