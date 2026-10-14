"""Render the four retained contact-compatible P5/Q14 states.

Exact faces are reconstructed from the reviewed palette certificate. Floating
point is used only for display, never for a geometric decision. This optional
visualization is not a certificate verifier.
"""
import json
import runpy
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.hashsalt"] = "arisearch-q14-contact-states-v1"
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "research/certificates/construction-adversary-2026-10-14-p5q14-palette.json"
OUTPUT = ROOT / "research/figures/contact-pentagon-5pi7-q14-dimer-patches.svg"


def main():
    data = json.loads(DATA.read_text())
    rows = [r for r in data["patches"]
            if r["status"] == "no_obstruction_in_this_patch" and
            "".join("v" if bit else "u" for bit in r["word"][:7]) == "vvuvvuu"]
    assert len(rows) == 4
    D = runpy.run_path(str(ROOT / "research/reviews/construction-adversary-2026-10-14-p5q14-independent.py"))
    patches = []
    for row in rows:
        word = row["word"]
        Q = D["polygon"]([(D["v"] if bit else 1)*D["z"]**(2*k) for k, bit in enumerate(word)])
        opts = [D["options"](Q, k, word) for k in range(14)]
        faces = [Q] + [opts[k][c]["face"] for k, c in enumerate(row["cycle"])]
        for face in faces[1:].copy():
            mate = D["mate"](face)
            if not any(set(mate) == set(other) for other in faces):
                faces.append(mate)
        assert len(faces) == 21
        patches.append([[(float(D["embedding"](p).real()), float(D["embedding"](p).imag()))
                         for p in face] for face in faces])
    all_points = [p for patch in patches for face in patch for p in face]
    xmin, xmax = min(p[0] for p in all_points), max(p[0] for p in all_points)
    ymin, ymax = min(p[1] for p in all_points), max(p[1] for p in all_points)
    margin = 0.06 * max(xmax-xmin, ymax-ymin)
    fig, axes = plt.subplots(2, 2, figsize=(10, 11))
    for number, (ax, patch) in enumerate(zip(axes.flat, patches), 1):
        for index, vertices in enumerate(patch):
            ax.add_patch(Polygon(vertices, facecolor="#9b84c9" if index == 0 else "#8ac7be",
                                 edgecolor="#273444", linewidth=0.65))
        ax.set_xlim(xmin-margin, xmax+margin)
        ax.set_ylim(ymin-margin, ymax+margin)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title("Local state " + str(number), fontsize=12)
    fig.suptitle("P5 / Q14: four surviving states for Q word (vvuvvuu)²", fontsize=14)
    fig.text(0.5, 0.025, "One Q and twenty P per patch. Contacts checked; plane extension remains unproved.",
             ha="center", fontsize=10, color="#39485c")
    fig.tight_layout(rect=(0, 0.05, 1, 0.96))
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, metadata={"Date": None})
    OUTPUT.write_text("\n".join(line.rstrip() for line in OUTPUT.read_text().splitlines()) + "\n")
    print(OUTPUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
