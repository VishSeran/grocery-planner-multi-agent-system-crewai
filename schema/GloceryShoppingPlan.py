

from pydantic import BaseModel, Field

from schema.meal_plan_schema import MealPlan
from schema.shopping_category import ShoppingCategory


class GloceryShoppingPlan(BaseModel):
    
    total_budget: str = Field(
        description="Total planned budget"
    )
    
    meal_plans: list[MealPlan] = Field(
        description="Planned meals"
    )
    
    shopping_sections: list[ShoppingCategory] = Field (
        description= "Organized by store sections"
    )
    
    shopping_tips: list[str] = Field (
        description="Money-saving and effciency tips"
    )