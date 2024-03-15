# Конвертер эмодзи Discord в эмодзи Telegram
Приводит эмодзи дискорда к формату телеграма (`webp`)  
Доступно также преобразование видео-эмодзи (`gif` -> `webm`)

# Порядок использования:

1. Зайти на нужный сервер в дискорд через браузер

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/5a37f187-8789-4dfb-af3c-add37c888129)

2. `Shift+f12` -> вкладка `Сеть`

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/80df898b-9f4c-4dfd-8098-2e44d70a9eaf)

3. `Ctrl+R` для перезагрузки страницы

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2ec86f47-57ce-41c1-9790-c8278faaaacd)

4. Нажать на меню эмодзи и прогрузить их, пролистав вниз

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/8ed12566-1ff2-4498-9314-79f4074fc112)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/abf772c9-6d47-4860-a575-8ab276902552)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2897e52b-c89d-41cc-a593-bde7ddf40775)

5. `*Шестеренка*` -> `Сохранить все как HAR`, в директорию `input`

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/75b28dba-3e0a-4f69-a12f-a8d01e53f518)

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/6ef3344e-ef97-4c7a-a9f4-183d2931ddd3)

6. Замените название файла в `har_of_downloaded_emojis` в разделе `[Path]` файла `config/constants.ini`

![изображение](https://github.com/GreatMimperator/Discord-moment/assets/93261336/2513cf17-cbd3-4fa4-af87-658e3b64e007)

7. Исполните действия ниже для получения результата


Для загрузки эмодзи (не загружает уже загруженное): 
```shell
python har_emoji_urls_getter.py
```

Для приведения формата эмодзи к телеграмовскому:
```shell
python images_for_telegram_resizer.py
```

Для приведения формата gif-эмодзи к телеграмовскому:
```shell
python gifs_for_telegram_resizer.py
```

Для проверки удачности ускорения gif-эмодзи:
```shell
python changed_gif_timing_check.py
```

Для изменения путей папок и параметров конвертации - `/config/constants`

# Нерешенные проблемы:
- Я не смог найти эндпоинт, который дает ответ в виде списка эмодзи, принадлежащих набору сервера
- При приведении формата gif-эмодзи к телеграмовскому ffmpeg выводит логи в стандартный вывод, подавить его не удается
- Метод замедления не работает как ожидается - ffmpeg в ряде случаев говорит, что выходной файл имеет одну длительность, однако в действительности он имеет совершенно другую. Исследовать этот феномен можно с помощью анализа вывода `changed_gif_timing_check.py` и `gifs_for_telegram_resizer.py`
- Скачивание и конвертация выполняются последовательно, а не параллельно

Помощь с проектом приветствуется
