"""
Repository responsible for the `dim_provincia` table.
"""

from __future__ import annotations

from typing import Any, Optional

from supabase import Client

from models.province import Province
from repositories.base_repository import BaseRepository

TABLE_NAME = "dim_provincia"


class ProvinceRepository(BaseRepository[Province]):
    """
    Data access layer for provinces.

    This is the only class in the application allowed to issue
    Supabase queries against `dim_provincia`.
    """

    def __init__(self, client: Client) -> None:
        """
        Initialize the province repository.

        Args:
            client: A configured Supabase client instance.
        """
        super().__init__(client=client, table_name=TABLE_NAME)

    def _to_entity(self, record: dict[str, Any]) -> Province:
        """
        Convert a raw `dim_provincia` record into a Province entity.

        Args:
            record: Raw dictionary returned by Supabase.

        Returns:
            A populated Province instance.
        """
        return Province.from_dict(record)

    def get_all_provinces(self) -> list[Province]:
        """
        Retrieve every province registered in the database.

        Returns:
            A list of all Province entities.
        """
        return self.get_all()

    def get_province_by_code(self, codigo: str) -> Optional[Province]:
        """
        Retrieve a province by its internal code.

        Args:
            codigo: Internal province code (`dim_provincia.codigo`).

        Returns:
            The matching Province, or None if no province has that code.
        """
        matches = self.find_by({"codigo": codigo})
        return matches[0] if matches else None
