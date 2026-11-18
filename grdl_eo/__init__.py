# -*- coding: utf-8 -*-
"""
GRDL-EO — geoint.org EO, MSI, HSI & Thermal/IR Component Catalog.

Provides modality-specific electro-optical, multispectral, hyperspectral,
and infrared image processing components built on the ``grdl`` framework,
along with an auto-discovered ``catalog.yaml`` for ``grdl-runtime``.

License
-------
MIT License
Copyright (c) 2024 geoint.org
See LICENSE file for full text.
"""

from pathlib import Path

from grdl_eo.filters import (
    HighPassFilter,
    LaplacianFilter,
    SobelFilter,
    UnsharpMaskFilter,
)
from grdl_eo.fusion import (
    BroveyPanSharpenTransform,
    SimpleMeanFusionTransform,
    brovey_pan_sharpen,
    simple_mean_fusion,
)
from grdl_eo.spectral import (
    SpectralIndexTransform,
    compute_spectral_index,
)

__version__ = "0.1.0"


def get_catalog_path() -> Path:
    """Return the path to the bundled ``grdl-eo`` ``catalog.yaml`` artifact."""
    return Path(__file__).resolve().parent / "catalog.yaml"


__all__ = [
    "__version__",
    "get_catalog_path",
    "BroveyPanSharpenTransform",
    "SimpleMeanFusionTransform",
    "brovey_pan_sharpen",
    "simple_mean_fusion",
    "SpectralIndexTransform",
    "compute_spectral_index",
    "SobelFilter",
    "LaplacianFilter",
    "UnsharpMaskFilter",
    "HighPassFilter",
]

