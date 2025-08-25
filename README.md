
# Milestone Quiz

100-item developmental milestones quiz with recall, computation, cases, red flags, reflexes, and drawing skills.
Styled like the website version. Runs entirely in Streamlit.

## Files
- `milestone_quiz_webstyle.py` — main app (entry file)
- `milestone_quiz_questions.json` — 100-item bank
- `requirements.txt` — dependencies

## Run locally
```bash
pip install -r requirements.txt
python -m streamlit run milestone_quiz_webstyle.py
```

## Deploy on Streamlit Community Cloud
1. Create a **public** GitHub repo and upload the three files to the repo root.
2. Go to https://streamlit.io/cloud → **New app**.
3. Set **Repository** to `your-username/your-repo`, **Branch** to `main` (or your default), and **Main file path** to `milestone_quiz_webstyle.py`.
4. Deploy and share the URL.
