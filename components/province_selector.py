"""
Province selector component.

Presents a dropdown for selecting a province. Receives the list of
provinces to display as an argument; it never queries the database
itself, per Mandatory Architecture Rule 3.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st

from models.province import Province


def render_province_selector(
    provinces: list[Province],
    key: str = "province_selector",
    label: str = "Selecione uma província",
) -> Optional[Province]:
    """
    Render a selectbox for choosing a province.

    Args:
        provinces: List of Province entities to populate the selector,
            typically obtained from ProvinceService.
        key: Unique Streamlit widget key.
        label: Label displayed above the selector.

    Returns:
        The selected Province, or None if the list is empty.
    """
    if not provinces:
        st.info("Nenhuma província disponível.")
        return None

    options = {province.nome: province for province in provinces}
    selected_name = st.selectbox(label=label, options=list(options.keys()), key=key)
    return options[selected_name]
