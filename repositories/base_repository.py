"""
Abstract base repository.

Defines the common contract every repository must implement.
Repositories are the ONLY modules allowed to communicate with
Supabase (Mandatory Architecture Rule 6). Services must never query
the database directly; they must always go through a repository.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, TypeVar

from supabase import Client

T = TypeVar("T")


class BaseRepository(ABC, Generic[T]):
    """
    Abstract base class for all repositories.

    Attributes:
        table_name: Name of the Supabase table this repository manages.
        client: Shared Supabase client used to perform queries.
    """

    def __init__(self, client: Client, table_name: str) -> None:
        """
        Initialize the repository.

        Args:
            client: A configured Supabase client instance.
            table_name: Name of the table this repository is responsible for.
        """
        self.client = client
        self.table_name = table_name

    @abstractmethod
    def _to_entity(self, record: dict[str, Any]) -> T:
        """
        Convert a raw database record into a domain entity.

        Args:
            record: Raw dictionary returned by Supabase.

        Returns:
            The corresponding domain entity instance.
        """
        raise NotImplementedError

    def get_all(self) -> list[T]:
        """
        Retrieve every record from the table.

        Returns:
            A list of domain entities.
        """
        response = self.client.table(self.table_name).select("*").execute()
        return [self._to_entity(record) for record in response.data]

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Retrieve a single record by its primary key.

        Args:
            id: Surrogate primary key of the record.

        Returns:
            The matching domain entity, or None if not found.
        """
        response = (
            self.client.table(self.table_name)
            .select("*")
            .eq("id", id)
            .limit(1)
            .execute()
        )
        if not response.data:
            return None
        return self._to_entity(response.data[0])

    def find_by(self, criteria: dict[str, Any]) -> list[T]:
        """
        Retrieve records matching the given equality criteria.

        Args:
            criteria: Mapping of column names to expected values. Every
                entry is combined with a logical AND.

        Returns:
            A list of matching domain entities.
        """
        query = self.client.table(self.table_name).select("*")
        for column, value in criteria.items():
            query = query.eq(column, value)
        response = query.execute()
        return [self._to_entity(record) for record in response.data]
