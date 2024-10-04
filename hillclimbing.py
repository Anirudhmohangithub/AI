def can_host_contest():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # Read number of hills
    index = 0
    N = int(data[index])
    index += 1

    # Calculate total energy requirement
    total_energy_required = 0
    for _ in range(N):
        H, B = map(int, data[index].split())
        total_energy_required += 3 * H  # Energy needed for this hill
        index += 1

    # Read number of students
    S = int(data[index])
    index += 1

    # Count how many students can participate
    sufficient_energy_count = 0
    for _ in range(S):
        E = int(data[index])
        if E >= total_energy_required:
            sufficient_energy_count += 1
        index += 1

    # Determine if at least half can participate
    if sufficient_energy_count * 2 >= S:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    can_host_contest()
