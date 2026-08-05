"""
Service layer for indicator-related business logic.
"""

from __future__ import annotations

from typing import Optional

from models.indicator import Indicator
from repositories.indicator_repository import IndicatorRepository
from services.base_service import BaseService


class IndicatorService(BaseService[Indicator]):
    """
    Business logic for statistical indicators.

    Streamlit pages must call this service instead of accessing
    IndicatorRepository directly.
    """

    def __init__(self, repository: IndicatorRepository) -> None:
        """
        Initialize the indicator service.

        Args:
            repository: An IndicatorRepository instance.
        """
        super().__init__(repository=repository)
        self.repository: IndicatorRepository = repository

    def list_indicators(self) -> list[Indicator]:
        """
        Return every indicator, sorted alphabetically by name.

        Returns:
            A list of Indicator entities sorted by `nome`.
        """
        indicators = self.repository.get_all_indicators()
        return sorted(indicators, key=lambda indicator: indicator.nome)

    def get_indicator(self, indicator_id: int) -> Optional[Indicator]:
        """
        Retrieve a single indicator by its primary key.

        Args:
            indicator_id: Surrogate primary key of the indicator.

        Returns:
            The matching Indicator, or None if not found.
        """
        return self.repository.get_by_id(indicator_id)

    def list_indicators_by_sector(self, sector_id: int) -> list[Indicator]:
        """
        Return every indicator belonging to a given sector.

        Args:
            sector_id: Primary key of the sector.

        Returns:
            A list of Indicator entities belonging to that sector, sorted
            alphabetically by name.
        """
        indicators = self.repository.get_indicators_by_sector(sector_id)
        return sorted(indicators, key=lambda indicator: indicator.nome)
