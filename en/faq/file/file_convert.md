# Q: How can I convert file encodings with the command line?

Use the following command line options:

/cp Encoding --- sets an encoding to open as.

/cps Encoding --- sets an encoding to save as.

/sa "DestFile" --- specifies a file name to save as after the encoding conversion

/ss+ --- saves the file with a Unicode signature (BOM) after the encoding conversion.

/ss- --- saves the file without a Unicode signature (BOM) after the encoding conversion.

For instance, if you want to convert a file from Western European (iso-8859-1) to UTF-8, use the following syntax:

emeditor.exe "windows1252.txt" /cp 1252 /cps 65001 /ss- /sa "utf8.txt"

See [Encoding Constants](../../macro/const/const_encoding) for the list of encodings.

See [Using Command Line Options](../../howto/file/file_commandline) for more information.