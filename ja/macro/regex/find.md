# Find メソッド ()

指定する文字列から正規表現を検索し、見つかったら [Matches コレクション](../matches/index) を返します。Global プロパティが設定されている場合、このメソッドは同じパラメータを使用して繰り返すことにより、複数のマッチを取得することができます。

## 

### \[JavaScript\]

```
match  = reg.Find( strText );
```

### \[VBScript\]

```
match  = reg.Find( strText )
```

## パラメータ

_strText_

正規表現が検索される文字列を指定します。

## 戻り値

指定した文字列が正規表現を含んでいる場合 [Matches コレクション](../matches/index) を返します。一致が見つからない場合は null を返します。

## 例

### \[JavaScript\]

```
re = editor.regex;
re.Engine = eeExFindRegexOnigmo;
re.Pattern = "[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\\.[A-Z]{2,}";
re.IgnoreCase = true;
re.OnlyWord = false;
matches = re.Find( "The email address is john@test.com." );
if( matches ) {
match = matches.Item(0);
alert( "Found: FirstIndex = " + match.FirstIndex + " , Length = " + match.Length + ", Value = " + match.Value );
}
```

### \[VBScript\]

```
Set re = editor.regex
re.Engine = eeExFindRegexOnigmo
re.Pattern = "[A-Z0-9.\%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}"
re.IgnoreCase = True
re.OnlyWord = False
Set matches = re.Find( "The email address is john@test.com." )
If Not IsNull( matches ) Then
Set match = matches.Item(0)
alert( "Found: FirstIndex = " & match.FirstIndex & " , Length = " & match.Length & ", Value = " & match.Value )
End If
```

## バージョン

EmEditor Professional Version 15.9 以上で利用できます。
