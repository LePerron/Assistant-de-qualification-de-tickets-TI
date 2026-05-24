from core.logger import logger


def read_file(file_path: str):
    try:
        with open(file_path, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        logger.error(f"The file {file_path} was not found.")
    except OSError:
        logger.error(f"Error when reading file at {file_path}")

    return None


