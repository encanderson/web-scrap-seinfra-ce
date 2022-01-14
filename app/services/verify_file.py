import re


def verifY_file_name(filepath):
    """
    Verify if file is a file of composition that start with 'C'

    Args:
        filepath (string): path to file

    Returns:
        boolean: if the file is valid to scrap the compositions
    """

    if re.search("C\/?\d{3}", filepath):
        return True

    return False
