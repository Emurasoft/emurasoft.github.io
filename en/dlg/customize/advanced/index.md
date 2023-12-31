# Advanced page

The **Advanced** page allows you to customize advanced settings. You will need to restart EmEditor if you change these options.

## Do not share process between documents (disables tabs) check box

By default, all EmEditor windows will run in one single process, and no more than one process will run on a system whether or not tabs are displayed. It is recommended to leave this option unchecked so
that EmEditor minimizes the system's memory usage. However, an application error can cause all documents
to terminate, even though the EmEditor's error handler can try to save unsaved documents when an application error happens. By checking this option, each window will run in an independent process, and an application error on one document will not cause other documents to terminate. If this is
checked, tabs will be disabled and cannot be displayed.

## Enable Disk-Based check box

If this box is checked, EmEditor uses file-based operations for editing, and reduces the system's memory usage. If the Read Unmodified Lines from the Original File check box is also set, unmodified lines will be read from the original file, which increases the speed to open a file. If not, the file contents will be saved as a temporary file while opening a file, which reduces the file opening speed. Both cases reduce the system's memory usage.

## Minimum File Size to Enable Disk-Based text box

Uses a disk-based operations when the file size is larger than the size specified here and the Enable Disk-Based check box is checked. Specifying zero will always enable disk-based operations.

## Read Unmodified Lines from the Original File check box

If this box is checked, unmodified lines will be read from the original file, which increases the speed to open a file.

## Lock the Original File check box

If this box is checked, the original file is locked when the disk-based is enabled to open a file.

## Use temporary files while editing check box

If this box is checked, modified file contents will be saved to a temporary file while editing. While this action reduces the system's memory usage, it will slow down the running speed.

## Minimum File Size to Open Asynchronously text box

Opens a file asynchronously when the file size is larger than the size specified here. Specifying zero
will always open a file asynchronously.

## Use System Temporary Folder check box

Uses the system temporary folder rather than a user-specified folder (see below).

## Temporary Folder text box

Specifies the temporary folder if the system temporary folder is not used.

## Number of Threads text box

Specifies the number of threads used for some features in EmEditor to improve the speed. When Auto is selected, EmEditor uses the most appropriate number of the threads.

## Automatically manage all memory sizes check box

If this box is checked, EmEditor automatically calculates optimal memory sizes from the total physical memory size and the available virtual memory size.

## Memory Size text box

This number specifies the virtual memory size of one large
chunk of memory. EmEditor will try to allocate a small memory first, and then
gradually increase the memory size up to this specified size when opening a very
large file. When EmEditor needs more memory, it will allocate several of these chunks of memory. The number you can specify is between 16 and 31 in case of the 64-bit version of EmEditor, and between 16 and 26 in case of the 32-bit version of EmEditor. The
actual maximum number of lines in a chunk memory is:

|     |     |
| --- | --- |
| Value | Maximum number of lines in a chunk of memory |
| 16 | 2 ^ 16 (65,536) |
| 20 | 2 ^ 20 (1,048,576) |
| 24 | 2 ^ 24 (16,777,216) |
| 26 | 2 ^ 26 (67,108,864) |
| 30 | 2 ^ 30 (1,073,741,824) |

## Maximum Memory Size text box

Specifies the approximate size and percentage of physical memory that EmEditor can use in various operations. For instance, EmEditor will NOT try to save undo information if the system physical memory in use becomes greater than the number specified in this text box. However, this option does NOT guarantee that EmEditor will always conserve memory within the specified size.

## Maximum Memory Size per File text box

Specifies the maximum size of physical memory that can be used to open a file. It is recommended to specify a larger value if you open a single large file, and a smaller value if you open multiple files at the same time.

## Instruction Set drop-down list box

Specifies the instruction set used to run EmEditor for certain portions of the code. When Auto is selected, EmEditor will select the best instruction set for the current CPU.

## Reset button

Resets to default settings.

