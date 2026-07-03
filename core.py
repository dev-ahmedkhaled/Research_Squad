from critic import critic_agent
from llm_core import LLM
from StateSchema import ResearchSchema
from writer_agent import writer_agent
from research_agent import research_agent
from functools import partial

from langgraph.graph import START,END,StateGraph


def should_end(state: ResearchSchema) -> str:
    if state.get("approved"):
        return "end"
    else:
        return "research"

def graph()-> StateGraph:
    model= LLM()
    graph= StateGraph(state_schema=ResearchSchema)
    graph.add_node("research_agent", partial(research_agent,llm=model))
    graph.add_node("writer_agent", partial(writer_agent,llm=model))
    graph.add_node("critic_agent", partial(critic_agent,llm=model))


    graph.add_edge(START,"research_agent")
    graph.add_edge("research_agent","writer_agent")
    graph.add_edge("writer_agent","critic_agent")
    graph.add_conditional_edges("critic_agent",should_end,{
        "research": "research_agent",
        "end": END
    })


    compiled_graph=graph.compile()
    return compiled_graph



















