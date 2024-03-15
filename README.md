# Discord to Telegram emojis converter
Converts Discord emoji to Telegram format (`webp`)  
Video emoji conversion (`gif` -> `webm`) is also available.

# How to use:
1. Go to the desired Discord server using a browser

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/5a37f187-8789-4dfb-af3c-add37c888129)

2. `Shift+f12` -> tab `Network`.

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/80df898b-9f4c-4dfd-8098-2e44d70a9eaf)

3. `Ctrl+R` to reload the page

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2ec86f47-57ce-41c1-9790-c8278faaaacd)

4. Click on the emoji menu and load them by scrolling downward

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/8ed12566-1ff2-4498-9314-79f4074fc112)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/abf772c9-6d47-4860-a575-8ab276902552)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2897e52b-c89d-41cc-a593-bde7ddf40775)

5. ``*Gears`` -> ``Save everything as HAR``, in the `input` directory

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/75b28dba-3e0a-4f69-a12f-a8d01e53f518)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/6ef3344e-ef97-4c7a-a9f4-183d2931ddd3)

7. Replace the file name in `har_of_downloaded_emojis` in the `[Path]` section of the `config/constants.ini` file

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2513cf17-cbd3-4fa4-af87-658e3b64e007)

8. Perform the steps below to get the result

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
- I couldn't find an endpoint that gives an answer in the form of a list of emojis belonging to the server set
- When converting gif emoji format to telegram format, ffmpeg outputs logs to standard output, suppressing it fails
- The slowdown method does not work as expected - ffmpeg in some cases says that the output file has one duration, but in reality it has a completely different one. You can investigate this phenomenon by analyzing the output of `changed_gif_timing_check.py` and `gifs_for_telegram_resizer.py`
- Downloads and conversions are performed sequentially, not in parallel

Help with the project is welcome
