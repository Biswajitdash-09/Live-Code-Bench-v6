from itertools import groupby
import bisect

def countZeroRequestServers(n, logs, x, queries):
    # Group logs by server_id
    logs.sort()
    server_times = {}
    for server_id, group in groupby(logs, key=lambda x: x[0]):
        server_times[server_id] = []
    
    for server_id, time in logs:
        server_times[server_id].append(time)
    
    result = []
    for q in queries:
        count = 0
        start = q - x
        end = q
        for i in range(n):
            if i not in server_times:
                count += 1
                continue
            times = server_times[i]
            # Binary search to find if any time is in [start, end]
            idx = bisect.bisect_left(times, start)
            if idx == len(times) or times[idx] > end:
                count += 1
        result.append(count)
    return result