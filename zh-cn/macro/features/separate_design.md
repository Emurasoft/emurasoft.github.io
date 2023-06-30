# EmEditor 中宏的模块化设计 (����)

EmEditor 中的宏是独立于EmEditor之外的模块，它是作为动态链结库 (DLL) 文件被执行的。为了维护系统资源，DLL 仅仅在宏执行期间被加载。