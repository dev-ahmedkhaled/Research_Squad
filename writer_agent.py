from StateSchema import ResearchSchema
from llm_core import LLM



def writer_agent(state: ResearchSchema,llm:LLM ) -> ResearchSchema:
    prompt= f"""
    Original Query: {state['query']}
    Research Results: {state['research_results']}
    Sources: {state['sources']}
    You are a writer agent tasked to generate a draft based on the original query, research results
    write a draft that is informative, well-structured, and engaging and simple to understand for the users with no prior knowledge of the topic. 
    Use the research results and sources to support your writing. Ensure that the draft is coherent and flows logically from one point to the next.
    """

    state['draft'] = llm.generate_response(prompt).content
    return state