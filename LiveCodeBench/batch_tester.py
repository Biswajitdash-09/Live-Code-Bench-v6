import json
import os
import sys

def init_tracking():
    """Initialize result tracking"""
    if not os.path.exists('cora_results.json'):
        with open('cora_results.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        print("✅ Created cora_results.json")
    else:
        print("ℹ️ cora_results.json already exists")

def show_progress():
    """Show current progress"""
    try:
        with open('cora_results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
    except FileNotFoundError:
        results = []
        
    completed = len(results)
    
    # Load total problems
    try:
        with open('my_100_problems.json', 'r', encoding='utf-8') as f:
            problems = json.load(f)
        total = len(problems)
    except FileNotFoundError:
        total = 100 # Fallback
        
    print(f"📊 Progress: {completed}/{total} problems tested")

if __name__ == "__main__":
    init_tracking()
    show_progress()
    
    # Import and run the problem viewer if available
    try:
        import test_single_problem
        test_single_problem.show_next_problem()
    except ImportError:
        print("⚠️ test_single_problem.py not found. Please create it.")
