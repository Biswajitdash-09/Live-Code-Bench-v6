import json
from datetime import datetime
import sys

def log_result(question_id, passed, solution_code="", notes=""):
    """Log a test result"""
    
    # Load problem details
    with open('my_100_problems.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    problem = None
    for p in problems:
        if p['question_id'] == question_id or str(p['index']) == str(question_id):
            problem = p
            break
    
    if not problem:
        print(f"❌ Problem {question_id} not found!")
        return
    
    # Load existing results
    try:
        with open('cora_results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
    except FileNotFoundError:
        results = []
    
    # Create result entry
    result = {
        "timestamp": datetime.now().isoformat(),
        "index": problem['index'],
        "question_id": problem['question_id'],
        "title": problem['title'],
        "difficulty": problem['difficulty'],
        "cora_solution": solution_code,
        "passed": passed,
        "notes": notes
    }
    
    results.append(result)
    
    # Save
    with open('cora_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    # Show progress
    completed = len(results)
    passed_count = sum(1 for r in results if r['passed'])
    pass_rate = (passed_count / completed * 100) if completed > 0 else 0
    
    print("\n" + "="*70)
    print(f"✅ Result Logged: {problem['title']}")
    print("="*70)
    print(f"Status: {'✓ PASS' if passed else '✗ FAIL'}")
    print(f"Progress: {completed}/100 ({completed}%)")
    print(f"Pass Rate: {pass_rate:.1f}% ({passed_count}/{completed})")
    print("="*70 + "\n")

def interactive_log():
    """Interactive logging mode"""
    
    print("\n🔧 Interactive Result Logger")
    print("="*70)
    
    # Get next problem
    with open('my_100_problems.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    try:
        with open('cora_results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
        tested_ids = {r['question_id'] for r in results}
    except FileNotFoundError:
        tested_ids = set()
    
    # Find first untested
    current_problem = None
    for p in problems:
        if p['question_id'] not in tested_ids:
            current_problem = p
            break
    
    if not current_problem:
        print("🎉 All problems completed!")
        return
    
    print(f"\nCurrent Problem: {current_problem['title']}")
    print(f"ID: {current_problem['question_id']}")
    print(f"Difficulty: {current_problem['difficulty']}")
    
    # Get result
    passed_input = input("\nDid the solution PASS? (y/n): ").strip().lower()
    passed = passed_input == 'y'
    
    print("\nPaste CORA's solution (press Enter, then Ctrl+D or Ctrl+Z to finish):")
    solution_lines = []
    try:
        while True:
            line = input()
            solution_lines.append(line)
    except EOFError:
        pass
    
    solution = "\n".join(solution_lines)
    
    notes = input("\nAny notes? (optional): ").strip()
    
    # Log it
    log_result(current_problem['question_id'], passed, solution, notes)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        # Command line mode: python log_result.py <question_id> <pass/fail>
        question_id = sys.argv[1]
        passed = sys.argv[2].lower() in ['pass', 'p', 'true', '1', 'yes', 'y']
        solution = sys.argv[3] if len(sys.argv) > 3 else ""
        notes = sys.argv[4] if len(sys.argv) > 4 else ""
        log_result(question_id, passed, solution, notes)
    else:
        # Interactive mode
        interactive_log()
