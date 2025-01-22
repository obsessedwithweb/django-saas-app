import requests
from pathlib import Path


def download_from_web(url: str, dest_path: Path, parent_mkdir: bool = True):
    if not isinstance(dest_path, Path):
        raise ValueError(f"{dest_path} must be a valid pathlib.Path object")
    if parent_mkdir:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file out in binary mode to prevent any newline conversions
        dest_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f'Failed to download {url}: {e}')
        return False
