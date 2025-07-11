# Copyright (c) [2024-2025] [Grogupy Team]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from numpy.testing import assert_allclose

from grogupy._core.utilities import *

pytestmark = [pytest.mark.core]


class TestCore:
    def test_commutator(self):
        A = np.random.random((10, 10))
        B = np.random.random((10, 10))

        assert not np.allclose(commutator(A, B), np.zeros_like(A))
        assert np.allclose(commutator(A, A), np.zeros_like(A))

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_tau_u(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_crossM(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_RotM(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_RotMa2b(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_setup_from_range(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_arrays_lists_equal(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_arrays_None_equal(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_onsite_projection(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_calc_Vu(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_build_hh_ss(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_make_contour(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_make_kset(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_hsk(self):
        raise NotImplementedError

    @pytest.mark.xfail(raises=NotImplementedError)
    def test_process_ref_directions(self):
        raise NotImplementedError


if __name__ == "__main__":
    pass
