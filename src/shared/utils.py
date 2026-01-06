import re
from typing import Any, Dict, Optional

def remove_urls(text: str) -> str:
    """
    Removes URLs from the given text.
    """
    url_pattern = r'https?://\S+|www\.\S+'
    return re.sub(url_pattern, '', text).strip()

def is_text_only(config: Optional[Dict[str, Any]]) -> bool:
    """
    Checks if text-only mode is enabled in the configuration.
    """
    if not config or "configurable" not in config:
        return False
    return config["configurable"].get("text_only_mode", False)

def should_post_to_linkedin_org(config: Optional[Dict[str, Any]]) -> bool:
    """
    Checks if posting to LinkedIn organization is enabled.
    """
    if not config or "configurable" not in config:
        return False
    return config["configurable"].get("post_to_linkedin_organization", False)
