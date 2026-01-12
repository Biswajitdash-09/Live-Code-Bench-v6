from datasets import load_dataset
import json

print("Downloading LiveCodeBench v6 dataset...")
print("This may take a few minutes on first download...\n")

try:
    # Fixed: Use split parameter instead of version_tag
    # The dataset uses 'test' split and we specify version in the dataset name
    lcb = load_dataset("livecodebench/code_generation_lite", split="test", trust_remote_code=True, streaming=True)
    
    # Select first 100 problems
    selected = []
    difficulty_counts = {'Easy': 0, 'Medium': 0, 'Hard': 0, 'Unknown': 0}
    
    print("Processing problems...")
    for i, problem in enumerate(lcb):
        if i >= 100:
            break
        
        # Get problem details
        difficulty = problem.get('difficulty', 'Unknown')
        
        selected.append({
            'index': i,
            'question_id': problem.get('question_id', f'problem_{i}'),
            'title': problem.get('question_title', 'Untitled'),
            'difficulty': difficulty,
            'description': problem.get('question_content', ''),
            'starter_code': problem.get('starter_code', ''),
            'input_output': problem.get('input_output', {}),
        })
        
        if difficulty in difficulty_counts:
            difficulty_counts[difficulty] += 1
        else:
            difficulty_counts['Unknown'] += 1
    
    print(f"Successfully processed {len(selected)} problems from LiveCodeBench")
    
    # Save to JSON file
    output_file = 'my_100_problems.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(selected, f, indent=2, ensure_ascii=False)
    
    print(f"\nSUCCESS! Saved 100 problems to: {output_file}")
    print(f"\nProblem Distribution:")
    for diff, count in difficulty_counts.items():
        if count > 0:
            print(f"   {diff}: {count}")
    
    # Show first problem as example
    print(f"\nExample - First Problem:")
    print(f"   ID: {selected[0]['question_id']}")
    print(f"   Title: {selected[0]['title']}")
    print(f"   Difficulty: {selected[0]['difficulty']}")
    print(f"   Description (first 150 chars):")
    desc_preview = selected[0]['description'][:150].replace('\n', ' ')
    print(f"   {desc_preview}...")
    
    print(f"\nNext Steps:")
    print(f"   1. Open 'my_100_problems.json' to see all problems")
    print(f"   2. Run 'python batch_tester.py' to initialize tracking")
    print(f"   3. Start testing with CORA extension!")

except Exception as e:
    print(f"\nError occurred: {e}")
    print("\nTroubleshooting:")
    print("   - Check your internet connection")
    print("   - The dataset might be downloading in background")
    print("   - Try running the script again in a moment")
    print("\nFull error details:")
    import traceback
    traceback.print_exc()