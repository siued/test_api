from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.
    """

    # General settings
    env: str = "prod"

    # Postgres settings
    postgres_user: str = ""
    postgres_password: str = ""
    postgres_host: str = ""
    postgres_port: int = 5432
    postgres_db: str = "postgres"

    # Sentry settings
    sentry_dsn: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        extra = "allow"


settings = Settings()
