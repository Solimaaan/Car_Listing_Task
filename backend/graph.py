from langgraph.graph import StateGraph, END
from backend.nodes.prompt_filter import filter_input
from backend.nodes.image_extraction import extract_image
from backend.nodes.feature_extraction import extract_text
from backend.nodes.email_sender import convert_to_json
from backend.state import CarState

def build_graph():
    builder = StateGraph(CarState)

    #Nodes
    builder.add_node("filter", filter_input)
    builder.add_node("input", extract_text)
    builder.add_node("image_extraction", extract_image)
    builder.add_node("output", convert_to_json)

    #Entry point
    builder.set_entry_point("filter")

    #Edges
    builder.add_edge("filter", "input")
    builder.add_edge("input", "image_extraction")
    builder.add_edge("image_extraction", "output")
    builder.add_edge("output", END)

    return builder.compile()

def run_chat_graph(input_text,image) -> str:
    graph = build_graph()
    #print("graph built")

    state: CarState = {
        "input": input_text,
        "filtered_input": "",
        "image": image,
        "output": {}
    }

    result = graph.invoke(state)
    

    return result.get("output","error")
