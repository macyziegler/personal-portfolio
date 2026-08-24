"""
Personal Portfolio — Streamlit Application
============================================
A recruiter-facing professional portfolio for Macy Ziegler.
Edit portfolio_content.py to update all text, links, and data.
"""

import streamlit as st
from pathlib import Path

from portfolio_content import (
    NAME,
    TAGLINE,
    HEADLINE,
    SUBHEADLINE,
    SNAPSHOT,
    HEADSHOT_PATH,
    HEADSHOT_ALT,
    EMAIL,
    LINKEDIN,
    RESUME_FILE,
    NAV_BRAND,
    NAV_ITEMS,
    METRICS,
    CASE_STUDIES,
    IN_THE_ROOM_LABEL,
    IN_THE_ROOM_FEATURED,
    IN_THE_ROOM_SUPPORTING,
    AI_SECTION_LABEL,
    AI_SECTION_HEADLINE,
    AI_SECTION_COPY,
    AI_APPLICATIONS,
    AI_HUMAN_LABEL,
    AI_HUMAN_VALUE,
    SUPERPOWERS_LABEL,
    SUPERPOWERS_HEADING,
    SUPERPOWERS_SUBTITLE,
    SUPERPOWERS,
    PROCESS_SECTION_TITLE,
    PROCESS_SECTION_SUBTITLE,
    PROCESS_STEPS,
    EXPERIENCE,
    BEYOND_LABEL,
    BEYOND_HEADLINE,
    BEYOND_YOGA_LABEL,
    BEYOND_YOGA_COPY,
    BEYOND_YOGA_IMAGE,
    BEYOND_YOGA_ALT,
    BEYOND_HOME_LABEL,
    BEYOND_HOME_COPY,
    BEYOND_HOME_IMAGE,
    BEYOND_HOME_ALT,
    BEYOND_WEDDING_LABEL,
    BEYOND_WEDDING_COPY,
    BEYOND_WEDDING_IMAGE,
    BEYOND_WEDDING_ALT,
    CONTACT_HEADLINE,
    CONTACT_TEXT,
)
from components import (
    render_navigation,
    render_section_header,
    render_hero_left,
    render_hero_section,
    render_headshot_image,
    render_snapshot_panel,
    render_impact_grid,
    render_in_the_room,
    render_ai_section,
    render_beyond_the_work,
    render_superpowers_banner,
    render_case_card,
    render_case_detail,
    render_process_step,
    render_timeline_entry,
    render_contact,
)

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- LOAD CSS ----------
css_path = Path(__file__).parent / "styles.css"
if css_path.exists():
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

# ---------- GOOGLE FONTS ----------
st.markdown(
    """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

# ---------- NAVIGATION ----------
render_navigation(NAV_BRAND, NAV_ITEMS, RESUME_FILE, LINKEDIN)

# ---------- HERO SECTION ----------
from components import render_hero_section
render_hero_section(
    name=NAME,
    headline=HEADLINE,
    subheadline=SUBHEADLINE,
    snapshot=SNAPSHOT,
    headshot_path=HEADSHOT_PATH,
)

# Impact grid outside the hero columns so it can use st.columns for popovers
st.markdown('<div id="impact"></div>', unsafe_allow_html=True)
render_impact_grid(METRICS, CASE_STUDIES)

st.markdown('<hr style="border:none;border-top:1px solid #E5E7EB;margin:1.5rem 0;">', unsafe_allow_html=True)

# ---------- IN THE ROOM ----------
render_in_the_room(IN_THE_ROOM_LABEL, IN_THE_ROOM_FEATURED, IN_THE_ROOM_SUPPORTING)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ---------- AI SECTION ----------
render_ai_section(AI_SECTION_LABEL, AI_SECTION_HEADLINE, AI_SECTION_COPY, AI_APPLICATIONS, AI_HUMAN_LABEL, AI_HUMAN_VALUE)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ---------- EXPERIENCE ----------
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
render_section_header("EXPERIENCE", "Career Timeline", "Key roles and contributions.")

st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

for entry in EXPERIENCE:
    render_timeline_entry(entry)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ---------- ABOUT / BEYOND THE WORK ----------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
render_beyond_the_work(
    BEYOND_LABEL, BEYOND_HEADLINE,
    BEYOND_YOGA_LABEL, BEYOND_YOGA_COPY, BEYOND_YOGA_IMAGE, BEYOND_YOGA_ALT,
    BEYOND_HOME_LABEL, BEYOND_HOME_COPY, BEYOND_HOME_IMAGE, BEYOND_HOME_ALT,
    BEYOND_WEDDING_LABEL, BEYOND_WEDDING_COPY, BEYOND_WEDDING_IMAGE, BEYOND_WEDDING_ALT,
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# ---------- CONTACT ----------
render_contact(CONTACT_HEADLINE, CONTACT_TEXT, EMAIL, LINKEDIN, RESUME_FILE)

# ---------- FOOTER ----------
st.markdown(
    '<div class="footer">Built with precision · Powered by Streamlit</div>',
    unsafe_allow_html=True,
)
