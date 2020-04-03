'''
This problem was asked by Walmart Labs.

There are M people sitting in a row of N seats, where M < N.
Your task is to redistribute people such that there are no gaps
between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1],
where 0 represents an empty seat and 1 represents a person. In this case, one
solution would be to place the person on the right in the fourth seat. We can
 consider the cost of a solution to be the sum of the absolute distance each person
 must move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving
people to remove all gaps.

'''
import random
s = [random.randint(0,1) for x in range(10)]


def should_swap(seats, median, rev=False):
    mark = False

    if rev:
        for x in seats[median+1:]:
            if x == 0:
                mark = True
            if x == 1 and mark:
                return True
        return False


    for x in seats[:median]:
        if x == 1:
            mark = True
        if x == 0 and mark:
            return True
    return False


def move(seats):
    # calculate indices of taken seats
    people = [i for i, x in enumerate(seats) if x == 1]
    n = len(people)
    # find median of seats taken
    median = people[n//2]
    cost = 0
    seats[median] = "x"
    print(seats)

    current_seat = median
    current_person = n//2 -1
    left_people = people[:n//2]
    # need to swap?
    need_to_loop = should_swap(seats, median)
    # if need to swap, move to right
    if need_to_loop:
        while len(left_people) > 0 and current_seat >=0:
            if seats[current_seat] == 0:
                current_person = left_people.pop(-1)
                # ensure current person is not greater than where seat is, if not this will mess up the ordering
                while current_person >= current_seat and left_people:
                    current_person = left_people.pop(-1)
                cost += abs(current_seat - current_person)
                seats[current_seat], seats[current_person] = seats[current_person], seats[current_seat]

            current_seat -= 1


    current_seat = median+1
    current_person = n//2+1
    right_people = people[current_person:]
    # need to swap?
    need_to_loop = should_swap(seats, median, True)
    # if need to swap, move to right
    if need_to_loop:
        while len(right_people) > 0 and current_person < len(seats):
            if seats[current_seat] == 0:
                current_person = right_people.pop(0)
                while current_seat >= current_person and right_people:
                    current_person = right_people.pop(0)
                cost += abs(current_seat - current_person)
                seats[current_seat], seats[current_person] = seats[current_person], seats[current_seat]
                #seats[people[current_person]] = '0'

            current_seat += 1
    return seats,cost

print(move(s))
