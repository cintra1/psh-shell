import sys


def main():
    valid_commands = ["echo"]
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        cmd = input()

        if cmd == "exit 0":
            exit(0)

        if "echo" not in cmd:
            sys.stdout.write(cmd[4:])

        if cmd not in valid_commands:
            sys.stdout.write("{}: command not found\n".format(cmd))

        continue

if __name__ == "__main__":
    main()
