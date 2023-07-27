# \#language 指示詞 (Script ���ܵ�)

指定要使用的指示詞碼語言。通過指定這個，您就可以使用 JavaScript 和 VBScript 之外的 ActiveScript 語言。這個指示詞必須在主代碼上方的指示詞碼中的第一行上被指定。

#language = "ScriptName"

## 參數

_ScriptName_

通過 ProgID 指定指示詞碼語言。這個指示詞碼引擎必須在指示詞碼被使用前安裝。

## 示例

用不同的指示詞碼語言，插入 "Hello!" 到游標位置處。

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

如果您想要用上述語言之外的另一種語言，請運行注冊表編輯器 (regedit.exe) 并搜尋鍵值 {F0B7A1A2-9847-11CF-8F20-00805F2CD064}。如果被搜尋的鍵在您想要的指示詞碼語言下，您就能找到那個語言的 ProgID。

## 備注

如果 JavaScript 和 VBScript 之外的指示詞碼語言被使用，巨集的常數則 (以 "ee" 開始) 不會被定義。要使用這些常數，您必須把這些常數指定為整數值。您能檢查這些值，例如，用 JavaScript 運行下面的一行:

alert( eeEncodingSystemDefault );

這些常數值可能以后會被更改。

如果用 JavaScript 和 VBScript 之外的指示詞碼語言的話，巨集就不能被自動錄制。我們也無法提供有關如何編寫 JavaScript 和 VBScript 之外的指示詞碼語言的方法。

## 版本

支持 EmEditor 6.00 或之後的版本。
