import sys
import os
import subprocess

def search_command(cmd):
    """Searches for the executable path of a command."""
    cmd_name = cmd.split()[0]
    # Retrieve system's PATH environment variable
    PATH = os.environ.get("PATH")
    # Split PATH into directories and search for the command
    paths = PATH.split(":")
    for path in paths:
        if os.path.isfile(f"{path}/{cmd_name}"):
            return f"{path}/{cmd_name}"
    return None

def main():
    # Define a set of valid shell built-in commands
    valid_commands = {"echo", "exit", "type", "pwd", "cd"}
    
    # Retrieve system's HOME environment variable
    HOME = os.environ.get("HOME")

    # Infinite loop to continuously prompt the user for input
    while True:
        # Display the shell prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()
        
        # Wait for user input
        cmd = input()

        # Exit the shell if the user inputs "exit 0"
        if cmd == "exit 0":
            exit(0)
        
        # Handle the "echo" command
        if cmd.startswith("echo "):
            sys.stdout.write(f"{cmd[5:]}\n")
        
        # Handle the "type" command
        elif cmd.startswith("type "):
            cmd_parts = cmd.split()
            cmd_name = cmd_parts[1]
            if cmd_name in valid_commands:
                sys.stdout.write(f"{cmd_name} is a shell builtin\n")
            else:
                cmd_path = search_command(cmd)
                if cmd_path:
                    sys.stdout.write(f"{cmd_name} is {cmd_path}\n")
                else:
                    sys.stdout.write(f"{cmd_name}: not found\n")
        
        # Handle the "pwd" command
        elif cmd == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")
        
        # Handle the "cd" command
        elif cmd.startswith("cd "):
            try:
                if cmd == "cd ~":
                    os.chdir(HOME)
                else:
                    os.chdir(cmd[3:])
            except OSError:
                sys.stderr.write(f"cd: {cmd[3:]}: No such file or directory\n")
        
        # Handle unknown commands
        else:
            cmd_path = search_command(cmd)
            if cmd_path:
                try:
                    subprocess.run([cmd_path] + cmd.split()[1:])
                except FileNotFoundError:
                    sys.stderr.write(f"{cmd}: command not found\n")
            else:
                sys.stderr.write(f"{cmd}: command not found\n")

if __name__ == "__main__":
    main()
