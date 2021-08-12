import streamlit as st
st.title ("MI PRIMERA APLICACION")
st.sidebar.title("PARAMETROS")
st.sidebar.header("INICIO")
st.write("Aplicaciones")
from PIL import Image 
imagen1=Image.open("juegos olimpicos.jpg")
st.image(imagen1)
import pandas as pd 
df=pd.read_excel("Data.xlsx")
df["CÁCULO"]=df.NUMEROS*3
lista_columna=df.columns
st.write(df)
st.write(lista_columna)
estadisticas=df.describe()
st.write(estadisticas)
barra_desplazadora=st.slider("Seleccione un valor",0,50,5,step=5)
st.write("Su valor seleccionado fue:",barra_desplazadora)
df["FUNCIÓN"]=df.NUMEROS*barra_desplazadora
st.write(df)
ingreso_numero=st.number_input("Ingrese un valor:")
ingreso_texto=st.text_input("Ingrese su nombre:")
caja_seleccion=st.selectbox("Seleccione una opción:",["a","b","c"],index=2)
with st.beta_expander("Menu"):
	col1,col2=st.beta_columns(2)
	with col1:
		opciones=st.radio("Seleccione una opción:",[1,2,3])
	with col2:
		check=st.checkbox("Casado")
		if check == True:
			st.write("Esta seguro:")
		else:
			st.write("No seleccionado el check")
lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[2,4,6,8,10,12,14,16,20,22]
lista3=[3,6,9,12,15,18,21,24,27,30]
data={"EJE X":lista1,
		"EJE Y":lista2,
		"EJE Z":lista3}
ejes=pd.DataFrame(data)
st.write(ejes)
		
import altair as alt 
grafico_altair=alt.Chart(ejes).mark_bar ().encode(
	x="EJE X",
	y="EJE Y",
	color="EJE Z").interactive()
st.altair_chart(grafico_altair)
import plotly.express as px
import matplotlib.pyplot as plt 
figura_3d=px.line_3d(ejes,x="EJE X",y="EJE Y",z="EJE Z")
st.write(figura_3d)
figura2=px.scatter(ejes,x="EJE X",y="EJE Z",animation_frame="EJE Y",range_x=[0,40],range_y=[0,40])
st.write(figura2)
grafico2,ax=plt.subplots()
ax.plot(ejes["EJE Y"],ejes["EJE X"],marker="X",label="X")
ax.set_xlabel("EJE X")
ax.set_ylabel("EJE Y")
ax.grid()
ax.legend(loc="best")
ax.set_title("GRÁFICO")
st.pyplot(grafico2)
