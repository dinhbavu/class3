import os
import matplotlib
import warnings

# Configure Matplotlib backend
matplotlib.use('Agg')

# Ignore warnings
warnings.filterwarnings('ignore')

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "household_power_consumption.txt")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Plotting constants
COLORS = ["#2196F3", "#FF5722", "#4CAF50", "#9C27B0", "#FF9800", "#00BCD4", "#E91E63"]
