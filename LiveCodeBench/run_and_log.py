#!/usr/bin/env python3
"""
Helper script to run solution.py, capture output, and auto-log result
Usage: python run_and_log.py <problem_index> [--passed|--failed] [--time <ms>]
"""
import subprocess
import sys
import json
from pathlib import Path

def get_test_input_from_problems(problem_index):
    """Extract test input from my_100_problems.json"""
    base_dir = Path(__file__).parent
    problems_file = base_dir / "my_100_problems.json"
    
    if not problems_file.exists():
        return None
    
    try:
        with open(problems_file, 'r') as f:
            problems = json.load(f)
        
        if problem_index < len(problems):
            problem = problems[problem_index]
            # Try to extract test input from problem
            if "input_output" in problem and problem["input_output"]:
                if isinstance(problem["input_output"], dict):
                    # Handle different formats
                    for key in ["inputs", "input", "test_input"]:
                        if key in problem["input_output"]:
                            return problem["input_output"][key]
    except:
        pass
    
    return None

import hashlib

def check_for_stale_code(solution_file, force=False):
    """
    Check if the current solution is identical to the previous one in cora_results.json
    Returns: True if code is fresh (or forced), False if stale
    """
    if force:
        return True
        
    base_dir = Path(__file__).parent
    results_file = base_dir / "cora_results.json"
    
    if not results_file.exists() or not solution_file.exists():
        return True
        
    # Read current code
    with open(solution_file, 'r') as f:
        current_code = f.read().strip()
        
    if not current_code:
        print("❌ Error: solution.py is empty")
        return False
        
    current_hash = hashlib.md5(current_code.encode()).hexdigest()
    
    try:
        with open(results_file, 'r') as f:
            results = json.load(f)
            
        if not results:
            return True
            
        # Get last result
        last_result = results[-1]
        last_code = last_result.get("cora_solution", "").strip()
        
        # Compare
        if not last_code:
            return True
            
        last_hash = hashlib.md5(last_code.encode()).hexdigest()
        
        if current_hash == last_hash:
            print(f"\n❌ CRITICAL ERROR: Stale Solution Detected!")
            print(f"   The code in 'solution.py' is IDENTICAL to the solution for the previous problem:")
            print(f"   Previous Problem: #{last_result.get('index')} - {last_result.get('title')}")
            print(f"\n   Did you forget to paste the new code from Cora?")
            print(f"   Use --force to override this check if you really mean to submit the same code.")
            return False
            
    except Exception as e:
        print(f"⚠️ Warning: Could not check for stale code: {e}")
        
    return True

