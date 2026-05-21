#!/usr/bin/env python3
"""
Setup script to create FoodLion backend directory structure
"""
import os
import sys
from pathlib import Path

def create_backend_structure():
    """Create the complete backend directory structure."""
    base_path = Path('e:\\FoodLion\\backend')
    
    dirs_to_create = [
        base_path,
        base_path / 'foodlion',
        base_path / 'authentication',
        base_path / 'restaurants',
        base_path / 'menu_items',
        base_path / 'orders',
        base_path / 'adminpanel',
    ]
    
    print("Creating FoodLion backend directory structure...")
    print("=" * 60)
    
    for dir_path in dirs_to_create:
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"✓ Created: {dir_path}")
        except Exception as e:
            print(f"✗ Failed to create {dir_path}: {e}")
            return False
    
    print("=" * 60)
    print("\nVerifying directory structure...")
    print("=" * 60)
    
    for dir_path in dirs_to_create:
        if dir_path.exists():
            print(f"✓ {dir_path.relative_to('e:\\FoodLion')}")
        else:
            print(f"✗ {dir_path.relative_to('e:\\FoodLion')} - NOT FOUND")
            return False
    
    print("=" * 60)
    print("\n✓ Backend directory structure created successfully!")
    return True

if __name__ == '__main__':
    try:
        success = create_backend_structure()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
