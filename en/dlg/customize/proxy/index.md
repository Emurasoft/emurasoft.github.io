# Proxy page

The **Proxy** page allows you to customize settings related to the proxy connection. EmEditor will use the proxy settings on this page to connect to `support.emeditor.org` via HTTP and HTTPS, and if using AI features, it will use the proxy settings to connect to `api.openai.com`.

## No proxy radio button

Connect to the internet without specifying proxy settings. Use this setting if you do not use a proxy or you have configured [proxy settings in Windows settings](https://support.microsoft.com/en-us/windows/use-a-proxy-server-in-windows-03096c53-0554-4ffe-b6ab-8b1deee8dae1#ID0EFD=Windows_11).

## Manual proxy configuration radio button

Check to enable the custom proxy settings below.

### Protocol drop-down list box

Select between HTTP or SOCKS5 protocol to connect to your proxy.

### Host name

Specify the host name or IP address for your proxy.

### Port number

Specify the port number for your proxy.

### Proxy authentication

Enable this option if your proxy requires a username and password to connect.

### Username

Specify the username to use to connect.

### Password

Specify the password to use to connect. You can click on o-o to show or hide the password. The username and password will be stored on your computer.

### Proxy URL

This field displays the URL that encodes all settings specified above. You can click on o-o to show or hide the URL. EmEditor will use this URL to connect to the proxy. 

## Check connection button

Click this button to test the connection to `support.emeditor.org` using the settings specified above. If the connection is successful, "✓ Connection successful!" will appear to the left of this button.

If unsuccessful, an error message will appear to diagnosing the issue. Double check the proxy settings and ensure that the proxy is accessible.

## Reset button

Resets to default settings.
