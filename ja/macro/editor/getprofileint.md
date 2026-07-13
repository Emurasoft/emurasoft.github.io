# GetProfileInt メソッド (Editor オブジェクト)

EmEditor の設定に応じて、レジストリまたは INI ファイルから、指定する整数値を取得します。

## 

### \[JavaScript\]

```
n = editor.GetProfileInt( nKey, strConfig, strEntry, nDefault );
```

### \[VBScript\]

```
n = editor.GetProfileInt( nKey, strConfig, strEntry, nDefault )
```

## パラメータ

_nKey_

以下の値のいずれかを指定して、キーを指定します。eeRegConfig および eeRegEmEditorPlugin には pszConfig パラメータが必要です。

|     |     |
| --- | --- |
| eeRegCommon | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Common または eeCommon.ini\\\[Common\] |
| eeRegRegist | HKEY\_CURRENT\_USER\\Software\\EmSoft\\Regist または eeCommon.ini\\\[Regist\] |
| eeRegLMCommon | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\EmEditor v3\\Common または eeLM.ini\\\[Common\] |
| eeRegLMRegist | HKEY\_LOCAL\_MACHINE\\SOFTWARE\\EmSoft\\Regist または eeLM.ini\\\[Regist\] |
| eeRegConfig | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditor v3\\Config\\(pszConfig) または eeConfig.ini\\\[(pszConfig)\] |
| eeRegEmEditorPlugins | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorPlugIns\\(pszConfig) または eePlugins.ini\\\[(pszConfig)\] |
| eeRegEmEditorUsers | HKEY\_CURRENT\_USER\\Software\\EmSoft\\EmEditorUsers\\(pszConfig) または eeUsers.ini\\\[(pszConfig)\] |

_strConfig_

eeRegConfig、eeRegEmEditorPlugin または eeRegEmEditorUsers が選択されたとき、キーを指定するための追加の文字列を指定します。

_strEntry_

取得する値の名前を指定します。

_nDefault_

値が見つからない場合や取得できない場合に備えて既定値を指定します。

## 例

この例は、64 ビット整数を取得する方法を説明します。

### \[JavaScript\]

```
nHigh = 0;
nLow = 0;
s = editor.GetProfileString( eeRegCommon, "", "FindFlag", "0" );
if( s.length == 18 && s.substr( 0, 2 ) == "0x" ) {
nHigh = parseInt( s.substr( 2, 8 ), 16 );
nLow = parseInt( s.substr( 10, 8 ), 16 );
}
```

## バージョン

EmEditor Professional Version 8.00 以上で利用できます。
