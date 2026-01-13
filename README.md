# Unit Converter Application

## How to Run

### Option 1: Using Docker (Recommended)

```bash
# Build the Docker image
docker build -t converter-app .

# Run the container
docker run -p 5000:5000 converter-app
```

The application will be available at `http://localhost:5000`

### Option 2: Windows (Local Development)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the application
python run_windows.py
```

The application will be available at `http://localhost:5000`

### Option 3: Linux/Mac (Local Development)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with gunicorn
gunicorn --bind 0.0.0.0:5000 --workers 4 --threads 2 wsgi:app
```

The application will be available at `http://localhost:5000`

