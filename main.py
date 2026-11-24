import os

# Real-Life Patch Notes entry: one-line comedy changelog.
ENTRY_TEXT = "v4.0.2: patched both knees to stop announcing the stairs. Known issue: the fix expires a little more every birthday."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
