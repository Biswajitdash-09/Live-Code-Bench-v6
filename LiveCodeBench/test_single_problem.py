import json
import sys

def show_problem(problem_index):
    """Display a problem for testing with CORA"""
    
    # Load problems
    with open('my_100_problems.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    if problem_index >= len(problems):
        print(f"❌ Problem {problem_index} not found. Max index: {len(problems)-1}")
        return
    
    problem = problems[problem_index]
    
    print("\n" + "="*80)
    print(f"PROBLEM #{problem_index}")
    print("="*80)
    print(f"ID: {problem['question_id']}")
    print(f"Title: {problem['title']}")
    print(f"Difficulty: {problem['difficulty']}")
    print("="*80)
    print("\n📋 PROBLEM DESCRIPTION (Copy this to CORA):\n")
    print(problem['description'])
    print("\n" + "="*80)
    
    if problem.get('starter_code'):
        print("\n💡 STARTER CODE:\n")
        print(problem['starter_code'])
        print("\n" + "="*80)
    
    print("\n🎯 INSTRUCTIONS:")
    print("1. Copy the problem description above")
    print("2. Open CORA in VS Code")
    print("3. Paste and ask CORA to solve it")
    print("4. Copy CORA's solution")
    print("5. Test the solution")
    print("6. Log the result using: python log_result.py")
    print("\n" + "="*80 + "\n")

def show_next_problem():
    """Show the next untested problem"""
    
    # Load problems and results
    with open('my_100_problems.json', 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    try:
        with open('cora_results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)
        tested_ids = {r['question_id'] for r in results}
    except FileNotFoundError:
        tested_ids = set()
    
    # Find first untested problem
    for i, problem in enumerate(problems):
        if problem['question_id'] not in tested_ids:
            show_problem(i)
            return
    
    print("🎉 All 100 problems completed!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Show specific problem by index
        try:
            index = int(sys.argv[1])
            show_problem(index)
        except ValueError:
            print("Usage: python test_single_problem.py [problem_number]")
    else:
        # Show next untested problem
        show_next_problem()
