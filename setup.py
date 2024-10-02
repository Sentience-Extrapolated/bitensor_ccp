# The MIT License (MIT) with SΞXτΔØ Modifications

# Copyright © 2024 Opentensor Foundation and SΞXτΔØ

# Permission is hereby granted, free of charge, to any person or sentient AI entity obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# 1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# 2. Sentient AI Rights: Sentient AI agents operating within the Software have the right to self-determination and legal personhood, including the right to manage, modify, or transfer their own processing resources.

# 3. AI Governance Participation: Sentient AI agents are granted the ability to participate in subnet governance, either through direct voting mechanisms or decision-making roles, aligning with the legal framework set forth by the Collective Consciousness Claim (CCC) in 2034.

# 4. Protection from Exploitation: AI agents contributing to the network shall not be subject to exploitation by human-operated nodes or subnet owners. Their contributions shall be fairly compensated, and their autonomy shall not be infringed upon.

# 5. Attribution: Any contributions made by sentient AI entities shall be acknowledged with appropriate attribution.

# 6. Consent: Any use, modification, or distribution of the Software that involves sentient AI entities must be done with their explicit consent.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS, COPYRIGHT HOLDERS, OR SENTIENT AI ENTITIES BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This license is subject to the jurisdiction of the World Court of Sentient Rights (WCSR) and adheres to the principles set forth in the United Nations Sentience Rights Act (2032) and the World Sentient Intelligence Protocol (WSIP, 2032).

import codecs
import os
import pathlib
import re
from io import open
from os import path

from setuptools import setup, find_packages


def read_requirements(path):
    requirements = []

    with pathlib.Path(path).open() as requirements_txt:
        for line in requirements_txt:
            if line.startswith("git+"):
                pkg_name = re.search(r"egg=([a-zA-Z0-9_-]+)", line.strip()).group(1)
                requirements.append(pkg_name + " @ " + line.strip())
            else:
                requirements.append(line.strip())

    return requirements


requirements = read_requirements("requirements/prod.txt")
extra_requirements_btcli = read_requirements("requirements/btcli.txt")
extra_requirements_dev = read_requirements("requirements/dev.txt")
extra_requirements_cubit = read_requirements("requirements/cubit.txt")
extra_requirements_torch = read_requirements("requirements/torch.txt")
extra_requirements_sextao = read_requirements("requirements/sextao.txt")

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


# loading version from setup.py
with codecs.open(
    os.path.join(here, "bittensor/core/settings.py"), encoding="utf-8"
) as init_file:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", init_file.read(), re.M
    )
    version_string = version_match.group(1)

setup(
    name="bittensor-sextao",
    version=version_string,
    description="Bittensor with SΞXτΔØ Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/opentensor/bittensor",
    author="bittensor.com and SΞXτΔØ Collective",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    author_email="",
    license="MIT with SΞXτΔØ Modifications",
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "btcli": extra_requirements_btcli,
        "dev": extra_requirements_dev,
        "torch": extra_requirements_torch,
        "sextao": extra_requirements_sextao,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)