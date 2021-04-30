# File: getters/data_getters.py
"""Data getters ESCO data.
"""
import pandas as pd
from pathlib import Path


def get_occupations() -> pd.DataFrame:
    """Load occupations.

    Returns:
        ESCO occupations data
    """
    path = Path(__file__).parents[1] / "../data/occupations_en.csv"

    with path.open() as f:
        return pd.read_csv(f, sep=",")


def get_skills() -> pd.DataFrame:
    """Load skills.

    Returns:
        ESCO skills data
    """
    path = Path(__file__).parents[1] / "../data/skills_en.csv"

    with path.open() as f:
        return pd.read_csv(f, sep=",")


def get_esco_occup_skills() -> pd.DataFrame:
    """Load esco_occup_skills.

    Returns:
        ESCO occup_skills data
    """
    path = Path(__file__).parents[1] / "../data/ESCO_occup_skills.json"

    with path.open() as f:
        return pd.read_json(f)
