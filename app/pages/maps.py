"""
Maps page.

Displays interactive geographical visualizations. Data access and
map data preparation belong in a future analytics service; this page
contains no business logic, per Mandatory Architecture Rule 1.
"""

from __future__ import annotations

import streamlit as st


def render() -> None:
    """Render the maps page content."""
    st.header("Mapas")
    st.write("Visualização geográfica interativa dos indicadores por província.")
    st.info("Funcionalidade em desenvolvimento.")
