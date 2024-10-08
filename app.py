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

st.subheader('Узнать сколько обучается мальчиков и девочек')
st.write(f"Количество мальчиков: {len(df[df['Gender'] == 'Male'])}")
st.write(f"Количество девочек: {len(df[df['Gender'] == 'Female'])}")

st.subheader('Найти минимальное и максимальное количество затрачиваемых часов в неделю на самообразование')
st.write(f"Минимальное количество затрачиваемых за неделю на самообразование: {np.min(df['Hours_Studied'])}")
st.write(f"Максимальное количество затрачиваемых за неделю на самообразование: {np.max(df['Hours_Studied'])}")

st.subheader('Количество часов на самообразование по полу')
st.write(f"Минимальное количество затрачиваемых за неделю на самообразование (среди мальчиков): {np.min(df[df['Gender'] == 'Male']['Hours_Studied'])}")
st.write(f"Максимальное количество затрачиваемых за неделю на самообразование (среди мальчиков): {np.max(df[df['Gender'] == 'Male']['Hours_Studied'])}")
st.write(f"Минимальное количество затрачиваемых за неделю на самообразование (среди девочек): {np.min(df[df['Gender'] == 'Female']['Hours_Studied'])}")
st.write(f"Максимальное количество затрачиваемых за неделю на самообразование (среди девочек): {np.max(df[df['Gender'] == 'Female']['Hours_Studied'])}")

st.subheader('Зависит ли посещаемость на успеваемость')

x = df['Attendance'].copy()
y = df['Exam_Score'].copy()
fig, axes = plt.subplots(figsize=(10, 10))
axes.scatter(x, y)
axes.set_title("Посещаемость учащихся")
axes.set_xlabel('Процент посещенных занятий за неделю', fontsize=15)
axes.set_ylabel('Итоговый балл экзамена Exam_Score', fontsize=15)

axes.grid(True)
fig.tight_layout()

st.pyplot(fig)

fig, axes = plt.subplots()
axes.hist(x)
axes.set(xlabel='Количество посещаемых')
st.pyplot(fig)

st.subheader('Зависит ли сон на обучающегося')

x = df['Sleep_Hours'].copy()
y = df['Exam_Score'].copy()
fig, axes = plt.subplots(figsize=(10, 5))
axes.scatter(x, y)
axes.set_xlabel('Среднее количество часов сна за ночь', fontsize=15)
axes.set_ylabel('Итоговый балл экзамена Exam_Score', fontsize=15)

axes.grid(True)
fig.tight_layout()

st.pyplot(fig)

st.subheader('Влияние самообразования на успеваемость')

x = df['Hours_Studied'].copy()
y = df['Exam_Score'].copy()
fig, axes = plt.subplots(figsize=(10, 10))
axes.scatter(x, y)
# axes.set_title("Посещаемость учащихся")
axes.set_xlabel('Самообразование', fontsize=15)
axes.set_ylabel('Итоговый балл экзамена Exam_Score', fontsize=15)

axes.grid(True)
fig.tight_layout()

st.pyplot(fig)

st.subheader('Зависимость самообразования на количество сна')

x = df['Sleep_Hours'].copy()
y = df['Hours_Studied'].copy()
fig, axes = plt.subplots(figsize=(10, 10))
axes.scatter(x, y)
# axes.set_title("Посещаемость учащихся")
axes.set_xlabel('Сон', fontsize=15)
axes.set_ylabel('Самообразование', fontsize=15)

axes.grid(True)
fig.tight_layout()

st.pyplot(fig)

st.subheader('Зависимость сна на самообрзование и данные средней оценки')

fig = plt.figure(figsize=(10,5), dpi=200)
snb.scatterplot(x="Sleep_Hours", y="Hours_Studied", data=df, hue="Exam_Score")

st.pyplot(fig)

st.subheader('Завимость сна на оценку от пола')

fig = plt.figure(figsize=(15, 10))
snb.boxplot(data=df, x='Sleep_Hours', y='Exam_Score', hue='Gender')
st.pyplot(fig)
