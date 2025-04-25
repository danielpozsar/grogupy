# Copyright (c) [2024-2025] [Laszlo Oroszlany, Daniel Pozsar]
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
import os
import subprocess

import pytest

pytestmark = [pytest.mark.cli]


class TestCommandLineTools:
    @pytest.mark.parametrize(
        "path",
        [
            "input0.py",
            "input1.py",
            "input2.py",
            "input3.py",
            "input4.py",
        ],
    )
    def test_run(self, path):
        subprocess.run(["grogupy_run", path])

        assert os.path.isfile("test.magnopy.txt")
        os.remove("test.magnopy.txt")
        assert os.path.isfile("test.pkl")
        os.remove("test.pkl")
        assert os.path.isdir("test_UppASD_output")
        assert os.path.isfile("./test_UppASD_output/jfile")
        assert os.path.isfile("./test_UppASD_output/momfile")
        assert os.path.isfile("./test_UppASD_output/posfile")
        assert os.path.isfile("./test_UppASD_output/cell.tmp.txt")
        os.remove("./test_UppASD_output/jfile")
        os.remove("./test_UppASD_output/momfile")
        os.remove("./test_UppASD_output/posfile")
        os.remove("./test_UppASD_output/cell.tmp.txt")
        os.rmdir("./test_UppASD_output")

    def test_analyze(self):
        subprocess.run(["grogupy_run", "input5.py"])
        subprocess.run(["grogupy_analyze", "test.pkl"])

        assert os.path.isfile("test.analysis.txt")
        os.remove("test.analysis.txt")
        assert os.path.isfile("test.contour.html")
        os.remove("test.contour.html")
        assert os.path.isfile("test.DMIs.html")
        os.remove("test.DMIs.html")
        assert os.path.isfile("test.kspace.html")
        os.remove("test.kspace.html")
        assert os.path.isfile("test.magnetic_entities.html")
        os.remove("test.magnetic_entities.html")
        assert os.path.isfile("test.pairs.html")
        os.remove("test.pairs.html")

        os.remove("test.pkl")


if __name__ == "__main__":
    pass
