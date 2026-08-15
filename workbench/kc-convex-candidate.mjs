/*
 * Exact finite audit for the Kari–Culik winding-cover source used by the
 * convex-honeycomb candidate.  This is a research artifact, not product code:
 * it enumerates source symbols, legal vertex flags, and legal face coronas.
 */

import { createHash } from "node:crypto";

const BASE_TILES = [
  // Division rows (multiplier 1/3).
  { s: "1", w: "0/3", n: "0", e: "1/3", kind: "D" },
  { s: "1", w: "1/3", n: "0", e: "2/3", kind: "D" },
  { s: "1", w: "2/3", n: "1", e: "0/3", kind: "D" },
  { s: "2", w: "0/3", n: "0", e: "2/3", kind: "D" },
  { s: "2", w: "1/3", n: "1", e: "0/3", kind: "D" },
  { s: "2", w: "2/3", n: "1", e: "1/3", kind: "D" },
  // Doubling rows (multiplier 2).  0 and 0' are distinct edge colors.
  { s: "0", w: "-1", n: "0'", e: "-1", kind: "M" },
  { s: "0", w: "0", n: "0'", e: "0", kind: "M" },
  { s: "0", w: "0", n: "1", e: "-1", kind: "M" },
  { s: "1", w: "-1", n: "1", e: "0", kind: "M" },
  { s: "1", w: "-1", n: "2", e: "-1", kind: "M" },
  { s: "1", w: "0", n: "2", e: "0", kind: "M" },
  { s: "0'", w: "0", n: "1", e: "-1", kind: "M" },
];

const BASE_TILE_OCCURRENCE_COORDINATES = [
  [-1, 0],
  [2, 0],
  [-2, -3],
  [-2, 3],
  [-2, 0],
  [3, 0],
  [-3, -2],
  [4, -2],
  [-1, 1],
  [-1, -1],
  [-2, -1],
  [-2, 2],
  [-3, -1],
];

function positiveMod(value, modulus) {
  return ((value % modulus) + modulus) % modulus;
}

function labelInThirds(label) {
  if (label === "0'") return 0n;
  if (label.endsWith("/3")) return BigInt(Number.parseInt(label, 10));
  return 3n * BigInt(Number.parseInt(label, 10));
}

for (const [index, tile] of BASE_TILES.entries()) {
  const south = labelInThirds(tile.s);
  const west = labelInThirds(tile.w);
  const north = labelInThirds(tile.n);
  const east = labelInThirds(tile.e);
  const residual =
    tile.kind === "D"
      ? south + 3n * west - 3n * north - 3n * east
      : 2n * south + west - north - east;
  if (residual !== 0n) {
    throw new Error(`base tile ${index} violates its multiplier equation`);
  }
}

function liftedAlphabet(modulus) {
  return BASE_TILES.flatMap((tile, base) =>
    Array.from({ length: modulus }, (_, sheet) => {
      const increment = tile.kind === "D" ? 1 : 0;
      return {
        id: base * modulus + sheet,
        base,
        sheet,
        kind: tile.kind,
        s: `${tile.s}@${sheet}`,
        w: `${tile.w}@${sheet}`,
        n: `${tile.n}@${positiveMod(sheet + increment, modulus)}`,
        e: `${tile.e}@${sheet}`,
      };
    }),
  );
}

function adjacency(alphabet) {
  const east = alphabet.map((tile) =>
    alphabet.filter((other) => tile.e === other.w).map((other) => other.id),
  );
  const north = alphabet.map((tile) =>
    alphabet.filter((other) => tile.n === other.s).map((other) => other.id),
  );
  const west = alphabet.map(() => []);
  const south = alphabet.map(() => []);
  for (const tile of alphabet) {
    for (const other of east[tile.id]) west[other].push(tile.id);
    for (const other of north[tile.id]) south[other].push(tile.id);
  }
  return { east, north, west, south };
}

function intersection(left, right) {
  const rightSet = new Set(right);
  return left.filter((value) => rightSet.has(value));
}

function stateKey(part, i, j, triple) {
  return `${part}:${i},${j}:${triple.join(",")}`;
}

