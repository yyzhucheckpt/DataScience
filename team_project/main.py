import streamlit as st
import pickle
import numpy as np
import pandas as pd
import shap
#import matplotlib
import matplotlib.pyplot as plt


#load the model and dataFrame
df = pd.read_csv("df.csv")
model = pickle.load(open("model.pkl","rb"))

st.title("Credit Card Customer Churn Perdiction")

#Card_Category
Card_Category = st.selectbox('Card_Category', ['Blue','Silver','Gold','Blue'])

#Gender 
Gender = st.selectbox('Gender', ['Male','Female'])

#Customer_Age 
Customer_Age = st.slider('Customer_Age', 0, 130, 46)

#Dependent_count 
Dependent_count = st.slider('Dependent_count', 0, 30, 2)

#Education_Level
Education_Level = st.selectbox('Education_Level',['Uneducated','High School','College','Graduate','Post-Graduate','Doctorate'])

#Education_Level
Marital_Status = st.selectbox('Marital_Status',['Single','Married','Divorced'])

#Income_Category
Income_Category = st.selectbox('Income_Category',['Less than $40K','$40K - $60K','$60K - $80K','$80K - $120K','$120K +'])

#Credit_Limit 
Credit_Limit = st.slider('Credit_Limit', 0, 100000, 8000.00, 0.01)

#Months_on_book 
Months_on_book = st.slider('Months_on_book', 0, 1200, 36, 1)

#Total_Relationship_Count 
Total_Relationship_Count = st.slider('Total_Relationship_Count', 1, 100, 3, 1)

#Months_Inactive_12_mon 
Months_Inactive_12_mon = st.slider('Months_Inactive_12_mon', 0, 1200, 2, 1)

#Contacts_Count_12_mon 
Contacts_Count_12_mon = st.slider('Contacts_Count_12_mon', 0, 1000, 2, 1)

#Total_Trans_Amt 
Total_Trans_Amt = st.slider('Total_Trans_Amt', 0, 100000, 4000.00, 0.01)

#Total_Trans_Ct 
Total_Trans_Ct = st.slider('Total_Trans_Ct', 0, 10000, 65, 1)

#Total_Revolving_Bal
Total_Revolving_Bal = st.slider('Total_Revolving_Bal', 0, 80000, 1000.00, 0.01)

#Avg_Open_To_Buy
Avg_Open_To_Buy = st.slider('Avg_Open_To_Buy', 0, 100000, 7500.00, 0.01)

#Total_Ct_Chng_Q4_Q1 
Total_Ct_Chng_Q4_Q1 = st.slider('Total_Ct_Chng_Q4_Q1', 0, 100, 0.7, 0.001)

#Total_Amt_Chng_Q4_Q1 
Total_Amt_Chng_Q4_Q1 = st.slider('Total_Amt_Chng_Q4_Q1', 0, 100, 0.7, 0.001)

#Avg_Utilization_Ratio 
Avg_Utilization_Ratio = st.slider('Avg_Utilization_Ratio', 0, 1, 0.3, 0.001)

