# Discord to Telegram emojis converter
Converts Discord emoji to Telegram format (`webp`)  
Video emoji conversion (`gif` -> `webm`) is also available.

# How to use:
1. Go to the desired Discord server using a browser
2. `Shift+f12` -> tab `Network`.
3. `Ctrl+R` to reload the page
4. Click on the emoji menu and load them by scrolling downward
5. ``*Gears`` -> ``Save everything as HAR``, in the `input` directory
6. Replace the file name in `har_of_downloaded_emojis` in the `[Path]` section of the `config/constants.ini` file
7. Perform the steps below to get the result

To load an emoji (does not load an already loaded emoji): 
```shell
python har_emoji_urls_getter.py
```

To bring the emoji format to the Telegram format:
```shell
python images_for_telegram_resizer.py
```

To convert gif emoji format to Telegram emoji format:
```shell
python gifs_for_telegram_resizer.py
```

To check if the gif emoji is successfully accelerated:
```shell
python changed_gif_timing_check.py
```

To change folder paths and conversion parameters - ``/config/constants``.

# Unresolved issues:
- When converting gif emoji format to telegram format, ffmpeg outputs logs to standard output, suppressing it fails
- The slowdown method does not work as expected - ffmpeg in some cases says that the output file has one duration, but in reality it has a completely different one. You can investigate this phenomenon by analyzing the output of `changed_gif_timing_check.py` and `gifs_for_telegram_resizer.py`
- Downloads and conversions are performed sequentially, not in parallel

Help with the project is welcome