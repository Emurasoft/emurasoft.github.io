# Q. EmEditor で Excel ファイルを開くにはどうしたらいいでしょうか?

Excel ファイルはバイナリ ファイルであり、EmEditor で直接 Excel ファイルを開くことはできません。しかし、この目的を達成するためにはいくつかの方法があります。

1. Excel で Excel ファイルを開き、ファイルをテキスト ファイル (タブ区切り、またはカンマ区切り) として保存します。そして、EmEditor で開きます。
2. Excel アドイン [CSV Import+Export](https://appsource.microsoft.com/en-us/product/office/wa200000025) を使って Excel ファイルを CSV ファイルとしてエクスポートします。そして EmEditor で CSV ファイルを開きます。
3. Excel で Excel ファイルを開き、Ctrl+A ですべてのセルを選択して、Ctrl+C でコピーします。そして、EmEditor を起動し、\[CSV\] ツール バーから \[タブ区切り\] を選択してから、Ctrl+V で貼り付けます。