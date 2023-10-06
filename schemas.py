from pydantic import BaseModel

ecommerce_schema = {
    "properties": {
        "ilan_basligi": {"type": "string"},
        "araba_fiyati": {"type": "number"},
        "araba_extra_bilgi": {"type": "string"}
    },
    "required": ["ilan_basligi", "araba_fiyati", "araba_extra_bilgi"],
}



sahibinden_schema = {
    "properties": {
        "item_title": {"type": "string"},
        "item_price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}

recipe_schema = {
    "properties": {
        "recipe_title": {"type": "string"},
        "recipe_url": {"type": "string", "sample_format":"https://www.allrecipes.com/recipe/18874/real-italian-calzones/"},
        "recipe_extra_info": {"type": "string"}
    },
    "required": ["recipe_title", "recipe_url", "recipe_extra_info"],
}




class SchemaNewsWebsites(BaseModel):
    news_headline: str
    news_short_summary: str
