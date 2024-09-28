import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

st.title("Исследование данных из датасета")

df = pd.read_csv('StudentPerformanceFactors.csv')
df.dropna()

st.subheader('Нахождение средней оценки (общую), среди мальчиков и девочек')
st.write(f"Общая средняя оценка: {np.round(df['Exam_Score'].agg('mean'),2)}")
st.write(f"Средняя оценка среди парней: {np.round(df[df['Gender'] == 'Male']['Exam_Score'].agg('mean'), 2)}")
st.write(f"Средняя оценка среди девушек: {np.round(df[df['Gender'] == 'Female']['Exam_Score'].agg('mean'), 2)}")
