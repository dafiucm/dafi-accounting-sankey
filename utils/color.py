def hex_to_rgb(hex_str: str) -> tuple:
    return tuple(int(hex_str.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))


def hex_to_rgba(hex_str: str, alpha: float) -> tuple:
    return hex_to_rgb(hex_str) + (alpha,)


def rgba_to_string(rgba: tuple) -> str:
    return f"rgba{rgba}"
