import asyncio
import pprint

from ai_extractor import extract
from schemas import ecommerce_schema, sahibinden_schema, recipe_schema
from scrape import ascrape_playwright
import json 

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    # Define URLs for news and e-commerce websites
    news_urls = [
        "https://www.cnn.com",
        "https://www.wsj.com",
        "https://www.nytimes.com/ca/"
    ]

    ecommerce_url = "https://www.amazon.ca/s?k=computers&crid=1LUXGQOD2ULFD&sprefix=%2Caps%2C94&ref=nb_sb_ss_recent_1_0_recent"
    sahibinden_url = "https://www.sahibinden.com/mercedes-benz-amg-gt-63-s-4matic"
    recipe_urls = "https://www.allrecipes.com/recipes/723/world-cuisine/european/italian/"

    async def scrape_and_extract(url: str, tags, schema_dict):
        html_content = await ascrape_playwright(url, tags)
        print(html_content)

        print(f"Extracting content from {url} with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(
            schema_dict=schema_dict,
            content=html_content_fits_context_window_llm
        )
        
        print(type(extracted_content))
        extracted_content = f"{extracted_content}"

        file_path = "recipes.txt" #change extension to .json
    
            
        with open(file_path,"w") as f:
            f.write(extracted_content)
            #json.dump(extracted_content,f)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM for news websites
    """for news_url in news_urls:
        asyncio.run(scrape_and_extract(
            url=news_url,
            tags=["span"],
            schema_pydantic=SchemaNewsWebsites
        ))"""

    """# Scrape and Extract with LLM for e-commerce website
    asyncio.run(scrape_and_extract(
        url=ecommerce_url,
        tags=["div", "h2", "p"],
        schema_dict=ecommerce_schema
    ))"""

    # Scrape and Extract with LLM for e-commerce website
    asyncio.run(scrape_and_extract(
        url=recipe_urls,
        tags=["div", "h2", "p","a"],
        schema_dict=recipe_schema
    ))