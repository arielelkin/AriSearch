"""Exact cheap witness for the explicitly relaxed pairwise affine gate.
No claim that the formal independent-side states are geometric coronas.
"""
from fractions import Fraction


def main():
    # Conservativity + seam-reflection equivariance: f = -f.
    # Exact elimination over Q: 2*f=0, so f=0, independently of lengths.
    involution_coefficient = Fraction(1) + Fraction(1)
    forced_flux = Fraction(0) / involution_coefficient
    for species, sides in (("P", 5), ("Q", 7)):
        fluxes = [forced_flux] * sides
        net = sum(fluxes, Fraction(0))
        required_surplus = Fraction(1)
        assert net == 0
        assert net < required_surplus
        print(f"{species}: {sides} admissible self-reflected pairwise sides; "
              f"net={net}; required={required_surplus}; relaxation infeasible")
    print("Scope: pairwise product domain only; no plane-tiling conclusion")


if __name__ == "__main__":
    main()
