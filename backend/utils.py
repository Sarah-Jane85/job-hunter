def normalize_german(text: str) -> str:
    """Convert German umlaut alternatives to proper characters"""
    if not text:
        return text
    
    replacements = {
        "ue": "ü",
        "ae": "ä",
        "oe": "ö",
        "Ue": "Ü",
        "Ae": "Ä",
        "Oe": "Ö",
        "UE": "Ü",
        "AE": "Ä",
        "OE": "Ö",
    }
    
    result = text
    for key, value in replacements.items():
        result = result.replace(key, value)
    
    return result