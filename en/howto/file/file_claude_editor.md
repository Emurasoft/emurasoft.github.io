# Using EmEditor as the editor for Claude Code

When you press Ctrl+G in Claude Code's [interactive mode](https://code.claude.com/docs/en/interactive-mode),  it opens Notepad so you can edit your prompt text. You can change the editor that opens on Ctrl+G to EmEditor by following the steps below.

1. Exit Claude Code.
2. Make sure EmEditor is in your `PATH`. If you used the desktop installer, this should already be set up. If you use the portable version, set `PATH` as follows:
   1. Open the Windows Start menu, search for **environment variables**, and select **Edit environment variables for your account**.
   2. In **System Properties**, click the **Environment Variables** button. 
   3. In the **User variables** section, select the **Path** entry and click **Edit**.
   4. Click **New** and paste the path to your EmEditor installation folder.
   5. Click **OK** on each open window to save.
   6. Close and reopen your terminal so the new `PATH` takes effect.
3. Open the file `%USERPROFILE%\.claude\settings.json` in EmEditor.
4. Add the `VISUAL` variable to the `env` section:

```json
{
  "env": {
    "VISUAL": "emeditor /sp"
  }
}
```

   - If the `"env"` section already exists, add the line `"VISUAL": "emeditor /sp"` inside, ensuring the previous line ends with a comma.
   - If there is no `"env"` section, add the entire block shown above. If the file already contains other settings, add `"env"` alongside them, separated by a comma.
   - Save the file.
5. Run Claude Code. When you press Ctrl+G, EmEditor should open. Typing text into the open document and close EmEditor. The text you typed will appear in the Claude Code input box.

## Troubleshooting

- **EmEditor does not open when you press Ctrl+G in Claude Code** Open Terminal and run `emeditor`. If EmEditor starts, `PATH` is set correctly. If EmEditor does not start, see step 2.
- **EmEditor does not open on Ctrl+G and `PATH` is correct.** Change the value of `VISUAL` to the full path of `emeditor.exe`. In JSON, backslashes must be escaped by doubling them. For example:

```json
{
  "env": {
    "VISUAL": "C:\\path_to\\EmEditor\\EmEditor.exe /sp"
  }
}
```