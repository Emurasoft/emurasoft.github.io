# Text Rendering page

The **Text Rendering** page customizes how text is rendered in the editor view. Changes are applied instantly, so that they can be previewed in the editor.

## Use DirectWrite check box

If this is checked, DirectWrite is used for drawing text in the editor view. If this is unchecked, GDI is used for drawing text. DirectWrite is a GPU-accelerated DirectX API which improves the rendering and readability of text compared to GDI. DirectWrite is not applied for printing, print preview, or the minimap.

## Auto-Detect Settings check box

Detects optimal settings for the monitor. This option may set
separate settings for different monitors. The DirectWrite options below are ignored if Auto-Detect Settings is on.

## Anti-Aliasing Mode drop-down list box

Sets the anti-aliasing mode for text display. **ClearType** is an anti-aliasing method that adds sub-pixel detail to text. **Grayscale** is a more simple antialiasing method. Selecting **None** will turn off anti-aliasing.

## Rendering Mode drop-down list box

Sets the rendering mode for text display. Different rendering modes add subtle changes to text appearance due to how anti-aliasing is rendered. By selecting **Default**, the rendering mode is automatically selected. If anti-aliasing mode is "None", rendering mode is ignored. ClearType and the rendering mode "Outline" cannot be used simultaneously. See ["DWRITE\_RENDERING\_MODE (Windows 8 and later) enumeration" on MSDN](https://docs.microsoft.com/en-us/windows/win32/api/dwrite/ne-dwrite-dwrite_rendering_mode) for detailed information on each rendering mode.

## Gamma slider

Gamma value used for gamma correction.

## Contrast slider

Adjusts edge sharpness. 0.0 is the lowest degree of contrast, and 3.0 is the highest degree of contrast.

## ClearType Level slider

The ratio of ClearType antialiasing. A value of 0.0 means no ClearType is applied, and 1.0 means ClearType has full effect.

## Use Color Fonts check box

Draws color using embedded color information in fonts. Available to Windows 8.1 and later platforms.

## Use Double Buffering check box

Uses double buffering to draw text on screen. Double buffering reduces flicker, but makes drawing slower. If a slower computer is used and if drawing
is slow, please clear this check box. This checkbox is disabled if DirectWrite is used.

## Fallback Fonts list box

Defines fallback fonts that can be used for characters that are not supported in the current font. The current display font is specified in the [**Customize Font** dialog box](../../properties/font/index). The top-most font in the Fallback Fonts list has the highest priority in selecting a fallback font. Right-clicking on the list will show additional commands, and drag and dropping an item will change ordering.

## Display Hangul Jamo Composed check box

If this is checked, EmEditor displays a correct series of Hangul Jamo as composed characters. For example, "ᄒ ᅡ ᆫ ᄀ ᅳ ᆯ" (without spaces) will be displayed as "한글". This option is also effective to display old Hangul correctly where composed characters are unavailable.

## Add button

Adds a new item to the list.

## Delete button

Deletes the selection from the list.

## Reset button

Resets all Text Rendering options to their default settings.

