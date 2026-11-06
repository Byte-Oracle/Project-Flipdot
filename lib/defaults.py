import tomllib
from pathlib import Path

default_settings_file = Path(__file__).resolve().parent.parent/"settings"/"defaults.toml"

def load() -> dict:
    with open(default_settings_file, "rb") as f:
        return tomllib.load(f)

settings = load()

SCROLLING_TEXT: str = settings.get("scrolling_text", "")
SCOLLING_TEXT_LOOP: str = settings.get("scrolling_text_loop", "")
MINECRAFT_SERVER: bool = settings.get("minecraft_server", "")