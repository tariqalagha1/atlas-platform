import sys
from atlas.hermes.runtime import HermesRuntime


VERSION = "0.1.0-alpha"


def print_help():
    print("Atlas OS CLI")
    print("")
    print("Commands:")
    print("  atlasctl version")
    print("  atlasctl status")
    print("  atlasctl hermes start <workspace>")


def main():
    args = sys.argv[1:]

    if not args:
        print_help()
        return

    if args[0] == "version":
        print(f"Atlas OS {VERSION}")
        return

    if args[0] == "status":
        print({
            "platform": "Atlas OS",
            "version": VERSION,
            "status": "online",
        })
        return

    if args[0] == "hermes":
        if len(args) >= 3 and args[1] == "start":
            workspace = args[2]
            print(HermesRuntime(workspace).start())
            return

        print("Usage: atlasctl hermes start <workspace>")
        return

    print(f"Unknown command: {args[0]}")
    print_help()


if __name__ == "__main__":
    main()
