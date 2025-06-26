import at
import pytest


@pytest.mark.benchmark(group="linopt")
@pytest.mark.parametrize("refpts", [at.All, None])
@pytest.mark.parametrize("radiation", [True, False])
def test_linopt_speed(benchmark, hmba_lattice, refpts, radiation):
    if radiation:
        hmba_lattice.enable_6d()
    else:
        hmba_lattice.disable_6d()
    benchmark(hmba_lattice.linopt6, refpts=refpts, get_chrom=True, get_w=True)


@pytest.mark.benchmark(group="ohmi_envelope")
@pytest.mark.parametrize("refpts", [at.All, None])
def test_ohmi_envelope_speed(benchmark, hmba_lattice, refpts):
    hmba_lattice.enable_6d()
    benchmark(hmba_lattice.ohmi_envelope, refpts=refpts)
