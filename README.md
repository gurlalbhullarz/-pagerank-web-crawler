# PageRank Web Crawler & Visualization
![PageRank Visualization](assets/graph-preview.png)

![MIT License](https://img.shields.io/badge/license-MIT-green)

This project is a **Python-based simulation of a search engine ranking system** inspired by Google’s original **PageRank algorithm**.

It crawls web pages, stores link relationships in a database, computes PageRank scores using an iterative algorithm, and visualizes the web structure as an interactive graph.

This project helped me connect Python programming with real-world concepts in web development and algorithms.
I hope this project can also serve as a learning guide for others who want to explore crawling, graph structures, and data visualization.

This is an **educational project** focused on understanding how search engines work internally.


---

## 📌 What This Project Does

- Crawls web pages starting from a seed URL  
- Extracts and stores links between pages  
- Builds a directed graph of the website  
- Computes PageRank scores iteratively  
- Visualizes the web graph using D3.js  

---

## 🛠️ Technologies Used

- Python  
- SQLite  
- BeautifulSoup  
- urllib  
- D3.js  
- HTML / JavaScript  

---

## 📂 Project Structure

```
pagerank-web-crawler/
├── spider.py        # Web crawler
├── sprank.py        # PageRank algorithm
├── spdump.py        # Link inspection tool
├── spjson.py        # Graph data generator
├── force.html       # Visualization (D3.js)
├── spider.js        # Generated graph data
├── .gitignore
└── README.md
```

---

## ✅ Prerequisites

- Python 3.7 or later
- Install dependency:

```bash
pip install beautifulsoup4


⸻

▶️ How to Run

1. Crawl the website

python spider.py

	•	Enter a starting URL when prompted
	•	Crawling is limited to one domain for ethical reasons
    •	The crawler fetches pages from the same domain.
	•	It stores the link structure for PageRank computation.
	•	Tip for beginners: Start with small websites so the visualization is manageable.

⸻
2. Compute PageRank

Run the PageRank calculation:

python sprank.py

	•	Enter the number of iterations (e.g., 10).
	•	The script calculates PageRank scores for each page.
	•	Learning point: Try different iteration counts and see how the PageRank scores stabilize.

⸻

3. Inspect the Graph (Optional)

To see the raw link structure:

python spdump.py

	•	Prints pages and their outgoing links.
	•	Helpful to understand how the crawler builds the graph.

⸻

4. Export Graph for Visualization

python spjson.py

	•	Generates graph.json with nodes and links.
	•	Nodes include PageRank scores for visualization.

⸻

5. Visualize the Graph

Serve the files using a local server:

python -m http.server

	•	Open your browser at http://localhost:8000/force.html.
	•	Nodes are sized by PageRank; links show page connections.
	•	Drag nodes for better visualization.
	•	Tip: For larger graphs, consider showing only the top-ranked pages to keep the visualization smooth.

⸻

📘 What I Learned
	•	How web crawlers work internally
	•	How PageRank distributes importance across links
	•	How iterative algorithms converge
	•	Practical use of graph theory
	•	Connecting backend data with frontend visualization

I also realized the importance of small, step-by-step experiments in programming — testing my crawler with a few pages first, checking outputs with spdump.py, and then moving to visualization.

⸻

Beginner Tips
	•	Start with small websites to avoid slow visualization.
	•	Inspect your graph with spdump.py before visualizing to understand what is happening behind the scenes.
	•	Experiment with different damping factors in sprank.py to see how PageRank changes.
	•	Make small modifications (crawl depth, max pages) to explore Python coding and crawling logic.
	•	Don’t be afraid to break things — experimenting is the best way to learn.

⸻

Possible Improvements
	•	Handle invalid URLs and network errors gracefully.
	•	Limit crawl depth or maximum number of pages for safety.
	•	Respect robots.txt and add polite delays between requests.
	•	Add labels or tooltips in the visualization to show URLs or PageRank.
	•	Modularize the code into reusable functions.
	•	Optimize PageRank computation using NumPy or sparse matrices for larger graphs.

⸻
⸻

⚠️ Notes
	•	Crawling is domain-restricted by design
	•	Visualization performance depends on node count
	•	This is not a production search engine

⸻

🙏 Acknowledgment

Inspired by the Python for Everybody course
by Dr. Charles R. Severance (Coursera)

⸻

👤 Author

Gurlal Singh
Computer Science Student
Python | Data Structures | Algorithms

⭐ If you find this project useful, feel free to star the repository.
