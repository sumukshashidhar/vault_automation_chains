from vault import File, Vault


def remove_blocks(file_content: str, pattern):
    """
    Remove blocks from a string, that match the pattern shown.
    """
    return file_content.replace(pattern, "")
