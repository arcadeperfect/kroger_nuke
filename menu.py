import nuke
import quick_write
import kroger_write
# from kroger_write import submit_button_callback


nodes_toolbar = nuke.toolbar("Nodes")
project_toolbar = nodes_toolbar.addMenu("Kroger")



# Add kroger write node item
project_toolbar.addCommand(
    "Kroger Write Node",
    "kroger_write.kroger_write_node(quick_write._quick_write_node)",
    tooltip="Create a kroger write node that generates write nodes for all views",
)


