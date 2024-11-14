from multi_agents.agents import ChiefEditorAgent

chief_editor = ChiefEditorAgent({
  "query": "Is AI in a hype cycle?",
  "max_sections": 3,
  "follow_guidelines": False,
  "model": "gpt-4o",
  "guidelines": [
    "The report MUST be written in APA format",
    "Each sub section MUST include supporting sources using hyperlinks. If none exist, erase the sub section or rewrite it to be a part of the previous section",
    "The report MUST be written in spanish"
  ],
  "verbose": False
}, websocket=None, stream_output=None)
graph = chief_editor.init_research_team()
graph = graph.compile()


from PIL import Image
import io

from langgraph.graph.graph import CompiledGraph

def ShowGraph(graph:CompiledGraph):


    image_bytes = graph.get_graph().draw_mermaid_png()
    image_stream = io.BytesIO(image_bytes)

    # Open the image with Pillow and display
    img = Image.open(image_stream)
    img.show()  

ShowGraph(graph)