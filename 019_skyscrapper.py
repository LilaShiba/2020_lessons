'''
This problem was asked by Mailchimp.

You are given an array representing the heights of 
neighboring buildings on a city street, from east to west. 
The city assessor would like you to write an algorithm 
that returns how many of these buildings have a view of 
the setting sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], 
you should return 3, since the top floors of the 
buildings with heights 8, 6, and 1 all have an 
unobstructed view to the west.

Can you do this using just one forward pass through the array?

'''

buildings = [20, 3, 7, 8, 3, 10, 1]
ans = [8,6,1]

def simple(buildings):
    height = 0
    views = []
    for x in range(len(buildings)-1,-1,-1):
        if buildings[x] > height:
            views.append(buildings[x])
        height = max(height, buildings[x])
    print(views)



def forward_pass(buildings):
    view = []
    height = 0
    
    
    for x in range(len(buildings)-1):
        if buildings[x] > buildings[x+1]:
            height = buildings[x]
            view.append(buildings[x])
        elif height > buildings[x]:
            view = [x for x in view if x >= height]
    view.append(buildings[-1])
    return view
    

def sunset_views(buildings):
    views = []
    highest = 0

    for building in buildings:
        while views and views[-1] <= building:
            views.pop()
        views.append(building)

    return len(views)

            
    
#print(simple(buildings))
print(forward_pass(buildings))