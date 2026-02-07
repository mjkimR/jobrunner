"""Pytest configuration and fixtures."""

import sys
from pathlib import Path

# Add src directory to Python path for app module imports
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

# Add project root for scripts package
sys.path.insert(0, str(project_root))
