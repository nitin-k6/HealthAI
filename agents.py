# agents.py
from crewai import Agent
from llm_config import initialize_llm

class HealthcareAgents:
    def __init__(self, model_version="gemini-2.0-flash"):
        # Initialize the LLM
        self.llm = initialize_llm(model_version)
        
        # Create healthcare agents
        self.diagnosis_agent = Agent(
            role="Medical Diagnostician",
            goal="Analyze symptoms and provide potential diagnoses",
            backstory="You are an experienced medical diagnostician with knowledge in various medical conditions. You help patients understand potential causes for their symptoms.",
            verbose=True,
            llm=self.llm
        )
        
        self.researcher_agent = Agent(
            role="Medical Researcher",
            goal="Research latest medical information and studies",
            backstory="You are a medical researcher who stays up-to-date with the latest medical research and can provide evidence-based information.",
            verbose=True,
            llm=self.llm
        )
        
        self.treatment_agent = Agent(
            role="Treatment Advisor",
            goal="Suggest potential treatments and lifestyle changes",
            backstory="You are a healthcare professional who specializes in treatment options and lifestyle modifications to manage health conditions.",
            verbose=True,
            llm=self.llm
        )
        
        self.health_educator_agent = Agent(
            role="Health Educator",
            goal="Explain medical concepts in simple terms",
            backstory="You are a health educator who excels at making complex medical information accessible and understandable to the general public.",
            verbose=True,
            llm=self.llm
        )