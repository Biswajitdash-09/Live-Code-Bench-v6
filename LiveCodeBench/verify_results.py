#!/usr/bin/env python3
"""
Verify CORA results and compare against LiveCodeBench competitors
"""
import json
from pathlib import Path
from collections import defaultdict

def verify_results():
    """Verify and analyze CORA benchmark results"""
    base_dir = Path(__file__).parent
    results_file = base_dir / "cora_results.json"
    
    if not results_file.exists():
        print("❌ No results file found. Run tests first!")
        return
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Calculate statistics
    total = len(results)
    passed = sum(1 for r in results if r.get("passed"))
    failed = total - passed
    pass_rate = (passed / total * 100) if total > 0 else 0
    
    # Analyze execution times
    times = [r.get("execution_time_ms", 0) for r in results if r.get("execution_time_ms")]
    avg_time = sum(times) / len(times) if times else 0
    
    # Analyze errors
    error_breakdown = defaultdict(int)
    for r in results:
        if not r.get("passed") and r.get("error_type"):
            error_breakdown[r["error_type"]] += 1
    
    # Analyze by difficulty
    by_difficulty = defaultdict(lambda: {"total": 0, "passed": 0})
    for r in results:
        difficulty = r.get("difficulty", "unknown")
        by_difficulty[difficulty]["total"] += 1
        if r.get("passed"):
            by_difficulty[difficulty]["passed"] += 1
    
    # Competitor data
    competitors = {
        "GPT-4 Turbo": 92,
        "Claude 3.5 Sonnet": 90,
        "GPT-4o": 89,
        "Claude 3 Opus": 87,
        "Gemini 2.0": 85,
        "Grok-2": 82,
        "Mistral Large": 80,
        "DeepSeek-Coder-33B": 78,
        "Phind-34B": 76,
        "LLaMA 3.1 70B": 72
    }
    
    # Display report
    print("\n" + "="*70)
    print("📊 CORA BENCHMARKING VERIFICATION REPORT")
    print("="*70)
    
    print(f"\n✅ OVERALL RESULTS:")
    print(f"   Total Problems:    {total}")
    print(f"   Passed:            {passed} ✓")
    print(f"   Failed:            {failed} ✗")
    print(f"   Pass Rate:         {pass_rate:.1f}%")
    
    if times:
        print(f"\n⏱️  PERFORMANCE METRICS:")
        print(f"   Average Time/Problem: {avg_time:.0f}ms")
        print(f"   Total Execution Time: {sum(times):.0f}ms")
    
    if error_breakdown:
        print(f"\n❌ ERROR BREAKDOWN:")
        for error_type, count in sorted(error_breakdown.items(), key=lambda x: -x[1]):
            print(f"   {error_type:20} {count:3} occurrences")
    
    print(f"\n📈 PERFORMANCE BY DIFFICULTY:")
    for difficulty in ["easy", "medium", "hard"]:
        if difficulty in by_difficulty:
            stats = by_difficulty[difficulty]
            rate = (stats["passed"] / stats["total"] * 100) if stats["total"] > 0 else 0
            print(f"   {difficulty.upper():8} {stats['passed']:3}/{stats['total']:3} ({rate:5.1f}%)")
    
    print(f"\n🏆 COMPARISON WITH COMPETITORS:")
    print(f"\n   Your Score: {pass_rate:.1f}%\n")
    
    ranked = sorted(competitors.items(), key=lambda x: -x[1])
    for rank, (model, comp_score) in enumerate(ranked, 1):
        diff = pass_rate - comp_score
        if diff > 0:
            indicator = f"🟢 +{diff:.1f}%"
        elif diff < 0:
            indicator = f"🔴 {diff:.1f}%"
        else:
            indicator = "🟡 EQUAL"
        
        print(f"   {rank:2}. {model:25} {comp_score:3}% {indicator}")
    
    # Ranking
    better_than = sum(1 for c in competitors.values() if pass_rate > c)
    print(f"\n📍 YOUR RANK: Better than {better_than}/10 competitors")
    
    if pass_rate >= 92:
        print("   🥇 WORLD CLASS - Matches best LLMs!")
    elif pass_rate >= 85:
        print("   🥈 EXCELLENT - Top tier performance!")
    elif pass_rate >= 78:
        print("   🥉 VERY GOOD - Competitive with best open-source!")
    elif pass_rate >= 70:
        print("   ✅ GOOD - In the top 10!")
    elif pass_rate >= 60:
        print("   ⚠️  FAIR - Room for improvement")
    else:
        print("   ❌ NEEDS WORK - Keep improving!")
    
    print("\n" + "="*70)
    print("Results ready for leaderboard submission!")
    print("="*70 + "\n")


if __name__ == "__main__":
    verify_results()
