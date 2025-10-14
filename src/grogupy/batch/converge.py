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

from typing import Union

from numpy.typing import NDArray


def generate_convergence(
    path: str,
    mode: str,
    values: Union[list[int], list[list[int]], NDArray],
    output: Union[None, str] = None,
):
    """Generate a list of files for convergence calculations.

    Parameters
    ----------
    path : str
        The input path to the .py or .fdf file
    mode : str
        The convergence parameter, which can be "eset",
        "esetp" or "eset"
    values : Union[list[int], list[list[int]], NDArray]
        The values that will be in the new input files
    output : Union[None, str], optional
        The output path for the placement of the generated files,
        if None, then the input path will be used, by default None

    Raises
    ------
    Exception
        Unknown convergence parameter!
    Exception
        Unknown file format!
    """

    # if mode is unknown raise exception
    if mode not in {"eset", "esetp", "kset"}:
        raise Exception("Unknown convergence parameter: {mode}!")

    # if output path is not given, then use input path
    if output is None:
        output = "/".join(path.split("/")[:-1])

    # get the input file format
    file_format = path.split(".")[-1]
    if file_format not in {"py", "fdf"}:
        raise Exception(f"Unknown file format: .{file_format}!")

    # open example file and read its lines
    with open(path, "r") as file:
        lines = file.readlines()

    # find the row to replace
    replace_line = None
    for i, l in enumerate(lines):
        l = l[: l.find("#")]
        if file_format == "py":
            l = l.split("=")[0].strip()
        else:
            l = l.split(" ")[0].strip().lower()

        if mode == "eset" and l == "eset":
            replace_line = i
            break
        if mode == "esetp" and l == "esetp":
            replace_line = i
            break
        if mode == "kset" and l == "kset":
            replace_line = i
            break

    # if a line was found with the given value, then take its comment
    comment = ""
    if replace_line is not None:
        comment = lines[replace_line][lines[replace_line].find("#") :]

    # write output files
    if file_format == "fdf":
        mode = mode.capitalize()
    prepend = f"\n# Convergence based on: {path}\n"
    for v in values:
        # preprocess value
        if file_format == "fdf" and mode == "Kset":
            v = str(v).replace(",", "").replace("[", "").replace("]", "")
            name = v.replace(" ", "_")
        elif file_format == "py" and mode == "kset":
            v = str(v)
            name = (
                str(v)
                .replace(",", "")
                .replace("[", "")
                .replace("]", "")
                .replace(" ", "_")
            )
        else:
            v = str(v)
            name = v

        # write to file
        with open(output + f"/grogupy_{mode}_convergence_{name}.py", "w") as file:
            # if replace not found, then append
            if replace_line is None:
                lines.append(
                    "\n\n"
                    + prepend
                    + mode
                    + " = "
                    + v
                    + "\t\t # convergence set automatically #"
                    + comment
                    + "\n"
                )
            # else replace the line
            else:
                lines[replace_line] = (
                    prepend
                    + mode
                    + " = "
                    + v
                    + "\t\t # convergence set automatically #"
                    + comment
                    + "\n"
                )

            file.writelines(lines)
