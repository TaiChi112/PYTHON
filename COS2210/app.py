import streamlit as st
from google import genai
import json
import os
from dotenv import load_dotenv
from pathlib import Path

# --- 1. CONFIG & SETUP ---
st.set_page_config(page_title="Auto-Spec Generator", page_icon="🚀", layout="wide")

# Load API Key
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.environ.get("GEMINI_API_KEY")

# --- 2. SIDEBAR (Configuration) ---
with st.sidebar:
    st.header("⚙️ Configuration")

    # เช็ค API Key
    if not api_key:
        st.error("❌ ไม่พบ API Key! กรุณาเช็คไฟล์ .env")
        st.stop()
    else:
        st.success(f"✅ API Connected (...{api_key[-4:]})")

    # เลือก Model (เผื่ออยากปรับเปลี่ยนในอนาคต)
    model_id = st.text_input(
        "Model ID",
        value="gemini-2.5-flash",
        help="ถ้า Error ให้ลองเปลี่ยนเป็น gemini-1.5-flash",
    )

    st.info("💡 Tip: ใส่ไอเดียดิบๆ ลงไป ระบบจะจัดระเบียบให้เอง")


# --- 3. CORE LOGIC (AI Function) ---
def generate_spec(raw_text):
    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are an expert Senior System Analyst.
    Your task is to analyze the unstructured raw text provided by the user.
    Extract relevant information and map it into the following JSON structure.

    Rules:
    1. Output MUST be valid JSON only. No Markdown code blocks.
    2. If information is missing, try to reasonably INFER it based on standard software engineering practices.
    3. If inference is impossible, use null.
    4. "Status" field should be "Draft", "Incomplete", or "Ready".

    Target JSON Structure:
    {
      "project_name": "String",
      "problem_statement": "String",
      "solution_overview": "String",
      "functional_requirements": ["Array of Strings"],
      "non_functional_requirements": ["Array of Strings"],
      "tech_stack_recommendation": ["Array of Strings"],
      "status": "String"
    }
    """

    try:
        response = client.models.generate_content(
            model=model_id,
            contents=f"{system_prompt}\n\nUser Input:\n{raw_text}",
        )
        # Cleaning & Parsing
        cleaned_text = response.text.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned_text)
    except Exception as e:
        st.error(f"Error: {e}")
        return None


# --- 4. MAIN UI ---
st.title("🚀 Auto-Spec Generator")
st.caption("เปลี่ยนไอเดียฟุ้งๆ ให้เป็น Software Requirement แบบมืออาชีพ")

# Input Area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Raw Idea Input")
    raw_input = st.text_area(
        "พิมพ์สิ่งที่คิดออกลงไปเลย (ไม่จำเป็นต้องเรียบเรียง)",
        height=400,
        placeholder="ตัวอย่าง: อยากทำแอพจดหวย ที่สแกนโพยได้ แล้วคำนวณกำไรขาดทุนให้อัตโนมัติ...",
    )

    generate_btn = st.button(
        "✨ Generate Specification", type="primary", use_container_width=True
    )

# Output Area
with col2:
    st.subheader("📄 Structured Requirement")

    if generate_btn and raw_input:
        with st.spinner("🤖 AI กำลังวิเคราะห์และเขียน Spec ให้คุณ..."):
            data = generate_spec(raw_input)

            if data:
                # สร้าง Tab เพื่อดูข้อมูล 2 แบบ
                tab1, tab2 = st.tabs(["📋 Document View", "code JSON View"])

                with tab1:
                    # แสดงผลแบบเอกสาร Markdown สวยๆ
                    st.markdown(f"# 🏗️ {data.get('project_name', 'Untitled Project')}")

                    st.info(f"**Status:** {data.get('status')}")

                    st.markdown("### 1. Problem Statement")
                    st.write(data.get("problem_statement"))

                    st.markdown("### 2. Solution Overview")
                    st.write(data.get("solution_overview"))

                    st.markdown("### 3. Functional Requirements")
                    for req in data.get("functional_requirements", []):
                        st.markdown(f"- {req}")

                    st.markdown("### 4. Non-Functional Requirements")
                    for nfr in data.get("non_functional_requirements", []):
                        st.markdown(f"- {nfr}")

                    st.markdown("### 5. Tech Stack Recommendation")
                    for tech in data.get("tech_stack_recommendation", []):
                        st.code(tech, language="text")

                with tab2:
                    # แสดง JSON ดิบเผื่อเอาไปใช้ต่อ
                    st.json(data)

    elif generate_btn and not raw_input:
        st.warning("⚠️ กรุณาใส่ข้อมูลก่อนกดปุ่มครับ")

    else:
        st.info("👈 ใส่ข้อมูลด้านซ้าย แล้วกดปุ่มเพื่อเริ่มงาน")
