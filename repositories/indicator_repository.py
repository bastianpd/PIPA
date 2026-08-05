"""
Repository responsible for the `dim_indicador` table.
"""

from __future__ import annotations

from typing import Any

from supabase import Client

from models.indicator import Indicator
from repositories.base_repository import BaseRepository

TABLE_NAME = "dim_indicador"


class IndicatorRepository(BaseRepository[Indicator]):
    """
    Data access layer for statistical indicators.

    This is the only class in the application allowed to issue
    Supabase queries against `dim_indicador`.
    """

    def __init__(self, client: Client) -> None:
        """
        Initialize the indicator repository.

        Args:
            client: A configured Supabase client instance.
        """
        super().__init__(client=client, table_name=TABLE_NAME)

    def _to_entity(self, record: dict[str, Any]) -> Indicator:
        """
        Convert a raw `dim_indicador` record into an Indicator entity.

        Args:
            record: Raw dictionary returned by Supabase.

        Returns:
            A populated Indicator instance.
        """
        return Indicator.from_dict(record)

    def get_all_indicators(self) -> list[Indicator]:
        """
        Retrieve every indicator registered in the database.

        Returns:
            A list of all Indicator entities.
        """
        return self.get_all()

    def get_indicators_by_sector(self, sector_id: int) -> list[Indicator]:
        """
        Retrieve every indicator belonging to a given sector.

        Args:
            sector_id: Primary key of the sector (`dim_setor.id`).

        Returns:
            A list of Indicator entities belonging to that sector.
        """
        return self.find_by({"setor_id": sector_id})
