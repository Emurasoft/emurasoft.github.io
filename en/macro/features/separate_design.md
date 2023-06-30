# Modular Design of EmEditor Macro (Features)

EmEditor macros are modules designed independently of EmEditor executable and
are implemented as a Dynamic Link Library (DLL) file. To conserve system
resources, the DLL is loaded only during the macro execution.