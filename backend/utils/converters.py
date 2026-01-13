"""
Converter utilities for various conversion types
"""


class LengthConverter:
    """Length unit converter"""
    # Base unit: meter
    CONVERSIONS = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Convert length from one unit to another"""
        if from_unit not in cls.CONVERSIONS or to_unit not in cls.CONVERSIONS:
            raise ValueError(f"Invalid unit: {from_unit} or {to_unit}")
        
        # Convert to base unit (meter), then to target unit
        base_value = value * cls.CONVERSIONS[from_unit]
        result = base_value / cls.CONVERSIONS[to_unit]
        return round(result, 6)


class WeightConverter:
    """Weight unit converter"""
    # Base unit: kilogram
    CONVERSIONS = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495,
        'ton': 1000.0,
        'stone': 6.35029
    }
    
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Convert weight from one unit to another"""
        if from_unit not in cls.CONVERSIONS or to_unit not in cls.CONVERSIONS:
            raise ValueError(f"Invalid unit: {from_unit} or {to_unit}")
        
        base_value = value * cls.CONVERSIONS[from_unit]
        result = base_value / cls.CONVERSIONS[to_unit]
        return round(result, 6)


class TemperatureConverter:
    """Temperature unit converter"""
    
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Convert temperature from one unit to another"""
        valid_units = ['celsius', 'fahrenheit', 'kelvin']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise ValueError(f"Invalid unit: {from_unit} or {to_unit}")
        
        if from_unit == to_unit:
            return value
        
        # Convert to Celsius first
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5 / 9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:
            celsius = value
        
        # Convert from Celsius to target
        if to_unit == 'fahrenheit':
            result = (celsius * 9 / 5) + 32
        elif to_unit == 'kelvin':
            result = celsius + 273.15
        else:
            result = celsius
        
        return round(result, 6)


class VolumeConverter:
    """Volume unit converter"""
    # Base unit: liter
    CONVERSIONS = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.236588,
        'fluid_ounce': 0.0295735,
        'cubic_meter': 1000.0,
        'cubic_centimeter': 0.001
    }
    
    @classmethod
    def convert(cls, value, from_unit, to_unit):
        """Convert volume from one unit to another"""
        if from_unit not in cls.CONVERSIONS or to_unit not in cls.CONVERSIONS:
            raise ValueError(f"Invalid unit: {from_unit} or {to_unit}")
        
        base_value = value * cls.CONVERSIONS[from_unit]
        result = base_value / cls.CONVERSIONS[to_unit]
        return round(result, 6)


class CurrencyConverter:
    """Currency converter with mock exchange rates"""
    # Mock exchange rates (base: USD)
    EXCHANGE_RATES = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'INR': 75.0,
        'CAD': 1.25,
        'AUD': 1.35,
        'CHF': 0.92,
        'CNY': 6.45,
        'MXN': 20.0
    }
    
    @classmethod
    def convert(cls, value, from_currency, to_currency):
        """Convert currency from one to another"""
        if from_currency not in cls.EXCHANGE_RATES or to_currency not in cls.EXCHANGE_RATES:
            raise ValueError(f"Invalid currency: {from_currency} or {to_currency}")
        
        # Convert to USD first, then to target currency
        usd_value = value / cls.EXCHANGE_RATES[from_currency]
        result = usd_value * cls.EXCHANGE_RATES[to_currency]
        return round(result, 2)


class NumberBaseConverter:
    """Number base converter (binary, decimal, hex, octal)"""
    
    @classmethod
    def convert(cls, value, from_base, to_base):
        """Convert number from one base to another"""
        valid_bases = ['binary', 'decimal', 'hexadecimal', 'octal']
        if from_base not in valid_bases or to_base not in valid_bases:
            raise ValueError(f"Invalid base: {from_base} or {to_base}")
        
        # Convert to decimal first
        if from_base == 'binary':
            decimal = int(value, 2)
        elif from_base == 'hexadecimal':
            decimal = int(value, 16)
        elif from_base == 'octal':
            decimal = int(value, 8)
        else:
            decimal = int(value)
        
        # Convert from decimal to target base
        if to_base == 'binary':
            result = bin(decimal)[2:]
        elif to_base == 'hexadecimal':
            result = hex(decimal)[2:].upper()
        elif to_base == 'octal':
            result = oct(decimal)[2:]
        else:
            result = str(decimal)
        
        return result

