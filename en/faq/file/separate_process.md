# Q. EmEditor is specified as an external text editor from another application. Why doesn't the change made by EmEditor reflect the application?

If EmEditor is specified as an external text editor from another application such as a mail client program, and if the application monitors the EmEditor process for its termination and the file change, the application might not reflect an edited and saved file with EmEditor. To work around this, specify the [/sp option](../../howto/file/file_commandline) to instruct EmEditor to be launched as a separate process. In this case, however, each EmEditor window will be displayed as a
separate group.
