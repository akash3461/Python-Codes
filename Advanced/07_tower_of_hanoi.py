# This function shows how to move disks in the Tower of Hanoi problem
def tower_of_hanoi(number_of_disks, from_rod, help_rod, to_rod):

    # If there is only one disk, just move it directly
    if number_of_disks == 1:
        print(f"Move disk 1 from {from_rod} to {to_rod}")
        return

    # Step 1: Move the top (number_of_disks - 1) disks to the helper rod
    tower_of_hanoi(number_of_disks - 1, from_rod, to_rod, help_rod)

    # Step 2: Move the biggest disk to the destination rod
    print(f"Move disk {number_of_disks} from {from_rod} to {to_rod}")

    # Step 3: Move the disks from helper rod to destination rod
    tower_of_hanoi(number_of_disks - 1, help_rod, from_rod, to_rod)


# Starting the program with 3 disks and three rods
tower_of_hanoi(3, "A", "B", "C")

'''
            OUTPUT:
    Move disk 1 from A to C
    Move disk 2 from A to B
    Move disk 1 from C to B
    Move disk 3 from A to C
    Move disk 1 from B to A
    Move disk 2 from B to C
    Move disk 1 from A to C
    
'''