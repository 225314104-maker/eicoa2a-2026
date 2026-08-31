def mm_to_inches(mm):
    """Convert millimetres to inches."""
    return mm / 25.4


def inches_to_mm(inches):
    """Convert inches to millimetres."""
    return inches * 25.4


def cm_to_inches(cm):
    """Convert centimetres to inches.

    Args:
        cm (float): Length in centimetres.

    Returns:
        float: Length in inches (1 inch = 2.54 cm).
    """
    return cm / 2.54


def inches_to_cm(inches):
    """Convert inches to centimetres.

    Args:
        inches (float): Length in inches.

    Returns:
        float: Length in centimetres (inches * 2.54).
    """
    return inches * 2.54