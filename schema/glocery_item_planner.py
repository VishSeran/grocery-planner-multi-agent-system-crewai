from pydantic import BaseModel, Field

class GloceryItem(BaseModel):
    
    name:str = Field(description="Name of the glocery item")
    quantity: str = Field(description="Quantity needed (for example: '2 lbs', '1 gallon')")
    estimated_price: str = Field(description="Estimated price of the glocery item (for example: '$5-10' )")
    category: str = Field(description="Store section (for example: 'produce', 'dairy')")
    
    
    