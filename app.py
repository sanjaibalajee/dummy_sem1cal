# Import Streamlit
import streamlit as st

# Define grades and credits
grades = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "C": 5}
credits = {"math": 4, "chemistry": 3, "physics": 3, "EG": 3, "python": 3,
           "python_lab": 1.5, "chem/phy_lab": 1.5}

# Create title and subtitle
st.title("GPA Calculator")
st.write("Enter your grades for each subject and click on Calculate GPA")
st.write("sanjai/dummy/sem1cal")

# Create input fields for each subject
math_grade = st.selectbox("Math grade", list(grades.keys()))
chem_grade = st.selectbox("Chemistry grade", list(grades.keys()))
phy_grade = st.selectbox("Physics grade", list(grades.keys()))
eg_grade = st.selectbox("EG grade", list(grades.keys()))
py_grade = st.selectbox("Python grade", list(grades.keys()))
py_lab_grade = st.selectbox("Python lab grade", list(grades.keys()))
cp_lab_grade = st.selectbox("Chem/Phy lab grade", list(grades.keys()))

# Create a button to calculate GPA
if st.button("Calculate GPA"):
    # Calculate the total grade points and total credits
    total_gp = (grades[math_grade] * credits["math"] +
                grades[chem_grade] * credits["chemistry"] +
                grades[phy_grade] * credits["physics"] +
                grades[eg_grade] * credits["EG"] +
                grades[py_grade] * credits["python"] +
                grades[py_lab_grade] * credits["python_lab"] +
                grades[cp_lab_grade] * credits["chem/phy_lab"])
    total_credits = sum(credits.values())
    # Calculate the GPA
    gpa = round(total_gp / total_credits, 2)
    # Display the GPA
    st.write(f"Your GPA is {gpa}")
