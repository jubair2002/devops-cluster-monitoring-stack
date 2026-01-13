import pytest
from backend.utils.converters import (
    LengthConverter, WeightConverter, TemperatureConverter,
    VolumeConverter, CurrencyConverter, NumberBaseConverter
)


class TestLengthConverter:
    """Test length converter"""
    
    def test_meter_to_kilometer(self):
        result = LengthConverter.convert(1000, 'meter', 'kilometer')
        assert result == 1.0
    
    def test_inch_to_centimeter(self):
        result = LengthConverter.convert(1, 'inch', 'centimeter')
        assert result == 2.54
    
    def test_mile_to_kilometer(self):
        result = LengthConverter.convert(1, 'mile', 'kilometer')
        assert result == 1.60934
    
    def test_invalid_unit(self):
        with pytest.raises(ValueError):
            LengthConverter.convert(100, 'invalid', 'meter')


class TestWeightConverter:
    """Test weight converter"""
    
    def test_gram_to_kilogram(self):
        result = WeightConverter.convert(1000, 'gram', 'kilogram')
        assert result == 1.0
    
    def test_pound_to_kilogram(self):
        result = WeightConverter.convert(1, 'pound', 'kilogram')
        assert result == pytest.approx(0.453592, rel=1e-5)
    
    def test_invalid_unit(self):
        with pytest.raises(ValueError):
            WeightConverter.convert(100, 'invalid', 'kilogram')


class TestTemperatureConverter:
    """Test temperature converter"""
    
    def test_celsius_to_fahrenheit(self):
        result = TemperatureConverter.convert(0, 'celsius', 'fahrenheit')
        assert result == 32.0
    
    def test_fahrenheit_to_celsius(self):
        result = TemperatureConverter.convert(32, 'fahrenheit', 'celsius')
        assert result == 0.0
    
    def test_celsius_to_kelvin(self):
        result = TemperatureConverter.convert(0, 'celsius', 'kelvin')
        assert result == 273.15
    
    def test_same_unit(self):
        result = TemperatureConverter.convert(100, 'celsius', 'celsius')
        assert result == 100.0


class TestVolumeConverter:
    """Test volume converter"""
    
    def test_liter_to_milliliter(self):
        result = VolumeConverter.convert(1, 'liter', 'milliliter')
        assert result == 1000.0
    
    def test_gallon_to_liter(self):
        result = VolumeConverter.convert(1, 'gallon', 'liter')
        assert result == pytest.approx(3.78541, rel=1e-5)
    
    def test_invalid_unit(self):
        with pytest.raises(ValueError):
            VolumeConverter.convert(100, 'invalid', 'liter')


class TestCurrencyConverter:
    """Test currency converter"""
    
    def test_usd_to_eur(self):
        result = CurrencyConverter.convert(100, 'USD', 'EUR')
        assert result == 85.0
    
    def test_eur_to_usd(self):
        result = CurrencyConverter.convert(100, 'EUR', 'USD')
        assert result == pytest.approx(117.65, rel=0.1)
    
    def test_invalid_currency(self):
        with pytest.raises(ValueError):
            CurrencyConverter.convert(100, 'INVALID', 'USD')


class TestNumberBaseConverter:
    """Test number base converter"""
    
    def test_decimal_to_binary(self):
        result = NumberBaseConverter.convert('10', 'decimal', 'binary')
        assert result == '1010'
    
    def test_binary_to_decimal(self):
        result = NumberBaseConverter.convert('1010', 'binary', 'decimal')
        assert result == '10'
    
    def test_decimal_to_hex(self):
        result = NumberBaseConverter.convert('255', 'decimal', 'hexadecimal')
        assert result == 'FF'
    
    def test_hex_to_decimal(self):
        result = NumberBaseConverter.convert('FF', 'hexadecimal', 'decimal')
        assert result == '255'
    
    def test_decimal_to_octal(self):
        result = NumberBaseConverter.convert('64', 'decimal', 'octal')
        assert result == '100'
    
    def test_octal_to_decimal(self):
        result = NumberBaseConverter.convert('100', 'octal', 'decimal')
        assert result == '64'
    
    def test_invalid_base(self):
        with pytest.raises(ValueError):
            NumberBaseConverter.convert('10', 'invalid', 'binary')

