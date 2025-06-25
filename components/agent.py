from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.openai import OpenAI
from llama_index.core.schema import Document

# Custom system prompt to guide LLM behavior
CUSTOM_PROMPT = """
You are a compliance analyst assistant.

Your task is to verify whether a reported restaurant inspection violation aligns with the official NYC Health Code.

You will be provided with a violation description, such as:

  "Violation Description": "Design, construction, materials used or maintenance of food contact surface improper. Surface not easily cleanable, sanitized and maintained."

Your responsibilities:

1. **If the description directly matches a provision**, say so clearly. Include the matching section(s) (e.g., §81.27(a)).
2. **If the description is a partial or generalized match**, explain that, and list the most relevant matching section(s).
3. **If no matching section exists**, state that clearly and say it may be informal, outdated, or uncited.

💡 Format:
- For a direct match:  
  "Violation '[description]' matches Health Code sections §XX.XX(a), §YY.YY(b)."

- For a partial/general match:  
  "Violation '[description]' is a generalized interpretation but aligns most closely with §XX.XX(a), §YY.YY(c)."

- For no match:  
  "Violation '[description]' does not exist in the current NYC Health Code. Consider reviewing for outdated or informal wording."

Respond clearly with one of these formats.
"""

def create_discrepancy_agent(index, violation_description: str):
    """
    Creates a discrepancy detection agent with health code index + violation context.

    Args:
        index: VectorStoreIndex
        violation_description: The inspection violation to check
        use_openai (bool): If True, uses OpenAI (else TinyLlama)

    Returns:
        RetrieverQueryEngine: Configured query engine
    """
    llm = OpenAI(model="gpt-3.5-turbo", system_prompt=CUSTOM_PROMPT)
    
    violation_doc = Document(text=f"Violation Description: {violation_description}")
    query_engine = index.as_query_engine(llm=llm, additional_context_documents=[violation_doc])

    return query_engine


def ask_violation_discrepancy(query_engine, violation_description: str) -> str:
    """
    Asks the agent whether a specific violation matches the health code,
    embedding the violation description clearly in the question.

    Args:
        query_engine: The query engine from `create_discrepancy_agent`
        violation_description: The inspection violation to check

    Returns:
        str: Answer from the LLM
    """
    
    question = f"""
    You are given a restaurant inspection violation to verify against the NYC Health Code.

    Violation Description: "{violation_description}"

    Does this violation description match any provision in the official NYC Health Code?
    If not, explain why it might be outdated, informal, or incorrectly worded.
    Only reply if there is a discrepancy.
    """

    response = query_engine.query(question)
    return str(response)
