# app.py
import streamlit as st
from algorithm.alignment_engine import needleman_wunsch, validate_sequences

st.set_page_config(
    page_title="Global Sequence Alignment",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 Global Sequence Alignment System")
st.markdown("Using the **Needleman-Wunsch** Dynamic Programming Algorithm.")
st.divider()

# --- Sequence Inputs ---
st.subheader("Enter Sequences")
seq1 = st.text_input("Sequence 1", placeholder="e.g. AGCTG")
seq2 = st.text_input("Sequence 2", placeholder="e.g. AGTCG")

# --- Scoring Parameters ---
st.subheader("Scoring Parameters")
col1, col2, col3 = st.columns(3)
match    = col1.number_input("Match Score",      value=1,  step=1)
mismatch = col2.number_input("Mismatch Penalty", value=-1, step=1)
gap      = col3.number_input("Gap Penalty",      value=-1, step=1)

st.divider()

# --- Warning for long sequences ---
if len(seq1) > 100 or len(seq2) > 100:
    st.warning("⚠️ Sequences are long — matrix display will be hidden for performance.")

# --- Align Button ---
if st.button("🔍 Align Sequences"):
    if not seq1 or not seq2:
        st.warning("⚠️ Please enter both sequences.")
    else:
        try:
            s1, s2 = validate_sequences(seq1, seq2)
            score, matrix = needleman_wunsch(s1, s2, match, mismatch, gap)

            st.subheader("📊 Results")
            st.success(f"✅ Optimal Alignment Score: **{score}**")

            # --- DP Matrix Display ---
            if len(s1) <= 20 and len(s2) <= 20:
                st.markdown("### 🔢 Dynamic Programming Matrix")

                # Build header row
                header = ["", ""] + list(s2)
                rows = [header]

                for i, row in enumerate(matrix):
                    if i == 0:
                        label = ""
                    else:
                        label = s1[i - 1]
                    rows.append([label] + [str(v) for v in row])

                # Display as a table
                st.table(rows)
            else:
                st.info("Matrix display hidden for sequences longer than 20 characters.")

        except ValueError as e:
            st.error(f"❌ Error: {e}")
