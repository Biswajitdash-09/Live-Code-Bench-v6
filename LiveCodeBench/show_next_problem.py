#!/usr/bin/env python3
"""
Show next untested problem and display its details
"""
import json
from pathlib import Path

def get_next_untested():
    """
    Find the next problem that hasn't been tested yet.
    """
    base_dir = Path(__file__).parent
    
    # Load all problems
    problems_file = base_dir / "my_100_problems.json"
    with open(problems_file, 'r') as f:
        all_problems = json.load(f)
    
    # Load results
    results_file = base_dir / "cora_results.json"
    tested_indices = set()
    
    if results_file.exists():
        with open(results_file, 'r') as f:
            results = json.load(f)
            tested_indices = {r.get("index") for r in results}
    
    # Find first untested
    for problem in all_problems:
        idx = problem["index"]
        if idx not in tested_indices:
            return idx, problem
    
    return None, None


def show_next_problem():
    """Display the next untested problem"""
    idx, problem = get_next_untested()
    
    if idx is None:
        print("🎉 All 100 problems completed!")
        return
    
    # Load cora_results for stats
    base_dir = Path(__file__).parent
    results_file = base_dir / "cora_results.json"
    passed_count = 0
    if results_file.exists():
        with open(results_file, 'r') as f:
            results = json.load(f)
            passed_count = sum(1 for r in results if r.get("passed", False))
    
    print("\n" + "="*70)
    print(f"📌 NEXT PROBLEM: #{idx}")
    print("="*70)
    print(f"\nID:         {problem.get('question_id')}")
    print(f"Title:      {problem.get('title')}")
    print(f"Difficulty: {problem.get('difficulty').upper()}")
    print(f"\nProgress: {passed_count} problems passed")
    print(f"Remaining: {100 - passed_count - 1} more to test by Tuesday")
    print("\n" + "-"*70)
    print("Description:")
    print("-"*70)
    desc = problem.get('description', '')
    print(desc)
    
    # Try to find input/output samples
    print("\n" + "-"*70)
    print("Sample Input/Output:")
    print("-"*70)
    
    found_sample = False
    
    # Check input_output field
    io = problem.get('input_output', {})
    if io:
        inputs = io.get('inputs', [])
        outputs = io.get('outputs', [])
        
        # Determine number of samples to show (up to 3)
        num_samples = min(len(inputs), len(outputs), 3)
        
        for i in range(num_samples):
            print(f"\nSample {i+1}:")
            print("Input:")
            print(str(inputs[i]).strip())
            print("Output:")
            print(str(outputs[i]).strip())
            found_sample = True
            
    # As a fallback, check if description contains "Sample Input" text if structured data is missing
    if not found_sample and "Sample Input" in desc:
         print("(Samples are embedded in the description above)")
    elif not found_sample:
         print("(No explicit sample input/output found in metadata)")

    print("\n" + "="*70)
    print(f"\nWorkflow:")
    print(f"1. python test_single_problem.py <problem_index>")
    print(f"   → This generates solution.py and script_output.txt")
    print(f"\n2. python auto_full_log.py {idx} --passed")
    print(f"   → Or: python auto_full_log.py {idx} --failed --notes 'reason'")
    print(f"\nThen run: python show_next_problem.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    show_next_problem()
