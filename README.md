# Macy Ziegler — Professional Portfolio

A modern, minimal professional portfolio built with Streamlit. Designed to help recruiters and hiring managers quickly understand your experience across analytics, operations, workforce strategy, and automation.

## Project Structure

```
├── app.py                  # Main Streamlit application (layout & rendering)
├── portfolio_content.py    # All editable content (text, metrics, links, case studies)
├── components.py           # Reusable rendering functions
├── styles.css              # Full visual styling
├── requirements.txt        # Python dependencies
├── .streamlit/config.toml  # Streamlit theme & server config
├── .gitignore
├── assets/
│   └── resume.pdf          # Place your resume here
├── Headshot.png            # Optional headshot (not used in current design)
└── README.md
```

## Local Setup

```bash
# 1. Navigate to the project
cd ~/Desktop/Personal\ Portfolio

# 2. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` (or the next available port).

## Editing Content

All content lives in `portfolio_content.py`. Update:
- Your name, headline, and links
- Impact metrics
- Case studies (title, summary, full detail)
- Process steps
- Experience timeline entries
- About text and interests
- Contact info

No need to touch `app.py` or `components.py` for content changes.

## Deploying to Streamlit Community Cloud (Free)

1. Push this folder to a GitHub repository (public or private)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **"New app"**
5. Select your repo, branch, and set main file to `app.py`
6. Click **"Deploy"**

Your portfolio will be live at `https://yourapp.streamlit.app` within ~2 minutes.

## Before Publishing Checklist

- [ ] Replace all `# TODO` placeholder content in `portfolio_content.py`
- [ ] Add your real email, LinkedIn URL
- [ ] Place your resume PDF in `assets/resume.pdf`
- [ ] Review case study text for confidentiality
- [ ] Remove or update the `Sample Mockup.png` and `Headshot.png` if not needed in production
- [ ] Test on mobile (resize browser or use device emulation)
