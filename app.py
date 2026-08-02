from PIL import Image
from ai_agent import ask_ai
from data_loader import load_data, calculate_kpis
import streamlit as st

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="HR Analytics AI Agent",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Heading
# -----------------------------
st.title("🤖 HR Analytics AI Agent")

st.write("Upload your HR Dashboard. You may also upload the HR dataset for enhanced KPI-based insights.")

# -----------------------------
# Upload Dashboard
# -----------------------------
dashboard = st.file_uploader(
    "📊 Upload Power BI Dashboard",
    type=["png", "jpg", "jpeg"]
)

st.caption("📌 The HR dataset is optional. If not uploaded, the AI will analyze only the dashboard image.")
# -----------------------------
# Upload Dataset
# -----------------------------
dataset = st.file_uploader(
    "📄 Upload HR Dataset (Optional)",
    type=["xlsx"]
)



# -----------------------------
# User Question
# -----------------------------
question = st.text_area(
    "Ask your business question",
    placeholder="Example: Which department has the highest attrition?"
)

# -----------------------------
# Analyze Button
# -----------------------------
if st.button("🔍 Analyze"):

    if dashboard is None:
        st.warning("Please upload the dashboard image.")

    elif question.strip() == "":
        st.warning("Please enter a question.")

    else:

        kpis = None

        st.success("Dashboard uploaded successfully!")

        st.write("Dashboard :", dashboard.name)

        if dataset is not None:

            df = load_data(dataset)

            st.write("Dataset :", dataset.name)

            st.subheader("Dataset Preview")
            st.dataframe(df.head())

            kpis = calculate_kpis(df)

            st.subheader("HR KPI Summary")
            st.json(kpis)

        image = Image.open(dashboard)

        with st.spinner("AI is analyzing the dashboard..."):

              answer = ask_ai(image, kpis, question)

        st.subheader("AI Response")

        st.write(answer)
