def calc_resistance(voltage, current):
    """Calculate electrical resistance using Ohm's law.

    Args:
        voltage (float): Voltage across the component in volts (V).
        current (float): Current through the component in amperes (A). Must be non-zero.

    Returns:
        float: Resistance in ohms (Ω).

    Notes:
        The function raises a ZeroDivisionError if current is 0.
    """
    return voltage / current


def calc_power(voltage, resistance):
    """Calculate electrical power dissipated in a resistor.

    Args:
        voltage (float): Voltage across the resistor in volts (V).
        resistance (float): Resistance in ohms (Ω). Must be non-zero.

    Returns:
        float: Power dissipated in watts (W).

    Notes:
        The function raises a ZeroDivisionError if resistance is 0.
    """
    current = voltage / resistance
    return voltage * current