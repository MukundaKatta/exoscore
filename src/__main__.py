"""CLI for exoscore."""
import sys, json, argparse
from .core import Exoscore

def main():
    parser = argparse.ArgumentParser(description="ExoScore — Exoplanet Habitability Scorer. Rank exoplanets by habitability using multi-parameter analysis.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Exoscore()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"exoscore v0.1.0 — ExoScore — Exoplanet Habitability Scorer. Rank exoplanets by habitability using multi-parameter analysis.")

if __name__ == "__main__":
    main()