def run_and_log(problem_index, passed=True, execution_time_ms=None, error_type=None, notes="", force=False):
    """
    Run solution.py, save output, and auto-log the result
    """
    import shutil
    
    base_dir = Path(__file__).parent
    solution_file = base_dir / "solution.py"
    test_input_file = base_dir / "test_input.txt"
    script_output_file = base_dir / "script_output.txt"
    
    # Check for solution.py in parent folder (where Cora writes)
    parent_solution = base_dir.parent / "solution.py"

    # Bidirectional Sync Logic
    if parent_solution.exists() and solution_file.exists():
        parent_mtime = parent_solution.stat().st_mtime
        solution_mtime = solution_file.stat().st_mtime
        
        if solution_mtime > parent_mtime:
            # Local is newer -> Copy to Parent
            try:
                shutil.copy2(solution_file, parent_solution)
                print(f"📤 Synced: Local solution.py → Parent folder (Local was newer)")
            except Exception as e:
                print(f"⚠️ Warning: Could not update parent file: {e}")
        elif parent_mtime > solution_mtime:
            # Parent is newer -> Copy to Local
            shutil.copy2(parent_solution, solution_file)
            print(f"📥 Synced: Parent solution.py → Local folder (Parent was newer)")
        else:
            # Times match (or identical), assume synced
            pass
            
    elif parent_solution.exists() and not solution_file.exists():
        # Only parent exists -> Copy to Local
        shutil.copy2(parent_solution, solution_file)
        print(f"📥 Auto-copied solution.py from parent folder")
        
    elif solution_file.exists() and not parent_solution.exists():
        # Only local exists -> Copy to Parent
        try:
            shutil.copy2(solution_file, parent_solution)
            print(f"📤 Auto-copied solution.py to parent folder")
        except Exception as e:
            print(f"⚠️ Warning: Could not create parent file: {e}")
            
    # Check if solution.py exists (after sync attempts)
    if not solution_file.exists():
        print(f"❌ Error: solution.py not found!")
        print(f"   Please paste CORA's code into solution.py (in Root or LiveCodeBench folder)")
        return False
        
    # STALE CODE CHECK
    if not check_for_stale_code(solution_file, force):
        return False
    
    # Create or check test_input.txt
    if not test_input_file.exists():
        print(f"📝 Creating test_input.txt from problem definition...")
        test_input = get_test_input_from_problems(problem_index)
        if test_input:
            with open(test_input_file, 'w') as f:
                f.write(test_input)
            print(f"✓ Created test_input.txt from problem data")
        else:
            print(f"⚠️  Could not auto-generate test_input.txt")
            print(f"   Please create test_input.txt manually")
            # Still allow logging without running
    
    
    # Run the solution if test input exists
    if test_input_file.exists():
        # Run solution.py with test input
        try:
            import time
            print(f"▶️  Running solution.py...")
            start_time = time.time()
            with open(test_input_file, 'r') as f_in:
                result = subprocess.run(
                    [sys.executable, str(solution_file)],
                    stdin=f_in,
                    capture_output=True,
                    text=True,
                    timeout=5
                )
            end_time = time.time()
            
            # Calculate execution time in milliseconds
            if execution_time_ms is None:
                execution_time_ms = int((end_time - start_time) * 1000)
            
            # Save output
            with open(script_output_file, 'w') as f_out:
                f_out.write(result.stdout)
                if result.stderr:
                    f_out.write("\n--- STDERR ---\n")
                    f_out.write(result.stderr)
            
            if result.returncode == 0:
                print(f"✓ Output saved to script_output.txt ({execution_time_ms}ms)")
            else:
                print(f"⚠️  Process returned code {result.returncode}")
                if not passed:
                    error_type = error_type or "Runtime Error"
                    notes = notes or f"Return code: {result.returncode}"
        
        except subprocess.TimeoutExpired:
            print(f"❌ Timeout: Solution took too long")
            if not passed:
                error_type = error_type or "Timeout"
        except Exception as e:
            print(f"❌ Error running solution: {e}")
            if not passed:
                error_type = error_type or "Runtime Error"
    
    # Auto-log the result
    print(f"\n📝 Logging result...")
    try:
        from auto_full_log import auto_log_result
        success = auto_log_result(
            problem_index,
            passed=passed,
            notes=notes,
            execution_time_ms=execution_time_ms,
            error_type=error_type
        )
        return success
    except Exception as e:
        print(f"❌ Error logging result: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_and_log.py <problem_index> [--passed|--failed] [--time <ms>] [--error <type>] [--notes '<text>'] [--force]")
        print("Example: python run_and_log.py 1 --passed")
        print("Example: python run_and_log.py 2 --failed --error 'Wrong Answer'")
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
    execution_time_ms = None
    error_type = None
    force = False
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == "--passed":
            passed = True
            i += 1
        elif arg == "--failed":
            passed = False
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
        elif arg == "--notes":
            if i + 1 < len(sys.argv):
                notes = sys.argv[i + 1]
                i += 2
            else:
                i += 1

        elif arg == "--force":
            force = True
            i += 1
        else:
            i += 1
    
    success = run_and_log(problem_index, passed=passed, 
                         execution_time_ms=execution_time_ms, 
                         error_type=error_type, notes=notes,
                         force=force)
    sys.exit(0 if success else 1)
