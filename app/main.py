import sys


def main():
    valid_commands = []
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        cmd = input()
        
        if cmd == "error":
            exit(0)

        if cmd is not valid_commands:
            sys.stdout.write("{}: command not found\n".format(cmd))

        continue

if __name__ == "__main__":
    main()
