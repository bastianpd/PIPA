"""
Supabase connection module.

Provides a single, shared Supabase client instance for the entire
application. No module outside `repositories/` should import this
module directly, per the mandatory architecture rules (Rule 6:
Repositories MUST communicate only with Supabase).
"""

from __future__ import annotations

from typing import Optional

from supabase import Client, create_client

from utils.config import get_settings


class SupabaseConnectionError(Exception):
    """Raised when the Supabase client cannot be created or is misconfigured."""


class SupabaseClientSingleton:
    """
    Singleton wrapper around the Supabase client.

    Ensures that only one Supabase client instance exists throughout
    the application lifecycle, avoiding redundant connections.
    """

    _instance: Optional["SupabaseClientSingleton"] = None
    _client: Optional[Client] = None

    def __new__(cls) -> "SupabaseClientSingleton":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_client(self) -> Client:
        """
        Return the shared Supabase client, creating it on first use.

        Returns:
            A configured Supabase `Client` instance.

        Raises:
            SupabaseConnectionError: If required credentials are missing
                or the client cannot be created.
        """
        if self._client is not None:
            return self._client

        settings = get_settings()

        if not settings.supabase_url or not settings.supabase_key:
            raise SupabaseConnectionError(
                "Supabase credentials are missing. Please configure "
                "SUPABASE_URL and SUPABASE_KEY via environment variables "
                "or .streamlit/secrets.toml."
            )

        try:
            self._client = create_client(settings.supabase_url, settings.supabase_key)
        except Exception as exc:  # noqa: BLE001 - surfaced as a domain-specific error
            raise SupabaseConnectionError(
                f"Failed to create Supabase client: {exc}"
            ) from exc

        return self._client


def get_supabase_client() -> Client:
    """
    Convenience accessor for the shared Supabase client.

    Returns:
        A configured Supabase `Client` instance.
    """
    return SupabaseClientSingleton().get_client()
