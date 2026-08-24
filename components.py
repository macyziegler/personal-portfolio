"""
Reusable Portfolio Components
==============================
Rendering functions for metric cards, case studies, timeline entries, etc.
"""

import streamlit as st
from pathlib import Path


def render_navigation(brand, items, resume_file, linkedin_url=""):
    """Render the top navigation bar."""
    import base64
    from pathlib import Path

    # Create download link for resume
    resume_href = resume_file
    resume_path = Path(resume_file.replace("app/static/", "static/"))
    if not resume_path.exists():
        resume_path = Path("assets/resume.pdf")
    if resume_path.exists():
        b64 = base64.b64encode(resume_path.read_bytes()).decode()
        resume_href = f"data:application/pdf;base64,{b64}"

    nav_links = ""
    for item in items:
        if "résumé" in item.lower() or "resume" in item.lower():
            nav_links += f'<a href="{resume_href}" download="Macy_Ziegler_Resume.pdf" class="nav-btn">{item}</a>'
        elif "linkedin" in item.lower():
            nav_links += f'<a href="{linkedin_url}" target="_blank" rel="noopener noreferrer">{item}</a>'
        elif item.lower() == "work":
            nav_links += f'<a href="#impact">{item}</a>'
        else:
            section_id = item.lower().replace(" ", "-")
            nav_links += f'<a href="#{section_id}">{item}</a>'

    st.markdown(
        f"""
        <div class="nav-container">
            <div class="nav-brand">{brand}</div>
            <div class="nav-links">{nav_links}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_ai_section(label, headline, copy, applications, human_label, human_value):
    """Render the How I Work With AI editorial section."""

    # Build applications HTML (three columns)
    apps_html = ""
    for i, app in enumerate(applications):
        divider = '<div style="width:1px;background:#E5E7EB;align-self:stretch;"></div>' if i > 0 else ""
        subtitle_part = f' | {app["subtitle"]}' if app.get("subtitle") else ""
        apps_html += (
            f'{divider}'
            f'<div style="flex:1;padding:0 1.25rem;">'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.62rem;'
            f'font-weight:700;color:#2955D4;letter-spacing:0.05em;display:block;'
            f'margin-bottom:0.3rem;">{app["number"]} · {app["title"].upper()}{subtitle_part}</span>'
            f'<span style="font-size:0.85rem;color:#4A4A5A;line-height:1.55;display:block;">'
            f'{app["description"]}</span>'
            f'</div>'
        )

    # Process copy — replace double newline with a small-gap break
    copy_html = copy.replace("\n\n", '</span><span style="display:block;height:0.75rem;"></span><span style="font-size:0.92rem;color:#4A4A5A;line-height:1.7;display:block;">')

    html = (
        '<div style="background:#F8F9FB;border:1px solid #E5E7EB;border-radius:12px;'
        'padding:3rem;margin:0.5rem 0;">'

        # Top: Point of view
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:1rem;'
        f'font-weight:600;letter-spacing:0.15em;text-transform:uppercase;'
        f'color:#7A7A8A;display:block;margin-bottom:0.6rem;">{label}</span>'
        f'<span style="font-size:1.5rem;font-weight:700;color:#1A1A2E;'
        f'line-height:1.2;display:block;margin-bottom:1rem;">{headline}</span>'
        f'<span style="font-size:0.92rem;color:#4A4A5A;line-height:1.7;display:block;max-width:900px;">'
        f'{copy_html}</span>'

        # Divider
        '<div style="border-top:1px solid #E5E7EB;margin:1.75rem 0;"></div>'

        # Middle: Three columns
        f'<div style="display:flex;align-items:flex-start;">{apps_html}</div>'

        # Bottom: Human ownership
        '<div style="border-top:1px solid #E5E7EB;margin-top:1.75rem;padding-top:1rem;">'
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;'
        f'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
        f'color:#2955D4;margin-right:0.75rem;">{human_label}</span>'
        f'<span style="font-size:0.88rem;font-weight:500;color:#1A1A2E;">{human_value}</span>'
        '</div>'

        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def render_in_the_room(label, featured, supporting):
    """Render the 'In the Room' editorial section with navy featured panel."""

    # SVG icons for supporting items
    icons = {
        "system": (
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="16" y="16" width="6" height="6" rx="1"/>'
            '<rect x="2" y="16" width="6" height="6" rx="1"/>'
            '<rect x="9" y="2" width="6" height="6" rx="1"/>'
            '<path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/>'
            '<path d="M12 12V8"/></svg>'
        ),
        "story": (
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/>'
            '<path d="m7 21 5-5 5 5"/><path d="M7 11l3-3 2 2 4-4"/></svg>'
        ),
        "relationships": (
            '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>'
            '<circle cx="9" cy="7" r="4"/>'
            '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'
            '<path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
        ),
    }

    # Featured question icon
    question_icon = (
        '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>'
        '<path d="M12 8v4"/><path d="M12 16h.01"/></svg>'
    )

    # Build supporting items (light background style)
    supporting_html = ""
    for i, item in enumerate(supporting):
        border_top = 'border-top:1px solid #E5E7EB;padding-top:1rem;margin-top:1rem;' if i > 0 else ''
        icon_svg = icons.get(item["icon"], "")
        supporting_html += (
            f'<div style="{border_top}display:flex;gap:0.75rem;align-items:center;">'
            f'<div style="color:#2955D4;flex-shrink:0;">{icon_svg}</div>'
            f'<div>'
            f'<span style="font-size:0.82rem;font-weight:600;color:#1A1A2E;'
            f'text-transform:uppercase;letter-spacing:0.05em;display:block;margin-bottom:0.2rem;">'
            f'{item["title"]}</span>'
            f'<span style="font-size:0.85rem;color:#4A4A5A;line-height:1.55;display:block;">'
            f'{item["description"]}</span>'
            f'</div></div>'
        )

    headline = featured["headline"]

    html = (
        '<div style="background:#F8F9FB;border:1px solid #E5E7EB;border-radius:12px;'
        'padding:2.5rem 3rem;margin:0.5rem 0;">'
        # Label
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;'
        f'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
        f'color:#1A1A2E;display:block;margin-bottom:1.5rem;">{label}</span>'
        # Two-column grid
        '<div style="display:grid;grid-template-columns:42% 58%;gap:2.5rem;">'
        # Left: Featured (light with blue border)
        '<div style="border-left:3px solid #2955D4;padding-left:1.5rem;'
        'display:flex;flex-direction:column;justify-content:center;">'
        f'<div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.75rem;">'
        f'<div style="color:#2955D4;flex-shrink:0;">{question_icon}</div>'
        f'<span style="font-size:1.1rem;font-weight:700;color:#1A1A2E;'
        f'line-height:1.3;">{headline}</span>'
        f'</div>'
        f'<span style="font-size:0.88rem;color:#4A4A5A;line-height:1.6;display:block;">'
        f'{featured["description"]}</span>'
        '</div>'
        # Right: Supporting on light background
        f'<div style="display:flex;flex-direction:column;justify-content:center;">{supporting_html}</div>'
        '</div></div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def render_superpowers_banner(label, heading, subtitle, superpowers):
    """Render a full-width dark banner showcasing professional superpowers."""

    # Lucide-style SVG icons (consistent 1.5 stroke, 24x24 viewBox, displayed at 56px)
    icons = {
        "search": (
            '<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>'
            '<path d="M12 8v4"/><path d="M12 16h.01"/></svg>'
        ),
        "network": (
            '<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="16" y="16" width="6" height="6" rx="1"/>'
            '<rect x="2" y="16" width="6" height="6" rx="1"/>'
            '<rect x="9" y="2" width="6" height="6" rx="1"/>'
            '<path d="M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3"/>'
            '<path d="M12 12V8"/></svg>'
        ),
        "presentation": (
            '<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M2 3h20"/><path d="M21 3v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V3"/>'
            '<path d="m7 21 5-5 5 5"/><path d="M7 11l3-3 2 2 4-4"/></svg>'
        ),
        "handshake": (
            '<svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/>'
            '<circle cx="9" cy="7" r="4"/>'
            '<path d="M22 21v-2a4 4 0 0 0-3-3.87"/>'
            '<path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>'
        ),
    }

    # Build the four superpowers
    items_html = ""
    for i, sp in enumerate(superpowers):
        divider = '<div class="sp-divider"></div>' if i > 0 else ""
        icon_svg = icons.get(sp["icon"], "")
        items_html += (
            f'{divider}'
            f'<div class="sp-item">'
            f'<div class="sp-icon">{icon_svg}</div>'
            f'<h3 class="sp-title">{sp["title"]}</h3>'
            f'<p class="sp-desc">{sp["description"]}</p>'
            f'</div>'
        )

    st.markdown(
        f"""
        <div class="sp-banner">
            <h2 class="sp-heading">{heading}</h2>
            <div class="sp-grid">{items_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(label, heading, subheading=""):
    """Render a section header with mono label and heading."""
    sub_html = f'<p class="section-subheading">{subheading}</p>' if subheading else ""
    st.markdown(
        f"""
        <p class="section-label">{label}</p>
        <p class="section-heading">{heading}</p>
        {sub_html}
        """,
        unsafe_allow_html=True,
    )


def render_hero_section(name, headline, subheadline, snapshot, headshot_path):
    """Render the full hero as a centered, balanced HTML section."""
    import base64
    from pathlib import Path

    # Encode headshot as base64 for inline display
    img_path = Path(headshot_path)
    img_html = ""
    if img_path.exists():
        img_data = base64.b64encode(img_path.read_bytes()).decode()
        ext = img_path.suffix.lstrip(".")
        if ext == "jpg":
            ext = "jpeg"
        img_html = (
            f'<img src="data:image/{ext};base64,{img_data}" '
            f'alt="Professional headshot of {name}" '
            f'style="width:300px;height:300px;object-fit:cover;object-position:center 25%;'
            f'border-radius:16px;border:1px solid #E5E7EB;display:block;'
            f'box-shadow:0 2px 8px rgba(0,0,0,0.06);" />'
        )
    else:
        img_html = '<div class="hero-headshot-placeholder"></div>'

    # Position line
    position = snapshot.get("current", "") if snapshot else ""

    st.markdown(
        f"""
        <div class="hero-wrapper">
            <div class="hero-grid">
                <div class="hero-img-col">
                    {img_html}
                </div>
                <div class="hero-text-col">
                    <h1 class="hero-name">{name}</h1>
                    <p class="hero-positioning">{headline}</p>
                    <p class="hero-subheadline">{subheadline}</p>
                    <p class="hero-position">{position}</p>
                    <a href="#impact" class="hero-explore-link">Explore Career Highlights ↓</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero_left(name, tagline, headline, subheadline, snapshot=None):
    """Render the hero section with name, position, and supporting text."""
    # Position line from snapshot
    position_html = ""
    if snapshot and snapshot.get("current"):
        position_html = (
            f'<p style="font-size:1rem;font-weight:400;color:#4A4A5A;'
            f'margin-bottom:1.5rem;line-height:1.5;">{snapshot["current"]}</p>'
        )

    st.markdown(
        f"""
        <div class="hero-section" style="padding-top:0;">
            <h1 class="hero-name">{name}</h1>
            {position_html}
            <p class="hero-positioning">{headline}</p>
            <p class="hero-subheadline">{subheadline}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero_right(headshot_path, headshot_alt, snapshot, focus_areas):
    """Render the hero right column with headshot and professional snapshot."""
    # Check if headshot exists
    img_path = Path(headshot_path)
    has_headshot = img_path.exists()

    # Build snapshot rows
    snapshot_fields = [
        ("ROLE", snapshot.get("current_role", "")),
        ("ORGANIZATION", snapshot.get("organization", "")),
        ("EXPERIENCE", snapshot.get("experience", "")),
        ("EDUCATION", snapshot.get("education", "")),
        ("LOCATION", snapshot.get("location", "")),
    ]

    rows_html = ""
    for label, value in snapshot_fields:
        if value:
            rows_html += f"""
                <div class="snapshot-row">
                    <span class="snapshot-label">{label}</span>
                    <span class="snapshot-value">{value}</span>
                </div>
            """

    # Focus area tags
    focus_html = "".join(
        f'<span class="focus-tag">{area}</span>' for area in focus_areas
    )

    st.markdown(
        f"""
        <div class="profile-panel">
            <div class="headshot-container">
                {"<img src='app/static/headshot' alt='" + headshot_alt + "' class='headshot-img' />" if False else ""}
                <div class="headshot-placeholder" {"style='display:none;'" if has_headshot else ""}>
                    <span class="headshot-placeholder-text">HEADSHOT</span>
                </div>
            </div>
            <div class="snapshot-section">
                <p class="snapshot-header">PROFESSIONAL SNAPSHOT</p>
                {rows_html}
                <div class="focus-tags">
                    {focus_html}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Use Streamlit's native image display for the headshot (reliable across deployment)
    if has_headshot:
        # We'll render the image via Streamlit in the app.py caller
        pass


def render_headshot_image(headshot_path, headshot_alt):
    """Display the headshot using Streamlit's native image component."""
    img_path = Path(headshot_path)
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
    else:
        # Graceful placeholder
        st.markdown(
            """
            <div class="headshot-placeholder-box">
                <div class="headshot-placeholder-inner">
                    <span style="font-family:var(--font-mono);font-size:0.7rem;color:var(--text-muted);letter-spacing:0.1em;">
                        ADD HEADSHOT
                    </span>
                    <span style="font-size:0.75rem;color:var(--text-muted);margin-top:0.3rem;">
                        assets/headshot.jpg
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_snapshot_panel(snapshot):
    """Render the professional snapshot panel (below headshot)."""
    snapshot_fields = [
        ("CURRENT", snapshot.get("current", "")),
        ("EDUCATION", snapshot.get("education", "")),
        ("LOCATION", snapshot.get("location", "")),
    ]

    rows_html = ""
    for label, value in snapshot_fields:
        if value:
            rows_html += (
                '<div style="display:flex;flex-direction:column;padding:0.45rem 0;'
                'border-bottom:1px solid #E5E7EB;">'
                f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;'
                f'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
                f'color:#7A7A8A;margin-bottom:0.15rem;">{label}</span>'
                f'<span style="font-size:0.88rem;font-weight:500;color:#1A1A2E;'
                f'line-height:1.4;">{value}</span>'
                '</div>'
            )

    st.markdown(
        f"""
        <div style="background:#FFFFFF;border:1px solid #E5E7EB;border-radius:12px;
                    padding:1.2rem 1.4rem;margin-top:1rem;
                    box-shadow:0 1px 3px rgba(0,0,0,0.04);">
            <p style="font-family:'JetBrains Mono',monospace;font-size:0.65rem;
                      font-weight:600;letter-spacing:0.15em;text-transform:uppercase;
                      color:#7A7A8A;margin-bottom:0.8rem;padding-bottom:0.5rem;
                      border-bottom:1px solid #E5E7EB;">PROFESSIONAL SNAPSHOT</p>
            {rows_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_data_visual():
    """Render the compact data-to-insight visual (used as transition or in How I Work)."""
    st.markdown(
        """
        <div class="data-visual-compact">
            <div class="visual-flow">
                <span class="visual-node">◆ Data Sources</span>
                <span class="visual-connector"></span>
                <span class="visual-node visual-node-active">⚙ Processing</span>
                <span class="visual-connector"></span>
                <span class="visual-node">◈ Insights</span>
            </div>
            <div class="visual-chart-compact">
                <svg width="100%" height="48" viewBox="0 0 300 48" preserveAspectRatio="none">
                    <line x1="0" y1="16" x2="300" y2="16" stroke="#E5E7EB" stroke-width="0.5"/>
                    <line x1="0" y1="32" x2="300" y2="32" stroke="#E5E7EB" stroke-width="0.5"/>
                    <polyline points="10,40 50,34 90,36 130,26 170,22 210,14 250,10 290,6"
                              fill="none" stroke="#2955D4" stroke-width="1.5" stroke-linecap="round"/>
                    <circle cx="130" cy="26" r="2.5" fill="#2955D4" opacity="0.6"/>
                    <circle cx="210" cy="14" r="2.5" fill="#2955D4" opacity="0.6"/>
                    <circle cx="290" cy="6" r="2.5" fill="#2955D4"/>
                </svg>
            </div>
            <div class="visual-endpoints">
                <span>COMPLEXITY</span>
                <span>CLARITY</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_impact_grid(metrics, case_studies=None):
    """Render a 2x2 impact grid using native Streamlit containers with buttons inside."""

    # Header
    st.markdown(
        '<p style="font-family:\'JetBrains Mono\',monospace;font-size:0.62rem;'
        'font-weight:600;letter-spacing:0.15em;text-transform:uppercase;'
        'color:#7A7A8A;margin-bottom:0.75rem;margin-top:0;">CAREER HIGHLIGHTS</p>',
        unsafe_allow_html=True,
    )

    def _render_card(m, col_key):
        """Render a single impact card inside a bordered container."""
        with st.container(border=True):
            # Behind the metric section
            behind_html = ""
            if m.get("behind_metric"):
                behind_html = (
                    '<div style="border-top:1px solid #E5E7EB;margin-top:0.6rem;padding-top:0.6rem;">'
                    '<div style="font-family:\'JetBrains Mono\',monospace;font-size:0.55rem;'
                    'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
                    'color:#2955D4;margin-bottom:0.2rem;">BEHIND THE METRIC</div>'
                    f'<div style="font-size:0.8rem;color:#1A1A2E;line-height:1.5;">'
                    f'{m["behind_metric"]}</div>'
                    '</div>'
                )

            st.markdown(
                f'<span style="font-size:1.8rem;font-weight:700;color:#2955D4;'
                f'line-height:1.2;display:block;margin-bottom:0.1rem;">{m["value"]}</span>'
                f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;'
                f'font-weight:600;letter-spacing:0.08em;text-transform:uppercase;'
                f'color:#7A7A8A;display:block;margin-bottom:0.3rem;">{m["label"]}</span>'
                f'<span style="font-size:0.82rem;color:#4A4A5A;line-height:1.5;display:block;">'
                f'{m.get("description", "")}</span>'
                f'{behind_html}',
                unsafe_allow_html=True,
            )

            # Case study button inside the card
            cs_idx = m.get("case_study_index")
            if cs_idx is not None and case_studies:
                st.button(
                    "Learn more →",
                    key=f"impact_case_{col_key}",
                    on_click=_open_case_study,
                    args=(cs_idx,),
                )

    # Row 1
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        _render_card(metrics[0], "labor")
    with col2:
        _render_card(metrics[1], "shrink")

    # Row 2
    col3, col4 = st.columns(2, gap="medium")
    with col3:
        _render_card(metrics[2], "mobile")
    with col4:
        _render_card(metrics[3], "llm")

    # Render expanded case study if one is active
    active_cs = st.session_state.get("active_case_study")
    if active_cs is not None and case_studies and active_cs < len(case_studies):
        cs = case_studies[active_cs]
        st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)
        render_case_detail(cs["detail"], detail_type=cs.get("detail_type"))
        if st.button("← Close", key="close_impact_case"):
            st.session_state.active_case_study = None


def _open_case_study(cs_idx):
    """Callback to open a case study from an impact card."""
    st.session_state.active_case_study = cs_idx


def render_hero_cta(linkedin_url, resume_file):
    """Render the hero CTA buttons and LinkedIn link in one row."""
    st.markdown(
        f"""
        <div style="margin-top:1.5rem;">
            <div class="hero-cta">
                <a href="#work" class="btn-primary">View Selected Work</a>
                <a href="{resume_file}" target="_blank" class="btn-secondary">Download Résumé</a>
                <a href="{linkedin_url}" target="_blank" rel="noopener noreferrer" class="hero-linkedin-link">LinkedIn →</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_case_card(case, index):
    """Render a case study card."""
    skills_html = "".join(
        f'<span class="skill-tag">{s}</span>' for s in case["skills"]
    )
    st.markdown(
        f"""
        <div class="case-card">
            <div class="case-category">{case["category"]}</div>
            <div class="case-title">{case["title"]}</div>
            <div class="case-summary">{case["summary"]}</div>
            <div class="case-skills">{skills_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_case_detail(detail, detail_type=None):
    """Render the expanded case study detail. Handles both simple and rich formats."""

    # Rich document format for specific case studies
    if detail_type in ("mobile_reporting", "shrink_reporting", "labor_optimization", "llm_evaluation"):
        _render_rich_case_detail(detail, detail_type)
        return

    # Simple format for other case studies
    fields = [
        ("Context", detail.get("context", "")),
        ("Challenge", detail.get("challenge", "")),
        ("My Role", detail.get("role", "")),
        ("Approach", detail.get("approach", "")),
        ("Solution", detail.get("solution", "")),
        ("Outcome", detail.get("outcome", "")),
        ("Key Takeaway", detail.get("takeaway", "")),
    ]
    tools = detail.get("tools", [])

    html = '<div class="case-detail">'
    for label, text in fields:
        if text:
            html += f'<div class="case-detail-label">{label}</div>'
            html += f'<div class="case-detail-text">{text.replace(chr(10), "<br>")}</div>'

    if tools:
        html += '<div class="case-detail-label">Tools Used</div>'
        html += f'<div class="case-detail-text">{" · ".join(tools)}</div>'

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def _render_rich_case_detail(detail, detail_type):
    """Render a case study as a contained document-style brief."""

    # Determine case study label
    cs_labels = {
        "mobile_reporting": "IMPACT HIGHLIGHT 01 · MOBILE ANALYTICS",
        "shrink_reporting": "IMPACT HIGHLIGHT 02 · DATA ENGINEERING",
        "labor_optimization": "IMPACT HIGHLIGHT 03 · OPERATIONS ANALYTICS",
        "llm_evaluation": "IMPACT HIGHLIGHT 04 · AI EVALUATION",
    }
    cs_titles = {
        "mobile_reporting": "Mobile Operational Reporting Platform",
        "shrink_reporting": "Inventory Shrink Visibility &amp; Reporting Automation",
        "labor_optimization": "Floor-Replenishment Labor Optimization",
        "llm_evaluation": "Automated LLM Evaluation Framework",
    }
    eyebrow = cs_labels.get(detail_type, "CASE STUDY")
    title = cs_titles.get(detail_type, "")

    # Split challenge and solution
    challenge = detail.get("challenge", "")
    solution = detail.get("solution", "")
    challenge_main = challenge.split("\n\n")[0] if challenge else ""
    solution_main = solution.split("\n\n")[0] if solution else ""

    # At a Glance
    glance = detail.get("at_a_glance", {})
    glance_html = ""
    for i, (label, value) in enumerate(glance.items()):
        divider = '<div style="width:1px;background:#E5E7EB;align-self:stretch;"></div>' if i > 0 else ""
        glance_html += (
            f'{divider}'
            f'<div style="flex:1;display:flex;flex-direction:column;padding:0 1.1rem;">'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.62rem;'
            f'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
            f'color:#7A7A8A;margin-bottom:0.15rem;">{label}</span>'
            f'<span style="font-size:0.92rem;font-weight:500;color:#1A1A2E;'
            f'line-height:1.3;">{value}</span>'
            f'</div>'
        )

    # Delivery steps
    delivery = detail.get("delivery", [])
    delivery_labels = detail.get("delivery_labels", ["Discover", "Build", "Validate", "Launch"])
    steps_html = ""
    for i, item in enumerate(delivery):
        lbl = delivery_labels[i] if i < len(delivery_labels) else f"Step {i+1}"
        steps_html += (
            f'<div style="display:flex;flex-direction:column;gap:0.2rem;">'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.58rem;'
            f'font-weight:600;letter-spacing:0.08em;text-transform:uppercase;'
            f'color:#7A7A8A;">0{i+1} · {lbl}</span>'
            f'<span style="font-size:0.9rem;color:#4A4A5A;line-height:1.6;">{item}</span>'
            f'</div>'
        )

    # Spacing constants (as inline values)
    # section_gap = 2.75rem (between major sections, including rule)
    # rule margin = 1.25rem top + 1.25rem bottom = consistent
    # label-to-content = 0.5rem
    # doc padding = 3.25rem on desktop

    # Single HTML block
    html = (
        # Outer background + sheet
        '<div style="background:#F0F2F5;padding:1.75rem 1.5rem;border-radius:12px;margin:1rem 0;">'
        '<div style="max-width:1050px;margin:0 auto;background:#FFFFFF;'
        'border:1px solid #E5E7EB;border-radius:10px;'
        'box-shadow:0 4px 20px rgba(0,0,0,0.06);padding:3.25rem;">'

        # Header
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.68rem;'
        'font-weight:600;letter-spacing:0.15em;text-transform:uppercase;'
        'color:#2955D4;display:block;margin-bottom:0.5rem;">'
        f'{eyebrow}</span>'
        f'<p style="font-size:2.1rem;font-weight:700;color:#1A1A2E;line-height:1.15;'
        f'margin-bottom:0.4rem;">{title}</p>'
        f'<p style="font-size:1.05rem;color:#4A4A5A;line-height:1.6;max-width:540px;'
        f'margin-bottom:0;">'
        f'{detail["headline"]}</p>'

        # Skill tags
        + (
            '<div style="display:flex;flex-wrap:wrap;gap:0.35rem;margin-top:0.75rem;">'
            + "".join(
                f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.6rem;'
                f'letter-spacing:0.05em;text-transform:uppercase;background:#E8EDFB;'
                f'color:#2955D4;padding:0.2rem 0.5rem;border-radius:4px;font-weight:500;">'
                f'{skill}</span>'
                for skill in detail.get("skills", [])
            )
            + '</div>'
            if detail.get("skills") else ''
        ) +

        # Rule
        '<div style="border-top:1px solid #E5E7EB;margin:1.25rem 0;"></div>'

        # Snapshot
        f'<div style="display:flex;align-items:stretch;">{glance_html}</div>'

        # Rule
        '<div style="border-top:1px solid #E5E7EB;margin:1.25rem 0 1.75rem 0;"></div>'

        # Two-column story
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;">'

        # Challenge column
        '<div>'
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.68rem;'
        'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
        'color:#2955D4;display:block;margin-bottom:0.5rem;">THE CHALLENGE</span>'
        f'<p style="font-size:0.95rem;color:#4A4A5A;line-height:1.7;margin:0;">'
        f'{challenge_main}</p>'
        '</div>'

        # Solution column
        '<div>'
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.68rem;'
        'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
        'color:#2955D4;display:block;margin-bottom:0.5rem;">WHAT I BUILT</span>'
        f'<p style="font-size:0.95rem;color:#4A4A5A;line-height:1.7;margin-bottom:0.75rem;">'
        f'{solution_main}</p>'
        + (
            '<p style="font-size:0.9rem;color:#4A4A5A;line-height:1.6;margin:0;">'
            '<span style="font-weight:600;color:#2955D4;">Dynamic KPI targeting:</span> '
            'Generated relevant performance targets using hour-of-day patterns, '
            'day-of-week effects, and fiscal-week trends.</p>'
            if detail_type == "mobile_reporting" else ''
        ) +
        '</div>'

        '</div>'  # close grid

        # Rule + Delivery
        '<div style="border-top:1px solid #E5E7EB;margin:1.75rem 0 1.25rem 0;"></div>'
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.68rem;'
        'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
        'color:#2955D4;display:block;margin-bottom:0.5rem;">HOW I DELIVERED IT</span>'
        f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem 2.5rem;">'
        f'{steps_html}</div>'

        # Rule + Outcome
        '<div style="border-top:1px solid #E5E7EB;margin:1.75rem 0 1.25rem 0;"></div>'
        '<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.68rem;'
        'font-weight:600;letter-spacing:0.12em;text-transform:uppercase;'
        'color:#2955D4;display:block;margin-bottom:0.5rem;">OUTCOME</span>'
        f'<p style="font-size:1.05rem;color:#1A1A2E;line-height:1.6;margin:0;'
        f'border-left:2px solid #2955D4;padding-left:1rem;">'
        f'{detail.get("outcome", "").replace(chr(10), "<br>")}</p>'

        # Close sheet + background
        '</div></div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def render_process_step(step, title, description):
    """Render a single process step card."""
    st.markdown(
        f"""
        <div class="process-step">
            <div class="process-number">STEP {step}</div>
            <div class="process-title">{title}</div>
            <div class="process-desc">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_timeline_entry(entry):
    """Render a single timeline entry."""
    achievements_html = ""
    if entry.get("achievements"):
        items = "".join(f"<li>{a}</li>" for a in entry["achievements"])
        achievements_html = f'<ul class="timeline-achievements">{items}</ul>'

    caps_html = ""
    if entry.get("capabilities"):
        tags = "".join(
            f'<span class="skill-tag">{c}</span>' for c in entry["capabilities"]
        )
        caps_html = f'<div class="timeline-caps">{tags}</div>'

    st.markdown(
        f"""
        <div class="timeline-entry">
            <div class="timeline-dates">{entry["dates"]}</div>
            <div class="timeline-title">{entry["title"]}</div>
            <div class="timeline-org">{entry["organization"]}</div>
            <div class="timeline-desc">{entry["description"]}</div>
            {achievements_html}
            {caps_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_beyond_the_work(label, headline, yoga_label, yoga_copy, yoga_image, yoga_alt,
                           home_label, home_copy, home_image, home_alt,
                           wedding_label="", wedding_copy="", wedding_image="", wedding_alt=""):
    """Render the Beyond the Work personal section."""
    import base64
    from pathlib import Path

    def _img_html(img_path, alt_text, placeholder_label):
        """Return image HTML or a graceful placeholder."""
        p = Path(img_path)
        if p.exists():
            b64 = base64.b64encode(p.read_bytes()).decode()
            ext = p.suffix.lstrip(".")
            if ext == "jpg":
                ext = "jpeg"
            return (
                f'<img src="data:image/{ext};base64,{b64}" alt="{alt_text}" '
                f'style="width:100%;height:100%;object-fit:cover;border-radius:10px;'
                f'border:1px solid #E5E7EB;display:block;" />'
            )
        else:
            return (
                f'<div style="background:#F0F2F5;border:1px dashed #D0D3DA;'
                f'border-radius:10px;padding:3rem 1.5rem;text-align:center;height:100%;">'
                f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.65rem;'
                f'color:#7A7A8A;letter-spacing:0.1em;text-transform:uppercase;">'
                f'{placeholder_label}</span></div>'
            )

    yoga_img = _img_html(yoga_image, yoga_alt, "YOGA PHOTO")
    home_img = _img_html(home_image, home_alt, "MILES & BARKLEY")
    wedding_img = _img_html(wedding_image, wedding_alt, "WEDDING PHOTO") if wedding_image else ""

    # Third panel HTML
    wedding_panel = ""
    if wedding_label and wedding_copy:
        wedding_panel = (
            '<div>'
            f'<div style="height:550px;overflow:hidden;border-radius:10px;margin-bottom:1rem;">{wedding_img}</div>'
            f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;'
            f'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
            f'color:#2955D4;display:block;margin-bottom:0.4rem;">{wedding_label}</span>'
            f'<span style="font-size:0.92rem;color:#4A4A5A;line-height:1.65;display:block;">'
            f'{wedding_copy}</span>'
            '</div>'
        )

    grid_cols = "1fr 1fr 1fr" if wedding_panel else "1fr 1fr"

    html = (
        '<div>'
        # Header
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.65rem;'
        f'font-weight:600;letter-spacing:0.15em;text-transform:uppercase;'
        f'color:#7A7A8A;display:block;margin-bottom:0.5rem;">{label}</span>'
        f'<span style="font-size:1.5rem;font-weight:700;color:#1A1A2E;'
        f'line-height:1.2;display:block;margin-bottom:1.5rem;">{headline}</span>'
        # Panels
        f'<div style="display:grid;grid-template-columns:{grid_cols};gap:2rem;">'
        # Yoga panel
        '<div>'
        f'<div style="height:550px;overflow:hidden;border-radius:10px;margin-bottom:1rem;">{yoga_img}</div>'
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;'
        f'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
        f'color:#2955D4;display:block;margin-bottom:0.4rem;">{yoga_label}</span>'
        f'<span style="font-size:0.92rem;color:#4A4A5A;line-height:1.65;display:block;">'
        f'{yoga_copy}</span>'
        '</div>'
        # Dogs panel
        '<div>'
        f'<div style="height:550px;overflow:hidden;border-radius:10px;margin-bottom:1rem;">{home_img}</div>'
        f'<span style="font-family:\'JetBrains Mono\',monospace;font-size:0.85rem;'
        f'font-weight:600;letter-spacing:0.1em;text-transform:uppercase;'
        f'color:#2955D4;display:block;margin-bottom:0.4rem;">{home_label}</span>'
        f'<span style="font-size:0.92rem;color:#4A4A5A;line-height:1.65;display:block;">'
        f'{home_copy}</span>'
        '</div>'
        # Wedding panel (if present)
        f'{wedding_panel}'
        '</div>'
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


def render_contact(headline, text, email, linkedin, resume_file):
    """Render the contact section."""
    import base64
    from pathlib import Path

    # Create download link for resume
    resume_href = resume_file
    resume_path = Path(resume_file.replace("app/static/", "static/"))
    if not resume_path.exists():
        resume_path = Path("assets/resume.pdf")
    if resume_path.exists():
        b64 = base64.b64encode(resume_path.read_bytes()).decode()
        resume_href = f"data:application/pdf;base64,{b64}"

    st.markdown(
        f"""
        <div class="contact-section">
            <div class="contact-heading">{headline}</div>
            <div class="contact-text">{text}</div>
            <div class="contact-links">
                <a href="mailto:{email}" class="btn-secondary">Email Me</a>
                <a href="{linkedin}" target="_blank" class="btn-secondary">LinkedIn</a>
                <a href="{resume_href}" download="Macy_Ziegler_Resume.pdf" class="btn-secondary">Download Resume</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
