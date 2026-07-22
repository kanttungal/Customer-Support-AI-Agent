from typing import TypedDict

class AgentState(TypedDict):
    query:str

    category:str

    context:str

    chat_history:list

    sources:list

    session:dict
    
    final_answer:str
    