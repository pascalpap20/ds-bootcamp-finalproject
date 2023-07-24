import streamlit as st
import numpy as np

#load ML package
import pickle
import os

attribute_info = """
                - Gender: The gender of the person (Male/Female).
                - Age: The age of the person in years.
                - Occupation: The occupation or profession of the person. (Nurse, Doctor, Engineer, Lawyer, Teacher, Accountant, Salesperson, Software Engineer, Scientist)         Sales Representat Manager               
                - Sleep Duration (hours): The number of hours the person sleeps per day.
                - Quality of Sleep (scale: 1-10): A subjective rating of the quality of sleep, ranging from 1 to 10.
                - Physical Activity Level (minutes/day): The number of minutes the person engages in physical activity daily.
                - Stress Level (scale: 1-10): A subjective rating of the stress level experienced by the person, ranging from 1 to 10.
                - BMI Category: The BMI category of the person (Normal, Overweight, Obese).
                - Blood Pressure (systolic/diastolic): The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.
                - Heart Rate (bpm): The resting heart rate of the person in beats per minute.
                - Daily Steps: The number of steps the person takes per day.
                - Sleep Disorder: The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).

                ### Details about Sleep Disorder Column:

                - None: The individual does not exhibit any specific sleep disorder.
                - Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.
                - Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.
                 """

dep = {'Sales & Marketing':1, 'Operations':2, 'Technology':3, 'Analytics':4,
       'R&D':5, 'Procurement':6, 'Finance':7, 'HR':8, 'Legal':9}
edu = {'Below Secondary':1, "Bachelor's":2, "Master's & above":3}
rec = {'referred':1, 'sourcing':2, 'other':3}
gen = {'m':1, 'f':2}
reg = {'region_1':1,'region_2':2,'region_3':3,'region_4':4,'region_5':5,
       'region_6':6,'region_7':7,'region_8':8,'region_9':9,'region_10':10,
       'region_11':11,'region_12':12,'region_13':13,'region_14':14,'region_15':15,
       'region_16':16,'region_17':17,'region_18':18,'region_19':19,'region_20':20,
       'region_21':21,'region_22':22,'region_23':23,'region_24':24,'region_25':25,
       'region_26':26,'region_27':27,'region_28':28,'region_29':29,'region_30':30,
       'region_31':31,'region_32':32,'region_33':33,'region_34':34}

bmi_category_encode = {
    'Normal' : 0, 
    'Overweight': 1, 
    'Obese': 2,
}

        
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

@st.cache_data 
def load_model(model_file):
    loaded_model = pickle.load(open(os.path.join(model_file),'rb'))
    return loaded_model

