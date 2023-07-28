# \#language 指示子 (スクリプト指示子)

スクリプト言語を指定します。この指定により、JavaScript、VBScript 以外の ActiveScript が利用できるようになります。この指示子は、スクリプトのメイン コードの上の最初の行に指定する必要があります。

#language = " _ScriptName_"

## パラメータ

_ScriptName_

使用するスクリプト言語を ProgID で指定します。あらかじめ、使用するスクリプト エンジンがシステムにインストールされている必要があります。

## 例

さまざまなスクリプト言語を使用して、現在のカーソル位置に "Hello!" という文字列を挿入します。

### \[JavaScript (JScript)\]

#language = "JScript"

document.write( "Hello!" );

## 

### \[JavaScript (V8)\]

#language = "V8"

document.write( "Hello!" );

## 

### \[PerlScript\]

#language = "PerlScript"

$Window->document->write( 'Hello!' );

## 

### \[PHPScript\]

#language = "PHPScript"

$Window->document->write( "Hello!" );

## 

### \[Python\]

#language = "Python"

Window.document.write( 'Hello' );

## 

### \[RubyScript\]

#language = "RubyScript"

Window.document.write( "Hello!" );

## 

### \[VBScript\]

```
```

#language = "VBScript"

document.write "Hello!";

他の ActiveScript の場合、レジストリエディタ (regedit.exe) で、{F0B7A1A2-9847-11CF-8F20-00805F2CD064} のキーを検索します。そして、その１つ上の階層のキーが、Implemented Categories になっていたら、さらにその上の階層のキーの既定の値が使いたいスクリプトの名前かどうかを調べます。目的のスクリプトだったら、その下の階層の ProgID のキーの既定の値を控えます。この値で ScriptName
パラメータを置き換えます。ただし、最後にピリオドと数字が付いていたら、その部分は、通常、省略することもできます。例えば、GlobalRubyScript.1 となっていたら GlobalRubyScript とだけ指定することができます。

## 注意

JavaScript、VBScript 以外の言語を使用する場合、ee で始まる定数は定義されないため、これらの定数を使用する場合は、整数の値で指定する必要があります。例えば、eeEncodingSystemDefault 定数の値を調べるには、JavaScript で

alert( eeEncodingSystemDefault );

を実行して調べることができます。ee で始まる定数の値は、将来のバージョンで変更になる可能性があります。

JavaScript、VBScript 以外の言語でマクロを自動的に記録することはできません。JavaScript、VBScript 以外の言語の使用方法は、サポートの対象外となります。

## バージョン

EmEditor Professional Version 6.00 以上で利用できます。
