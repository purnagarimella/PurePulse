# PurePulse Package Initialization

# Import all the necessary modules from this package for easy access
from .health_data import collect_health_data
from .speech_analysis import detect_slurred_speech
from .motion_analysis import detect_alcohol_effects
from .recommendations import analyze_health_data
from .utils import some_utility_function

# Optionally, you can include versioning information here
__version__ = '1.0.0'

# Add any package-level variables or functions you want to expose here
