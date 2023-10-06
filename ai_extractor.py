import os
from constants import OPENAI_API_KEY

from langchain.chains import (create_extraction_chain,
                              create_extraction_chain_pydantic)
from langchain.chat_models import ChatOpenAI

openai_api_key = OPENAI_API_KEY


llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo",
                 openai_api_key=openai_api_key)

def extract(content: str, **kwargs):
    """
    The `extract` function takes in a string `content` and additional keyword arguments, and returns the
    extracted data based on the provided schema.
    """

    if 'schema_dict' in kwargs:
        response = create_extraction_chain(
            schema=kwargs["schema_dict"], llm=llm).run(content)
        response_as_dict = [item for item in response]

        return response_as_dict
    elif 'schema_pydantic' in kwargs:
        response = create_extraction_chain_pydantic(
            pydantic_schema=kwargs["schema_pydantic"], llm=llm).run(content)
        response_as_dict = [item.dict() for item in response]

        return response_as_dict
    else:
        return create_extraction_chain(schema=kwargs["schema"], llm=llm).run(content)

