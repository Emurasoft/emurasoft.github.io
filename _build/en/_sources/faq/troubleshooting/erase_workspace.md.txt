# Q. When I try to launch EmEditor, it is trying to load very large files. Can you disable this?

EmEditor is trying to load the last used workspace. In the Command Prompt, run:

emeditor.exe /clw

and the last used workspace will be erased, and an untitled EmEditor window will be launched.