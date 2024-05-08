from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    debug: bool = True
    port: int = 5000


app_settings = AppSettings()
