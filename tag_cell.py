import json
import sys

def addseqnum(notestring: str) -> str:
    noteobj = json.loads(notestring)

    cells = noteobj["cells"] # list

    for seq, cell in enumerate(cells, start=1):
        metadata = cell["metadata"] if "metadata" in cell else dict()
        tags = metadata["tags"] if "tags" in metadata else list()
        tags.append(str(seq))

        metadata["tags"] = tags
        cell["metadata"] = metadata

    return json.dumps(noteobj, indent=2)


def main():
    if len(sys.argv) > 0:
        path = sys.argv[1]
        with open(path, "r") as f:
            tagged = addseqnum(f.read())

        with open(path, "w") as f:
            f.write(tagged)


if __name__ == "__main__":
    main()
