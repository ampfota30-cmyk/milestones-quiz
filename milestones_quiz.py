
import streamlit as st
import random

st.set_page_config(page_title="Developmental Milestones — Board‑Style Quiz", page_icon="🧠", layout="centered")

# ----------------------------
# Question bank (from user's module)
# ----------------------------

QUESTIONS = [
    # --- Core recall items (kept and refined) ---
    {
        "id": 1,
        "stem": "At what age should an infant typically SIT WITHOUT SUPPORT (average age of attainment in this module)?",
        "choices": ["4 months", "6 months", "9 months", "12 months"],
        "answer_index": 1,
        "rationale": "Sits without support at ~6 months (gross motor table). By CDC, should be present by ~9 months.",
        "tags": ["recall", "gross"],
    },
    {
        "id": 2,
        "stem": "Average age to TRANSFER an object hand‑to‑hand?",
        "choices": ["4 months", "5.5 months", "7 months", "9 months"],
        "answer_index": 1,
        "rationale": "Transfers at ~5.5 months (fine motor table).",
        "tags": ["recall", "fine"],
    },
    {
        "id": 3,
        "stem": "Age for THUMB–FINGER (pincer) grasp (as defined in the module)?",
        "choices": ["6 months", "8 months", "10 months", "12 months"],
        "answer_index": 1,
        "rationale": "Thumb–finger (pincer) grasp at ~8 months (fine motor table).",
        "tags": ["recall", "fine"],
    },
    {
        "id": 4,
        "stem": "Average age of FIRST REAL WORD (expressive language)?",
        "choices": ["9 months", "12 months", "15 months", "18 months"],
        "answer_index": 1,
        "rationale": "First real word around 12 months (language table).",
        "tags": ["recall", "language"],
    },
    {
        "id": 5,
        "stem": "According to this module, the average age for TWO‑WORD sentences is:",
        "choices": ["15 months", "19 months", "24 months", "30 months"],
        "answer_index": 1,
        "rationale": "Two‑word sentences ~19 months in table (though many 2‑year‑olds use 2‑word phrases).",
        "tags": ["recall", "language"],
    },
    {
        "id": 6,
        "stem": "Object permanence (uncovering a hidden toy) typically emerges at:",
        "choices": ["4 months", "6 months", "8 months", "12 months"],
        "answer_index": 2,
        "rationale": "Uncovers a hidden toy ~8 months (cognitive table).",
        "tags": ["recall", "cognitive"],
    },
    {
        "id": 7,
        "stem": "Which gross motor skill is expected at 3 YEARS?",
        "choices": ["Hop on one foot", "Ride a tricycle", "Skip", "Broad jump"],
        "answer_index": 1,
        "rationale": "Rides a tricycle at ~3 years; hop ~4 years; skip ~5 years.",
        "tags": ["recall", "gross"],
    },
    {
        "id": 8,
        "stem": "A 4‑year‑old should be able to:",
        "choices": [
            "Ride a bicycle without training wheels",
            "Hop on one foot",
            "Skip",
            "Stand on tiptoe for 30 seconds",
        ],
        "answer_index": 1,
        "rationale": "Hop ~4 years; skipping ~5 years.",
        "tags": ["recall", "gross"],
    },
    {
        "id": 9,
        "stem": "Which shape should a 4‑year‑old typically draw?",
        "choices": ["Circle", "Cross", "Square", "Triangle"],
        "answer_index": 1,
        "rationale": "Circle ~3 y; Cross ~3.5–4 y; Square ~4–4.5 y; Triangle ~5 y.",
        "tags": ["recall", "fine"],
    },
    {
        "id": 10,
        "stem": "Bedwetting (nocturnal enuresis) is considered physiologic/normal up to what age in BOYS?",
        "choices": ["3 years", "4 years", "5 years", "6 years"],
        "answer_index": 2,
        "rationale": "Physiologic up to ~5 y in boys (4 y in girls).",
        "tags": ["recall", "social"],
    },
    {
        "id": 11,
        "stem": "Which of the following is a CDC RED FLAG at 9 months?",
        "choices": [
            "Stranger anxiety persists",
            "Inability to sit without support",
            "Says 'mama' & 'dada' specifically",
            "Bangs two objects together",
        ],
        "answer_index": 1,
        "rationale": "Inability to sit at 9 months is a red flag; others can be normal skills.",
        "tags": ["recall", "growth"],
    },
    {
        "id": 12,
        "stem": "Which primitive reflex PERSISTS throughout life?",
        "choices": ["Moro", "Rooting", "Parachute", "Asymmetric tonic neck"],
        "answer_index": 2,
        "rationale": "Parachute appears ~7–8 months and persists; others extinguish in infancy.",
        "tags": ["recall", "reflex"],
    },
    {
        "id": 13,
        "stem": "Speech intelligibility to an unfamiliar listener at AGE 3 is approximately:",
        "choices": ["25%", "50%", "75%", "100%"],
        "answer_index": 2,
        "rationale": "Rule of thumb: 1y~25%, 2y~50%, 3y~75%, 4y~100%.",
        "tags": ["recall", "language"],
    },
    {
        "id": 14,
        "stem": "Stranger anxiety typically begins around:",
        "choices": ["2–3 months", "4–5 months", "6–8 months", "10–12 months"],
        "answer_index": 2,
        "rationale": "Emerges ~6–8 months.",
        "tags": ["recall", "social"],
    },
    {
        "id": 15,
        "stem": "Which is the BEST red flag at 2 years warranting evaluation?",
        "choices": [
            "Uses more than one gesture (e.g., blows kiss)",
            "Kicks a ball and runs",
            "Lack of two‑word meaningful phrases",
            "Plays with more than one toy at a time",
        ],
        "answer_index": 2,
        "rationale": "Lack of two‑word meaningful phrases at 2 y is concerning.",
        "tags": ["recall", "language"],
    },
    # --- New recall items ---
    {
        "id": 16,
        "stem": "Typical age for INDEPENDENT WALKING (average in module)?",
        "choices": ["10 months", "12 months", "15 months", "18 months"],
        "answer_index": 1,
        "rationale": "Walks alone around 12 months (gross motor).",
        "tags": ["recall", "gross"],
    },
    {
        "id": 17,
        "stem": "Most 5‑year‑olds can:",
        "choices": ["Skip", "Hop on one foot", "Ride a tricycle", "Broad jump"],
        "answer_index": 0,
        "rationale": "Skipping ~5 y; hopping ~4 y; tricycle ~3 y.",
        "tags": ["recall", "gross"],
    },
    {
        "id": 18,
        "stem": "A 3‑year‑old should be able to copy a:",
        "choices": ["Triangle", "Cross", "Circle", "Square"],
        "answer_index": 2,
        "rationale": "Copies circle ~3 y; cross ~3.5–4 y; square ~4–4.5 y; triangle ~5 y.",
        "tags": ["recall", "fine"],
    },
    {
        "id": 19,
        "stem": "Parallel play is characteristic of about what age?",
        "choices": ["12 months", "18 months", "2–3 years", "4–5 years"],
        "answer_index": 2,
        "rationale": "Parallel play ~2–3 years; cooperative play later.",
        "tags": ["recall", "social"],
    },
    {
        "id": 20,
        "stem": "What percent of speech is typically intelligible at age 2?",
        "choices": ["25%", "50%", "75%", "100%"],
        "answer_index": 1,
        "rationale": "~50% at 2 years (rule of thumb).",
        "tags": ["recall", "language"],
    },
    {
        "id": 21,
        "stem": "Red flag at 18 months:",
        "choices": [
            "Does not point to show interest",
            "Throws ball overhead",
            "Walks up steps with hand held",
            "Scribbles spontaneously",
        ],
        "answer_index": 0,
        "rationale": "Lack of pointing/gestures to share interest at 18 mo is concerning.",
        "tags": ["recall", "social"],
    },
    {
        "id": 22,
        "stem": "By ~4 years, most children can draw a:",
        "choices": ["Triangle", "Square", "Diamond", "Pentagon"],
        "answer_index": 1,
        "rationale": "Square ~4–4.5 y; triangle ~5 y.",
        "tags": ["recall", "fine"],
    },
    # --- Computation-style growth items ---
    {
        "id": 23,
        "stem": "A term newborn weighs 3.2 kg at birth. Assuming typical growth, the EXPECTED weight at ~12 months is:",
        "choices": ["6.4 kg", "8.0 kg", "9.6 kg", "12.8 kg"],
        "answer_index": 2,
        "rationale": "Birth weight roughly TRIPLES by ~12 months (3.2 × 3 ≈ 9.6 kg).",
        "tags": ["computation", "growth"],
    },
    {
        "id": 24,
        "stem": "A term newborn’s length is 50 cm. Expected length at ~12 months is closest to:",
        "choices": ["60 cm", "70 cm", "75 cm", "100 cm"],
        "answer_index": 2,
        "rationale": "Length increases ~50% by 12 months (≈75 cm from 50 cm).",
        "tags": ["computation", "growth"],
    },
    {
        "id": 25,
        "stem": "A child’s birth length was 50 cm. At ~4 years, expected length is approximately:",
        "choices": ["70 cm", "90 cm", "100 cm", "120 cm"],
        "answer_index": 2,
        "rationale": "Length roughly DOUBLES by ~4 years (≈100 cm).",
        "tags": ["computation", "growth"],
    },
    {
        "id": 26,
        "stem": "An infant was born at 32 weeks’ gestation. At a chronological age of 6 months, the corrected developmental age is:",
        "choices": ["3 months", "4 months", "5 months", "6 months"],
        "answer_index": 1,
        "rationale": "32 weeks is ~8 weeks early. Corrected age = chronological − 8 weeks ⇒ 6 mo − 2 mo = 4 months.",
        "tags": ["computation", "growth", "gross"],
    },
    {
        "id": 27,
        "stem": "A late‑preterm infant (born at 35 weeks) is now 10 months old. The corrected age is closest to:",
        "choices": ["8 months", "8.5 months", "9 months", "10 months"],
        "answer_index": 2,
        "rationale": "Born ~5 weeks early (~1.25 mo). 10 − 1.25 ≈ 8.75 → best answer 9 months.",
        "tags": ["computation", "growth"],
    },
    {
        "id": 28,
        "stem": "A term infant weighed 3.4 kg at birth. At the 4‑month visit, which weight BEST reflects normal growth?",
        "choices": ["4.5 kg", "5.8 kg", "6.8 kg", "8.5 kg"],
        "answer_index": 2,
        "rationale": "Birth weight roughly DOUBLES by ~4–5 months: 3.4 × 2 ≈ 6.8 kg.",
        "tags": ["computation", "growth"],
    },
    # --- Case vignettes / problem‑solving ---
    {
        "id": 29,
        "stem": "A 9‑month‑old pulls to stand, cruises, and bangs two cubes together but cannot sit unsupported. Which is the BEST interpretation?",
        "choices": [
            "Normal variation",
            "Likely fine motor delay",
            "Gross motor delay — evaluate",
            "Isolated language delay",
        ],
        "answer_index": 2,
        "rationale": "Inability to sit unsupported at 9 mo is a red flag, even if other skills are present.",
        "tags": ["case", "gross"],
    },
    {
        "id": 30,
        "stem": "A 15‑month‑old says 3 words, points to show interest, and follows one‑step commands. She cannot stack 6 cubes. Next best step?",
        "choices": [
            "Reassure and re‑screen at 18 months",
            "Refer to speech therapy",
            "Urgent neuro evaluation",
            "Order brain MRI",
        ],
        "answer_index": 0,
        "rationale": "Language/social appropriate for 15 mo; 6‑cube tower is typically older. Reassess at 18 mo.",
        "tags": ["case", "fine", "language"],
    },
    {
        "id": 31,
        "stem": "A 2‑year‑old has ~10 single words and does not combine words. Hearing screen was never done. BEST next step?",
        "choices": [
            "Wait 6 months and recheck",
            "Immediate hearing evaluation and early intervention referral",
            "MRI brain",
            "Start stimulant medication",
        ],
        "answer_index": 1,
        "rationale": "Language delay → rule out hearing loss and involve early intervention.",
        "tags": ["case", "language"],
    },
    {
        "id": 32,
        "stem": "A 4‑year‑old is 100% intelligible to strangers and can hop on one foot but cannot skip. Interpretation?",
        "choices": [
            "Normal for age",
            "Global developmental delay",
            "Specific language disorder",
            "Fine motor delay",
        ],
        "answer_index": 0,
        "rationale": "Skipping is a ~5‑year skill; hopping at 4 y is appropriate.",
        "tags": ["case", "gross", "language"],
    },
    {
        "id": 33,
        "stem": "A 6‑month‑old (corrected age) does not roll or sit with support. BEST interpretation?",
        "choices": [
            "Likely normal",
            "Possible gross motor delay — evaluate",
            "Speech‑only delay",
            "Autism spectrum disorder",
        ],
        "answer_index": 1,
        "rationale": "At ~6 months corrected, rolling/sitting with support are expected; absence warrants evaluation.",
        "tags": ["case", "gross"],
    },
    {
        "id": 34,
        "stem": "A 18‑month‑old does not point, lacks pretend play, and has no words. Which is MOST concerning today?",
        "choices": [
            "No words",
            "No pointing/gestures to share interest",
            "Still in parallel play",
            "Not toilet trained",
        ],
        "answer_index": 1,
        "rationale": "Lack of joint attention gestures is a stronger red flag at 18 mo.",
        "tags": ["case", "social", "language"],
    },
    {
        "id": 35,
        "stem": "A 5‑year‑old cannot draw a triangle. Otherwise normal exam and development. Next step?",
        "choices": [
            "Reassure and monitor",
            "Refer to neurology",
            "Order EEG",
            "Start occupational therapy immediately",
        ],
        "answer_index": 0,
        "rationale": "Triangle often emerges around ~5 years; mild variation without other concerns can be monitored.",
        "tags": ["case", "fine"],
    },
    # --- Reflexes & screening ---
    {
        "id": 36,
        "stem": "Moro reflex typically disappears by:",
        "choices": ["2 months", "4 months", "6 months", "9 months"],
        "answer_index": 2,
        "rationale": "Moro fades by ~5–6 months.",
        "tags": ["recall", "reflex"],
    },
    {
        "id": 37,
        "stem": "Asymmetric tonic neck reflex (fencer) disappears by about:",
        "choices": ["1–2 months", "3–4 months", "6–7 months", "9–10 months"],
        "answer_index": 2,
        "rationale": "ATNR usually disappears by ~6–7 months.",
        "tags": ["recall", "reflex"],
    },
    # --- More computation & applied items ---
    {
        "id": 38,
        "stem": "A 3‑year‑old’s speech should be ~75% intelligible. Which counseling statement is MOST accurate for AGE 4?",
        "choices": [
            "Expect ~80% intelligibility",
            "Expect ~90% intelligibility",
            "Expect ~100% intelligibility",
            "Hard to predict at 4 years",
        ],
        "answer_index": 2,
        "rationale": "By ~4 years, speech is ~100% intelligible to strangers.",
        "tags": ["computation", "language"],
    },
    {
        "id": 39,
        "stem": "A term infant weighed 3.0 kg at birth and is 9.0 kg at 12 months. Which BEST describes this?",
        "choices": [
            "Below expected — should quadruple",
            "Appropriate — ~triple by 12 months",
            "Excessive — should double only",
            "Insufficient data",
        ],
        "answer_index": 1,
        "rationale": "Tripling of birth weight by ~12 months is expected.",
        "tags": ["computation", "growth"],
    },
    {
        "id": 40,
        "stem": "A 2‑year‑old uses ~30 words and is ~50% intelligible but does not combine words. BEST next step?",
        "choices": [
            "Reassure; this is normal",
            "Audiology/hearing + early intervention referral",
            "Neuroimaging",
            "Genetic testing",
        ],
        "answer_index": 1,
        "rationale": "Lack of two‑word phrases at 2 y warrants hearing eval and early intervention.",
        "tags": ["case", "language"],
    },
]

