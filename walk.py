def feet_to_steps(feet_walked):
    steps = feet_walked // 2.5
    return int(steps)

def main():
    walk_dist = float(input())
    
    steps = feet_to_steps(walk_dist)
    
    print(steps)
    
main()