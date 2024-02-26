# 特長

EmEditor Professional では、JavaScript または VBScript を用いた高機能マクロが利用できます。EmEditor マクロには、次のような特長があります。

```{toctree}
:maxdepth: 1
can_script_all
keystroke_mouse
macro_ide
script_language
separate_design
windows_scripting_host
```

## 注意

最近の JavaScript/ECMAScript の新しいメソッドを利用するには、V8 エンジンを有効にします。V8 エンジンを有効にするには、[マクロのカスタマイズ] ダイアログ ボックスの [\[オプション\] ページ](../../dlg/macro_customize/options)にある [JavaScript エンジンとして V8 を使用する] チェック ボックスを設定するか、あるいはマクロの先頭に [#language](../directive/language) = "V8" を挿入します。

V8 を選択しないと、EmEditor マクロは JScript 5.8 (Internet Explorer 8.0 に相当) を使用しているため、JScript 5.8 より後に追加された新しいメソッドは利用できません。新しいメソッドを使用する前に、必須バージョンの要件を満たしているか確認してください。