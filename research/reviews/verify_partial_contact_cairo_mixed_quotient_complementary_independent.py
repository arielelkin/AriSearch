"""Replay the independent native checker on the complementary actual gluing."""
import runpy
import sys
from pathlib import Path
sys.argv.append('--complementary')
runpy.run_path(str(Path(__file__).with_name('verify_partial_contact_cairo_mixed_quotient_independent.py')),run_name='__main__')
