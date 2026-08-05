"""
Indicators page.

Displays the catalog of statistical indicators. All data is obtained
through IndicatorService; this page never queries Supabase directly,
per Mandatory Architecture Rules 1, 2 and 4.
"""

from __future__ import annotations

import streamlit as st

from components.indicator_selector import render_indicator_selector
from database.supabase_client import SupabaseConnectionError, get_supabase_client
from repositories.indicator_repository import IndicatorRepository
from services.indicator_service import IndicatorService


def render() -> None:
    """Render the indicators page content."""
    st.header("Indicadores")
    st.write("Explore os indicadores estatísticos oficiais disponíveis na plataforma.")

    try:
        client = get_supabase_client()
    except SupabaseConnectionError as error:
        st.warning(
            "Não foi possível ligar à base de dados. Configure as "
            "credenciais do Supabase para visualizar os indicadores."
        )
        st.caption(str(error))
        return

    service = IndicatorService(IndicatorRepository(client))
    indicators = service.list_indicators()

    selected = render_indicator_selector(indicators)
    if selected:
        st.subheader(selected.nome)
        if selected.descricao:
            st.write(selected.descricao)
        if selected.unidade:
            st.caption(f"Unidade: {selected.unidade}")
