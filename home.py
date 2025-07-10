import streamlit as st

st.set_page_config(page_title="Tutoring Signup Form", page_icon="📝")
st.title("Tutoring Signup Form")

st.markdown("""
<style>
.input-row {
    display: flex;
    align-items: center;
    margin-bottom: 1.5em;
}
.input-label {
    width: 180px;
    font-size: 1.2em;
    font-family: 'Comic Sans MS', 'Comic Sans', cursive;
}
</style>
""", unsafe_allow_html=True)

def input_row(label, key, **kwargs):
    col1, col2 = st.columns([1,2])
    with col1:
        st.markdown(f'<div class="input-label">{label}</div>', unsafe_allow_html=True)
    with col2:
        return st.text_input("", key=key, **kwargs)


# Default fields for a tutor signup page
first_name = input_row("First Name", "first_name")
last_name = input_row("Last Name", "last_name")
email = input_row("Email Address", "email")
phone = input_row("Phone Number", "phone")
subjects = input_row("Subjects You Can Tutor", "subjects")
availability = input_row("Availability (Days/Times)", "availability")
experience = input_row("Tutoring Experience", "experience")
background = input_row("Educational Background", "background")


if st.button("Submit"):
    if not (first_name and last_name and email):
        st.warning("Please fill in all required fields (First Name, Last Name, Email Address).")
    else:
        st.success(f"Thank you for signing up, {first_name} {last_name}!")
        st.write("**Email:**", email)
        st.write("**Phone Number:**", phone)
        st.write("**Subjects You Can Tutor:**", subjects)
        st.write("**Availability:**", availability)
        st.write("**Tutoring Experience:**", experience)
        st.write("**Educational Background:**", background)