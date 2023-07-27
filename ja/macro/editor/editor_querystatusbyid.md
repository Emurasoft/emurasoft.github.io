# QueryStatusByID メソッド ()

EmEditor のコマンドが実行できるかどうか、またチェックされているかどうかを取得します。

## 

### \[JavaScript\]

```
nStatus = editor.QueryStatusByID( nID );
```

### \[VBScript\]

```
nStatus = editor.QueryStatusByID( nID )
```

## パラメータ

_nID_

実行したいコマンドを整数の ID で指定します。利用できるコマンドの一覧は、 [コマンド \
リファレンス](../../cmd/index) を参照してください。すべてのコマンドが利用できないことがあります。その場合、QueryStatusByID の利用はサポートの対象外になることがあります。

## 戻り値

次の組み合わせになります。

|     |     |
| --- | --- |
| eeStatusEnabled | コマンドが有効です。 |
| eeStatusLatched | コマンドがチェックされた状態になっています。 |

## バージョン

EmEditor Professional Version 4.00 以上で利用できます。
