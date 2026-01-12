import json

with open('my_100_problems.json', 'r') as f:
    problems = json.load(f)
    p = problems[1]
    
print('=' * 70)
print(f'PROBLEM #{p.get("index")}: {p.get("title")}')
print(f'ID: {p.get("question_id")} | Difficulty: {p.get("difficulty").upper()}')
print('=' * 70)
print()
print('DESCRIPTION:')
print(p.get('description', 'N/A')[:900])
print()
print('=' * 70)
print('SAMPLE INPUT:')
if p.get('input_output'):
    print(p['input_output'].get('inputs', 'N/A'))
print()
print('SAMPLE OUTPUT:')
if p.get('input_output'):
    print(p['input_output'].get('outputs', 'N/A'))
print('=' * 70)
