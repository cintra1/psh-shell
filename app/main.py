import sys


def main():
    valid_commands = ["echo","exit","type"]
    
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        cmd = input()

        if cmd == "exit 0":
            exit(0)

        if cmd.split()[0] == "echo":
            sys.stdout.write("{}\n".format(cmd[5:]))

        if cmd.split()[0] == "type":
            if cmd.split()[1] in valid_commands:
                sys.stdout.write("{} is a shell builtin\n".format(cmd.split()[1]))

        if cmd.split()[0] not in valid_commands:
            sys.stdout.write("{}: command not found\n".format(cmd))

        continue

if __name__ == "__main__":
    main()
