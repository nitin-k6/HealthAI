# crew.py
from crewai import Crew
from agents import HealthcareAgents
from tasks import HealthcareTasks

class HealthcareCrew:
    def __init__(self, model_version="gemini-2.0-flash"):
        # Initialize agents
        healthcare_agents = HealthcareAgents(model_version)
        self.diagnosis_agent = healthcare_agents.diagnosis_agent
        self.researcher_agent = healthcare_agents.researcher_agent
        self.treatment_agent = healthcare_agents.treatment_agent
        self.health_educator_agent = healthcare_agents.health_educator_agent
        
        # Initialize task creator
        self.tasks_creator = HealthcareTasks()
    
    def run_diagnosis_workflow(self, user_input, patient_info=""):
        """Run a complete diagnosis workflow with all agents"""
        
        # Step 1: Initial diagnosis
        diagnosis_task = self.tasks_creator.create_diagnosis_task(
            self.diagnosis_agent, user_input
        )
        
        # Create a crew with just the diagnosis agent
        initial_crew = Crew(
            agents=[self.diagnosis_agent],
            tasks=[diagnosis_task],
            verbose=True
        )
        
        # Execute to get diagnosis
        diagnosis_result = initial_crew.kickoff()
        
        # Extract the result text from the CrewOutput object
        # This handles different possible return types from CrewAI
        if hasattr(diagnosis_result, 'raw_output'):
            diagnosis_text = diagnosis_result.raw_output
        elif hasattr(diagnosis_result, 'final_output'):
            diagnosis_text = diagnosis_result.final_output
        elif isinstance(diagnosis_result, str):
            diagnosis_text = diagnosis_result
        else:
            # If we can't extract the text directly, convert to string
            diagnosis_text = str(diagnosis_result)
        
        # Extract the first line to use as the main condition
        # In a real app, you might parse this more carefully
        condition_lines = diagnosis_text.split("\n")
        condition = condition_lines[0] if condition_lines else "Unknown condition"
        
        # Step 2: Research and treatment recommendation
        research_task = self.tasks_creator.create_research_task(
            self.researcher_agent, condition
        )
        
        treatment_task = self.tasks_creator.create_treatment_task(
            self.treatment_agent, condition, patient_info
        )
        
        education_task = self.tasks_creator.create_education_task(
            self.health_educator_agent, condition
        )
        
        # Create the full crew with all agents and tasks
        full_crew = Crew(
            agents=[
                self.researcher_agent,
                self.treatment_agent,
                self.health_educator_agent
            ],
            tasks=[
                research_task,
                treatment_task,
                education_task
            ],
            verbose=True
        )
        
        # Execute all tasks
        final_results = full_crew.kickoff()
        
        # Process the final results
        if hasattr(final_results, 'raw_output'):
            final_text = final_results.raw_output
        elif hasattr(final_results, 'final_output'):
            final_text = final_results.final_output
        elif isinstance(final_results, str):
            final_text = final_results
        else:
            # If we can't extract the text directly, convert to string
            final_text = str(final_results)
        
        # Return all results
        return {
            "diagnosis": diagnosis_text,
            "full_report": final_text
        }