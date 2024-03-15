import logging
import os
import sys
from subprocess import Popen
from config_util import *
from util import *

from har_parser import receive_content_info_from_har


def ffmpeg_resize_call(input_path: str, output_path: str, output_webm_size: int, max_duration_secs: float,
                       gif_duration_secs: float | None) -> Popen:
    if gif_duration_secs is None:
        gif_duration_secs = get_duration_secs(input_path)
    slowdown_coefficient = calculate_slowdown_coefficient(gif_duration_secs, max_duration_secs)
    command = (f"ffmpeg -i {input_path} "
               f"-vf \"scale={output_webm_size}:{output_webm_size}:"
               f"force_original_aspect_ratio=decrease,"
               f"setpts=PTS/{slowdown_coefficient},"
               f"pad={output_webm_size}:{output_webm_size}:(ow-iw)/2:(oh-ih)/2:color=black@0\" "
               f"-c:v libvpx-vp9 "
               f"{output_path}")
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)


def main() -> int:
    logging.basicConfig(level=logging.INFO)
    config = get_constants_config()
    output_webm_size = ConversionSection.get_output_webm_size(config)
    max_duration_secs = ConversionSection.get_max_duration_secs(config)

    extension_emoji_ids = receive_content_info_from_har(PathSection.get_har_path(config))
    downloaded_dir = PathSection.get_downloaded_dir(config)
    processed_dir = PathSection.get_processed_dir(config)

    if "gif" in extension_emoji_ids:
        input_path = f"{downloaded_dir}/gif"
        converted_path = f"{processed_dir}/{PathSection.get_gif_to_tg_webm_dir(config)}"
        if not os.path.exists(converted_path):
            os.mkdir(converted_path)
        counter = 0
        length = len(extension_emoji_ids["gif"])
        failed_count = 0
        for identification in extension_emoji_ids["gif"]:
            counter += 1
            input_file_path = f"{input_path}/{identification}.gif"
            gif_duration_secs = get_duration_secs(input_file_path)
            logging.info(f"{identification} has {gif_duration_secs} duration")
            if gif_duration_secs > max_duration_secs:
                slowdown_coefficient = calculate_slowdown_coefficient(gif_duration_secs, max_duration_secs)
                logging.info(f"{identification} will be converted with {slowdown_coefficient} slowdown coefficient")
                fasten_path = f"{converted_path}/{PathSection.get_gif_to_tg_webm_fasten_dir(config)}"
                if not os.path.exists(fasten_path):
                    os.mkdir(fasten_path)
                output_file_path = f"{fasten_path}/{identification}.webm"
            else:
                output_file_path = f"{converted_path}/{identification}.webm"
            if os.path.exists(output_file_path):
                logging.info(
                    f"{identification} has already converted from gif to {output_webm_size}x{output_webm_size} webm")
                continue
            process = ffmpeg_resize_call(input_file_path, output_file_path,
                                         output_webm_size, max_duration_secs,
                                         gif_duration_secs)
            process.wait()
            logging.info(f"{counter}/{length} {identification} "
                         f"from gif to {output_webm_size}x{output_webm_size} webm converted...")
        if failed_count == 0:
            logging.info(f"\tAll {length} files converted successfully!")
        else:
            logging.info(f"\t{length - failed_count}/{length} files converted successfully!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
