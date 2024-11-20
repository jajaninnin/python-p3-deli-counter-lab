def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        current_line = "The line is currently: " + " ".join([f"{i+1}. {name}" for i, name in enumerate(queue)])
        print(current_line)

def take_a_number(curr_line, new_person):
    curr_line.append(new_person)
    print(f"Welcome, {new_person}. You are number {len(curr_line)} in line.")

def now_serving(queue):
    if len(queue) == 0:
        print("There is nobody waiting to be served!")
    else:   # Call out the next person in line and remove them
        print(f"Currently serving {queue.pop(0)}.")