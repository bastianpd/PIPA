"""
Abstract base service.

Services encapsulate business logic and are the only layer that
Streamlit pages are allowed to call directly (Mandatory Architecture
Rule 4). Services must never talk to Supabase directly; they must
always delegate data access to a repository (Rule 5).
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, TypeVar

from repositories.base_repository import BaseRepository

T = TypeVar("T")


class BaseService(ABC, Generic[T]):
    """
    Abstract base class for all services.

    Attributes:
        repository: The repository this service delegates data access to.
    """

    def __init__(self, repository: BaseRepository[T]) -> None:
        """
        Initialize the service.

        Args:
            repository: A repository instance implementing BaseRepository.
        """
        self.repository = repository
