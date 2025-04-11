# app.py
import streamlit as st
from crew import HealthcareCrew
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if the API key is set
if not os.getenv("GOOGLE_API_KEY"):
    st.error("Google API key is not set. Please add it to your .env file.")
    st.stop()

# Set page configuration
st.set_page_config(
    page_title="Healthcare Assistant",
    page_icon="🏥",
    layout="wide"
)

# Initialize the crew with model selection
@st.cache_resource
def load_crew(model_version):
    return HealthcareCrew(model_version)

# App header
st.title("🏥 Healthcare Assistant")
st.markdown("""
This application uses multiple AI agents to provide healthcare information:
- **Diagnosis Assistant**: Analyzes symptoms
- **Medical Researcher**: Provides latest medical information
- **Treatment Advisor**: Suggests potential treatments
- **Health Educator**: Explains medical concepts simply
""")

st.warning("**Disclaimer**: This is a demonstration only. Always consult with healthcare professionals for medical advice.")

# Model selection
model_version = st.selectbox(
    "Select Gemini Model",
    ["gemini-2.0-flash", "gemini-1.5-flash"],
    index=0
)

# Initialize the crew with selected model
healthcare_crew = load_crew(model_version)

# User input form
with st.form("health_query_form"):
    user_symptoms = st.text_area("Describe your symptoms or health concerns in detail:", 
                                height=150,
                                placeholder="Example: I've been experiencing headaches for the past week, particularly in the morning. I also feel dizzy when standing up quickly...")
    
    st.subheader("Additional Information (Optional)")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=30)
        height = st.number_input("Height (cm)", min_value=0, max_value=250, value=170)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        weight = st.number_input("Weight (kg)", min_value=0, max_value=500, value=70)
    
    medical_history = st.text_area("Relevant medical history or conditions:", 
                                  placeholder="Example: Diagnosed with hypertension 2 years ago, family history of diabetes...")
    
    medications = st.text_area("Current medications:", 
                             placeholder="Example: Lisinopril 10mg daily, Metformin 500mg twice daily...")
    
    submit_button = st.form_submit_button("Get Health Analysis")

# Process the request when submitted
# In app.py - update the results display section

# Process the request when submitted
if submit_button and user_symptoms:
    # Show a spinner while processing
    with st.spinner("The healthcare agents are analyzing your information. This may take a few minutes..."):
        # Prepare patient info
        patient_info = f"Age: {age}, Gender: {gender}, Height: {height}cm, Weight: {weight}kg"
        if medical_history:
            patient_info += f", Medical History: {medical_history}"
        if medications:
            patient_info += f", Medications: {medications}"
        
        # Run the crew with the input
        try:
            results = healthcare_crew.run_diagnosis_workflow(user_symptoms, patient_info)
            
            # Display results in expandable sections
            st.success("Analysis complete!")
            
            # Display diagnosis section
            st.subheader("Initial Assessment")
            if "diagnosis" in results and results["diagnosis"]:
                st.markdown(results["diagnosis"])
            else:
                st.warning("No diagnosis information available")
            
            # Display full report
            st.subheader("Detailed Information")
            if "full_report" in results and results["full_report"]:
                st.markdown(results["full_report"])
            else:
                st.info("No detailed report available")
            
        except Exception as e:
            st.error(f"An error occurred during the analysis: {str(e)}")
            st.info("Please try again with more specific information or contact support if the issue persists.")
            # Print the exception for debugging
            import traceback
            st.code(traceback.format_exc())
else:
    if submit_button:
        st.warning("Please enter your symptoms or health concerns.")



















