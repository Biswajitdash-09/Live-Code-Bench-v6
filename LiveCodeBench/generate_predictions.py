#!/usr/bin/env python3
"""
Generate LiveCodeBench-compatible predictions file from results.

Usage:
    python generate_predictions.py [--model MODEL_NAME] [--input INPUT_FILE] [--output OUTPUT_FILE]

Examples:
    python generate_predictions.py
    python generate_predictions.py --model cora
    python generate_predictions.py --model gpt4 --input gpt4_results.json
"""

import json
import argparse
from pathlib import Path
from datetime import datetime


def generate_predictions(
    model_name: str = "cora",
    input_file: str = None,
    output_file: str = None
) -> dict:
    """
    Convert detailed results JSON to LiveCodeBench-compatible predictions format.
    
    Input format (e.g., cora_results.json):
    [
      {"question_id": "1873_A", "cora_solution": "def solve()...", "passed": true, ...},
      ...
    ]
    
    Output format (LiveCodeBench-compatible):
    [
      {"question_id": "1873_A", "code_list": ["def solve()..."]},
      ...
    ]
    """
    base_dir = Path(__file__).parent
    
    # Determine input file
    if input_file:
        results_file = Path(input_file)
        if not results_file.is_absolute():
            results_file = base_dir / input_file
    else:
        results_file = base_dir / f"{model_name}_results.json"
    
    # Determine output file
    predictions_dir = base_dir / "predictions"
    predictions_dir.mkdir(exist_ok=True)
    
    if output_file:
        output_path = Path(output_file)
        if not output_path.is_absolute():
            output_path = predictions_dir / output_file
    else:
        output_path = predictions_dir / f"{model_name}_predictions.json"
    
    # Load results
    if not results_file.exists():
        print(f"❌ Error: Results file not found: {results_file}")
        return None
    
    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)
    
    print(f"📖 Loaded {len(results)} results from {results_file.name}")
    
    # Convert to predictions format
    # Group by question_id to support multiple solutions per problem
    predictions_map = {}
    
    for entry in results:
        qid = entry.get("question_id")
        if not qid:
            continue
        
        # Get solution code (support both old and new key names)
        solution = entry.get("cora_solution") or entry.get("solution_code") or ""
        
        if qid not in predictions_map:
            predictions_map[qid] = []
        
        if solution:
            predictions_map[qid].append(solution)
    
    # Convert to list format
    predictions = [
        {"question_id": qid, "code_list": codes}
        for qid, codes in predictions_map.items()
    ]
    
    # Sort by question_id for consistency
    predictions.sort(key=lambda x: x["question_id"])
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(predictions, f, indent=2)
    
    print(f"✅ Generated {len(predictions)} predictions → {output_path}")
    
    # Summary stats
    total_codes = sum(len(p["code_list"]) for p in predictions)
    print(f"   Total code samples: {total_codes}")
    
    return {
        "predictions_file": str(output_path),
        "num_problems": len(predictions),
        "total_codes": total_codes
    }


def main():
    parser = argparse.ArgumentParser(
        description="Generate LiveCodeBench-compatible predictions file"
    )
    parser.add_argument(
        "--model", "-m",
        default="cora",
        help="Model name (default: cora)"
    )
    parser.add_argument(
        "--input", "-i",
        default=None,
        help="Input results file (default: {model}_results.json)"
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help="Output predictions file (default: predictions/{model}_predictions.json)"
    )
    
    args = parser.parse_args()
    
    result = generate_predictions(
        model_name=args.model,
        input_file=args.input,
        output_file=args.output
    )
    
    if result:
        print(f"\n🎯 Ready for LiveCodeBench evaluation!")
        print(f"   Use: {result['predictions_file']}")


if __name__ == "__main__":
    main()
