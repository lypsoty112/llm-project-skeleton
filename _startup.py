import dotenv


def startup() -> None:
    """
    Function to run at the start of the program. Starts logging, loads environment variables, ...
    :return:
    """
    dotenv.load_dotenv()
