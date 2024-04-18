import streamlit as st
st.title = 'Find largest of the Three numbers'
st.header('IITM streamlit exercise')
st.write('Give 3 numbers which you want largest of:')
num1 = st.number_input("Enter the First number", step =1)
num2 = st.number_input("Enter the Second number", step =1)
num3 = st.number_input("Enter the Third number", step =1)
if(st.button('Get the Max of these numbers')):
    if num1 == num2 or num2 == num3 or num3 == num1:
        st.warning('Give different numbers')
    # Check if the first number is greater than the second and third numbers
    elif num1 > num2 and num1 > num3:
        st.success(num1)

    # Check if the second number is greater than the first and third numbers
    elif num2 > num1 and num2 > num3:
        st.success(num2)

    # Otherwise, the third number must be the greatest
    else:
        st.success(num3)
