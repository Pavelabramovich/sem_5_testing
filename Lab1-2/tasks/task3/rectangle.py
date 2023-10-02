import argparse
from math import isinf, isnan
from main_decorator import main


@main
def main():
    parser = argparse.ArgumentParser(description='Calculating rectangle square')
    parser.add_argument('width', type=float, help='Input width')
    parser.add_argument('height', type=float, help='Input height')

    try:
        args = parser.parse_args()
    except (SystemExit, ValueError, argparse.ArgumentError) as error:
        raise ValueError("You need enter only 2 positive finite float arguments: width and height.") from error
    else:
        width = args.width
        height = args.height

        if (
            isnan(width) or isinf(width) or
            isnan(height) or isinf(height) or
            width <= 0 or height <= 0
        ):
            raise ValueError("You need enter only 2 positive finite float arguments: width and height.")
        else:
            area = width * height

            if isinf(area):
                raise ValueError("Arguments too large: overflow occurred.")
            else:
                print(area)
