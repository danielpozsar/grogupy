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

from grogupy._core.constants import *

pytestmark = [pytest.mark.core]


class TestConstants:
    def test_pauli_matrixes(self):
        assert np.allclose(TAU_0, np.array([[1, 0], [0, 1]]))
        assert np.allclose(TAU_X, np.array([[0, 1], [1, 0]]))
        assert np.allclose(TAU_Y, np.array([[0, -1j], [1j, 0]]))
        assert np.allclose(TAU_Z, np.array([[1, 0], [0, -1]]))


if __name__ == "__main__":
    pass
