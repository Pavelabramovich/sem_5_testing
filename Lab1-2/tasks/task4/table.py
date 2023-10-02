from .hex_rgb_converters import rgb_to_hex
from main_decorator import main


def get_table():
    table_inner = ''

    for i in range(255, -1, -1):
        table_inner += f"""
        <tr style="background: {rgb_to_hex((i, i, i))};">
            <td>&nbsp;</td>
        </tr>
        """

    return f"""
    <table>
        {table_inner}
    </table>
    """


@main
def main():
    with open("data_file.txt", "w+") as file:
        file.write(get_table())
