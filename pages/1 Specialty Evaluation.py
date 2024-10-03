import streamlit as st
import pandas as pd
import numpy as np
import random

# Load your dataset
@st.cache
def load_data():
    # Replace with the path to your dataset
    return pd.read_csv('spec_df1.csv'), pd.read_csv('spec_df2.csv'), pd.read_csv('spec_df3.csv'), pd.read_csv('spec_df4.csv'), pd.read_csv('spec_df5.csv'), pd.read_csv('spec_df6.csv')

df1,df2,df3,df4,df5,df6 = load_data()

st.title('MCQ Specialty Based Evaluation')



specialties = ['Obstetrics_and_Gynecology', 'Internal_Medicine', 'Cardiology',
       'Endocrinology', 'General_Surgery', 'Infectious_Disease',
       'Pediatrics', 'Hematology', 'Neurology', 'Gastroenterology']
selected_specialty = st.selectbox('Select Specialty:', specialties)





    # Randomly select predictions from 3 out of 6 models
if st.button('Regenerate Questions'):
    final_df = pd.DataFrame()
    data = [
        df1,df2,df3,df4,df5,df6
    ]
    selected_data = random.sample(data, 3)

    for i in selected_data:
        filtered_df = i[i['specialty'] == selected_specialty]
        filtered_true = filtered_df[filtered_df['correct'] == True]
        filtered_false = filtered_df[filtered_df['correct'] == False]
        num = np.random.randint(10000)

        if len(filtered_true) > 5:
            filtered_true = filtered_true.sample(n=5,random_state=num)
        if len(filtered_false) > 5:
            filtered_false = filtered_false.sample(n=5,random_state=num)
        
        true_false_df = pd.concat([filtered_true, filtered_false],ignore_index=True)
        
        final_df = pd.concat([final_df,true_false_df],ignore_index=True)

    new_cols = ['sample_id', 'question', 'rationale', 'model number', 'model_answer', 'model rationale']  

    final2 = final_df[new_cols] 
    st.write(final2)
        

    # # Filter columns to only include the selected models' predictions and corresponding 'correct' columns
    # model_columns = [f'{model}' for model in selected_models]
    # correct_columns = [f'{model}_outputs' for model in selected_models]
    # others = ['question', 'answer','rationale']
    # columns_to_keep = ['sample_id'] + others + model_columns + correct_columns

    # # Ensure only 30 questions are displayed
    # num = np.random.randint(10000)
    # if len(filtered_df) > 30:
    #     filtered_df = filtered_df.sample(n=30, random_state=num)


    # # Display the filtered DataFrame
    # filtered_df = filtered_df[columns_toS_keep]
    # filtered_df.reset_index(drop=True,inplace=True)
    # filtered_df2 = filtered_df.drop(columns=['sample_id'],axis=1)
    # st.write(filtered_df2)

# Button to download the filtered dataset as a CSV file
    @st.cache
    def convert_df_to_csv(df1):
        return df1.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(final2)
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='MCQ_data.csv',
        mime='text/csv'
    )
