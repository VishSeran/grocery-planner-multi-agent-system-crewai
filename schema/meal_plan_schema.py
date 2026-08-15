from pydantic import BaseModel, Field

class MealPlanner(BaseModel):

    name: str = Field(description="name of the meal")
    difficulty_level: str = Field(description="'Easy', 'Medium', 'Hard'")
    servings: int = Field(description="Number of people it serves")
    researched_ingredients: list[str] = Field(
        description="Ingredients found through research"
    )