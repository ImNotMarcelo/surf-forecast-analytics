from fetch_marine_data import fetch_marine_data
from process_data import process_data


def run_pipeline():
    """Fetch forecast data and generate processed Surf Scores."""
    fetch_marine_data()
    return process_data()


if __name__ == "__main__":
    run_pipeline()