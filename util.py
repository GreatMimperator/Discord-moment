import math
import subprocess


def get_duration_secs(input_file_path: str):
    command = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {input_file_path}"
    popen = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    out, err = popen.communicate()
    return float(out)


def calculate_slowdown_coefficient(gif_duration_secs: float, needed_duration_secs: float):
    if gif_duration_secs > needed_duration_secs:
        return math.ceil(gif_duration_secs / needed_duration_secs) + 1
    else:
        return 1
