# バイト オーダー マーク (BOM)

バイト オーダー マーク (BOM) は、文字コードの値 FEFF を持ちます。これは、Unicode
でデータがどのようにエンコードされるかを示します。Unicode (Little endian) では、最初のバイトが FF、2 番目のバイトが FE
になります。Unicode big endian では、最初のバイトが FE、2 番目のバイトが FF になります。UTF-8 では、最初のバイトが EF、2
番目のバイトが BB、3 番目のバイトが BF になります。