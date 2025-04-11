# tasks.py
from crewai import Task

class HealthcareTasks:
    def create_diagnosis_task(self, agent, user_input):
        return Task(
            description=f"Analyze the following symptoms and provide potential diagnoses: {user_input}",
            expected_output="A list of potential conditions that match the symptoms, with probability assessments and reasoning.",
            agent=agent
        )
    
    def create_research_task(self, agent, condition):
        return Task(
            description=f"Research the latest information about: {condition}",
            expected_output="A summary of the latest research, treatments, and medical understanding of this condition.",
            agent=agent
        )
    
    def create_treatment_task(self, agent, condition, patient_info):
        return Task(
            description=f"Suggest potential treatments for {condition} considering patient information: {patient_info}",
            expected_output="A comprehensive list of treatment options, lifestyle changes, and considerations specific to the patient.",
            agent=agent
        )
    
    def create_education_task(self, agent, medical_concept):
        return Task(
            description=f"Explain the following medical concept in simple terms: {medical_concept}",
            expected_output="A clear, simple explanation of the medical concept that a layperson could understand.",
            agent=agent
        )