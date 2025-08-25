
import streamlit as st
import json, random, os

APP_TITLE = "Milestone Quiz"

st.set_page_config(page_title=APP_TITLE, page_icon="🧠", layout="centered")
st.title(APP_TITLE)

DATA_FILE = "milestone_quiz_questions.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        QUESTIONS = json.load(f)
else:
    st.error(f"Could not find {DATA_FILE}. Place it next to this app and rerun.")
    st.stop()

def shuffle_array(array):
    arr = list(array)
    random.shuffle(arr)
    return arr

def filter_bank(tag):
    if tag == "all":
        return QUESTIONS
    return [q for q in QUESTIONS if tag in q.get("tags", [])]

if "filter" not in st.session_state:
    st.session_state.filter = "all"
if "questions" not in st.session_state:
    st.session_state.questions = shuffle_array(filter_bank(st.session_state.filter))
if "index" not in st.session_state:
    st.session_state.index = 0
if "selected" not in st.session_state:
    st.session_state.selected = None
if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "correct" not in st.session_state:
    st.session_state.correct = 0
if "attempted" not in st.session_state:
    st.session_state.attempted = 0
if "missed_ids" not in st.session_state:
    st.session_state.missed_ids = []

def restart(new_filter=None, use_missed=False):
    if use_missed:
        missed_set = set(st.session_state.missed_ids)
        bank = [q for q in QUESTIONS if q["id"] in missed_set]
        st.session_state.questions = shuffle_array(bank) if bank else shuffle_array(filter_bank(st.session_state.filter))
        st.session_state.missed_ids = []
    else:
        if new_filter is None:
            new_filter = st.session_state.filter
        st.session_state.filter = new_filter
        st.session_state.questions = shuffle_array(filter_bank(new_filter))
    st.session_state.index = 0
    st.session_state.selected = None
    st.session_state.revealed = False
    st.session_state.correct = 0
    st.session_state.attempted = 0

def choose(i):
    if st.session_state.revealed:
        return
    q = st.session_state.questions[st.session_state.index]
    st.session_state.selected = i
    is_correct = (i == q["answer_index"])
    st.session_state.revealed = True
    st.session_state.attempted += 1
    if is_correct:
        st.session_state.correct += 1
    else:
        st.session_state.missed_ids.append(q["id"])

def next_question():
    if st.session_state.index < len(st.session_state.questions) - 1:
        st.session_state.index += 1
        st.session_state.selected = None
        st.session_state.revealed = False

with st.sidebar:
    st.markdown("### 🎛️ Options")
    bank = st.selectbox("Question bank", ["all", "recall", "computation", "case", "gross", "fine", "language", "social", "growth", "reflex", "redflag"], index=0)
    colA, colB = st.columns(2)
    if colA.button("Restart", use_container_width=True):
        restart(new_filter=bank)
    if colB.button("Review missed", use_container_width=True):
        restart(use_missed=True)
    st.caption("Banks: filter by tag. Review missed builds a quiz from your incorrect answers.")

q_total = len(st.session_state.questions)
q_index = st.session_state.index
progress = 0 if q_total == 0 else int((q_index / q_total) * 100)
st.progress(progress)

if q_total == 0:
    st.info("No questions in this bank yet. Use Restart to reload all questions.")
else:
    q = st.session_state.questions[q_index]
    st.write(f"**Question {q_index + 1} of {q_total}**")
    st.markdown(f"#### {q['stem']}")

    if q.get("tags"):
        st.caption(" • ".join(q["tags"]))

    for i, choice in enumerate(q["choices"]):
        is_correct = (i == q["answer_index"])
        is_selected = (st.session_state.selected == i)
        label = f"{chr(65+i)}. {choice}"
        cols = st.columns([1,9])
        with cols[1]:
            if st.button(label, key=f"c_{q['id']}_{i}", use_container_width=True, disabled=st.session_state.revealed):
                choose(i)
        if st.session_state.revealed:
            with cols[0]:
                if is_selected and is_correct:
                    st.success("✔", icon="✅")
                elif is_selected and not is_correct:
                    st.error("✘", icon="❌")
                elif is_correct:
                    st.success("✔", icon="✅")

    if st.session_state.revealed:
        if st.session_state.selected == q["answer_index"]:
            st.success("Correct")
        else:
            st.error("Incorrect")
        st.markdown(f"**Explanation:** {q['rationale']}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Correct", st.session_state.correct)
        with col2:
            st.metric("Attempted", st.session_state.attempted)
        with col3:
            ratio = f"{st.session_state.correct}/{st.session_state.attempted}"
            st.metric("Ratio", ratio)

        if q_index < q_total - 1:
            st.button("Next question ➜", on_click=next_question, use_container_width=True)
        else:
            st.success("End of quiz.")
            colR1, colR2 = st.columns(2)
            with colR1:
                st.button("Review missed", on_click=lambda: restart(use_missed=True), use_container_width=True)
            with colR2:
                st.button("Restart all", on_click=lambda: restart(new_filter=st.session_state.filter), use_container_width=True)
    else:
        st.info("Click an answer to check it.")
