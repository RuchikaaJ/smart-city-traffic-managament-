# 🚦 Smart City Traffic System

A Streamlit web app that applies classic graph algorithms to model a city's road network, plan routes, analyse traffic, check connectivity and design cost-efficient road layouts.

Roads and intersections are represented as a weighted graph (built with NetworkX), and each module runs a different algorithm on that graph so you can compare how they behave.

---

## ✨ Features

| Module | Algorithm(s) | What it does |
|---|---|---|
| **Route Planner** | Dijkstra | Finds the shortest path between two locations in the road network |
| **Traffic Analysis** | Bellman-Ford | Computes shortest paths when edge weights vary (e.g. congestion penalties) and handles negative weights |
| **Connectivity Module** | BFS, DFS | Explores which areas of the city are reachable from a given point |
| **MST Planner** | Prim's, Kruskal's | Builds a minimum spanning tree: the cheapest set of roads that still connects every location |

---

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** for the interactive web interface
- **NetworkX** for graph construction and visualisation

---

## 📁 Project Structure

```
smart-city-traffic-system/
├── App.py                  # Streamlit app (entry point)
├── route_planner.py        # Dijkstra's shortest path
├── traffic_analysis.py     # Bellman-Ford
├── connectivity_module.py  # BFS and DFS traversal
├── mst_planner.py          # Prim's and Kruskal's MST
├── requirements.txt        # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/RuchikaaJ/smart-city-traffic-managament-.git
cd smart-city-traffic-managament-
```

### 2. (Optional) Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run App.py
```

The app opens in your browser at `http://localhost:8501`.

---

## 🧠 How It Works

1. A road network is built as a weighted graph where **nodes** are intersections or locations and **edges** are roads weighted by distance or travel cost.
2. Each module imports its algorithm and runs it on this graph.
3. `App.py` ties everything together in a Streamlit interface, so you can pick inputs and see results immediately.

### Algorithm Complexity

| Algorithm | Time Complexity | Used For |
|---|---|---|
| Dijkstra | O((V + E) log V) | Shortest route (non-negative weights) |
| Bellman-Ford | O(V · E) | Shortest route with variable or negative weights |
| BFS / DFS | O(V + E) | Reachability and connectivity |
| Prim's / Kruskal's | O(E log V) | Minimum-cost road network |
---

### Output 
<img width="1866" height="972" alt="image" src="https://github.com/user-attachments/assets/76236ed7-a724-42ba-bc0d-1a41f1493948" />
<img width="1882" height="1007" alt="image" src="https://github.com/user-attachments/assets/17743945-510a-41e1-a04d-548669e3a42c" />



## 🔮 Future Improvements

- Load real road-network data (e.g. OpenStreetMap)
- Simulate live traffic with changing edge weights
- Add A* search for faster route planning
- Interactive map-based visualisation
- Deploy online with Streamlit Community Cloud

---
**Ruchika Jaiswal**
GitHub: [@RuchikaaJ](https://github.com/RuchikaaJ)
