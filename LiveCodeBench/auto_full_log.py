#!/usr/bin/env python3
"""
Auto-log CORA results - copies solution and predictions, updates cora_results.json
Usage: python auto_full_log.py <problem_index> [--passed] [--failed]
"""
import json
import sys
import os
from pathlib import Path
from datetime import datetime
import shutil

def auto_log_result(problem_index, passed=True, notes="", execution_time_ms=None, error_type=None):
    """
    Automatically log CORA result for a problem.
    - Copies solution.py to solutions/solution_<index>.py
    - Copies script_output.txt to predictions/prediction_<index>.txt
    - Updates cora_results.json with metadata and metrics
    
    Args:
        problem_index: Index of the problem
        passed: Whether the test passed
        notes: Additional notes (e.g., "Wrong answer", "Timeout")
        execution_time_ms: Execution time in milliseconds (optional)
        error_type: Type of error if failed (e.g., "Wrong Answer", "TLE", "Runtime Error")
    """
    base_dir = Path(__file__).parent
    
    # Source files
    solution_src = base_dir / "solution.py"
    
    # Destination directories
    solutions_dir = base_dir / "solutions"
    
    # Ensure directories exist
    solutions_dir.mkdir(exist_ok=True)
    
    # Destination files
    solution_dest = solutions_dir / f"solution_{problem_index}.py"
    
    # Copy solution file
    try:
        if solution_src.exists():
            shutil.copy2(solution_src, solution_dest)
            print(f"✓ Copied solution.py → {solution_dest.relative_to(base_dir)}")
        else:
            print(f"⚠ Warning: solution.py not found")
    except Exception as e:
        print(f"✗ Error copying files: {e}")
        return False
    
    # Load and update cora_results.json
    results_file = base_dir / "cora_results.json"
    
    try:
        # Load existing results
        if results_file.exists():
            with open(results_file, 'r') as f:
                results = json.load(f)
        else:
            results = []
        
        # Load problem metadata
        problems_file = base_dir / "my_100_problems.json"
        with open(problems_file, 'r') as f:
            all_problems = json.load(f)
        
        problem = all_problems[problem_index]
        
        # Create result entry
        entry = {
            "timestamp": datetime.now().isoformat(),
            "index": problem_index,
            "question_id": problem.get("question_id"),
            "title": problem.get("title"),
            "difficulty": problem.get("difficulty"),
            "cora_solution": solution_src.read_text() if solution_src.exists() else "",
            "passed": passed,
            "execution_time_ms": execution_time_ms,
            "error_type": error_type,
            "notes": notes
        }
        
        # Replace existing entry for this index or append
        entry_idx = next((i for i, r in enumerate(results) if r.get("index") == problem_index), None)
        if entry_idx is not None:
            results[entry_idx] = entry
        else:
            results.append(entry)
        
        # Write updated results
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        status = "PASSED ✓" if passed else "FAILED ✗"
        print(f"✓ Updated cora_results.json [{problem_index}] {status}")
        
        # Auto-regenerate predictions file
        try:
            from generate_predictions import generate_predictions
            generate_predictions(model_name="cora")
        except Exception as pred_err:
            print(f"⚠ Could not auto-update predictions: {pred_err}")
        
        return True
    
    except Exception as e:
        print(f"✗ Error updating cora_results.json: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python auto_full_log.py <problem_index> [--passed|--failed] [--notes 'notes'] [--time <ms>] [--error <type>]")
        print("Example: python auto_full_log.py 1 --passed --time 1200")
        print("Example: python auto_full_log.py 2 --failed --error 'Wrong Answer' --notes 'Test 5 failed'")
        sys.exit(1)
    
    try:
        problem_index = int(sys.argv[1])
    except ValueError:
        print(f"Error: problem_index must be an integer, got '{sys.argv[1]}'")
        sys.exit(1)
    
    # Parse flags
    passed = True
    notes = ""
    execution_time_ms = None
    error_type = None
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--passed":
            passed = True
            i += 1
        elif arg == "--failed":
            passed = False
            i += 1
        elif arg == "--notes":
            if i + 1 < len(sys.argv):
                notes = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        elif arg == "--time":
            if i + 1 < len(sys.argv):
                try:
                    execution_time_ms = int(sys.argv[i + 1])
                    i += 2
                except ValueError:
                    print(f"Warning: Invalid time value: {sys.argv[i + 1]}")
                    i += 2
            else:
                i += 1
        elif arg == "--error":
            if i + 1 < len(sys.argv):
                error_type = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        else:
            i += 1
    
    success = auto_log_result(problem_index, passed=passed, notes=notes, 
                            execution_time_ms=execution_time_ms, error_type=error_type)
    sys.exit(0 if success else 1)
