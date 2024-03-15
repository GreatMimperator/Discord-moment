import logging
import os
import sys
from config_util import *

from PIL import ImageOps
from PIL import Image

from config_util import get_constants_config


def main() -> int:
    logging.basicConfig(level=logging.INFO)
    config = get_constants_config()

    output_pic_size = ConversionSection.get_output_image_size(config)
    out_extension = ConversionSection.get_tg_image_extension(config)
    downloaded_dir = PathSection.get_downloaded_dir(config)
    processed_dir = PathSection.get_processed_dir(config)

    if not os.path.exists(downloaded_dir):
        print(f"\"{downloaded_dir}\" does not exist, so nothing to resize", file=sys.stderr)
        return -1

    if not os.path.exists(processed_dir):
        os.makedirs(processed_dir)
        print(f"\"{processed_dir}\" has created", file=sys.stderr)

    transparency_color = (0, 0, 0, 0)
    dir_names = []
    logging.info(f"Directories to be processed:")
    for dir_name in os.listdir(downloaded_dir):
        if dir_name == "gif":
            logging.info(f"\tskip gif")
            continue
        if f".{dir_name}" not in Image.registered_extensions():
            logging.info(f"\t{dir_name} not an image extension - skip")
            continue
        dir_names.append(dir_name)
        logging.info(f"\t{dir_name} is an image extension - files inside will be processed")

    for dir_name in dir_names:
        logging.info(f"Start processing {dir_name}")
        output_dir_name = f"{processed_dir}/{dir_name}-resized-and-padded-to-{output_pic_size}x{output_pic_size}"
        if not os.path.exists(output_dir_name):
            os.mkdir(output_dir_name)
            logging.info(f"{output_dir_name} directory created for output")
        dir_path = f"{downloaded_dir}/{dir_name}"
        img_names = os.listdir(dir_path)
        logging.info(f"Start resizing {len(img_names)} files of {dir_name} directory")
        counter = 0
        img_count = len(img_names)
        for img_name in img_names:
            counter += 1
            img_name_without_extension, _ = os.path.splitext(img_name)
            out_img_path = f"{output_dir_name}/{img_name_without_extension}.{out_extension}"
            if os.path.exists(out_img_path):
                logging.info(f"{counter}/{img_count} {out_img_path} already exists "
                              f"(means it has processed already) - skip")
                continue
            file_path = f"{dir_path}/{img_name}"
            image = Image.open(file_path)
            resized_and_padded_image = ImageOps.pad(image,
                                                    (output_pic_size, output_pic_size),
                                                    color=transparency_color,
                                                    centering=(0.5, 0.5))
            resized_and_padded_image.save(out_img_path)
            logging.info(f"{counter}/{img_count} {out_img_path} resized and padded successfully "
                          f"(from {image.width}x{image.height} "
                          f"to {resized_and_padded_image.width}x{resized_and_padded_image.height})")
    return 0


if __name__ == '__main__':
    sys.exit(main())
