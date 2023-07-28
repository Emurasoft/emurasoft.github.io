# More Support for Very Large Files

EmEditor can now open files containing very long lines (longer than 4GB). When EmEditor loads a file containing a very long line, it will split the long line into several lines, but it will recombine them when saving the file.

Pasting very large text via the Clipboard became more stable by dynamically creating a temporary file. The various **Sort** commands and the **[Delete Duplicate Lines](../cmd/edit/delete_duplicate)** command were also optimized for large files, and there is no longer a limitation of size to run these commands.

The new version also allows you to combine or split very large files easily. The new **[Split Current Document into Several Files](../cmd/tools/split_to_files)** command allows you to split the current document into several files either every user-specified number of lines, or before every bookmarked line. It also allows you to specify a header and/or footer to each separated file. The new **[Combine Documents into a Single File](../cmd/tools/combine_files)** command allows you to combine multiple documents into one file.