function canonicalDihedralCycle(cycle) {
  const variants = [];
  for (const oriented of [cycle, [...cycle].reverse()]) {
    for (let offset = 0; offset < oriented.length; offset += 1) {
      variants.push(
        [...oriented.slice(offset), ...oriented.slice(0, offset)].join(","),
      );
    }
  }
  variants.sort();
  return variants[0];
}

const BASE_VERTICES_TIMES_TWO = [
  [4n, 0n],
  [2n, 3n],
  [-2n, 3n],
  [-4n, 0n],
  [-2n, -3n],
  [2n, -3n],
];

function cross(left, right) {
  return left[0] * right[1] - left[1] * right[0];
}

function dot(left, right) {
  return left[0] * right[0] + left[1] * right[1];
}

function integerSquareRoot(value) {
  if (value < 0n) throw new Error("square root of a negative integer");
  if (value < 2n) return value;
  let estimate = 1n << BigInt(Math.ceil(value.toString(2).length / 2));
  while (true) {
    const next = (estimate + value / estimate) >> 1n;
    if (next >= estimate) return estimate;
    estimate = next;
  }
}

// An angle is represented exactly as (numerator / denominator) * sqrt(2).
function reduceAngle(angle) {
  let { numerator, denominator } = angle;
  while (numerator % 2n === 0n && denominator % 2n === 0n) {
    numerator /= 2n;
    denominator /= 2n;
  }
  while (numerator % 3n === 0n && denominator % 3n === 0n) {
    numerator /= 3n;
    denominator /= 3n;
  }
  return { numerator, denominator };
}

function angleLessThanOne(angle) {
  return 2n * angle.numerator * angle.numerator <
    angle.denominator * angle.denominator;
}

function angleLessThanTwoThirds(angle) {
  return 18n * angle.numerator * angle.numerator <
    4n * angle.denominator * angle.denominator;
}

function angleInPrimeZeroInterval(angle) {
  const squareNumerator = angle.numerator * angle.numerator;
  const squareDenominator = angle.denominator * angle.denominator;
  return (
    18n * squareNumerator >= squareDenominator &&
    8n * squareNumerator <= squareDenominator
  );
}

function nextAngle(angle) {
  if (angleLessThanOne(angle)) {
    return {
      angle: reduceAngle({
        numerator: 2n * angle.numerator,
        denominator: angle.denominator,
      }),
      kind: "M",
    };
  }
  return {
    angle: reduceAngle({
      numerator: angle.numerator,
      denominator: 3n * angle.denominator,
    }),
    kind: "D",
  };
}

function previousAngle(angle) {
  if (angleLessThanTwoThirds(angle)) {
    return reduceAngle({
      numerator: 3n * angle.numerator,
      denominator: angle.denominator,
    });
  }
  return reduceAngle({
    numerator: angle.numerator,
    denominator: 2n * angle.denominator,
  });
}

function angleAtRow(row) {
  let angle = { numerator: 1n, denominator: 1n };
  if (row >= 0) {
    for (let index = 0; index < row; index += 1) {
      angle = nextAngle(angle).angle;
    }
  } else {
    for (let index = 0; index > row; index -= 1) {
      angle = previousAngle(angle);
    }
  }
  return angle;
}

function floorAngleMultiple(column, angle) {
  if (column === 0) return 0n;
  const magnitude = BigInt(Math.abs(column)) * angle.numerator;
  const floorPositive =
    integerSquareRoot(2n * magnitude * magnitude) / angle.denominator;
  return column > 0 ? floorPositive : -floorPositive - 1n;
}

function verticalLabel(value, prime) {
  if (value === 0n && prime) return "0'";
  return value.toString();
}

