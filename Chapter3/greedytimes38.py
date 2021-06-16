# Chapter 3, Computer Project 8: Given the starting and ending times of n talks, use the
# appropriate greedy algorithm to schedule the most talks
# possible in a single lecture hall.

# Greedy Algorithm for Scheduling Summary:
# Algorithms that make what seems to be the “best”
# choice at each step are called greedy algorithms.
# For the case of talks, it can be shown that we schedule the most talks possible if in each 
# step we select the talk with the earliest ending time among the talks compatible with those 
# already selected.

def main():
    # Input: Array of n 3-tuples where first element of the 3-tuple is talk name(a string), second element 
    # start time, third element is end time. Times should be on 24 hour clock.
    talks = [("Talk 1", "12:10", "13:30"), ("Talk 2", "10:10", "11:30"),("Talk 3", "9:10", "10:30"),("Talk 4", "13:30", "14:50")]

    # Sort talks by earliest ending time
    talks.sort(key=lambda x: x[2]) 
    # [('Talk 3', '9:10', '10:30'), ('Talk 2', '10:10', '11:30'), ('Talk 1', '12:10', '13:30')]

    
    # Generate Schedule of Talks
    schedule =[]
    schedule.append(talks[0])
    i = 0
    for j in range(1,len(talks)):
        if (talks[j][1] >= schedule[i][2]):
            schedule.append(talks[j])
            i += 1

    # Output Scheduled Talks
    print(schedule)
        


if __name__ == "__main__":
    main()