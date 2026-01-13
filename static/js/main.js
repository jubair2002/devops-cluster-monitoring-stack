// Tab switching functionality
document.addEventListener('DOMContentLoaded', function() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');
            
            // Remove active class from all tabs and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked tab and corresponding content
            button.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
    
    // Check application health
    checkHealth();
});

function checkHealth() {
    fetch('/health')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'healthy') {
                console.log('Application is healthy');
            }
        })
        .catch(error => {
            console.error('Health check failed:', error);
        });
}

// Conversion functions
async function convertLength() {
    const value = document.getElementById('length-value').value;
    const fromUnit = document.getElementById('length-from').value;
    const toUnit = document.getElementById('length-to').value;
    const messageDiv = document.getElementById('length-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter a value', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/length', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_unit: fromUnit,
                to_unit: toUnit
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('length-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

async function convertWeight() {
    const value = document.getElementById('weight-value').value;
    const fromUnit = document.getElementById('weight-from').value;
    const toUnit = document.getElementById('weight-to').value;
    const messageDiv = document.getElementById('weight-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter a value', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/weight', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_unit: fromUnit,
                to_unit: toUnit
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('weight-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

async function convertTemperature() {
    const value = document.getElementById('temp-value').value;
    const fromUnit = document.getElementById('temp-from').value;
    const toUnit = document.getElementById('temp-to').value;
    const messageDiv = document.getElementById('temp-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter a value', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/temperature', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_unit: fromUnit,
                to_unit: toUnit
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('temp-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

async function convertVolume() {
    const value = document.getElementById('volume-value').value;
    const fromUnit = document.getElementById('volume-from').value;
    const toUnit = document.getElementById('volume-to').value;
    const messageDiv = document.getElementById('volume-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter a value', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/volume', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_unit: fromUnit,
                to_unit: toUnit
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('volume-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

async function convertCurrency() {
    const value = document.getElementById('currency-value').value;
    const fromCurrency = document.getElementById('currency-from').value;
    const toCurrency = document.getElementById('currency-to').value;
    const messageDiv = document.getElementById('currency-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter an amount', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/currency', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: parseFloat(value),
                from_currency: fromCurrency,
                to_currency: toCurrency
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('currency-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

async function convertNumberBase() {
    const value = document.getElementById('number-value').value.trim();
    const fromBase = document.getElementById('number-from').value;
    const toBase = document.getElementById('number-to').value;
    const messageDiv = document.getElementById('number-message');
    
    if (!value || value === '') {
        showMessage(messageDiv, 'Please enter a number', 'error');
        return;
    }
    
    try {
        const response = await fetch('/api/convert/number-base', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                value: value,
                from_base: fromBase,
                to_base: toBase
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            document.getElementById('number-result').value = data.result;
            showMessage(messageDiv, `${data.from} = ${data.to}`, 'success');
        } else {
            showMessage(messageDiv, data.error || 'Conversion failed', 'error');
        }
    } catch (error) {
        showMessage(messageDiv, 'Error: ' + error.message, 'error');
    }
}

function showMessage(element, message, type) {
    element.textContent = message;
    element.className = `message ${type}`;
    setTimeout(() => {
        element.className = 'message';
    }, 5000);
}