function baseTileAt(column, row) {
  const bottomAngle = angleAtRow(row);
  const { angle: topAngle, kind } = nextAngle(bottomAngle);
  const previous = previousAngle(bottomAngle);
  const bottomLeft = floorAngleMultiple(column - 1, bottomAngle);
  const bottomRight = floorAngleMultiple(column, bottomAngle);
  const topLeft = floorAngleMultiple(column - 1, topAngle);
  const topRight = floorAngleMultiple(column, topAngle);
  const sValue = bottomRight - bottomLeft;
  const nValue = topRight - topLeft;
  let w;
  let e;
  if (kind === "M") {
    w = (2n * bottomLeft - topLeft).toString();
    e = (2n * bottomRight - topRight).toString();
  } else {
    w = `${bottomLeft - 3n * topLeft}/3`;
    e = `${bottomRight - 3n * topRight}/3`;
  }
  const s = verticalLabel(sValue, angleInPrimeZeroInterval(previous));
  const n = verticalLabel(nValue, angleInPrimeZeroInterval(bottomAngle));
  const matches = BASE_TILES.flatMap((tile, index) =>
    tile.s === s &&
    tile.w === w &&
    tile.n === n &&
    tile.e === e &&
    tile.kind === kind
      ? [index]
      : [],
  );
  if (matches.length !== 1) {
    throw new Error(
      `basic construction produced ${JSON.stringify({
        column,
        row,
        s,
        w,
        n,
        e,
        kind,
      })}, matches=${matches.join(",")}`,
    );
  }
  return { base: matches[0], kind };
}

function sheetAtRow(row, modulus) {
  let sheet = 0;
  if (row >= 0) {
    for (let index = 0; index < row; index += 1) {
      if (nextAngle(angleAtRow(index)).kind === "D") sheet += 1;
    }
  } else {
    for (let index = -1; index >= row; index -= 1) {
      if (nextAngle(angleAtRow(index)).kind === "D") sheet -= 1;
    }
  }
  return positiveMod(sheet, modulus);
}

function liftedTileAt(column, row, modulus) {
  const tile = baseTileAt(column, row);
  return tile.base * modulus + sheetAtRow(row, modulus);
}

function auditBasicConstruction(modulus, radius = 12) {
  const alphabet = liftedAlphabet(modulus);
  const seenBaseTiles = new Set();
  const firstOccurrenceByBaseTile = new Map();
  const exactOccurrenceByBaseTile = Object.fromEntries(
    BASE_TILE_OCCURRENCE_COORDINATES.map(([column, row], base) => {
      const actual = baseTileAt(column, row).base;
      if (actual !== base) {
        throw new Error(
          `claimed base tile ${base} occurrence at (${column},${row}) produced ${actual}`,
        );
      }
      return [base, [column, row]];
    }),
  );
  for (let row = -radius; row <= radius; row += 1) {
    for (let column = -radius; column <= radius; column += 1) {
      const id = liftedTileAt(column, row, modulus);
      const tile = alphabet[id];
      seenBaseTiles.add(tile.base);
      const previousOccurrence = firstOccurrenceByBaseTile.get(tile.base);
      const candidateRadius = Math.max(Math.abs(column), Math.abs(row));
      const previousRadius = previousOccurrence
        ? Math.max(
            Math.abs(previousOccurrence[0]),
            Math.abs(previousOccurrence[1]),
          )
        : Number.POSITIVE_INFINITY;
      if (candidateRadius < previousRadius) {
        firstOccurrenceByBaseTile.set(tile.base, [column, row]);
      }
      const east = alphabet[liftedTileAt(column + 1, row, modulus)];
      const north = alphabet[liftedTileAt(column, row + 1, modulus)];
      if (tile.e !== east.w || tile.n !== north.s) {
        throw new Error(`source mismatch at (${column},${row})`);
      }
    }
  }
  return {
    radius,
    checkedTiles: (2 * radius + 1) ** 2,
    seenBaseTileCount: seenBaseTiles.size,
    exactOccurrenceByBaseTile,
    firstOccurrenceByBaseTile: Object.fromEntries(
      [...firstOccurrenceByBaseTile.entries()].sort(
        ([left], [right]) => left - right,
      ),
    ),
  };
}

