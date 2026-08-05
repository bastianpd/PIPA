"""
Provinces page.

Displays the catalog of provinces. All data is obtained through
ProvinceService; this page never queries Supabase directly, per
Mandatory Architecture Rules 1, 2 and 4.
"""

from __future__ import annotations

import streamlit as st

from components.province_selector import render_province_selector
from database.supabase_client import SupabaseConnectionError, get_supabase_client
from repositories.province_repository import ProvinceRepository
from services.province_service import ProvinceService


def render() -> None:
    """Render the provinces page content."""
    st.header("Províncias")
    st.write("Explore os indicadores organizados por província de Angola.")

    try:
        client = get_supabase_client()
    except SupabaseConnectionError as error:
        st.warning(
            "Não foi possível ligar à base de dados. Configure as "
            "credenciais do Supabase para visualizar as províncias."
        )
        st.caption(str(error))
        return

    service = ProvinceService(ProvinceRepository(client))
    provinces = service.list_provinces()

    selected = render_province_selector(provinces)
    if selected:
        st.subheader(selected.nome)
        st.caption(f"Código: {selected.codigo}")
