from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки телеграмм-бота"""
    TOKEN: str
    TELEGRAM_LINK: str = "https://t.me/so1ez"
    VK_LINK: str = "https://vk.com/so1ez"
    GITHUB_LINK: str = "https://github.com/so1ez"
    IN_TAGRAM_LINK: str = "https://instagram.com/lso1ezl"
    HELLO_MSG: str = "Привет👋! Я Владимир, мой никнейм в соцсетях - Сóлез (so1ez). " + \
    "Этот бот нужен только для одной цели - предоставить ссылки на мои соцсети!🔗"

    class Config:
        env_file = '.env'


SETTINGS = Settings()