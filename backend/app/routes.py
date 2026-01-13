from flask import Blueprint, render_template, jsonify, request
from backend.utils.converters import (
    LengthConverter, WeightConverter, TemperatureConverter,
    VolumeConverter, CurrencyConverter, NumberBaseConverter
)

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    """Home page with converter interface"""
    return render_template('index.html')


@bp.route('/health')
def health():
    """Health check endpoint for DevOps"""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    }), 200


@bp.route('/api/info')
def info():
    """API info endpoint"""
    return jsonify({
        'name': 'Multi-Converter Application',
        'version': '1.0.0',
        'description': 'A comprehensive converter application with multiple conversion types',
        'features': [
            'Length Converter',
            'Weight Converter',
            'Temperature Converter',
            'Volume Converter',
            'Currency Converter',
            'Number Base Converter'
        ]
    })


@bp.route('/api/convert/length', methods=['POST'])
def convert_length():
    """Convert length units"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        
        result = LengthConverter.convert(value, from_unit, to_unit)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value} {from_unit}",
            'to': f"{result} {to_unit}"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/convert/weight', methods=['POST'])
def convert_weight():
    """Convert weight units"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        
        result = WeightConverter.convert(value, from_unit, to_unit)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value} {from_unit}",
            'to': f"{result} {to_unit}"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/convert/temperature', methods=['POST'])
def convert_temperature():
    """Convert temperature units"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        
        result = TemperatureConverter.convert(value, from_unit, to_unit)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value}° {from_unit.capitalize()[0]}",
            'to': f"{result}° {to_unit.capitalize()[0]}"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/convert/volume', methods=['POST'])
def convert_volume():
    """Convert volume units"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        from_unit = data.get('from_unit')
        to_unit = data.get('to_unit')
        
        result = VolumeConverter.convert(value, from_unit, to_unit)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value} {from_unit}",
            'to': f"{result} {to_unit}"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/convert/currency', methods=['POST'])
def convert_currency():
    """Convert currency"""
    try:
        data = request.get_json()
        value = float(data.get('value', 0))
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')
        
        result = CurrencyConverter.convert(value, from_currency, to_currency)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value} {from_currency}",
            'to': f"{result} {to_currency}"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/convert/number-base', methods=['POST'])
def convert_number_base():
    """Convert number between different bases"""
    try:
        data = request.get_json()
        value = data.get('value', '').strip()
        from_base = data.get('from_base')
        to_base = data.get('to_base')
        
        result = NumberBaseConverter.convert(value, from_base, to_base)
        return jsonify({
            'success': True,
            'result': result,
            'from': f"{value} ({from_base})",
            'to': f"{result} ({to_base})"
        })
    except (ValueError, TypeError, KeyError) as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@bp.route('/api/units', methods=['GET'])
def get_units():
    """Get available units for each converter type"""
    return jsonify({
        'length': list(LengthConverter.CONVERSIONS.keys()),
        'weight': list(WeightConverter.CONVERSIONS.keys()),
        'temperature': ['celsius', 'fahrenheit', 'kelvin'],
        'volume': list(VolumeConverter.CONVERSIONS.keys()),
        'currency': list(CurrencyConverter.EXCHANGE_RATES.keys()),
        'number_base': ['binary', 'decimal', 'hexadecimal', 'octal']
    })
