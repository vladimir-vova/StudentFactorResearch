import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb

st.title("Исследование данных из датасета")

df = pd.read_csv('StudentPerformanceFactors.csv')
df.dropna()



