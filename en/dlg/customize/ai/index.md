# AI Options page

The **AI Options** page allows you to customize settings related to AI.

## Enable AI check box

Enable writing assistance using [**OpenAI**](https://openai.com/) in EmEditor. You must also set the **AI assisted writing** check box in the [**General**](../../properties/general/index) page of each configuration's properties after enabling this option. The feature requires an [**OpenAI API key**](https://platform.openai.com/api-keys) to use.

## Use 'OPENAI_API_KEY' environment variable

If this is checked, the OpenAI API key will be saved using the 'OPENAI_API_KEY' environment variable. This is the recommended way of storing it by OpenAI and is shared with other apps. If this is not checked, the API key will be saved for use with EmEditor only.

## OpenAI API key text box

Specify the OpenAI API key. You can click the **o-o** on the right side of this text box to toggle the display/hide of characters. If you modify this text box and click the **OK** button on this dialog box, EmEditor will perform a connection test to the OpenAI API to check whether the entered API key is valid.

## Preferred model drop-down list box.

Specify the name of the model you want to use. You can either select an already defined model name from the list or directly enter an undefined model name. Depending on the model used, the AI's responses may differ, and OpenAI's usage fees may vary. If you specify an undefined model name and click the **OK** button in this dialog box, a connection test to the OpenAI API will be performed to check whether the entered model name is valid.

## Disable AI (per computer) button

Prohibits all AI related features in EmEditor, including the **AI assisted writing** feature, **AI** macro, and any other macros using the **fetch** function. This button requires an administrative privilege to proceed.

## Reset button

Resets to default settings.

