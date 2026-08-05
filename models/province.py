"""
Data model for the `dim_provincia` dimension table.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True)
class Province:
    """
    Represents an administrative province of Angola.

    Attributes:
        id: Surrogate primary key.
        nome: Official province name.
        codigo: Internal province code.
        codigo_iso: ISO administrative code.
        latitude_centro: Latitude of the province's centroid.
        longitude_centro: Longitude of the province's centroid.
        geojson_id: Identifier matching the geographic boundary files.
    """

    id: int
    nome: str
    codigo: str
    codigo_iso: Optional[str] = None
    latitude_centro: Optional[float] = None
    longitude_centro: Optional[float] = None
    geojson_id: Optional[str] = None

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Province":
        """
        Build a Province instance from a raw database record.

        Args:
            data: Dictionary as returned by the Supabase client.

        Returns:
            A populated Province instance.
        """
        return Province(
            id=data["id"],
            nome=data["nome"],
            codigo=data["codigo"],
            codigo_iso=data.get("codigo_iso"),
            latitude_centro=data.get("latitude_centro"),
            longitude_centro=data.get("longitude_centro"),
            geojson_id=data.get("geojson_id"),
        )
