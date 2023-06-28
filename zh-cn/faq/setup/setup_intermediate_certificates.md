# Q. 无法验证程序文件的数字签名（当 Internet 连接不可用时）。

如果在没有网络连接的 PC 上运行 EmEditor，可能会遇到以下问题：

- 当尝试启动 EmEditor 时出现一个警告对话框“无法验证程序文件的数字签名”。
- 无法验证 EmEditor 文件（例如 emeditor.exe 和 .msi 安装程序）的数字签名。
- EmEditor 的启动速度变慢。

在这种情况下，请在运行 EmEditor 或验证程序文件的数字签名时连接网络。 建立网络连接后，无需连接网络就可以继续使用 EmEditor。

如果无法连接到网络，请按照以下步骤安装 Sectigo Code Signing Intermediate Certificate（Sectigo 代码签名中间证书）：

1. 从连接互联网的 PC 上，转到 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)。
2. 到 "Code Signing" 部分下载 "Standard Sectigo RSA Cod Signing CA"。
3. 将下载的文件复制到存在 EmEditor 文件的目标离线 PC。
4. 在目标 PC 上，右键单击该文件，选择 "Install Certificate" （安装证书）。会出现 "Certificate Import Wizard" （证书导入向导）。
5. 按照向导选择 "Place all certificates in the following store" （将所有证书放入以下存储区）, 单击 "Browse"（浏览），然后选择 "Intermediate Certification Authorities"（中间证书颁发机构）。单击“下一步”导入证书。

查看 EmEditor 文件（例如 emeditor.exe）的数字签名，然后确认数字签名没问题就可以了。如果由于无法验证根证书让数字签名不 OK，请按照以下步骤安装 Sectigo 根证书：

1. 从连接互联网的 PC 转到 ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)。
2. 到 "Root Certificates" 部分中下载 "SHA-2 Root: USERTrust RSA Certification Authority"。
3. 将下载的文件复制到目标 PC。
4. 在目标 PC 上，右键单击该文件，然后选择 "Install Certificate" （安装证书）。会出现 "Certificate Import Wizard" （证书导入向导）。
5. 按照向导选择 "Place all certificates in the following store" （将所有证书放入以下存储区）, 单击 "Browse"（浏览），然后选择 "Intermediate Certification Authorities"（中间证书颁发机构）。单击“下一步”导入证书。