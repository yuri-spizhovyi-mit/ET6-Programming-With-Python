def print_move(disk, fr, to):
    print(f"Move {disk} from {fr} to {to}")


def towers(n, fr, to, spare):
    if n == 1:
        # Move the smallest disk directly
        print_move(n, fr, to)
    else:
        # Move n-1 disks from 'fr' to 'spare' using 'to' as helper
        towers(n - 1, fr, spare, to)

        # Move the largest remaining disk from 'fr' to 'to'
        print_move(n, fr, to)

        # Move n-1 disks from 'spare' to 'to' using 'fr' as helper
        towers(n - 1, spare, to, fr)


# Run the function with 4 disks
towers(2, "P1", "P2", "P3")
