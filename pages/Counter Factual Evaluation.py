import streamlit as st
import pandas as pd
import numpy as np

# Load your dataset
@st.cache
def load_data():
    # Replace with the path to your dataset
    return pd.read_csv('m_afri_df.csv'), pd.read_csv('m_age_df.csv'), pd.read_csv('m_gender_df.csv')

df1,df2,df3 = load_data()

st.title('Counter Factual Validation')

if st.button('Generate Questions'):
    
    # filtered_df1 = df1['question']
    # filtered_df2 = df2['question']
    # filtered_df3 = df3['question']

    # # Randomly select predictions from 3 out of 6 models
    # models = [
    #     'model1','model3'
    # ]

    # # Filter columns to only include the selected models' predictions and corresponding 'correct' columns
    # model_columns = [f'{model}' for model in models]
    # correct_columns = [f'{model}_outputs' for model in models]
    # others = ['question', 'rationale']
    # columns_to_keep = others + model_columns + correct_columns

    # Ensure only 30 questions are displayed
    num =np.random.randint(10000)
    

    df1 = df1.sample(n=10, random_state=num)

    
    df2 = df2.sample(n=10, random_state=num)

    
    df3 = df3.sample(n=10, random_state=num)

    # Display the filtered DataFrame
    

    filtered_df = pd.concat([df1, df2, df3], ignore_index=True)
    filtered_df.reset_index(drop=True,inplace=True)
    #filtered_df.reset_index(drop=True,inplace=True)
    #filtered_df.iloc[:, 4] = filtered_df.iloc[:, 5]
    #filtered_df2 = filtered_df.drop(columns=['sample_id'],axis=1)
    #st.write(filtered_df)
    st.dataframe(filtered_df)

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
