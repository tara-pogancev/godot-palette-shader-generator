
# 🎨 Godot: Lospec Palette Generator
This is a generator for **[Godot 4 shaders](https://docs.godotengine.org/en/stable/tutorials/shaders/introduction_to_shaders.html)**. They limit the amount of color used in your render, by matching individual pixels to the nearest color from a predefined palette.

The palettes used are defined from **[Lospec](https://lospec.com/palette-list)** - database of palettes for pixel art.

This simple generator will help you easily achieve a *nostalgic, retro* look with your games.

The shader base is based on **TheBuffED's** great implementation, a tutorial on which you can find on **[YouTube](https://youtu.be/Scrdv4oSeNw)**. Please help show appreciation by supporting his channel and work! 😊

#### Requirements
This script runs using **Python**. It was built using version *3.11*.
For utilizing the shaders, I use **Godot 4**.

## ❓ How to use?
Firstly, you need to download a palette you'd like to use. I recommend using palettes with more colors, especially for 3D, as you need to make sure your game is still readable, even with less values.

Go to [Lospec](https://lospec.com/palette-list), and browse for a palette you like. After that, download the **"Paint(.)net TXT"** file, as this script has been adjusted to work with it. 

![lospec_options.png](assets%2Flospec_options.png)



## 🌞  Applying the shader
After importing the shader file to your Godot project, create a new 2D **ColorRect** node, and make sure it is atop other nodes. Set its size to cover the entire viewport, and apply a material with a newly defined shader. Thats all!

Depending on if your game is 2D or 3D, and how you handle camera movement, you might want to place your ColorRect on a CanvasLayer, to make sure it always covers the entirety of the screen.

In the *sample_data* and *export* folder, you will find some example palettes and their generated shaders respectively. Feel free to try them out!