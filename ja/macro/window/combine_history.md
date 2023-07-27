# CombineHistory プロパティ ()

元に戻す/やり直しの履歴を組み合わせるかどうかを指定します。

## 

### \[JavaScript\]

```
b =CombineHistory;
CombineHistory = b;
```

### \[VBScript\]

```
b =CombineHistory
CombineHistory = b;
```

## 例

### \[JavaScript\]

```
CombineHistory = true;
document.writeln( "ABC" );
document.writeln( "DEF" );
CombineHistory = false;
```

### \[VBScript\]

```
CombineHistory = True
document.writeln "ABC"
document.writeln "DEF"
CombineHistory = False
```

## バージョン

EmEditor Professional Version 15.5 以上で利用できます。
