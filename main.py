from core import graph
from StateSchema import init_state





if __name__ == "__main__":
    uquery = input("Enter your research query: ")
    state=init_state(user_query=uquery)
    compiled_graph=graph()
    final_state=compiled_graph.invoke(state)
    print(final_state["draft"])