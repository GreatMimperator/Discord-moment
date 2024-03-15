import os.path
import sys
from pathlib import Path

from config_util import *
from util import *


def main() -> int:
    config = get_constants_config()
    processed_dir = f"{PathSection.get_processed_dir(config)}"
    converted_path = (f"{processed_dir}/"
                      f"{PathSection.get_gif_to_tg_webm_dir(config)}")
    timing_changed_path = (f"{converted_path}/"
                           f"{PathSection.get_gif_to_tg_webm_fasten_dir(config)}")

    if not os.path.exists(timing_changed_path):
        print(f"\"{timing_changed_path}\" does not exists, can not check", file=sys.stderr)
        return -1

    webm_names = os.listdir(timing_changed_path)
    for webm_name in webm_names:
        webm_name_without_extension = Path(webm_name).stem
        webm_path = f"{timing_changed_path}/{webm_name}"
        downloaded_dir = f"{PathSection.get_downloaded_dir(config)}"
        gif_path = f"{downloaded_dir}/gif/{webm_name_without_extension}.gif"
        webm_secs = get_duration_secs(webm_path)
        source_gif_secs = get_duration_secs(gif_path)
        insert_if_bad_duration = ""
        if webm_secs > 3:
            insert_if_bad_duration = " (^^^)"
        elif webm_secs < 1.5:
            insert_if_bad_duration = " (vvv)"
        print(f"{webm_name} has {webm_secs}{insert_if_bad_duration} seconds duration, "
              f"was {source_gif_secs} seconds, so real slow coefficient is {math.floor(source_gif_secs / webm_secs * 10) / 10} "
              f"and putted PTS is {calculate_slowdown_coefficient(source_gif_secs, 3)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
