from main_decorator import main
from io import BytesIO
from os.path import isdir as directory_exists
import argparse
import requests


@main
def main():
    parser = argparse.ArgumentParser(description='Save file from url')
    parser.add_argument('url', type=str, help='Input file url')
    parser.add_argument('path', type=str, help='Input directory for saving')

    try:
        args = parser.parse_args()
    except (SystemExit, ValueError, argparse.ArgumentError) as error:
        raise ValueError("You need enter only 2 string arguments: url and path.") from error
    else:
        url = args.url
        path = args.path

        if not directory_exists(path):
            raise NotADirectoryError(f"Path {path} is incorrect.")

        filename = url.rsplit('/', 1)[1]

        try:
            res = requests.get(url)

            if res.status_code == 404:
                if len(filename.split('.')) == 1:
                    filename += '.html'
                else:
                    raise requests.exceptions.RequestException("Request status 404.")

        except requests.exceptions.InvalidURL:
            raise

        res_bytes = BytesIO(res.content)

        with open(f"{path}/{filename}", "wb") as file:
            file.write(res_bytes.getbuffer())


# "https://htmlbook.ru/files/images/html/tag_form_1.png"
# C:\Users\HP\PycharmProjects\vpo\Lab1\tasks\task5\tests\test_dir
