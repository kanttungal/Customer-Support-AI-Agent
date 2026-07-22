from langchain_community.tools.tavily_search import TavilySearchResults
from settings import MAX_SEARCH_RESULTS

search_tool = TavilySearchResults(
    max_results = MAX_SEARCH_RESULTS
)

def web_search(query:str):

    """
    Search latest Information from Internet.
    """

    result = search_tool.invoke(query)
    return result


