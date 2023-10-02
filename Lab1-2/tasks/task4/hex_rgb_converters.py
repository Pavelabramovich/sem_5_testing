rgb = list[int, int, int] | tuple[int, int, int]


def rgb_to_hex(rgb_color: rgb) -> str:
    if len(rgb_color) == 3 and all([0 <= component <= 255 for component in rgb_color]):
        r, g, b = rgb_color
        rgb_color = f'#{r:02X}{g:02X}{b:02X}'
        return rgb_color
    else:
        raise ValueError(f"Incorrect color format: {rgb_color}")


def hex_to_rgb(hex_color: str) -> rgb:
    if hex_color.startswith('#'):
        hex_color = hex_color[1:]
    else:
        raise ValueError(f"Incorrect color format: {hex_color}")

    if len(hex_color) != 6:
        raise ValueError(f"Incorrect color format: {hex_color}")

    try:
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError as error:
        raise ValueError(f"Incorrect color format: {hex_color}") from error