def shuffle_array(array):
    arr = list(array)
    random.shuffle(arr)
    return arr

def filter_bank(tag):
    if tag == "all":
        return QUESTIONS
    return [q for q in QUESTIONS if tag in q.get("tags", [])]

# ----------------------------
# Session state init
# ----------------------------
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

# ----------------------------
# UI
# ----------------------------
st.title("Developmental Milestones — Board‑Style Quiz (Python)")

with st.sidebar:
    st.markdown("### 🎛️ Options")
    bank = st.selectbox("Question bank", ["all", "case", "computation", "recall"], index=["all","case","computation","recall"].index(st.session_state.filter))
    colA, colB = st.columns(2)
    if colA.button("Restart", use_container_width=True):
        restart(new_filter=bank)
    if colB.button("Review missed", use_container_width=True):
        restart(use_missed=True)
    st.caption("Banks: **all / case / computation / recall** • Restart shuffles the items. Review missed builds a quiz from your incorrect answers.")

# Progress
q_total = len(st.session_state.questions)
q_index = st.session_state.index
progress = 0 if q_total == 0 else int((q_index / q_total) * 100)
st.progress(progress)

if q_total == 0:
    st.info("No questions in this bank yet. Use **Restart** to reload all questions.")
else:
    q = st.session_state.questions[q_index]
    st.write(f"**Question {q_index + 1} of {q_total}**")
    st.markdown(f"#### {q['stem']}")

    # Choices as clickable buttons
    for i, choice in enumerate(q["choices"]):
        is_correct = (i == q["answer_index"])
        is_selected = (st.session_state.selected == i)
        label = f"{chr(65+i)}. {choice}"
        button_key = f"choice_{q['id']}_{i}"
        # Apply visual cue post-reveal by grouping in columns to avoid width issues
        cols = st.columns([1,9])
        with cols[1]:
            if st.button(label, key=button_key, use_container_width=True, disabled=st.session_state.revealed):
                choose(i)
        if st.session_state.revealed:
            with cols[0]:
                if is_selected and is_correct:
                    st.success("✔", icon="✅")
                elif is_selected and not is_correct:
                    st.error("✘", icon="❌")
                elif is_correct:
                    st.success("✔", icon="✅")

    # Reveal & navigation
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

# Footer
st.caption("Mapped to your module: gross/fine motor, language, cognitive milestones; early‑childhood skills; CDC red flags; primitive reflexes; growth rules (weight doubles ~4–5 mo, triples ~12 mo; length +50% at ~12 mo; ≈2× by ~4 y; corrected age = chronological − weeks premature).")
