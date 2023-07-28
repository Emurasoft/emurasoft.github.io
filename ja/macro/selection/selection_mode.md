# Mode プロパティ (Selection オブジェクト)

選択の種類 (箱型選択、行選択など) を取得、または設定します。

## 

### \[JavaScript\]

```
nMode = document.selection.Mode;
document.selection.Mode = nMode;
```

### \[VBScript\]

```
nMode = document.selection.Mode
document.selection.Mode = nMode
```

## パラメータ

_nMode_

次の値の組み合わせになります。ただし、eeModeStream、eeModeLine、および eeModeBox
は一緒に組み合わせて使用することができません。eeModeKeyboard は、eeModeStream、eeModeLine、または eeModeBox と組み合わせて使用できます。プロパティを設定時、eeModeSelected は無視されます。

|     |     |
| --- | --- |
| eeModeStream | 線形選択です。 |
| eeModeLine | 行選択です。 |
| eeModeBox | 箱型選択です。 |
| eeModeMask | 選択状態を調べるためのマスクです。設定には使用できません。Mode プロパティの値を調べる場合は、このマスクとの And <br> を調べて、eeModeStream、eeModeLine、および eeModeBox と比較します。 |
| eeModeKeyboard | キーボードを使った選択状態を表します。この値は、他の値と組み合わせて使うことができます。 |
| eeModeSelected | 選択された状態です。プロパティの取得時のみ有効です。 |

## 例

### \[JavaScript\]

```
nMode = document.selection.Mode;
switch( nMode & eeModeMask ) {
case eeModeStream:
alert( "線形選択です。" );
break;
case eeModeLine:
alert( "行選択です。" );
break;
case eeModeBox:
alert( "箱型選択です。");
break;
}
if( nMode & eeModeKeyboard )  alert( "しかも、キーボード選択の状態です。" );
```

### \[VBScript\]

```
nMode = document.selection.Mode
Select Case nMode And eeModeMask
Case eeModeStream
alert "線形選択です。"
Case eeModeLine
alert "行選択です。"
Case eeModeBox
alert "箱型選択です。"
End Select
If nMode And eeModeKeyboard Then
alert "しかも、キーボード選択の状態です。"
End If
```

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。ただし、EmEditor Professional Version 5.00 から、eeModeSelected が追加され、テキストが選択されていない場合でも、選択状態を取得できるようになりました。
