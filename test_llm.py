# test_llm.py
from llm_config import initialize_llm
from crewai import Agent, Task, Crew

# Initialize the LLM
llm = initialize_llm("gemini-2.0-flash")

# Create a test agent
test_agent = Agent(
    role="Test Agent",
    goal="Test if the Gemini integration works",
    backstory="You are testing the integration between CrewAI and Gemini 2.0 Flash",
    verbose=True,
    llm=llm
)

# Create a simple test task
test_task = Task(
    description="Say hello and confirm you're a healthcare assistant running on Gemini 2.0 Flash",
    expected_output="A confirmation message",
    agent=test_agent
)

# Create a test crew
test_crew = Crew(
    agents=[test_agent],
    tasks=[test_task],
    verbose=True
)

# Run the test
print("Testing CrewAI with Gemini 2.0 Flash...")
result = test_crew.kickoff()
print("\nResult:", result)