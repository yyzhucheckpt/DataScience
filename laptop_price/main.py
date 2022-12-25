import streamlit as st
import pickle
import numpy as np
import pandas as pd

#load the model and dataFrame
df = pd.read_csv("df.csv")
pipe = pickle.load(open("pipe.pkl","rb"))

st.title("Laptop Price Predict")

#Brand
company = st.selectbox('Brand', df['Company'].unique())

#typeName
typeName = st.selectbox('Type', df['TypeName'].unique())


#Inches 
inches = st.number_input('Screen size')

#Touchscreen
touchscreen = st.selectbox('TouchScreen',['No','Yes'])

#Ips
ips = st.selectbox("IPS", ['No', 'Yes'])

# resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])


#ram
ram = st.selectbox("Ram(GB)", [2,4,6,8,12,16,24,32,64])

#cpu
cpu = st.selectbox('CPU',df['Cpu_brand'].unique())

#cpu freq

cpuFreq = st.number_input('Cpu_frequency(GHz)')

#HDD
hdd = st.selectbox('HDD(GB)',[0,128,256,512,1024,2048])

#SSD
ssd = st.selectbox('SSD(GB)',[0,8,128,256,512,1024])

#GPU
gpu = st.selectbox('GPU',df['Gpu_brand'].unique())

#OS
os = st.selectbox('OS',df['OpSys'].unique())

#weight
weight = st.number_input("Weight of the Laptop")


if st.button('Predict Price'):
    ppi = None
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0
        
    if ips == "Yes":
        ips = 1
    else:
        ips = 0
        
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res**2)) ** 0.5 / inches
    query = np.array([company,typeName,inches,touchscreen,ips, X_res, Y_res, ppi,cpu,cpuFreq,ram,hdd,ssd,gpu,os,weight])
    query = query.reshape(1, 16)
    print(query)
    prediction = str(int(np.exp(pipe.predict(query)[0])))
    st.title("The predicted price of this configuration is " + prediction)
