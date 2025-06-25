## Project Summary: Legal Discrepancy Agent for NYC Health Code Article 81

---

### Replication Steps

1. Download and extract the Google drive link https://drive.google.com/file/d/1ssi1dZp2eI10eT0KABL6kxlvFLmcs6pG/view?usp=sharing

2. cd nyc-healthcode-discrepancy-detector/

3. source venv_311/bin/activate


### What Problem You Decided to Tackle

You aimed to:
- Parse NYC Health Code Article 81 into structured nodes,
- Build a vector index for semantic search over the legal content,
- Create an agent that can detect **discrepancies** between natural language violation descriptions and the actual health code.

---

### How You Approached It

1. **Document Parsing**
   - Parsed PDF using `load_and_parse_markdown()` to generate structured nodes.
   - Nodes saved with `save_nodes_to_json()` and reloaded via `load_nodes_from_json()`.

2. **Vector Indexing**
   - Created a semantic index of the legal nodes using `build_and_persist_index()`.
   - Reloaded the index when needed via `load_index()`.

3. **Discrepancy Detection Agent**
   - Sampled a random violation using `get_random_violation_description()`.
   - Initialized the agent with `create_discrepancy_agent()`.
   - Queried for inconsistencies using `ask_violation_discrepancy()`.

4. **Automation & Modularity**
   - Modular component architecture via:
     - `components.loader`
     - `components.indexer`
     - `components.agent`
     - `components.utils`

---

### What’s Working

- Legal markdown nodes are loaded and stored correctly.
- Vector index is built, persisted, and reloaded as expected.
- Random violation descriptions are sampled from CSV.
- Agent returns a response judging the consistency with Article 81.

---

### What’s Not (or Needs Improvement)

- Parsing quality: Are clauses like `(a)`, `(1)`, `(i)` being properly segmented?
- Agent reasoning could be more explainable — verify the prompt encourages legal grounding in output.

Eg: "Food contact surface not properly washed, rinsed and sanitized after each use and following any activity when contamination may have occurred."


Dataset
1. Violation, Citations, Assessment whether or not violation was clear 
   - Semantic search using vectors (working for some)
   - Insights to City
   
2. Aggregate all citations, to summarize the violation. (Agent)
   - Violation 1 has 100 relevant healthcodes
   - Summarize the 100 healthcodes, natural language that can give insight

City as a User:
   - Client health_code that has violations
   - Index violations to search on that
   - Query using the Health Code and retrieve what are all restaurants.
   - Narrow down to rootcause with aspects, location, cuisines




Violation Issues:
- Food contact surface not properly washed - Section 81.4
- Rinsed and sanitized after each use and following any activity - Section 81.6

Root Cause:
Food contact surface need

- Retrieve relevant citations that reduces the search space 
- Guidance tool, recommend best practices based on the updated health codes


Inspector Violation Report
Restaurants Approached - Document to explain?? 