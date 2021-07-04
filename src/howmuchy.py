import os
from argparse import ArgumentParser
from time import monotonic

__version__ = "0.1.0"

def search_files(directory, extension):
    idx = 1
    for _, _, files in os.walk(directory):
        for name in(files):
            if extension and name.endswith(extension):
                print(f"{idx}: {os.path.join(name)}")
            elif not extension:
                print(f"{idx}: {os.path.join(name)}")
            idx += 1

def main():
    start = monotonic()

    parser = ArgumentParser(description="Ultimate tool to check your files, space left and more")

    parser.add_argument('-v', '--version',
                        action="version", version=__version__,
                        help="Display version"
                        )
    parser.add_argument('event',
                        help="""What do you want to do?
                        [f] => count of files,
                        [s] => space left
                        """
                        )
    parser.add_argument('-dir', '--directory',
                        action="store_true",
                        help="Change directory (default = current directory)"
                        )
    parser.add_argument('-ext', '--extension',
                        action="store_true",
                        help="specify extenstion (default = all extenstions)"
                        )

    # arg_group = parser.add_mutually_exclusive_group()
    # arg_group.add_argument('-s', '--short',
    #                        action='store_true',
    #                        help="Print little text"
    #                        )
    # arg_group.add_argument('-l', '--long',
    #                        action='store_true',
    #                        help="Print lots of text"
    #                        )

    args = parser.parse_args()

    if args.event == "f":
        if args.directory:
            directory = args.directory
        else:
            directory = os.getcwd()
        
        if args.extension:
            extension = args.extension
        else:
            extension = ''
        search_files(directory, extension)

    print(f"\nTook {format(monotonic() - start, '.3f')} seconds.")

if __name__ == "__main__":
    main()