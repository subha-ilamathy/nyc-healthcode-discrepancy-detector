from components.loader import load_and_parse_markdown, save_nodes_to_json, load_nodes_from_json
from components.indexer import build_and_persist_index, load_index
from components.agent import create_discrepancy_agent, ask_violation_discrepancy
from components.utils import get_random_violation_description

SOURCE = "./data/health-code-article81.pdf"  # or a specific file path
PERSIST_DIR = "./storage"

# Step 1: Load and parse markdown
# nodes = load_and_parse_markdown(SOURCE)

# print(f"Loaded {len(nodes)} markdown nodes.")
# print(f"First node preview:\n{nodes[0].text[:300]}")

# save_nodes_to_json(nodes, PERSIST_DIR + "/nodes.json")

# STEP 2: Later (or in a different script), reload the nodes
nodes = load_nodes_from_json(PERSIST_DIR + "/nodes.json")

print(f"First node preview:\n{nodes[0].text[:300]}")

# Step 3: Build and store the index

# index = build_and_persist_index(nodes, PERSIST_DIR + '/vector_index')

# # Load the index
index = load_index(persist_dir=PERSIST_DIR + '/vector_index')
print("\n\nReady to start your agent!\n\n")

violation = get_random_violation_description("./data/cleaned_violation_descriptions.csv")
print(f"Random Violation to query: {violation}\n\n")

agent = create_discrepancy_agent(index, violation)

response = ask_violation_discrepancy(agent, violation)

print(f"\n\nDiscrepancy Check Response:\n{response}")