# Get the Name of a Computer User (Tutorial)

To get the name of a computer user, use the UserName Property of WshNetwork Object.

The following example demonstrates how to get the name of a current computer user:

#### \[JavaScript (JScript)\]

WshNetwork = new ActiveXObject( "WScript.Network" );

alert( "User Name = " + WshNetwork.UserName );

#### \[VBScript\]

Set WshNetwork = CreateObject( "WScript.Network" )

alert "User Name = " & WshNetwork.UserName

## References

)