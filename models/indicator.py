"""
Data model for the `dim_indicador` dimension table.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class Indicator:
    """
    Represents a statistical indicator available on the platform.

    Attributes:
        id: Surrogate primary key.
        nome: Indicator name.
        descricao: Human-readable description of the indicator.
        unidade: Unit of measurement.
        setor_id: Foreign key to the `dim_setor` table.
    """

    id: int
    nome: str
    descricao: Optional[str] = None
    unidade: Optional[str] = None
    setor_id: Optional[int] = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Indicator":
        """
        Build an Indicator instance from a raw database record.

        Args:
            data: Dictionary as returned by the Supabase client.

        Returns:
            A populated Indicator instance.
        """
        return Indicator(
            id=data["id"],
            nome=data["nome"],
            descricao=data.get("descricao"),
            unidade=data.get("unidade"),
            setor_id=data.get("setor_id"),
        )
