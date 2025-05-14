# To use Chat with AI

## How to install
Chat with AI is included in the **ChatAI** plug-in. You can download the plug-in from [emeditor.com](https://www.emeditor.com/download-chatai/). We recommend using the installer for easy installation. If you have a portable version of EmEditor, download the zip archive and unzip the `ChatAI.dll` file to the `PlugIns` folder of your EmEditor folder. Go to [**Customize Plug-ins**](../../cmd/tools/customize_plug_ins) and **Add** the `ChatAI.dll` file.

## Setup
1. After **ChatAI** is installed, open EmEditor and open **Tools > Customize... > AI Options**.
2. Log into OpenAI, and go to the [API keys page](https://platform.openai.com/settings/organization/api-keys).
3. Click on **Create a new secret key**. Optionally add a name, and select any project.
4. Select **All** permissions, or select **Restricted** and add the required permission below. The required resources may change in the future as new features are added.
- **Model capabilities**: **Write**
- All other resources: **None**
5. Copy the API key to the **OpenAI API key** field in **AI Options**. Click **OK**.