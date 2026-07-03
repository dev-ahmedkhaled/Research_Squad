from typing import TypedDict, Optional

class ResearchSchema(TypedDict):
    query: str
    current_query: Optional[str]
    research_results: Optional[list]
    sources: Optional[list]
    draft: Optional[str]
    approved: Optional[bool]

def init_state(user_query: str) -> ResearchSchema:
    return {
        "query": user_query,
        "current_query": user_query,
        "research_results": None,
        "sources": None,
        "draft": None,
        "approved": False,
    }

