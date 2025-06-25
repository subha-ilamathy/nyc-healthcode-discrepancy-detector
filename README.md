## Project Summary: Legal Discrepancy Agent for NYC Health Code Article 81

---

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
- The vector index may lose fine-grained legal logic in long sections — check for semantically accurate matches.
- CSV may need cleanup or balance check — ensure variety and clarity in violation samples.
- Agent reasoning could be more explainable — verify the prompt encourages legal grounding in output.



### Replication Steps

virtualenv -p python3 test

pip install -q --progress-bar off --no-warn-conflicts llama-index-core llama-index-readers-docling llama-index-node-parser-docling llama-index-embeddings-huggingface llama-index-llms-huggingface-api llama-index-readers-file python-dotenv