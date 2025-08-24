from langgraph.graph import  MessagesState
from langgraph.constants import START, END
from langgraph.graph import StateGraph

class GraphState(MessagesState):
    pass

def to_do(state: GraphState):
    return {"messages": "hi"}


class Agent:
    def __init__(self):
        builder = StateGraph(GraphState)
        builder.add_node("to_do", to_do)

        builder.add_edge(START, "to_do")
        builder.add_edge("to_do", END)
        
        self.graph = builder.compile()

        graph_image = self.graph.get_graph().draw_mermaid_png()
        with open("static/chatbot_agent.png", "wb") as f:
            f.write(graph_image)