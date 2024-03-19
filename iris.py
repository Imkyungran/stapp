import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# st.columns() : 화면을 여러 열로 나누고 각 열에 요소 배치
_, col, _ = st.columns([2,6,2]) # 첫번째 열 : 너비 2 비율 / 두번째 열 : 너비 6 / 세번쨰 열 : 너비 2
col.header('streamlit 시각화')
' ' # 한칸 띄우기

dfiris = sns.load_dataset('iris')
colors = {'setosa':'red', 'virginica':'green', 'versicolor':'blue'}

# 사이드바 만들기
st.sidebar.title('iris species')

with st.sidebar:
   selectX = st.selectbox("X 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"]) 
   ' '
   selectY = st.selectbox("Y 변수 선택:", ["sepal_length", "sepal_width", "petal_length", "petal_width"])
   ' '
   selectSpecies = st.multiselect('붓꽃 유형 선택 (:blue[다중]):', ['setosa','versicolor','virginica'])
   selectAlpha = st.slider('alpha 설정:', 0.1, 1.0, 0.5)

# 산점도 시각화 표현
if selectSpecies:
   fig = plt.figure(figsize=(7,5))
   for aSpecies in selectSpecies:
      df = dfiris[dfiris.species==aSpecies]
      plt.scatter(df[selectX], df[selectY], color=colors[aSpecies], label=aSpecies, alpha=selectAlpha)
      plt.legend(loc='lower right')
      plt.xlabel(selectX) ; plt.ylabel(selectY)
      plt.title('iris scatter plot')
      st.pyplot(fig)
else:
   st.warning('붓꽃 유형 선택 바람')
