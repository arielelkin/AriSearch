"""Replay the independent checker on this complementary native gluing."""
import runpy
import sys
from pathlib import Path
sys.argv.append('--complementary')
runpy.run_path(str(Path(__file__).with_name('verify_partial_contact_cairo_orbit0_flat23_independent.py')),run_name='__main__')
