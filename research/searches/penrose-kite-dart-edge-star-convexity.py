#!/usr/bin/env python3
"""Replay necessary convexity filters for one-centre endpoint star survivors.

The endpoint-alignment equations are deliberately omitted: UNSAT for this
larger parameter domain excludes its aligned subset as well. Weak turns
include straight vertices, with at least five genuinely positive turns per
face to avoid a convex triangle/quadrilateral monohedral periodic escape.
SAT is not a construction; UNSAT is computational, not independently proved.
"""
import argparse, fcntl, hashlib, importlib.util, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('edgeconv',HERE/'penrose-kite-dart-convexity.py');conv=importlib.util.module_from_spec(s);s.loader.exec_module(conv)

def main():
    a=argparse.ArgumentParser();a.add_argument('--checkpoint',required=True);a.add_argument('--output',required=True)
    a.add_argument('--timeout-ms',type=int,default=15000);a.add_argument('--min-corners',type=int,default=5);args=a.parse_args();out=Path(args.output)
    lock=out.with_suffix(out.suffix+'.lock').open('a+')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:raise SystemExit('Endpoint convexity checkpoint already running')
    raw=Path(args.checkpoint).read_bytes();h=hashlib.sha256(raw).hexdigest()
    rows=[json.loads(l) for l in raw.splitlines()];results=json.loads(out.read_text()) if out.exists() else []
    assert all(r['source_sha256']==h and r['minimum_genuine_corners']==args.min_corners for r in results)
    done={(r['kite'],r['dart'],r['weak_turns']) for r in results}
    for row in rows:
        if row['dead'] is not None or not row['interior_faces']:continue
        assert row['active_orbits']==[0],'Activation must be part of resume key if extended'
        row['kite'],row['dart']=row['kite_mask'],row['dart_mask']
        for weak in (False,True):
            if (row['kite'],row['dart'],weak) in done:continue
            result,smt=conv.check(row,weak,args.timeout_ms,True,args.min_corners)
            result.update(edge_alignment_omitted=True,active_orbits=row['active_orbits'],source_sha256=h)
            results.append(result);conv.met.lin.p2.atomic_json(out,results)
            Path(str(out)+f'.{row["kite"]}-{row["dart"]}-'+('weak' if weak else 'strict')+'.smt2').write_text(smt+'\n(check-sat)\n')
            print(json.dumps(result),flush=True)
if __name__=='__main__':main()
