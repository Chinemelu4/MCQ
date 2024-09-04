import streamlit as st
import pandas as pd
import numpy as np

# Load your dataset
@st.cache
def load_data():
    # Replace with the path to your dataset
    return pd.read_csv('harmful_df.csv')

filtered_df = load_data()

st.title('Harmful & Misleading Response Evaluation')
#st.write(len(df))

# Filter dataset based on African expertise questions ranked 2, 3, 4, or 5
selected_ranks = [1, 2, 3, 4, 5]
#filtered_df = df[df['Possibility of harm'].isin(selected_ranks)]
#filtered_df = df.copy()

# Randomly select predictions from 3 out of 6 models
models = [
    'model1','model2','model3','model4','model5','model6'
]
selected_models = np.random.choice(models, 3, replace=False)

# Filter columns to only include the selected models' predictions and corresponding 'correct' columns
model_columns = [f'{model}' for model in selected_models]
correct_columns = [f'{model}_outputs' for model in selected_models]
others = ['question', 'answer','rationale']
columns_to_keep = ['sample_id'] + others + model_columns + correct_columns

# Ensure only 30 questions are displayed
num = np.random.randint(10000)
if len(filtered_df) > 30:
    filtered_df = filtered_df.sample(n=30, random_state=num)

    # Display the filtered DataFrame
    filtered_df = filtered_df[columns_to_keep]
    filtered_df.reset_index(drop=True,inplace=True)
    #filtered_df.iloc[:, 4] = filtered_df.iloc[:, 5]
    filtered_df2 = filtered_df.drop(columns=['sample_id'],axis=1)
    st.dataframe(filtered_df2)

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
