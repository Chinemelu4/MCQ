import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome To The MCQ Validation Site! 👋")

st.markdown(
    """
    ## Evaluation Instructions

### To begin your evaluation, please follow these steps:

#### 1. Select Your Question Type of Interest for Evaluation:
- **Questions from a specific Specialty.**
- **Questions requiring African Expertise.**
- **Questions with LLM responses marked as having Potential for Bias.**
- **Questions with LLM responses marked as having Potential for Harm.**

#### 2. Generate Questions:
- Create a CSV file containing randomized questions from the **AfriMed-QA** dataset that meet your selected criteria.

#### 3. Review Questions and Model Responses:
- Download your CSV file.
- Carefully review the questions and the corresponding model responses, using the provided feedback form as a guide.

#### 4. Submit Feedback:
- Complete the feedback survey based on the set of 30 questions you reviewed in step 1.

---

Thank you for your valuable contribution to advancing healthcare research in Africa!

"""
)
