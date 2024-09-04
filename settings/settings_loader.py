import yaml

from settings.database_settings import DatabaseSettings

def getDatabaseSettings() -> DatabaseSettings:
    database_configs: dict = __load_settings()['database']
    return DatabaseSettings(database_configs)

def __load_settings() -> dict:
    with open('settings.yaml') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


database_settings: DatabaseSettings = getDatabaseSettings()
