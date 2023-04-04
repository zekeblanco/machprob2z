import streamlit as st
from sympy import *
import pandas as pd
import numpy as np
import math

x = symbols('x')
e = symbols('e')
pi = symbols('pi')
print(math.pi)

st.title("Bisection/Secant Method Calculator")
fnb = st.text_input('Enter the function: ')
a = st.number_input("Enter a", value=0.01)
b = st.number_input("Enter b", value=0.01)

if fnb:
    fbsym = sympify(fnb)

fbsyme = fbsym.subs(e,math.e)
fbsympi = fbsyme.subs(pi,math.pi)

choice = st.radio('Choose one ', ['Iteration', 'Error'])
if choice == 'Iteration':
    iter = st.number_input("Enter no. of iterations ", value=1)
if choice == 'Error':
    error = st.number_input("Enter error. ", value = 0.000001)

choice2= st.radio('Choose a method ', ['Bisection', 'Secant'])

if (choice == 'Iteration') and choice2 == ('Bisection'):
    count = 2
    c = (a+b)/2
    d = N(fbsympi, subs={x: c})
    ee = abs(float(a)-(b))
    data = {
        "a": [a],
        "b": [b],
        "c": [c],
        "f(c)": [d],
        "|a-b|": [ee]
    }
    df = pd.DataFrame(data)

    while count <= iter:
        if d < 0:
            b = c
        else:
            a = c

        count += 1
        c = (a + b) / 2
        d = N(fbsympi, subs={x: c})
        ee = abs(a - b)

        new_row = {'a': a, 'b': b, 'c': c, 'f(c)': d, '|a-b|':[ee]}
        df = pd.concat([df, pd.DataFrame(new_row)])

    st.write("---")
    st.write("Cn= ", c)
    st.write("f(Cn)= ", d)

    # Display the dataframe in a table
    st.write("---")
    st.write("Table:")
    df.index = np.arange(1, len(df) + 1)
    st.write(df)

elif (choice == 'Error') and choice2 == ('Bisection'):
    c = (a + b) / 2
    d = N(fbsympi, subs={x: c})
    ee = abs(a - b)
    data = {
        "a": [a],
        "b": [b],
        "c": [c],
        "f(c)": [d],
        "|a-b|": [ee]
    }
    df = pd.DataFrame(data)

    while error <= ee:
        if N(fbsympi, subs={x: a})*d > 0:
            a = c
        elif N(fbsympi, subs={x: b})*d > 0
            b = c

        c = (a + b) / 2
        d = N(fbsympi, subs={x: c})
        ee = abs(a - b)

        new_row = {'a': a, 'b': b, 'c': c, 'f(c)': d, '|a-b|':[ee]}
        df = pd.concat([df, pd.DataFrame(new_row)])

    st.write("---")
    st.write("Error= ", error)
    st.write("Cn= ", c)
    st.write("f(Cn)= ", d)

    # Display the dataframe in a table
    st.write("---")
    st.write("Table:")
    df.index = np.arange(1, len(df) + 1)
    st.write(df)

elif (choice == 'Iteration') and choice2 == ('Secant'):
    count = 2
    c = N(fbsympi, subs={x: a})
    d = N(fbsympi, subs={x: b})
    ee = (b - ((d) * (b - a) / (d - c)))
    f = abs(ee - b)
    data = {
        "Xi-1": [a],
        "Xi": [b],
        "f(Xi-1)": [c],
        "f(Xi)": [d],
        "Xi+1": [ee],
        "|Xi+1 - Xi|": [f],
    }
    df = pd.DataFrame(data)

    while count <= iter:
        tempa = b
        tempb = ee

        a = tempa
        b = tempb
        count += 1
        c = N(fbsympi, subs={x: a})
        d = N(fbsympi, subs={x: b})
        ee = (b - ((d) * (b - a) / (d - c)))
        f = abs(ee - b)

        new_row = {'Xi-1': a, 'Xi': b, 'f(Xi-1)': c, 'f(Xi)': d, 'Xi+1': ee, '|Xi+1 - Xi|': [f]}
        df = pd.concat([df, pd.DataFrame(new_row)])

    st.write("---")
    st.write("Cn= ", c)
    st.write("f(Cn)= ", d)

    # Display the dataframe in a table
    st.write("---")
    st.write("Table:")
    df.index = np.arange(1, len(df) + 1)
    st.write(df)
else:
    c = N(fbsympi, subs={x: a})
    d = N(fbsympi, subs={x: b})
    ee = (b - ((d)*(b-a)/(d-c)))
    f = abs(ee-b)
    data = {
        "Xi-1": [a],
        "Xi": [b],
        "f(Xi-1)": [c],
        "f(Xi)": [d],
        "Xi+1": [ee],
        "|Xi+1 - Xi|": [f],
    }
    df = pd.DataFrame(data)
    
    while error <= f:
        tempa = b
        tempb = ee

        a = tempa
        b = tempb
        c = N(fbsympi, subs={x: a})
        d = N(fbsympi, subs={x: b})
        ee = (b - ((d) * (b - a) / (d - c)))
        f = abs(ee - b)

        new_row = {'Xi-1': a, 'Xi': b, 'f(Xi-1)': c, 'f(Xi)': d, 'Xi+1': ee, '|Xi+1 - Xi|': [f]}
        df = pd.concat([df, pd.DataFrame(new_row)])

    st.write("---")
    st.write("Error= ", error)
    st.write("Cn= ", ee)
    st.write("f(Cn)= ", N(fbsympi, subs={x: ee}))

    # Display the dataframe in a table
    st.write("---")
    st.write("Table:")
    df.index = np.arange(1, len(df) + 1)
    st.write(df)
