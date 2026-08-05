"""
Indicator selector component.

Presents a dropdown for selecting a statistical indicator. Receives
the list of indicators to display as an argument; it never queries
the database itself, per Mandatory Architecture Rule 3.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st

from models.indicator import Indicator


def render_indicator_selector(
    indicators: list[Indicator],
    key: str = "indicator_selector",
    label: str = "Selecione um indicador",
) -> Optional[Indicator]:
    """
    Render a selectbox for choosing an indicator.

    Args:
        indicators: List of Indicator entities to populate the selector,
            typically obtained from IndicatorService.
        key: Unique Streamlit widget key.
        label: Label displayed above the selector.

    Returns:
        The selected Indicator, or None if the list is empty.
    """
    if not indicators:
        st.info("Nenhum indicador disponível.")
        return None

    options = {indicator.nome: indicator for indicator in indicators}
    selected_name = st.selectbox(label=label, options=list(options.keys()), key=key)
    return options[selected_name]
