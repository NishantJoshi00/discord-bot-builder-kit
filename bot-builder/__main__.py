import sys


from create import create_command
from host import host_command, rehost_command


def handle_args(argv):

    if len(argv) == 1:
        print("Subcommands\n\tcreate\n\thost\n\trehost")
    elif len(argv) >= 2:

        if argv[1] == "create":
            
            create_command(argv[2:])
            
        elif argv[1] == "host":
            host_command(argv[2:])
        elif argv[1] == "rehost":
            rehost_command(argv[2:])

        else:
            
            return handle_args(argv[:1])


handle_args(sys.argv)