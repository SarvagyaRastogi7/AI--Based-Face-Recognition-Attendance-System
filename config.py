from functools import lru_cache

from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    # General
    app_name: str = "RAG Briefing Generator"

    # Azure OpenAI / Azure Models via openai SDK
    azure_openai_endpoint: AnyHttpUrl | None = Field(
        default=None, env="AZURE_OPENAI_ENDPOINT"
    )
    azure_openai_api_key: str | None = Field(
        default=None, env="AZURE_OPENAI_API_KEY"
    )
    azure_openai_deployment: str | None = Field(
        default=None, env="AZURE_OPENAI_DEPLOYMENT"
    )
    azure_openai_api_version: str = Field(
        default="2024-10-21", env="AZURE_OPENAI_API_VERSION"
    )

    # Database (Oracle or other)
    db_dsn: str | None = Field(default=None, env="DB_DSN")
    db_user: str | None = Field(default=None, env="DB_USER")
    db_password: str | None = Field(default=None, env="DB_PASSWORD")
    db_host: str | None = Field(default=None, env="DB_HOST")
    db_port: int | None = Field(default=1521, env="DB_PORT")
    db_service: str | None = Field(default=None, env="DB_SERVICE")

    # Web search
    search_api_key: str | None = Field(default=None, env="SEARCH_API_KEY")
    search_endpoint: AnyHttpUrl | None = Field(
        default=None, env="SEARCH_ENDPOINT"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()

