import tomllib
from pathlib import Path

default_settings_file = Path(__file__).resolve().parent.parent/"settings"/"defaults.toml"
local_settings_file = Path(__file__).resolve().parent.parent/"settings"/"local.toml"

def read(path: Path) -> dict:
    with open(path, "rb") as f:
        return tomllib.load(f)

def load() -> dict:
    settings = read(default_settings_file)
    if not local_settings_file.exists():
        local_settings_file.write_text("# Add in what you want overwritten here\n")
    settings.update(read(local_settings_file))
    return settings

settings = load()

SCROLLING_TEXT: str = settings.get("scrolling_text", "")
SCROLLING_TEXT_LOOP: str = settings.get("scrolling_text_loop", "")
MINECRAFT_SERVER: bool = settings.get("minecraft_server", "")

BAMBU_IP: str = settings.get("bambu_ip", "")
BAMBU_ACCESS_CODE: str = settings.get("bambu_access_code", "")
BAMBU_SERIAL_NUMBER: str = settings.get("bambu_serial_number", "")