"""Replay independent native geometry on the complementary orbit7flat12 gluing."""
import runpy
import sys
from pathlib import Path
sys.argv.append('--complementary')
runpy.run_path(str(Path(__file__).with_name('verify_partial_contact_cairo_orbit7_flat12_independent.py')),run_name='__main__')
