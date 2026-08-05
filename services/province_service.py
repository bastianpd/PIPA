"""
Service layer for province-related business logic.
"""

from __future__ import annotations

from typing import Optional

from models.province import Province
from repositories.province_repository import ProvinceRepository
from services.base_service import BaseService


class ProvinceService(BaseService[Province]):
    """
    Business logic for provinces.

    Streamlit pages must call this service instead of accessing
    ProvinceRepository directly.
    """

    def __init__(self, repository: ProvinceRepository) -> None:
        """
        Initialize the province service.

        Args:
            repository: A ProvinceRepository instance.
        """
        super().__init__(repository=repository)
        self.repository: ProvinceRepository = repository

    def list_provinces(self) -> list[Province]:
        """
        Return every province, sorted alphabetically by name.

        Returns:
            A list of Province entities sorted by `nome`.
        """
        provinces = self.repository.get_all_provinces()
        return sorted(provinces, key=lambda province: province.nome)

    def get_province(self, province_id: int) -> Optional[Province]:
        """
        Retrieve a single province by its primary key.

        Args:
            province_id: Surrogate primary key of the province.

        Returns:
            The matching Province, or None if not found.
        """
        return self.repository.get_by_id(province_id)

    def get_province_by_code(self, codigo: str) -> Optional[Province]:
        """
        Retrieve a single province by its internal code.

        Args:
            codigo: Internal province code.

        Returns:
            The matching Province, or None if not found.
        """
        return self.repository.get_province_by_code(codigo)
