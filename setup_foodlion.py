"""
FoodLion Django Backend Setup Script
Creates complete directory structure and initializes all Django apps
"""
import os
import sys
from pathlib import Path


def setup_backend():
    """Main setup function."""
    base = Path('e:\\FoodLion\\backend')
    
    # Create directories
    dirs = [
        base / 'foodlion',
        base / 'authentication',
        base / 'restaurants',
        base / 'menu_items',
        base / 'orders',
        base / 'adminpanel',
    ]
    
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"Created: {d}")
    
    # Create __init__.py files for all apps
    for app_dir in dirs:
        if app_dir.name != 'foodlion':  # Skip main project
            init_file = app_dir / '__init__.py'
            init_file.touch()
            print(f"Created: {init_file}")
    
    print("\n✓ Backend structure created successfully!")


if __name__ == '__main__':
    try:
        setup_backend()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
