
import streamlit as st
import networkx as nx

from route_planner import dijkstra
from traffic_analysis import bellman_ford
from connectivity_module import bfs, dfs
from mst_planner import prim_mst, kruskal_mst


st.set_page_config(
    page_title="Smart City Traffic System",
    page_icon="🚦",
    layout="wide",
)

st.title("🚦 Smart City Traffic System")
st.caption("Graph algorithms for route planning and road-network analysis")

# Build the road network.
city = nx.Graph()
city.add_weighted_edges_from([
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
], weight="weight")

nodes = sorted(city.nodes())

st.sidebar.header("Route settings")
source = st.sidebar.selectbox("Starting intersection", nodes, index=0)
destination = st.sidebar.selectbox(
    "Destination intersection",
    nodes,
    index=3,
)

algorithm = st.sidebar.selectbox(
    "Algorithm",
    ["Dijkstra", "Bellman-Ford", "BFS", "DFS", "Prim MST", "Kruskal MST"],
)

congested = st.sidebar.checkbox(
    "Simulate congestion on road B–D",
    value=False,
)

# Apply congestion to this dashboard's independent graph.
if congested:
    city["B"]["D"]["weight"] = 12

st.subheader("Road network")

left, middle, right = st.columns(3)
left.metric("Intersections", city.number_of_nodes())
middle.metric("Roads", city.number_of_edges())
right.metric("Traffic scenario", "Congested" if congested else "Normal")

with st.expander("View road weights", expanded=True):
    st.dataframe(
        [
            {"From": u, "To": v, "Travel time (minutes)": data["weight"]}
            for u, v, data in city.edges(data=True)
        ],
        use_container_width=True,
        hide_index=True,
    )

if st.button("Calculate", type="primary"):
    st.divider()
    st.subheader(f"{algorithm} results")

    if algorithm == "Dijkstra":
        path, cost, updates = dijkstra(city, source, destination)
        if path:
            st.success(" → ".join(path))
            st.metric("Travel time", f"{cost} minutes")
        else:
            st.warning("No route connects these intersections.")

    elif algorithm == "Bellman-Ford":
        path, cost, updates = bellman_ford(city, source, destination)
        if path:
            st.success(" → ".join(path))
            st.metric("Travel time", f"{cost} minutes")
        else:
            st.warning("No route connects these intersections.")

    elif algorithm == "BFS":
        order = bfs(city, source)
        st.write("Traversal order:", " → ".join(order))
        st.caption("BFS explores the network level by level.")

    elif algorithm == "DFS":
        order = dfs(city, source)
        st.write("Traversal order:", " → ".join(order))
        st.caption("DFS explores each branch deeply before backtracking.")

    elif algorithm == "Prim MST":
        edges, cost = prim_mst(city, source)
        st.write("Minimum spanning tree roads:")
        st.dataframe(
            [
                {"From": u, "To": v, "Cost": weight}
                for u, v, weight in edges
            ],
            use_container_width=True,
            hide_index=True,
        )
        st.metric("Total MST cost", cost)

    elif algorithm == "Kruskal MST":
        edges, cost = kruskal_mst(city)
        st.write("Minimum spanning tree roads:")
        st.dataframe(
            [
                {"From": u, "To": v, "Cost": weight}
                for u, v, weight in edges
            ],
            use_container_width=True,
            hide_index=True,
        )
        st.metric("Total MST cost", cost)

    if algorithm in ["Dijkstra", "Bellman-Ford"]:
        with st.expander("Intermediate distance updates"):
            for update in updates:
                st.text(update)

st.divider()
st.caption("Capstone prototype • Synthetic road-network data")