"""
Configuration module for the PIPA platform.

Centralizes access to environment variables and application-wide
settings. No other module should read environment variables directly;
all configuration must be resolved through this module.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """
    Immutable container for application configuration values.

    Attributes:
        supabase_url: Base URL of the Supabase project.
        supabase_key: API key used to authenticate with Supabase.
        app_title: Display title of the Streamlit application.
        app_layout: Streamlit page layout mode.
    """

    supabase_url: str
    supabase_key: str
    app_title: str = "PIPA - Public Indicators Platform"
    app_layout: str = "wide"


def _read_env_or_secret(key: str) -> str:
    """
    Read a configuration value from environment variables.

    Streamlit Cloud injects values from `.streamlit/secrets.toml` into
    `os.environ` at runtime, so reading from the environment is
    sufficient for both local and cloud execution.

    Args:
        key: Name of the environment variable to read.

    Returns:
        The value associated with the given key, or an empty string
        if it is not set.
    """
    return os.environ.get(key, "")


def get_settings() -> Settings:
    """
    Build and return the application settings.

    Returns:
        A populated, immutable Settings instance.
    """
    return Settings(
        supabase_url=_read_env_or_secret("SUPABASE_URL"),
        supabase_key=_read_env_or_secret("SUPABASE_KEY"),
    )
