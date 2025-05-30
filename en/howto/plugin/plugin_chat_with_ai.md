# To use Chat with AI plug-in

## Installation
**Chat with AI** is available as the **ChatAI** plug-in. You can download it from [ChatAI plug-in downloads](https://www.emeditor.com/download-chatai/). The **ChatAI** plug-in is not available for the Store App or the 32-bit version of EmEditor.

- If you use the **Desktop Installer** version of EmEditor, click **Installer** to download the installer version. Run the downloaded installer.
- If you use the **Portable** version of EmEditor, click **Zip archive** to download the zip file, then unzip the `ChatAI.dll` file to the `PlugIns` folder in your EmEditor folder. Navigate to [**Customize Plug-ins**](../../cmd/tools/customize_plug_ins) in EmEditor and **Add** the `ChatAI.dll` file.

## OpenAI API Key
You will need an OpenAI API key to use the ChatAI plug-in. If you don't have an OpenAI API key, follow these steps:
1. Log into your OpenAI account and visit the [API keys page](https://platform.openai.com/settings/organization/api-keys).
2. Click **Create a new secret key**. Optionally, add a name and select any project.
3. Select **All** permissions, or select **Restricted** and add the required permissions below. The required resources may change in the future as new features are added:
   - **Model capabilities**: **Write**
   - All other resources: **None**
4. Copy the generated API key. You will need it for the next step.

## Setup
1. After **ChatAI** is installed, the **AI** menu should appear in the main menu. Click the **AI** menu, select **Customize**, and then select **AI Options**. If the **AI** menu does not appear, you can also go to **Tools > Customize... > AI Options**.
2. Check the **Enable AI** box. A prompt will appear asking whether you agree to the terms. Click **Continue** if you agree.
3. Paste your API key into the **OpenAI API key** text box. Click **OK**.

## Launching Chat with AI
In EmEditor, select **Chat with AI** on the **AI** menu. If the **AI** menu does not appear, you can also access **Chat with AI** from the **Plug-ins** menu.

## Chat panel
- Type your question or prompt in the input box at the bottom and press Enter or click **&#8593;** to send.
- Your message appears on the right; the AI’s response will appear just below it shortly. Prompts and responses remain in the conversation for context-aware replies.
- Hover over any message to see buttons for:
  - **Copy to clipboard**: Copies the message to clipboard
  - **Edit message**: Make revisions to the message.
  - **Regenerate response**: Requests a new reply based on the same prompt. Useful if you would like a different phrasing.
- Right-click on any message for additional options:
  - **Copy**: Copies to clipboard
  - **Copy to Editor**: Inserts the text at the cursor position in the editor.
  - **Copy to New Document**: Opens a new document and inserts the text.
- Code blocks contain programming code. In a code block, you can click on **…** for options to copy the code.

## Sidebar
- Conversations are listed in the sidebar. Click on **+ New chat** to create a new chat that contains a different conversation. Responses in a chat will use the context of messages in that chat conversation only.
- Click on **&#8230;** on any entry for these options:
  - **Delete Chat**: Clears all messages in that chat.
  - **Copy to New Document**: Copies all messages in the conversation to a new document.
- Click on &#9881;&#65039; (Open menu) for app options.
  - **Debug Log Options**: The debug log helps diagnose technical issues with the app.
  - **Keyboard Shortcuts**: View keyboard shortcuts for Chat with AI
- You can hide the sidebar with the **Close sidebar** button.