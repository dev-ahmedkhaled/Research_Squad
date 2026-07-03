from StateSchema import ResearchSchema
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import create_agent
from llm_core import LLM


def search_tool(query: str) -> list:
    """"search_tool is a tool that takes a query and returns a list of search results and its links. It uses the DuckDuckGoSearchRun tool from langchain_community to perform the search."""
    search = DuckDuckGoSearchResults(output_format="list")
    results = search.run(query)
    links = [result['link'] for result in results]
    return links,results



def research_agent(state: ResearchSchema,llm: LLM) -> ResearchSchema:
    if state.get("research_results") is None:
        links,results = search_tool(state['current_query'])
        state["research_results"] = results
        state["sources"] = links
        
    else:
       
        prompt=f"""
            Original Query: {state['query']}
            previous research results: {state['research_results']}
            you are a research agent tasked to improve previous query and to generate a new query that will yield better results.
            """
        state['current_query'] = llm.generate_response(prompt).content
        links,results = search_tool(state['current_query'])
        state["research_results"] = results
        state["sources"] = links
    return state
    








