from datetime import datetime
from pathlib import Path
from sys import argv

import pandas as pd
from tinytag import TinyTag


if __name__ == "__main__":
    files_dir = argv[1]

    durations_minutes = pd.Series([
        TinyTag.get(file_path).duration / 60
        for file_path in Path(files_dir).glob("*.mp4")
    ])

    print("Min:", durations_minutes.min())
    print("Max:", durations_minutes.max())
    print("Mean:", durations_minutes.mean())
    print("Std:", durations_minutes.std())
    print("Total:", durations_minutes.sum())
