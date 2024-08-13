import streamlit as st 
import math

#Funções

def calcula_perimetro_triangulo(lado1, lado2, lado3):
    perimetro_tri = lado1 + lado2 + lado3
    return perimetro_tri

def calcula_perimetro_circulo(r):
    perimetro_circ = math.pi * r * 2
    return perimetro_circ

def calcula_perimetro_quadrilatero(x,y):
    if y == 0:
        forma = 'quadrado'
        perimetro_quadrado = 4 * x
        return forma, perimetro_quadrado
    else:
        forma = 'retângulo'
        perimetro_retangulo = 2*x + 2*y
        return forma, perimetro_retangulo
    
#Corpo

st.header ('Calculo de perimetros')

escolha = st.radio("Escolha uma forma geometrica", ["Triângulo", "Círculo", "Quadrilatero"], index=None)

#Processamento
if escolha == "Quadrilatero":
        q1 = st.number_input("Medida do lado 1", value=0)
        q2 = st.number_input("Medida do lado 2", value=0)
        st.write('Informe os dois lados do retângulo. Se for um quadrado, digite 0 para a segunda medida.')
        forma, quadrilatero = calcula_perimetro_quadrilatero(q1, q2)
        if q1 != 0 or q2 != 0:
            st.write(f'O perimetro do {forma} é {quadrilatero}')

if escolha == "Triângulo":
        t1 = st.number_input('Lado 1 do triângulo: ', value=0)
        t2 = st.number_input('Lado 2 do triângulo: ', value=0)
        t3 = st.number_input('Lado 3 do triângulo: ', value=0)
        triangulo = calcula_perimetro_triangulo(t1,t2,t3)
        if t1 != 0 and t2 != 0 and t3 != 0:
            st.write(f'O perimetro do triângulo é {triangulo}')

if escolha == "Círculo":
        c = st.number_input('Raio do circulo: ', value=0)
        circulo = calcula_perimetro_circulo(c)
        if c != 0:
            st.write(f'O perimetro do círculo é {circulo:.2f}')