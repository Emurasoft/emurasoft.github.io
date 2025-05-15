# To use Chat with AI

## Installation
Chat with AI is available in the **ChatAI** plug-in. You can download it from [emeditor.com](https://www.emeditor.com/download-chatai/). We recommend using the installer for a simple setup. If you are using the portable version of EmEditor, download the zip archive, then  unzip the `ChatAI.dll` file to the `PlugIns` folder of your EmEditor folder. Navigate to [**Customize Plug-ins**](../../cmd/tools/customize_plug_ins) and **Add** the `ChatAI.dll` file.

## Setup
1. After **ChatAI** is installed, open EmEditor and go to **Tools > Customize... > AI Options**.
2. Log into your OpenAI account, and visit the [API keys page](https://platform.openai.com/settings/organization/api-keys).
3. Click **Create a new secret key**. Optionally add a name, and select any project.
4. Select **All** permissions, or select **Restricted** and add the required permission below. The required resources may change in the future as new features are added.
- **Model capabilities**: **Write**
- All other resources: **None**
5. Copy the generated API key and paste it into the **OpenAI API key** field in **AI Options**. Click **OK**.

## Launching Chat with AI
In EmEditor, go to **AI > Chat with AI**.

## Chat panel
- Type your question or prompt in the input box at the bottom and press Enter or click **↑** to send.
- Your message appears on the right; the AI’s response will appear just below it shortly. Prompts and responses remain in the conversation for context-aware replies.
- Hover over any message to see buttons for:
  - **Copy to clipboard**: Copies the message to clipboard
  - **Edit message**: Make revisions to the message.
  - **Regenerate response**: Requests a new reply based on the same prompt. Useful if you would like a different phrasing.
- Right-click on any message for additional options:
  - **Copy**: Copies to clipboard
  - **Copy to Editor**: Inserts the text at the caret position in the editor.
  - **Copy to New Document**: Opens a new document and inserts the text.
- Code blocks contain programming code. In a code block, you can click on **…** for options to copy the code.

## Sidebar
- Conversations are listed in the sidebar. Click on **+ New chat** to create a new chat that contains a different conversation. Responses in a chat will use the context of other messages in that chat conversation only.
- Click on *…* on any entry for these options:
  - **Delete Chat**: Clears all messages in that chat.
  - **Copy to New Document**: Copies all messages in the conversation to a new document.
- Click on ⚙️ (Open menu) for app options.
  - **Debug Log Options**: The debug log helps diagnose technical issues with the app.
  - **Keyboard Shortcuts**: View keyboard shortcuts for Chat with AI
- You can hide the sidebar with the **Close sidebar** button.