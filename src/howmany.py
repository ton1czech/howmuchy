from argparse import ArgumentParser
from time import monotonic

def main():
    start = monotonic()

    parser = ArgumentParser()

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    print(args.accumulate(args.integers))

    print(f"Took {format(monotonic() - start, '.3f')} seconds.")

if __name__ == "__main__":
    main()