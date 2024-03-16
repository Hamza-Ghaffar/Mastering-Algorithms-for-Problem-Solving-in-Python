# Write code for tower of Hanoi with logical_example no 1
def TOH(n_o_disk, Source, Dest, Helper):
    # first we need to check our base cases
    if n_o_disk == 0:
        # In my case I will also check poles are empty or not !
        print(f'Your Tower of Hanoi Poles Having {n_o_disk} Disks')
    if n_o_disk == 1:
        print(f'Move disk {n_o_disk} from {Source} Pole to {Dest}')
        # if base case matches so our programme return and not process further
        return
    TOH(n_o_disk-1,Source,Helper,Dest)
    print(f'Move disk {n_o_disk} from {Source} Pole to {Dest}')
    TOH(n_o_disk - 1, Helper,Dest,Source)





TOH(3,"Pole A", "Pole B","Pole C")

