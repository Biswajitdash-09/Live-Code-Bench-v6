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

def run_and_log(problem_index, passed=True, execution_time_ms=None, error_type=None, notes=""):
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
    
    if parent_solution.exists():
        # Auto-copy from parent folder
        shutil.copy2(parent_solution, solution_file)
        print(f"📥 Auto-copied solution.py from parent folder")
    
    # Check if solution.py exists
    if not solution_file.exists():
        print(f"❌ Error: solution.py not found!")
        print(f"   Please paste CORA's code into solution.py first")
        print(f"   Or save it to: {parent_solution}")
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
        print("Usage: python run_and_log.py <problem_index> [--passed|--failed] [--time <ms>] [--error <type>] [--notes '<text>']")
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
        else:
            i += 1
    
    success = run_and_log(problem_index, passed=passed, 
                         execution_time_ms=execution_time_ms, 
                         error_type=error_type, notes=notes)
    sys.exit(0 if success else 1)
