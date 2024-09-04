class DatabaseSettings():
    __user: str
    __password: str
    __host: str
    __port: int
    __database: str

    def __initialize(self, user: str, password: str, host: str, port: int, database: str) -> None:
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__database = database

    def __init__(self, dict:dict) -> None:
        self.__initialize(str(dict['user']),
                      str(dict['password']),
                      str(dict['host']),
                      int(dict['port']),
                      str(dict['database']))

    def get_user(self) -> str:
        return self.__user

    def get_password(self) -> str:
        return self.__password

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port

    def get_database(self) -> str:
        return self.__database


    def get_url_connection(self) -> str:
        return f"postgresql+psycopg2://{self.get_user()}:{self.get_password()}@{self.get_host()}:{self.get_port()}/{self.get_database()}"
