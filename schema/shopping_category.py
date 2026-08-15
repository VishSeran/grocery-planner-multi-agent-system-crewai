from pydantic import BaseModel, Field

from schema.glocery_item_planner import GloceryItem


class ShoppingCategory(BaseModel):
    
    section_name: str = Field(
        description="Store section (example: 'Produce', 'Dairy')"
    )
    items: list[GloceryItem] = Field(
        description="Items in this section"
    )
    estimated_total: str = Field(
        description="Estimated cost for this section"
    )