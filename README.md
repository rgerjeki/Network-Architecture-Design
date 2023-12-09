# Network Diagram Script

This Python script generates a network diagram using Matplotlib and NetworkX. It is designed to be customizable and extendable for various network architectures.

<a href="https://ibb.co/Nskf1M0"><img src="https://i.ibb.co/VthbHsF/network-Diagram.png" alt="network-Diagram" border="0" /></a>

## How to Run the Script

To run the script, you will need Python installed on your system along with the `matplotlib` and `networkx` libraries. If you don't have these libraries installed, you can install them using pip:

```

pip install matplotlib networkx

```

Once you have the required libraries, you can run the script with the following command:

```

python main.py

```

Ensure that `main.py` is in your current working directory.

## Script Details

The script works by creating a graph object using NetworkX and then adding nodes and edges to represent hosts, switches, routers, and other network components. The Matplotlib library is used for visualizing this graph.

### Network Components

- **Hosts**: Represented by nodes labeled `Host 1`, `Host 2`, etc.

- **Switches**: Represented by nodes labeled `Switch 1`, `Switch 2`, etc.

- **Router**: Represented by a node labeled `Router`.

- **Firewall**: Represented by a node labeled `Firewall`.

- **Servers**: Represented by nodes labeled `Server 1`, `Server 2`, etc.

- **Internet**: Represented by a node labeled `Internet`.

### Edges

- **Wired Connections**: Represented by solid lines between nodes.

- **Wireless Connections**: Represented by dashed lines between nodes.

### Customizing the Architecture

To modify the network architecture, adjust the following variables in the script:

- `nodes`: A dictionary where keys are node labels and values are paths to images representing the nodes.

- `wired_edges` and `wireless_edges`: Lists of tuples representing the connections between nodes.

Example:

```python

nodes = {

    "Host 1": "path/to/image.png",

    # Add or modify nodes as needed

}

wired_edges = [

    ("Host 1", "Switch 1"),

    # Add or modify wired edges as needed

]

wireless_edges = [

    ("Host 3", "Switch 2"),

    # Add or modify wireless edges as needed

]

```

### Positioning Nodes Manually

Manually positioning nodes in the network diagram allows for precise control over the layout, ensuring that each component is placed logically according to its function within the network. Follow these steps to position nodes manually:

#### Understanding Coordinates

The network diagram is laid out in a two-dimensional plane where each node's position is defined by an (x, y) coordinate:
- The `x` coordinate determines the node's horizontal position, with higher values moving the node to the right.
- The `y` coordinate determines the node's vertical position, with higher values moving the node upward.

#### Steps to Position Nodes

1. **Identify Components**: List all the network components you wish to include in the diagram, such as hosts, switches, routers, servers, etc.

2. **Determine Layout**: Sketch a rough layout of the network on paper. Decide where you want to place each type of component. For example, you might place:
   - Routers and switches towards the center.
   - Servers above or to the right of the routers.
   - Hosts below or to the left of the switches.

3. **Assign Coordinates**:
   - Start with the central components such as routers and switches. Assign them coordinates with the router at the center (e.g., `(0.5, 0.5)` if you want to use normalized coordinates between 0 and 1).
   - Place other components relative to the central ones. For example, if hosts connect to a switch, they should be near the switch's coordinates.

4. **Use the Positions Dictionary**: In the script, you will find (or need to create) a `positions` dictionary where you'll map each component's label to its (x, y) coordinates.

Example:

```python
positions = {
    "Router": (0.5, 0.5),  # Central position
    "Switch 1": (0.3, 0.5),  # To the left of the router
    "Host 1": (0.1, 0.3),  # Below and to the left of Switch 1
    "Server 1": (0.7, 0.7),  # Above and to the right of the router
    # ... add more nodes with their positions
}
```

1.  **Edit the Positions Dictionary**:

    -   Open the script in a text editor.
    -   Locate the `positions` dictionary.
    -   Edit the entries to match the layout you designed. You can add new entries for new components or modify existing ones.
2.  **Run the Script**: After saving the changes, run the script to generate the diagram. Check if the components are placed as desired.

3.  **Iterate**: It's common to need several iterations to get the layout just right. Adjust the coordinates in the `positions` dictionary and re-run the script as needed.

#### Tips for Manual Positioning

-   **Keep it Simple**: Start with a simple layout and gradually add complexity.
-   **Group Related Components**: Place related components (like hosts connected to the same switch) close together.
-   **Avoid Overlap**: Ensure that nodes and labels do not overlap for clarity.
-   **Use Consistent Spacing**: Try to keep uniform distances between similar components for a neat appearance.

Remember, the beauty of manual positioning is that you have complete control over the appearance of your network diagram. Take your time to design a layout that is both functional and visually appealing.

### Adding New Images

To add new images for the network components, follow these steps:

1\. Place the new image in the directory accessible by the script.

2\. Update the `nodes` dictionary with the label of the node and the path to the new image.

Example:

```python

nodes = {

    "New Host": "path/to/new_image.png"

}

```

3\. Add the node to the `positions` dictionary with the desired coordinates.

Example:

```python

positions = {

    "New Host": (x, y)

}

```

4\. If this new host needs to connect to other components, add the appropriate edge to either `wired_edges` or `wireless_edges`.

### Diagram Layout

- The `positions` dictionary defines the x, y coordinates for each node.

- The `draw_network_box` function is used to draw a box around a group of nodes, indicating a network segment.

This README provides a basic guide for users to understand how to run the script and make modifications. Adjust the content as necessary to match the specific functionalities and configurations in your script.

### Author

[rgerjeki](https://github.com/rgerjeki)

Feel free to reach out if you have any questions or feedback!
