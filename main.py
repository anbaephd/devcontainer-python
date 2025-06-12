from pathlib import Path
def get_project_root() -> Path:
    """Returns the root directory of the project."""
    return Path(__file__).parent.parent




if __name__ == "__main__":
    print(get_project_root())
    # Example usage
    root = get_project_root()
    print(f"Project root directory: {root}")
    print(f"Absolute path: {root.resolve()}")
    print(f"Is directory: {root.is_dir()}")