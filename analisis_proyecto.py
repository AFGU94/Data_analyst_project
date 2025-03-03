import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno

filename = ("Datos de la vivienda.CSV")
filename2 = ('Tecnologías de información y comunicación (1).CSV')
data = pd.read_csv(filename, delimiter=';')
data2 = pd.read_csv(filename2, delimiter=';')

# imprimo la informacion para comenzar del archivo datos de la vivienda
print(data.head())
print('Información del DataFrame 1: \n',data.info())
print(data.columns)

# filtro el departamento por el numero 05 que pertenece a antioquia
data_filtr = data.loc[data['P1_DEPARTAMENTO']== 5]
print(data_filtr.head())
print(data_filtr.info())

# Selecciono la columna que voy a utilizar eliminando el resto
data_direct = data_filtr[['DIRECTORIO']]
print(data_direct.head())
print(data_direct.info())

# imprimo la informacion para comenzar del archivo tecnologías de información y comunicación
print(data2.head())
print('Información del DataFrame 2: \n',data2.info())
print(data2.columns)

# uno por medio de inner joint los dos dataframes
df_merged = pd.merge(data_direct, data2, on='DIRECTORIO', how='inner')
print("\nDataFrame después de merge (inner join):\n", df_merged.head())
print(df_merged.info())

#Filtro las columnas que quiero utilizar o analizar
df_filtr = df_merged[['DIRECTORIO','FEX_C','P765S1','P765S2','P765S4','P1085S1','P1085S2','P1085S3','P1083S2','P1083S3','P1083S4','P1083S5','P1083S6','P1083S15','P1083S16']]
print(df_filtr.head())
print(df_filtr.info())
print(df_filtr.columns)
print('***********************************')

# visualizo los datos nulos con missingno
msno.matrix(df_filtr)
plt.show()

# Conteo de las filas (celdas = 1) en cada columna

# 'P765S1','P765S2','P765S4'
cont_P1= df_filtr['P765S1'].value_counts()
cont_P2= df_filtr['P765S2'].value_counts()
cont_P4= df_filtr['P765S4'].value_counts()

# 'P1085S1','P1085S2','P1085S3'
cont_S1= df_filtr['P1085S1'].value_counts()
cont_S2= df_filtr['P1085S2'].value_counts()
cont_S3= df_filtr['P1085S3'].value_counts()

# 'P1083S2','P1083S3','P1083S4','P1083S5','P1083S6','P1083S15'
cont_A2= df_filtr['P1083S2'].value_counts()
cont_A3= df_filtr['P1083S3'].value_counts()
cont_A4= df_filtr['P1083S4'].value_counts()
cont_A5= df_filtr['P1083S5'].value_counts()
cont_A6= df_filtr['P1083S6'].value_counts()
cont_A15= df_filtr['P1083S15'].value_counts()
cont_A16= df_filtr['P1083S16'].value_counts()

# Creo los dataframes que quiero mostrar a partir de los counts
con_d1 = pd.DataFrame({ 'Pc de escritorio': cont_P1, 'Pc laptop': cont_P2, 'Telefono celular': cont_P4 }).fillna(0) 
con_d2 = pd.DataFrame({ 'En el hogar': cont_S1, 'En el trabajo': cont_S2, 'En institución educativa': cont_S3 }).fillna(0) 
con_d3 = pd.DataFrame({ 'Enviar o recibir correos': cont_A2, 'Redes sociales': cont_A3, 'Comprar productos o servicios': cont_A4, 
                       'Banca electronica': cont_A5 , 'Educación o aprendizaje': cont_A6, 'Para trabajar': cont_A15, 
                       'Para hacer videollamadas': cont_A16}).fillna(0) 

# GRAFICOS

# Creo variables para plotear los dataframes
ax = con_d1.plot(kind='bar', figsize=(12, 6)) 
plt.title('Dispositivo utilizado para acceder a internet') 
plt.xlabel('Valor') 
plt.ylabel('Cantidad de personas') 
plt.legend(title='Columnas')
plt.show()

ax2 = con_d2.plot(kind='bar', figsize=(12, 6)) 
plt.title('Lugar donde utiliza internet') 
plt.xlabel('Valor') 
plt.ylabel('Cantidad de personas') 
plt.legend()
plt.show()

ax3 = con_d3.plot(kind='bar', figsize=(12, 6)) 
plt.title('Para que utiliza internet?') 
plt.xlabel('Valor') 
plt.ylabel('Cantidad de personas') 
plt.legend()
plt.show()


# Conteo columnas relacionadas a CELULAR con .value_counts
cont_c1= df_filtr[['P765S4','P1085S2','P1083S3']].value_counts() #celular, trabajo, redes sociales
cont_c2= df_filtr[['P765S4','P1085S1','P1083S3']].value_counts() #celular, hogar, redes sociales
print(cont_c1,' ',type(cont_c1))

con_d4= pd.DataFrame({'En el lugar de trabajo para ver redes sociales':cont_c1,'En el hogar para ver redes sociales':cont_c2})

con_d4.plot(kind='bar', figsize=(12, 6))
plt.title('Uso de internet en CELULAR') 
plt.xlabel('Valores') 
plt.ylabel('Cantidad de personas')
plt.legend(loc='best')
plt.show()

# Conteo columnas relacionadas a PC, LAPTOP con .value_counts
cont_c3= df_filtr[['P765S1','P765S2','P1085S2','P1083S6','P1083S15']].value_counts() #PC,LAP, trabajo, estudiar o trabajar
cont_c4= df_filtr[['P765S1','P765S2','P1085S1','P1083S6','P1083S15']].value_counts() #PC,LAP, hogar, estudiar o trabajar

con_d5= pd.DataFrame({'En el lugar de trabajo para estudiar o trabajar':cont_c3,'En el hogar para estudiar o trabajar':cont_c4})

con_d5.plot(kind='bar', figsize=(12, 6), color=['red','green'])
plt.title('Uso de internet en PC y LAPTOP') 
plt.xlabel('Valores') 
plt.ylabel('Cantidad de personas')
plt.legend(loc='best')
plt.show()

