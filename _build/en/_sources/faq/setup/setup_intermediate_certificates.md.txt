# Q. The digital signature of a program files could not be verified (when the Internet connection is unavailable).

If you run EmEditor on a PC where the Internet connection is unavailable, you might run into an issue such as:

- A warning dialog box "The digital signature of a program file could not be verified." appears when you try to launch EmEditor.
- The digital signature of EmEditor files (such as emeditor.exe and .msi installers) cannot be verified.
- EmEditor launch becomes slow.

In these cases, please connect to the Internet while you run EmEditor or verify the digital signature of program files. Once the Internet connection is made, you can continue to use EmEditor without the Internet connection.

If it is not possible to connect to the Internet, please install a Sectigo Code Signing Intermediate Certificate by following these steps:

1. From an Internet-connected PC, go to ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)
2. Download "Standard Sectigo RSA Cod Signing CA" in the "Code Signing" section.
3. Copy the downloaded file to the target offline PC where EmEditor files exist.
4. On the target PC, right-click this file, select "Install Certificate". "Certificate Import Wizard" appears.
5. Follow the wizard to select "Place all certificates in the following store", click Browse, and select "Intermediate Certification Authorities". Click Next to import the certificate.

Check the digital signature of an EmEditor file (such as emeditor.exe), and verify the digital signature is OK. If it is not OK because the root certificate cannot be verified, please install a Sectigo Root Certificate by following steps:

1. From an Internet-connected PC, go to ["How to Download & Install Sectigo Intermediate Certificates - RSA"](https://support.sectigo.com/articles/Knowledge/Sectigo-Intermediate-Certificates?retURL=%2Fapex%2FCom_KnowledgeWeb2Casepagesectigo&popup=false)
2. Download "SHA-2 Root: USERTrust RSA Certification Authority" in the "Root Certificates" section.
3. Copy the downloaded file to the target PC.
4. On the target PC, right-click this file, select "Install Certificate". "Certificate Import Wizard" appears.
5. Follow the wizard to select "Place all certificates in the following store", click Browse, and select "Trusted Root Certification Authorities". Click Next to import the certificate.

Alternatively, there was a report that [turning off Windows Automatic Root Certificates Update](https://admx.help/?Category=Windows_7_2008R2&Policy=Microsoft.Policies.InternetCommunicationManagement::CertMgr_DisableAutoRootUpdates&Language=en) by the Windows Group Policy resolved the issue.