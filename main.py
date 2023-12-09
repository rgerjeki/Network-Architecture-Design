import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.lines import Line2D

# Initialize the graph
G = nx.Graph()

# Nodes and their positions
nodes = {
    "Host 1": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/desktop.png",
    "Host 2": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/desktop.png",
    "Host 3": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/desktop.png",
    "Host 4": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/desktop.png",
    "Host 5": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/desktop.png",
    "Switch 1": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/switch.png",
    "Switch 2": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/switch.png",
    "Router": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/router.png",
    "Firewall": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/firewall.png",
    "Server 1": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/server.png",
    "Server 2": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/server.png",
    "Internet": "/Users/rgerjekiU/Downloads/cybv326_finalProject/imgs/cloud.png"
}

# Adding edges (connections between devices)
wired_edges = [
    ("Host 1", "Switch 1"), ("Host 2", "Switch 1"), ("Host 5", "Switch 1"),
    ("Switch 1", "Router"), ("Switch 2", "Router"),
    ("Router", "Firewall"), ("Firewall", "Internet"),
    ("Server 1", "Internet"), ("Server 2", "Internet")
]

wireless_edges = [
    ("Host 3", "Switch 2"), ("Host 4", "Switch 2")
]

G.add_edges_from(wired_edges)
G.add_edges_from(wireless_edges)

# Define the positions for each node
positions = {
    "Host 1": (0, 1), "Host 2": (0, 2), "Host 3": (2, 1), "Host 4": (2, 2), "Host 5": (0, 3),
    "Switch 1": (1, 2), "Switch 2": (3, 2),
    "Router": (2, 3), "Firewall": (3, 4),
    "Server 1": (4, 3), "Server 2": (4, 4),
    "Internet": (5, 4)
}

fig, ax = plt.subplots()


# Function to draw a box around a group of nodes to represent a network
def draw_network_box(ax, positions, nodes, label, padding=0.1):
    # Extract the positions of the nodes to be boxed
    node_positions = [positions[node] for node in nodes]

    # Find the minimum and maximum points for the box
    min_x = min(pos[0] for pos in node_positions) - padding
    max_x = max(pos[0] for pos in node_positions) + padding
    min_y = min(pos[1] for pos in node_positions) - padding
    max_y = max(pos[1] for pos in node_positions) + padding

    # Draw a rectangle with the min and max as corners
    box = plt.Rectangle((min_x, min_y), max_x - min_x, max_y - min_y,
                        linewidth=2, edgecolor='blue', facecolor='none', label=label, alpha=0.3)
    ax.add_patch(box)

    # Add the label for the box
    ax.text((min_x + max_x) / 2, max_y, label,
            horizontalalignment='center', verticalalignment='bottom',
            fontsize=10, color='blue', weight='bold')


# Define the nodes in each network
network_1_nodes = ["Host 1", "Host 2", "Host 5", "Switch 1"]
network_2_nodes = ["Host 3", "Host 4", "Switch 2"]

# Draw the network boxes
draw_network_box(ax, positions, network_1_nodes, 'Network 1')
draw_network_box(ax, positions, network_2_nodes, 'Network 2')

# Draw wired edges with solid lines
nx.draw_networkx_edges(G, positions, edgelist=wired_edges, ax=ax, width=2, edge_color='black')

# Draw wireless edges with dashed lines
nx.draw_networkx_edges(G, positions, edgelist=wireless_edges, ax=ax, width=2, edge_color='black', style='dashed')

legend_elements = [
    Line2D([0], [0], color='black', lw=2, label='Wired'),
    Line2D([0], [0], color='black', lw=2, ls='dashed', label='Wireless')
]

# Create the legend
ax.legend(handles=legend_elements, loc='upper right')


# Function to create and add an image at a given position with a fixed size
def add_image(ax, path, position, img_size):
    # Read the image file
    img = plt.imread(path)
    # Determine the image size in inches, assuming 100 dpi
    dpi = 100
    zoom_factor = img_size[0] * dpi / img.shape[1]

    # Create an OffsetImage with the zoom factor
    im = OffsetImage(img, zoom=zoom_factor)
    ab = AnnotationBbox(im, position, xycoords='data', frameon=False)
    ax.add_artist(ab)


# Set the desired image size in inches (width x height)
desired_image_size = (0.5, 0.5)  # For example, 0.5 inches by 0.5 inches

# Add images to the nodes with the fixed size
for node, image_path in nodes.items():
    add_image(ax, image_path, positions[node], desired_image_size)


def add_labels(positions, labels, ax, img_size, offset=(0.1, 0.1)):
    for node, (label, ip) in labels.items():
        x, y = positions[node]
        label_x, label_y = x, y - img_size[1] / 2 - offset[1]
        ax.text(label_x, label_y, f"{label}\n{ip}",
                ha='center', va='top',
                fontsize=9, color='black', weight='bold')


# Define your labels and IP addresses for each node
labels = {
    "Host 1": ("Host 1", "192.168.1.2"),
    "Host 2": ("Host 2", "192.168.1.3"),
    "Host 3": ("Host 3", "192.168.2.2"),
    "Host 4": ("Host 4", "192.168.2.3"),
    "Host 5": ("Host 5", "192.168.1.4"),
    "Switch 1": ("Switch 1", "192.168.1.100"),
    "Switch 2": ("Switch 2", "192.168.2.100"),
    "Router": ("Router", "10.0.0.1"),
    "Firewall": ("Firewall", "Public IP"),
    "Server 1": ("Server 1", "Public IP"),
    "Server 2": ("Server 2", "Public IP"),
    "Internet": ("Internet", "")
}

# Call the function to add labels to the diagram after drawing images
add_labels(positions, labels, ax, desired_image_size, offset=(0, 0.06))

# Set the limits, remove the axes and show the plot
ax.set_xlim(-1, 6)
ax.set_ylim(0, 5)
plt.axis('off')
plt.show()
