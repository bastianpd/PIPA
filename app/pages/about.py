"""
About page.

Describes the PIPA project, its mission and its official data
sources. Static content only; no business logic or database access.
"""

from __future__ import annotations

import streamlit as st


def render() -> None:
    """Render the about page content."""
    st.header("Sobre o PIPA")
    st.write(
        "O PIPA (Public Indicators Platform for Angola) é uma plataforma "
        "de conhecimento dedicada à exploração, análise e divulgação de "
        "indicadores públicos oficiais de Angola."
    )

    st.subheader("Missão")
    st.write(
        "Transformar dados públicos oficiais em informação compreensível, "
        "transparente e reprodutível."
    )

    st.subheader("Fontes Oficiais")
    st.write(
        "Todos os valores apresentados na plataforma têm origem em fontes "
        "de dados oficiais, incluindo o Instituto Nacional de Estatística "
        "(INE), ministérios governamentais, o Banco Nacional de Angola e "
        "organizações internacionais."
    )
