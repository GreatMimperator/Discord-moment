import logging
import os
import sys

import requests

from config_util import *
from har_parser import receive_content_info_from_har


def main() -> int:
    logging.basicConfig(level=logging.INFO)
    config = get_constants_config()

    extension_emoji_ids = receive_content_info_from_har(PathSection.get_har_path(config))

    downloaded_dir = PathSection.get_downloaded_dir(config)
    if not os.path.exists(downloaded_dir):
        os.makedirs(downloaded_dir)
        logging.info(f"Created \"{downloaded_dir}\" for output")

    logging.info("Extensions with counts: ")
    for extension, identifications in extension_emoji_ids.items():
        logging.info(f"\t{extension}: {len(identifications)}")
    logging.info("")

    for extension, identifications in extension_emoji_ids.items():
        logging.info(f"\tStart downloading {extension} files")
        extension_path = f"{downloaded_dir}/{extension}"
        extension_folder_path = os.path.join(extension_path)
        if not os.path.exists(extension_folder_path):
            os.mkdir(extension_folder_path)
        counter = 0
        for identification in identifications:
            counter += 1
            file_path = f"{extension_path}/{identification}.{extension}"
            if os.path.exists(file_path):
                logging.info(
                    f"{counter}/{len(identifications)} {identification}.{extension} already downloaded! Delete it for force-download")
                continue
            response = requests.get(
                f"https://cdn.discordapp.com/emojis/{identification}.{extension}?size=100&quality=lossless")
            open(file_path, "wb").write(response.content)
            logging.info(f"{counter}/{len(identifications)} {identification}.{extension} downloaded...")
        logging.info(f"\tAll {extension} files downloaded successfully!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
