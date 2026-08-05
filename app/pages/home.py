"""
Home page.

Presents the PIPA landing page. Contains no business logic and no
database access; navigation state is the only local state handled
here, per Mandatory Architecture Rule 1.
"""

from __future__ import annotations

import streamlit as st


def render() -> None:
    """Render the home page content."""
    st.header("PIPA - Plataforma de Indicadores Públicos de Angola")
    st.subheader("Transformando dados oficiais em conhecimento acessível")

    st.write(
        "Explore indicadores económicos, sociais, demográficos e "
        "territoriais de Angola através de uma experiência de "
        "storytelling orientada por dados oficiais."
    )

    if st.button("Explorar Indicadores"):
        st.session_state["active_page"] = "indicators"
        st.rerun()