def run_ml_app():
    st.subheader("ML section")

    with st.expander("Attribute Info"):
        st.markdown(attribute_info)

    st.subheader("Input Your Data")

    age = st.number_input("Age",10,60)
    gender = st.radio('Gender', ['Male','Female'])
    occupation = st.selectbox('Occupation', ["Accountant", "Doctor", "Engineer", "Lawyer", "Manager", "Nurse", "Sales Representative", "Salesperson", "Scientist", "Software Engineer", "Teacher"])
    sleep_duration = st.number_input("Sleep Duration (hours)",step=1.,format="%.2f")
    quality_of_sleep = st.number_input("Quality of Sleep (scale: 1-10)",1,10)
    physical_activity = st.number_input("Physical Activity Level (minutes/day)",1,1440) 
    stress_level = st.number_input("Stress Level (scale: 1-10)",1,10)
    bmi_category = st.selectbox('BMI Category', ["Normal", "Overweight", "Obese"])
    blood_pressure_systolic = st.number_input("Blood Pressure (systolic)",1,200)
    blood_pressure_diastolic = st.number_input("Blood Pressure (diastolic)",1,200)
    heart_rate = st.number_input("Heart Rate (bpm)",1,200)
    daily_steps = st.number_input("Daily Steps",1,10000)

    with st.expander("Your Selected Options"):
        result = {
            'Age':age,
            'Sleep Duration (hours)':sleep_duration,
            'Quality of Sleep (scale: 1-10)':quality_of_sleep,
            'Physical Activity Level (minutes/day)':physical_activity,
            'Stress Level (scale: 1-10)':stress_level,
            'BMI Category':bmi_category,
            'Heart Rate (bpm)':heart_rate,
            'Daily Steps':daily_steps,
            'Blood Pressure (systolic)':blood_pressure_systolic,
            'Blood Pressure (diastolic)':blood_pressure_diastolic,
            'Gender':gender,
            'Occupation': occupation,
        }

    st.write(result)

    # 0 : Age                              
    # 1 : Sleep Duration                   
    # 2 : Quality of Sleep                 
    # 3 : Physical Activity Level          
    # 4 : Stress Level                     
    # 5 : BMI Category                     
    # 6 : Heart Rate                       
    # 7 : Daily Steps                      
    # 8 : Blood Pressure Systolic          
    # 9 : Blood Pressure Diastolic          
    # 10 : Gender_Male                      
    # 11 : Occupation_Accountant            
    # 12 : Occupation_Doctor                
    # 13 : Occupation_Engineer              
    # 14 : Occupation_Lawyer                
    # 15 : Occupation_Manager               
    # 16 : Occupation_Nurse                 
    # 17 : Occupation_Sales Representative  
    # 18 : Occupation_Salesperson           
    # 19 : Occupation_Scientist             
    # 20 : Occupation_Software Engineer     
    # 21 : Occupation_Teacher       
    
    data = {
        'Age': age,                         
        'Sleep Duration': sleep_duration,                   
        'Quality of Sleep': quality_of_sleep,                 
        'Physical Activity Level': physical_activity,          
        'Stress Level': stress_level,                     
        'BMI Category': bmi_category,                     
        'Heart Rate': heart_rate,                       
        'Daily Steps': daily_steps,                      
        'Blood Pressure Systolic': blood_pressure_systolic,          
        'Blood Pressure Diastolic': blood_pressure_diastolic,          
        'Gender_Male': gender,                      
        'Occupation_Accountant': 0,            
        'Occupation_Doctor': 0,                
        'Occupation_Engineer': 0,              
        'Occupation_Lawyer': 0,                
        'Occupation_Manager': 0,               
        'Occupation_Nurse': 0,                 
        'Occupation_Sales Representative': 0,  
        'Occupation_Salesperson': 0,           
        'Occupation_Scientist': 0,             
        'Occupation_Software Engineer': 0,     
        'Occupation_Teacher': 0, 
    }

    for key, value in result.items():
        if key == 'BMI Category':
            data[key] = bmi_category_encode[value]
        elif key == 'Gender':
            data['Gender_Male'] = 1 if value == 'Male' else 0
        elif key == 'Occupation':
            data['Occupation_' + value] = 1
            
    st.write(data)
    encoded_result = []
    for item in data.values():
        encoded_result.append(item)

    st.write(encoded_result)

    ## prediction section
    st.subheader('Prediction Result')
    single_sample = np.array(encoded_result).reshape(1,-1)
    # st.write(single_sample)

    model = load_model("LogReg.sav")

    prediction = model.predict(single_sample)
    pred_proba = model.predict_proba(single_sample)
    st.write(prediction)
    st.write(pred_proba)

    pred_probability_score = {
        'None':round(pred_proba[0][0]*100,4),
        'Insomnia':round(pred_proba[0][1]*100,4),
        'Sleep Apnea':round(pred_proba[0][2]*100,4),
    }

    if prediction == 2:
        st.warning("Sleep Apnea: The individual suffers from pauses in breathing during sleep, resulting in disrupted sleep patterns and potential health risks.")
        st.write(pred_probability_score)
    elif prediction == 1:
        st.warning("Insomnia: The individual experiences difficulty falling asleep or staying asleep, leading to inadequate or poor-quality sleep.")
        st.write(pred_probability_score)
    else:
        st.success("None: The individual does not exhibit any specific sleep disorder.")
        st.write(pred_probability_score)