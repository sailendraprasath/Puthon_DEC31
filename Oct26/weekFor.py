"""
expect output like this using nested for loop
Week-1:-
        Days-1
        Days-2
        Days-3
        ...
Week-2:-
        Days-1
        Days-2
        Days-3
        ...
"""
for week in range(1,5):
    print(f"Week-{week}:-")
    for day in range(1,8):
        print(f"\tDays-{day}")