if st.button('Predict Churn'):
    if Gender == "Male":
        gender_val = 1
    else:
        gender_val = 0
        
    if Card_Category == "Blue":
        Card_Category_Blue = 1
        Card_Category_Gold = 0          
        Card_Category_Platinum = 0            
        Card_Category_Silver = 0

    elif Card_Category == "Sliver":
        Card_Category_Blue = 0
        Card_Category_Gold = 0          
        Card_Category_Platinum = 0            
        Card_Category_Silver = 1

    elif Card_Category == "Gold":
        Card_Category_Blue = 0
        Card_Category_Gold = 1         
        Card_Category_Platinum = 0            
        Card_Category_Silver = 0
    else:
        Card_Category_Blue = 0
        Card_Category_Gold = 0         
        Card_Category_Platinum = 1            
        Card_Category_Silver = 0
    
    #'Less than $40K','$40K - $60K','$60K - $80K','$80K - $120K','$120K +'
    if Income_Category == "$120K +":
        Income_Category_40K = 0
        Income_Category_60K = 0
        Income_Category_80K = 0
        Income_Category_120K = 0
        Income_Category_120K_plus = 1
        Income_Category_Unknown = 0
    elif Income_Category == "$40K - $60K":
        Income_Category_40K = 0
        Income_Category_60K = 1
        Income_Category_80K = 0
        Income_Category_120K = 0
        Income_Category_120K_plus = 0
        Income_Category_Unknown = 0
    elif Income_Category == "$60K - $80K":
        Income_Category_40K = 0
        Income_Category_60K = 0
        Income_Category_80K = 1
        Income_Category_120K = 0
        Income_Category_120K_plus = 0
        Income_Category_Unknown = 0
    elif Income_Category == "$80K - $120K":
        Income_Category_40K = 0
        Income_Category_60K = 0
        Income_Category_80K = 0
        Income_Category_120K = 1
        Income_Category_120K_plus = 0
        Income_Category_Unknown = 0
    else:
        Income_Category_40K = 1
        Income_Category_60K = 0
        Income_Category_80K = 0
        Income_Category_120K = 0
        Income_Category_120K_plus = 0
        Income_Category_Unknown = 0
    
    #['Uneducated','High School','College','Graduate','Post-Graduate','Doctorate']
    if Education_Level == "College":
        Education_Level_College = 1             
        Education_Level_Doctorate = 0           
        Education_Level_Graduate = 0            
        Education_Level_High_School  = 0         
        Education_Level_Post_Graduate  = 0      
        Education_Level_Uneducated  = 0         
        Education_Level_Unknown  = 0
    elif Education_Level == "Doctorate":
        Education_Level_College = 0             
        Education_Level_Doctorate = 1           
        Education_Level_Graduate = 0            
        Education_Level_High_School  = 0         
        Education_Level_Post_Graduate  = 0      
        Education_Level_Uneducated  = 0         
        Education_Level_Unknown  = 0
    elif Education_Level == "Graduate":
        Education_Level_College = 0             
        Education_Level_Doctorate = 0           
        Education_Level_Graduate = 1            
        Education_Level_High_School  = 0         
        Education_Level_Post_Graduate  = 0      
        Education_Level_Uneducated  = 0         
        Education_Level_Unknown  = 0
    elif Education_Level == "Post-Graduate":
        Education_Level_College = 0            
        Education_Level_Doctorate = 0           
        Education_Level_Graduate = 0            
        Education_Level_High_School  = 0         
        Education_Level_Post_Graduate  = 1      
        Education_Level_Uneducated  = 0         
        Education_Level_Unknown  = 0
    elif Education_Level == "Uneducated":
        Education_Level_College = 0            
        Education_Level_Doctorate = 0           
        Education_Level_Graduate = 0            
        Education_Level_High_School  = 0         
        Education_Level_Post_Graduate  = 0      
        Education_Level_Uneducated  = 1         
        Education_Level_Unknown  = 0
    else:
        Education_Level_College = 0            
        Education_Level_Doctorate = 0           
        Education_Level_Graduate = 0            
        Education_Level_High_School  = 1         
        Education_Level_Post_Graduate  = 0      
        Education_Level_Uneducated  = 0         
        Education_Level_Unknown  = 0

    #'Single','Married','Divorced'
    if Marital_Status == 'Single':
        Marital_Status_Divorced = 0            
        Marital_Status_Married = 0               
        Marital_Status_Single = 1                
        Marital_Status_Unknown = 0 
    elif Marital_Status == 'Married':
        Marital_Status_Divorced = 0            
        Marital_Status_Married = 1               
        Marital_Status_Single = 0                
        Marital_Status_Unknown = 0 
    else:
        Marital_Status_Divorced = 1            
        Marital_Status_Married = 0               
        Marital_Status_Single = 0                
        Marital_Status_Unknown = 0
        
    query = np.array([Customer_Age,Gender,Dependent_count,Months_on_book,
    Total_Relationship_Count, Months_Inactive_12_mon ,Contacts_Count_12_mon, 
Credit_Limit, Total_Revolving_Bal, Avg_Open_To_Buy, Total_Amt_Chng_Q4_Q1, 
Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio,              
Education_Level_College, Education_Level_Doctorate, Education_Level_Graduate,            
Education_Level_High_School, Education_Level_Post_Graduate,       
Education_Level_Uneducated, Education_Level_Unknown,             
Marital_Status_Divorced, Marital_Status_Married,              
Marital_Status_Single,  Marital_Status_Unknown,              
Income_Category_120K_plus,  Income_Category_60K,         
Income_Category_80K,  Income_Category_120K,        
Income_Category_40K, Income_Category_Unknown,            
Card_Category_Blue, Card_Category_Gold,                  
Card_Category_Platinum, Card_Category_Silver ])
    query = query.reshape(1, 36)
    print(query)
    prediction = str(int(np.exp(model.predict(query)[0])))
    st.title("The predicted churn of this customer is " + prediction)


    shap.initjs()

    #set the tree explainer as the model of the pipeline
    explainer = shap.TreeExplainer(model)

    #get Shap values from preprocessed data
    shap_values = explainer.shap_values(query)

    #plot the feature importance
    fig = shap.force_plot(explainer.expected_value, shap_values,query, matplotlib=True,show=False)
    st.pyplot(fig)


                  
             