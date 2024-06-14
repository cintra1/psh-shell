import sys
import os
import subprocess

def main():
    # Define a list of valid shell built-in commands
    valid_commands = ["echo", "exit", "type", "pwd", "cd"]
    
    # Retrieve system's PATH and HOME environment variables
    PATH = os.environ.get("PATH")
    HOME = os.environ.get("HOME")
    OP = True

    # Infinite loop to continuously prompt the user for input
    while OP:

        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        cmd = input()

        if cmd == "!q":
            OP = False
        
        # Exit the shell if the user inputs "exit 0"
        if cmd == "exit 0":
            exit(0)

        # Handle the "echo" command
        if cmd.split()[0] == "echo":
            sys.stdout.write("{}\n".format(cmd[5:]))

        # Handle the "type" command
        if cmd.split()[0] == "type":
            # Initialize command path as None
            cmd_path = None
            # Split PATH into directories and search for the command
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd.split()[1]}"):
                    cmd_path = f"{path}/{cmd.split()[1]}"

            # Check if the command is a built-in
            if cmd.split()[1] in valid_commands:
                sys.stdout.write("{} is a shell builtin\n".format(cmd.split()[1]))
            # If not a built-in, check if it is an external command
            elif cmd_path:
                sys.stdout.write(f"{cmd.split()[1]} is {cmd_path}\n")
            # If the command is not found
            else:
                sys.stdout.write("{}: not found\n".format(cmd.split()[1]))

        # Handle the "pwd" command
        if cmd.split()[0] == "pwd":
             sys.stdout.write("{}\n".format(os.getcwd()))

        # Handle the "cd" command
        if cmd.split()[0] == "cd":
            # If the argument is "~", change to the HOME directory
            if cmd.split(' ', 1)[1] == "~":
                try:
                    os.chdir(HOME)
                except OSError:
                    print(f"cd: {cmd.split(' ', 1)[1]}: No such file or directory")
            # Otherwise, change to the specified directory
            else:
                try:
                    os.chdir(cmd.split(' ', 1)[1])
                except OSError:
                    print(f"cd: {cmd.split(' ', 1)[1]}: No such file or directory")
                
        # Handle unknown commands
        if cmd.split()[0] not in valid_commands:
            # Initialize command path as None
            cmd_path = None
            # Split PATH into directories and search for the command
            paths = PATH.split(":")
            for path in paths:
                if os.path.isfile(f"{path}/{cmd.split()[0]}"):
                    cmd_path = f"{path}/{cmd.split()[0]}"
            
            # If the command is found, execute it
            if cmd_path:
                file = [cmd_path, cmd.split(' ', 1)[1]]
                subprocess.call(file) 
            # If the command is not found, display an error message
            else:
                sys.stdout.write("{}: command not found\n".format(cmd))

        continue

if __name__ == "__main__":
    main()