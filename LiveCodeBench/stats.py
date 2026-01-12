#!/usr/bin/env python3
"""
Quick stats for CORA benchmark progress
Shows: Passed/Failed counts, completion %, time remaining, pace needed
"""
import json
from pathlib import Path
from datetime import datetime

def show_stats():
    base_dir = Path(__file__).parent
    results_file = base_dir / "cora_results.json"
    
    if not results_file.exists():
        print("No results yet. Start testing to generate results!")
        return
    
    with open(results_file, 'r') as f:
        results = json.load(f)
    
    # Calculate stats
    total_problems = 100
    completed = len(results)
    passed = sum(1 for r in results if r.get("passed", False))
    failed = completed - passed
    remaining = total_problems - completed
    
    # Completion percentage
    completion_pct = (completed / total_problems) * 100
    
    # Pace calculation (Tuesday deadline)
    # Assuming it's Monday now, need to finish by end of Tuesday (2 days)
    days_left = 2  # Approximately 2 days (Mon evening to Tue end)
    pace_needed = remaining / days_left if days_left > 0 else 0
    
    # Display
    print("\n" + "="*60)
    print("📊 CORA BENCHMARK PROGRESS REPORT")
    print("="*60)
    print(f"\n✓ Completed:    {completed:3d}/100 ({completion_pct:5.1f}%)")
    print(f"  ├─ Passed:   {passed:3d}")
    print(f"  └─ Failed:   {failed:3d}")
    print(f"\n⏳ Remaining:    {remaining:3d} problems")
    print(f"📅 Deadline:    Tuesday (≈{days_left} days)")
    print(f"⚡ Pace needed:  {pace_needed:.1f} problems/day")
    
    # Progress bar
    bar_length = 40
    filled = int(bar_length * completed / total_problems)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\nProgress: [{bar}] {completion_pct:.1f}%")
    
    # Status
    if remaining == 0:
        print("\n🎉 ALL PROBLEMS COMPLETED!")
    elif pace_needed <= 10:
        print(f"\n✅ On track! Test ~{pace_needed:.0f}/day to finish on time")
    elif pace_needed <= 15:
        print(f"\n⚠️  Need to pick up pace! Test ~{pace_needed:.0f}/day")
    else:
        print(f"\n🔴 Behind schedule! Test ~{pace_needed:.0f}/day to catch up")
    
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    show_stats()
