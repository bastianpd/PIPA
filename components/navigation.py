"""
Navigation component.

Renders the platform's top-level navigation. This component contains
no business logic and no database access, per Mandatory Architecture
Rule 3 (visualization components must never know database details).
"""

from __future__ import annotations

import streamlit as st


def render_navigation(active_page: str = "home") -> None:
    """
    Render the main navigation bar.

    Args:
        active_page: Key of the currently active page, used only for
            visual highlighting. Does not affect routing.
    """
    pages = {
        "home": "Início",
        "indicators": "Indicadores",
        "provinces": "Províncias",
        "maps": "Mapas",
        "about": "Sobre",
    }

    columns = st.columns(len(pages))
    for column, (page_key, label) in zip(columns, pages.items()):
        with column:
            if page_key == active_page:
                st.markdown(f"**{label}**")
            else:
                st.markdown(label)

    st.divider()
