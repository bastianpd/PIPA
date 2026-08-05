"""
KPI card component.

Displays a single key indicator value. This component only renders
data passed to it; it never fetches data itself, per Mandatory
Architecture Rule 3.
"""

from __future__ import annotations

from typing import Optional

import streamlit as st


def render_kpi_card(
    label: str,
    value: str,
    unit: Optional[str] = None,
    source: Optional[str] = None,
) -> None:
    """
    Render a single KPI card.

    Args:
        label: Name of the indicator being displayed.
        value: Pre-formatted value to display (already resolved by a Service).
        unit: Optional unit of measurement shown next to the value.
        source: Optional official data source, shown as a caption for
            transparency, per the project's Transparency principle.
    """
    display_value = f"{value} {unit}" if unit else value
    st.metric(label=label, value=display_value)
    if source:
        st.caption(f"Fonte: {source}")
