"""Execute every workshop notebook with its exercise solutions filled in.

Each ``# %load solutions/...`` cell is replaced by the solution file it loads,
so the solutions run too. Executed copies go to ``executed/``. The script exits
nonzero if any notebook fails, after trying them all.
"""

import pathlib
import sys
import time

import nbformat
from nbclient import NotebookClient

ROOT = pathlib.Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
OUT = ROOT / "executed"


def execute(path):
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        lines = cell.source.strip().splitlines()
        # a bare "# %load" cell gets its solution; one with the solution already pasted in runs as is
        if cell.cell_type == "code" and len(lines) == 1 and lines[0].startswith("# %load solutions/"):
            cell.source = (CONTENT / lines[0].split()[-1]).read_text()
    client = NotebookClient(
        nb, timeout=1800, kernel_name="python3", resources={"metadata": {"path": str(CONTENT)}}
    )
    try:
        client.execute()
        return nb, None
    except Exception as error:  # noqa: BLE001
        return nb, error
    finally:
        OUT.mkdir(exist_ok=True)
        nbformat.write(nb, OUT / path.name)


def main(names):
    paths = [CONTENT / n for n in names] if names else sorted(CONTENT.glob("*.ipynb"))
    failed = []
    for path in paths:
        start = time.perf_counter()
        _, error = execute(path)
        elapsed = time.perf_counter() - start
        if error is None:
            print(f"ok      {path.name} ({elapsed:.0f} s)", flush=True)
        else:
            print(f"FAILED  {path.name} ({elapsed:.0f} s)\n{str(error)[-3000:]}", flush=True)
            failed.append(path.name)
    if failed:
        print(f"\n{len(failed)} notebook(s) failed: {', '.join(failed)}")
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
