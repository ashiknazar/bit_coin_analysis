import os

# Run this inside your existing project root directory

STRUCTURE = [
    "collector",
    "processor",
    "storage/raw",
    "storage/candles",
    "storage/features",
    "utils",
    "config",
    "app",
    "docker",
]

FILES = {
    "main.py": "",
    "collector/stream.py": "",
    "processor/candles.py": "",
    "processor/features.py": "",
    "storage/writer.py": "",
    "utils/time_utils.py": "",
    "config/settings.py": "",
    "app/dashboard.py": "",
    "docker/docker-compose.yml": "",
    "README.md": "# BTC Intraday ML Pipeline\n",
}


def create_structure(base_path="."):
    print("\n🚀 Initializing project structure...\n")

    # create directories
    for folder in STRUCTURE:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"📁 {path}")

    # create files
    for file_path, content in FILES.items():
        full_path = os.path.join(base_path, file_path)

        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        if not os.path.exists(full_path):
            with open(full_path, "w") as f:
                f.write(content)
            print(f"📄 created: {full_path}")
        else:
            print(f"⚠️ exists: {full_path} (skipped)")

    print("\n✅ Structure ready inside existing root folder!")


if __name__ == "__main__":
    create_structure()