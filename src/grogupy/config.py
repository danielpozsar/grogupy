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

import warnings
from os import environ
from typing import Literal


class Config:
    """Configuration class of grogupy.

    Contains the environment variables.

    Parameters
    ----------
    architecture: str
        The architecture read from os.environ
    tqdm: str
        tqdm request read from os.environ

    Attributes
    ----------
    viz_loaded: bool
        Returns wether visualization packages are loaded or not
    MPI_loaded: bool
        Returns wether MPI packages are loaded or not
    architecture: Literal["CPU", "GPU"]
        Returns the architecture
    parallel_size: int
        Returns the parallel size over CPU or GPU
    is_CPU: bool
        Returns wether CPU is the architecture or not
    is_GPU: bool
        Returns wether GPU is the architecture or not
    tqdm_requested: bool
        Returns wether tqdm was requested or not
    """

    def __init__(self, architecture: str, tqdm: str):
        """Initializing configuration class."""
        self.__viz_loaded: bool = False
        self.__MPI_loaded: bool = False

        # get architecture
        if architecture.lower() == "CPU":
            self.__architecture: Literal["CPU", "GPU"] = "CPU"
        elif architecture.lower() == "GPU":
            self.__architecture: Literal["CPU", "GPU"] = "GPU"
        else:
            raise Exception("Unknown architecture, use CPU or GPU!")

        if self.__architecture == "CPU":
            try:
                from mpi4py import MPI

                self.__MPI_loaded: bool = True
                self.__parallel_size: int = MPI.COMM_WORLD.Get_size()
            except:
                warnings.warn(
                    """MPI could not be loaded in CPU architecture! 
                              Parallelization will not be possible!"""
                )
                self.__parallel_size: int = 1

        elif self.__architecture == "GPU":
            import cupy as cp

            self.__parallel_size: int = cp.cuda.runtime.getDeviceCount()

        # get tqdm
        if tqdm.lower() == "true":
            self.__tqdm_requested: bool = True
        else:
            self.__tqdm_requested: bool = False

    @property
    def viz_loaded(self) -> bool:
        """Returns wether visualization packages are loaded or not"""
        return self.__viz_loaded

    @property
    def MPI_loaded(self) -> bool:
        """Returns wether MPI packages are loaded or not"""
        return self.__MPI_loaded

    @property
    def architecture(self) -> Literal["CPU", "GPU"]:
        """Returns the architecture"""
        return self.__architecture

    @property
    def parallel_size(self) -> int:
        """Returns the parallel size over CPU or GPU"""
        return self.__parallel_size

    @property
    def is_CPU(self) -> bool:
        """Returns wether CPU is the architecture or not"""
        return self.__architecture == "CPU"

    @property
    def is_GPU(self) -> bool:
        """Returns wether GPU is the architecture or not"""
        return self.__architecture == "GPU"

    @property
    def tqdm_requested(self) -> bool:
        """Returns wether tqdm was requested or not"""
        return self.__tqdm_requested


CONFIG = Config(
    environ.get("GROGUPY_ARCHITECTURE", "CPU"), environ.get("GROGUPY_TQDM", "TRUE")
)

if __name__ == "__main__":
    pass
