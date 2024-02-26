# GetEnv メソッド (Shell オブジェクト)

環境変数を取得します。

## 

### \[JavaScript\]

```
str = shell.GetEnv( strName );
```

### \[VBScript\]

```
str = shell.GetEnv( strName )
```

## パラメータ

_strName_

環境変数の名前。

## 例

### \[JavaScript\]

```
str = shell.GetEnv( "OPENAI_API_KEY" );
```

### \[VBScript\]

```
str = shell.GetEnv( "OPENAI_API_KEY" )
```

## 戻り値

指定する環境変数の中身を返します。

## バージョン

EmEditor Professional Version 24.0 以上で利用できます。
