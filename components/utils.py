
import pandas as pd
import random

def get_random_violation_description(csv_path="cleaned_violation_descriptions.csv") -> str:
    """
    Selects a random violation description from the cleaned CSV.

    Args:
        csv_path (str): Path to cleaned violation descriptions.

    Returns:
        str: A randomly selected violation description.
    """
    df = pd.read_csv(csv_path)
    if df.empty or 'VIOLATION DESCRIPTION' not in df.columns:
        raise ValueError("CSV is empty or missing 'VIOLATION DESCRIPTION' column.")
    
    descriptions = df['VIOLATION DESCRIPTION'].dropna().unique().tolist()
    return random.choice(descriptions)