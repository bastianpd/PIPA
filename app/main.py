"""
Application entrypoint for the PIPA Streamlit app.

This module ONLY configures the page and renders navigation and
top-level routing. It contains no business logic and no database
access, per Mandatory Architecture Rules 1 and 2.
"""

from __future__ import annotations

import streamlit as st

from app.pages import about, home, indicators, maps, provinces
from components.navigation import render_navigation

PAGES = {
    "home": home,
    "indicators": indicators,
    "provinces": provinces,
    "maps": maps,
    "about": about,
}


def configure_page() -> None:
    """Configure global Streamlit page settings."""
    st.set_page_config(
        page_title="PIPA - Public Indicators Platform",
        layout="wide",
    )


def main() -> None:
    """Render the PIPA application shell and dispatch to the active page."""
    configure_page()

    if "active_page" not in st.session_state:
        st.session_state["active_page"] = "home"

    render_navigation(active_page=st.session_state["active_page"])

    st.title("PIPA - Public Indicators Platform")
    st.info("PIPA - Em Desenvolvimento")

    page_module = PAGES.get(st.session_state["active_page"], home)
    page_module.render()


if __name__ == "__main__":
    main()
