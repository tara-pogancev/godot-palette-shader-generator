import os
from PIL import ImageColor

def read_file_contents(file_path: str) -> str:
    """Reads the contents of a file given its relative or absolute path."""
    try:
        abs_path = os.path.abspath(file_path)

        with open(abs_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def get_hex_lines():
    """Reads a file and extracts lines that start with 'FF'."""
    hex_lines = [line.strip() for line in file_content.split("\n") if line.strip().startswith("FF")]
    return hex_lines

def get_rgb_colors():
    colors = []
    for color in hex_colors:
        rgb_value = ImageColor.getcolor(f"#{color[2:]}", "RGB")
        colors.append(rgb_value)

    return colors


def get_color_array():
    colors_count = len(rgb_colors)

    # Convert each RGB tuple to a vec4 format for GDShader
    color_array_str = f"const vec4 colors[{colors_count}] = {{"
    color_array_str += ", ".join([f"vec4({r / 255.0}, {g / 255.0}, {b / 255.0}, 1.0)" for r, g, b in rgb_colors])
    color_array_str += "};"

    return color_array_str


def get_shader_content(color_array):
    return f"""
shader_type canvas_item;

uniform sampler2D SCREEN_TEXTURE: hint_screen_texture, filter_linear_mipmap;

{color_array}

void fragment() {{
    float min_diff = -1.0;
    vec4 min_color = vec4(0.0, 0.0, 0.0, 1.0);

    vec2 uv = SCREEN_UV;

    vec4 temp = textureLod(SCREEN_TEXTURE, uv, 0.0);

    min_diff = 1000.0;
    for (int i = 0; i < colors.length(); i++) {{
        float curr_dist = distance(colors[i], temp);
        if (curr_dist < min_diff) {{
            min_diff = curr_dist;
            min_color = colors[i];
        }}
    }}

    COLOR.rgb = min_color.rgb;
}}
"""

def save_shader_file(content):
    palette_name = file_content.split("\n")[2].split(": ")[1]
    palette_name = palette_name.replace(" ", "_")
    palette_name = palette_name.replace("-", "_")
    palette_name = palette_name.lower()

    export_folder = 'export'

    # Create the export folder if it doesn't exist
    os.makedirs(export_folder, exist_ok=True)

    new_file_path = os.path.join(export_folder, f"{palette_name}_palette_shader.gdshader")

    with open(new_file_path, 'w', encoding='utf-8') as shader_file:
        shader_file.write(content)

    print(f"Shader file saved as: {new_file_path}")

if __name__ == '__main__':
    file_content = read_file_contents("sample_data/zenit-241.txt")
    hex_colors = get_hex_lines()
    rgb_colors = get_rgb_colors()

    color_array = get_color_array()
    shader_content = get_shader_content(color_array)

    save_shader_file(shader_content)

