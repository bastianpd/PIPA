"""
Data model for the `fato_indicador` fact table.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class Observation:
    """
    Represents a single statistical observation.

    Each observation corresponds to exactly one province, one
    indicator, one year, one source and one value, as defined in the
    PIPA database specification (Appendix A, Table `fato_indicador`).

    Attributes:
        id: Surrogate primary key.
        provincia_id: Foreign key to `dim_provincia`.
        indicador_id: Foreign key to `dim_indicador`.
        ano: Reference year of the observation.
        valor: Numerical value of the observation.
        fonte_id: Foreign key to `fonte_dados`.
    """

    provincia_id: int
    indicador_id: int
    ano: int
    valor: float
    fonte_id: int
    id: Optional[int] = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Observation":
        """
        Build an Observation instance from a raw database record.

        Args:
            data: Dictionary as returned by the Supabase client.

        Returns:
            A populated Observation instance.
        """
        return Observation(
            id=data.get("id"),
            provincia_id=data["provincia_id"],
            indicador_id=data["indicador_id"],
            ano=data["ano"],
            valor=data["valor"],
            fonte_id=data["fonte_id"],
        )
