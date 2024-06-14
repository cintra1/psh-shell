import sys
import os
import subprocess

def main():
    valid_commands = ["echo","exit","type"]
    PATH = os.environ.get("PATH")
    
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

            #searching the command into the path
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd.split()[1]}"):
                    cmd_path = f"{path}/{cmd.split()[1]}"

            if cmd.split()[1] in valid_commands:
                sys.stdout.write("{} is a shell builtin\n".format(cmd.split()[1]))
            elif cmd_path:
                sys.stdout.write(f"{cmd.split()[1]} is {cmd_path}\n")
            else:
                sys.stdout.write("{}: not found\n".format(cmd.split()[1]))

        if cmd_path:
            file = [cmd_path, cmd.split()[1]]
            subprocess.call(file)

            # subprocess.run([cmd.split()[0], cmd.split(' ', 1)[1]])

        if cmd.split()[0] not in valid_commands:
            sys.stdout.write("{}: command not found\n".format(cmd))

        continue

if __name__ == "__main__":
    main()
