import streamlit as st

def FindLargest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def main():
    st.title("TDS Graded Assignment Wk8 : Find the Largest Among Three Numbers")
    st.write("Enter three numbers.")

    num1 = st.number_input("First number:", step=1.0)
    num2 = st.number_input("Second number:", step=1.0)
    num3 = st.number_input("Third number:", step=1.0)

    if st.button("Find Largest"):
        largest = FindLargest(num1, num2, num3)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
