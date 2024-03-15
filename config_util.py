from configparser import ConfigParser, ExtendedInterpolation


def get_constants_config() -> ConfigParser:
    constants_config_path = "config/constants.ini"
    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read(constants_config_path)
    return config


class PathSection:
    name = "Path"

    @staticmethod
    def get(config: ConfigParser, option_name: str) -> str:
        return config.get(PathSection.name, option_name)

    @staticmethod
    def get_input_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "input_dir")

    @staticmethod
    def get_output_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "output_dir")

    @staticmethod
    def get_downloaded_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "downloaded_dir")

    @staticmethod
    def get_processed_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "processed_dir")

    @staticmethod
    def get_gif_to_tg_webm_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "gif_to_tg_webm_dir")

    @staticmethod
    def get_gif_to_tg_webm_fasten_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "gif_to_tg_webm_fasten_dir")

    @staticmethod
    def get_webp_to_tg_converted_dir(config: ConfigParser) -> str:
        return PathSection.get(config, "webp_to_tg_converted_dir")

    @staticmethod
    def get_har_path(config: ConfigParser) -> str:
        return PathSection.get(config, "har_of_downloaded_emojis")


class ConversionSection:
    name = "Conversion"

    @staticmethod
    def get(config: ConfigParser, option_name: str) -> str:
        return config.get(ConversionSection.name, option_name)

    @staticmethod
    def get_int(config: ConfigParser, option_name: str) -> int:
        return config.getint(ConversionSection.name, option_name)

    @staticmethod
    def get_float(config: ConfigParser, option_name: str) -> float:
        return config.getint(ConversionSection.name, option_name)

    @staticmethod
    def get_output_webm_size(config: ConfigParser) -> int:
        return ConversionSection.get_int(config, "output_webm_size")

    @staticmethod
    def get_output_image_size(config: ConfigParser) -> int:
        return ConversionSection.get_int(config, "output_image_size")

    @staticmethod
    def get_max_duration_secs(config: ConfigParser) -> float:
        return ConversionSection.get_float(config, "max_duration_size")

    @staticmethod
    def get_tg_image_extension(config: ConfigParser) -> str:
        return ConversionSection.get(config, "tg_image_extension")
