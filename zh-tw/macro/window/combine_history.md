# CombineHistory 屬性 (Window ��H)

指定要不要合併復原/重做記錄。

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

## 範例

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

## 版本

支持 EmEditor Professional 15.5 或之後的版本。