function enumerate(modulus = 5, phaseModulus = 3, sampleRadius = 12) {
  const alphabet = liftedAlphabet(modulus);
  const adjacent = adjacency(alphabet);
  const blackStates = new Map();
  const whiteStates = new Map();

  // B(i,j) sees faces (i,j), (i-1,j+1), (i-1,j).
  // W(i,j) sees faces (i,j), (i,j+1), (i-1,j+1).
  for (let i = 0; i < phaseModulus; i += 1) {
    for (let j = 0; j < phaseModulus; j += 1) {
      for (const a of alphabet) {
        for (const c of adjacent.west[a.id]) {
          for (const b of adjacent.north[c]) {
            const key = stateKey("B", i, j, [a.id, b, c]);
            blackStates.set(key, {
              id: blackStates.size,
              part: "B",
              phase: [i, j],
              triple: [a.id, b, c],
            });
          }
        }
        for (const d of adjacent.north[a.id]) {
          for (const b of adjacent.west[d]) {
            const key = stateKey("W", i, j, [a.id, d, b]);
            whiteStates.set(key, {
              id: whiteStates.size,
              part: "W",
              phase: [i, j],
              triple: [a.id, d, b],
            });
          }
        }
      }
    }
  }

  let coronaCount = 0;
  const graphEdges = new Set();
  const graphEdgeBands = new Map();
  const graphEdgeVectors = new Map();
  const graphEdgeSquaredLengths = new Map();
  const squaredLengthOwners = new Map();
  const polygonCycles = new Set();
  const unorientedPolygonCycles = new Set();
  const displacementDenominator =
    4096n * BigInt(blackStates.size) * BigInt(whiteStates.size);
  const coordinateCertificate = createHash("sha256");
  coordinateCertificate.update(
    `modulus=${modulus};phase=${phaseModulus};D=${displacementDenominator}\n`,
  );

  function scaledCoordinate(state, vertex) {
    const [baseX, baseY] = BASE_VERTICES_TIMES_TWO[vertex];
    const displacementNumerator =
      state.part === "B"
        ? BigInt(state.id)
        : BigInt(blackStates.size) * BigInt(state.id + 1);
    return [
      baseX * displacementDenominator + 2n * displacementNumerator,
      baseY * displacementDenominator,
    ];
  }

  for (let i = 0; i < phaseModulus; i += 1) {
    for (let j = 0; j < phaseModulus; j += 1) {
      for (const a of alphabet) {
        for (const c of adjacent.west[a.id]) {
          for (const d of adjacent.north[a.id]) {
            const northwest = intersection(
              adjacent.north[c],
              adjacent.west[d],
            );
            if (northwest.length === 0) continue;
            for (const e of adjacent.east[a.id]) {
              for (const g of adjacent.south[a.id]) {
                const southeast = intersection(
                  adjacent.south[e],
                  adjacent.east[g],
                );
                if (southeast.length === 0) continue;
                for (const b of northwest) {
                  for (const f of southeast) {
                    coronaCount += 1;
                    const vertexKeys = [
                      stateKey("B", i, j, [a.id, b, c]),
                      stateKey("W", i, j, [a.id, d, b]),
                      stateKey(
                        "B",
                        positiveMod(i + 1, phaseModulus),
                        j,
                        [e, d, a.id],
                      ),
                      stateKey(
                        "W",
                        positiveMod(i + 1, phaseModulus),
                        positiveMod(j - 1, phaseModulus),
                        [f, e, a.id],
                      ),
                      stateKey(
                        "B",
                        positiveMod(i + 1, phaseModulus),
                        positiveMod(j - 1, phaseModulus),
                        [f, a.id, g],
                      ),
                      stateKey(
                        "W",
                        i,
                        positiveMod(j - 1, phaseModulus),
                        [g, a.id, c],
                      ),
                    ];
                    const stateRecords = vertexKeys.map((key, index) => {
                      const state =
                        index % 2 === 0
                          ? blackStates.get(key)
                          : whiteStates.get(key);
                      if (!state) throw new Error(`missing state ${key}`);
                      return state;
                    });
                    const states = stateRecords.map(
                      (state) => `${state.part}${state.id}`,
                    );
                    if (new Set(states).size !== 6) {
                      throw new Error(`face cycle is not simple: ${states}`);
                    }
                    const coordinates = stateRecords.map((state, vertex) =>
                      scaledCoordinate(state, vertex),
                    );
                    coordinateCertificate.update(
                      `${states.join(",")}:` +
                        coordinates
                          .map(([x, y]) => `${x.toString()},${y.toString()}`)
                          .join(";") +
                        "\n",
                    );
                    for (let k = 0; k < coordinates.length; k += 1) {
                      const previous =
                        coordinates[
                          positiveMod(k - 1, coordinates.length)
                        ];
                      const current = coordinates[k];
                      const next = coordinates[(k + 1) % coordinates.length];
                      const incoming = [
                        current[0] - previous[0],
                        current[1] - previous[1],
                      ];
                      const outgoing = [
                        next[0] - current[0],
                        next[1] - current[1],
                      ];
                      const toPrevious = [-incoming[0], -incoming[1]];
                      if (cross(incoming, outgoing) <= 0n) {
                        throw new Error(`nonconvex cycle ${states}`);
                      }
                      if (dot(toPrevious, outgoing) >= 0n) {
                        throw new Error(`non-obtuse cycle ${states}`);
                      }
                    }
                    for (let k = 0; k < states.length; k += 1) {
                      const u = states[k];
                      const v = states[(k + 1) % states.length];
                      const edge = u < v ? `${u}|${v}` : `${v}|${u}`;
                      const band = k === 1 || k === 4 ? "horizontal" : "slant";
                      const previousBand = graphEdgeBands.get(edge);
                      if (previousBand && previousBand !== band) {
                        throw new Error(
                          `graph edge ${edge} occurs in two length bands`,
                        );
                      }
                      graphEdgeBands.set(edge, band);
                      graphEdges.add(edge);
                      const from = coordinates[k];
                      const to = coordinates[(k + 1) % coordinates.length];
                      const dx = to[0] - from[0];
                      const dy = to[1] - from[1];
                      const blackToWhiteVector =
                        stateRecords[k].part === "B"
                          ? [dx, dy]
                          : [-dx, -dy];
                      const previousVector = graphEdgeVectors.get(edge);
                      if (
                        previousVector !== undefined &&
                        (previousVector[0] !== blackToWhiteVector[0] ||
                          previousVector[1] !== blackToWhiteVector[1])
                      ) {
                        throw new Error(
                          `graph edge ${edge} has inconsistent black-to-white vectors`,
                        );
                      }
                      graphEdgeVectors.set(edge, blackToWhiteVector);
                      const squaredLength = dx * dx + dy * dy;
                      const previousSquaredLength =
                        graphEdgeSquaredLengths.get(edge);
                      if (
                        previousSquaredLength !== undefined &&
                        previousSquaredLength !== squaredLength
                      ) {
                        throw new Error(
                          `graph edge ${edge} has inconsistent geometry`,
                        );
                      }
                      graphEdgeSquaredLengths.set(edge, squaredLength);
                      const previousOwner =
                        squaredLengthOwners.get(squaredLength);
                      if (previousOwner && previousOwner !== edge) {
                        throw new Error(
                          `length collision between ${edge} and ${previousOwner}`,
                        );
                      }
                      squaredLengthOwners.set(squaredLength, edge);
                    }
                    polygonCycles.add(states.join(","));
                    unorientedPolygonCycles.add(
                      canonicalDihedralCycle(states),
                    );
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  const blackCount = blackStates.size;
  const whiteCount = whiteStates.size;
  return {
    modulus,
    phaseModulus,
    alphabetSize: alphabet.length,
    blackCount,
    whiteCount,
    graphEdgeCount: graphEdges.size,
    coronaCount,
    polygonCycleCount: polygonCycles.size,
    congruenceClassCount: unorientedPolygonCycles.size,
    displacementDenominator: displacementDenominator.toString(),
    exactConvexityChecks: coronaCount * 6,
    exactVectorConsistencyChecks: graphEdgeVectors.size,
    exactUniqueLengthChecks: graphEdgeSquaredLengths.size,
    coordinateFingerprintSha256: coordinateCertificate.digest("hex"),
    basicConstructionAudit: auditBasicConstruction(modulus, sampleRadius),
  };
}

const modulus = Number.parseInt(process.argv[2] ?? "5", 10);
const phaseModulus = Number.parseInt(process.argv[3] ?? "3", 10);
const sampleRadius = Number.parseInt(process.argv[4] ?? "12", 10);
console.log(
  JSON.stringify(enumerate(modulus, phaseModulus, sampleRadius), null, 2),
);
