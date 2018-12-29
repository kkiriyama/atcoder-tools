import sys

from atcodertools.tools.envgen import main as envgen_main
from atcodertools.tools.tester import main as tester_main


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("gen", "test"):
        print("Usage:")
        print("{} gen -- to generate workspace".format(sys.argv[0]))
        print("{} test -- to test codes in your workspace".format(sys.argv[0]))
        sys.exit(-1)

    prog = " ".join(sys.argv[:2])
    args = sys.argv[2:]

    if sys.argv[1] == "gen":
        envgen_main(prog, args)

    if sys.argv[1] == "test":
        sys.exit(tester_main(prog, args))


if __name__ == '__main__':
    main()