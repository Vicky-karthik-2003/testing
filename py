from datetime import datetime

with open("output.txt", "a") as f:
    f.write(f"Script ran at: {datetime.now()}\n")
