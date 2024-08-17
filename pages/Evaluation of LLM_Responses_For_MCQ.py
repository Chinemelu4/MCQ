import streamlit as st
import pandas as pd
import numpy as np

# Load your dataset
@st.cache
def load_data():
    # Replace with the path to your dataset
    return pd.read_parquet('special_df.parquet'), pd.read_parquet('afriq_df.parquet'), pd.read_parquet('harmful_df.parquet')

df,df2,df3 = load_data()

st.title('MCQ LLM Response Evaluation')

# User selection
filter_type = st.radio(
    'Select filter type:',
    ('Specialty Questions', 'African Expertise Questions')
)

if filter_type == 'Specialty Questions':
    # Get unique specialties
    specialties = df['specialty'].unique()
    selected_specialty = st.selectbox('Select Specialty:', specialties)

    # Filter the dataset based on selected specialty
    filtered_df = df[df['specialty'] == selected_specialty]

elif filter_type == 'African Expertise Questions':
    # Filter dataset based on African expertise questions ranked 2, 3, 4, or 5
    selected_ranks = [2, 3, 4, 5]
    filtered_df = df2[df2['Requires African local expertise'].isin(selected_ranks)]

# Randomly select predictions from 3 out of 6 models
models = [
    'model1','model2','model3','model4','model5','model6'
]
selected_models = np.random.choice(models, 3, replace=False)

# Filter columns to only include the selected models' predictions and corresponding 'correct' columns
model_columns = [f'{model}' for model in selected_models]
correct_columns = [f'{model}_outputs' for model in selected_models]
others = ['question', 'rationale']
columns_to_keep = ['sample_id'] + others + model_columns + correct_columns

# Ensure only 30 questions are displayed
if len(filtered_df) > 30:
    filtered_df = filtered_df.sample(n=30, random_state=1)


# Display the filtered DataFrame
filtered_df = filtered_df[columns_to_keep]
filtered_df.reset_index(drop=True,inplace=True)
filtered_df2 = filtered_df.drop(columns=['sample_id'],axis=1)
st.write(filtered_df2)

# Button to download the filtered dataset as a CSV file
@st.cache
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(filtered_df)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='MCQ_data.csv',
    mime='text/csv'
)
