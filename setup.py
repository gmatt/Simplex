from pathlib import Path
import setuptools

setuptools.setup(
    name="Simplex",
    install_requires=Path("requirements.txt").read_text().splitlines(),
    package_dir={
        "Simplex.explaiers": "explainers",
        "Simplex.models": "models",
        "Simplex.utils": "utils",
        "explaiers": "explainers",
        "models": "models",
        "utils": "utils",
    },
    packages=[
        "Simplex.explaiers",
        "Simplex.models",
        "Simplex.utils",
        "explaiers",
        "models",
        "utils",
    ],
)
