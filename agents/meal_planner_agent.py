
from crewai import Agent
from crewai_tools import SerperDevTool

from configs.logger import get_logger



logger = get_logger("meal_planner")

class MealPlannerAgent:
    
    def __init__(self):
        
        self.meal_planner_agent:Agent = Agent(
            role = "Meal planner & recipe researcher",
            goal = "Search for optimal recipes and create detailed meal plans",
            backstory = "A skilled meal planner who researches the best recipes online, considering dietary needs, cooking skill levels, and budget constraints.",
            tools = [SerperDevTool()]
            
        )