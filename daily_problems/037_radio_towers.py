'''
This problem was asked by Spotify.

You are the technical director of WSPT radio,
serving listeners nationwide. For simplicity's
sake we can consider each listener to live along a
horizontal line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers,
each placed at various locations along this line, determine
what the minimum broadcast range would have to be in order for
each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15].
In this case the minimum range would be 5, since that would
be required for the tower at position 15 to reach the listener at position 20.

'''
listeners = [1, 5, 11, 20]
towers = [4, 8, 15]


# ON2

def tower_range(listeners, towers):
    max_range = -1
    best_personal_range = float('inf')

    for person in listeners:
        for tower in towers:
            best_personal_range = min( abs(tower-person), best_personal_range)
        max_range = max(best_personal_range, max_range)
        best_personal_range = float('inf')
    return max_range

print(tower_range(listeners, towers))

# O(M+N)
# if sorted
def b_range(listener, towers):
    tower = [-float('inf') + towers + float('inf')]
    min_range = 0 ; i = 0

    for person in listeners:
        while person < tower[i+1]:
            i += 1
        current_min = min(person - tower[i], tower[i+1] - person)
        min_range = max(current_min, min_range)
    return min_range

print(tower_range(listeners, towers))

# O(M+N log M)
def broadcast_range(listeners, towers):
    min_range = 0
    tower = [-float('inf')] + sorted(towers) + [float('inf')]

    for person in listeners:
        idx = search(person, tower)

        left = person - tower[idx -1]
        right = tower[idx] - person

        min_range = max(min_range, min(left, right))
    return min_range

def search(person,tower):
    lo = 0; hi = len(tower)-1

    while lo <= hi:
        mid = (lo+hi)//2

        if tower[mid] > person:
            hi = mid - 1
        elif tower[mid] < person:
            lo = mid + 1
        else:
            return mid

    return lo

print(broadcast_range(listeners, towers))
