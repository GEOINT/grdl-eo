# -*- coding: utf-8 -*-
"""
Unit tests for grdl-eo processors:
- Edge & sharpening filters: SobelFilter, LaplacianFilter, UnsharpMaskFilter, HighPassFilter
- Fusion: BroveyPanSharpenTransform, SimpleMeanFusionTransform
- Spectral: SpectralIndexTransform, compute_spectral_index
"""

import numpy as np
import pytest

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


class TestEdgeFilters:
    def test_sobel_gradient_components(self):
        arr = np.random.rand(20, 20).astype(np.float32)
        f_mag = SobelFilter(output_type="magnitude")
        out_mag = f_mag.apply(arr)
        assert out_mag.shape == arr.shape

        f_gx = SobelFilter(output_type="gradient_x")
        out_gx = f_gx.apply(arr)
        assert out_gx.shape == arr.shape

        f_gy = SobelFilter(output_type="gradient_y")
        out_gy = f_gy.apply(arr)
        assert out_gy.shape == arr.shape

    def test_laplacian_filter(self):
        arr = np.random.rand(20, 20).astype(np.float32)
        f = LaplacianFilter(mode="reflect")
        out = f.apply(arr)
        assert out.shape == arr.shape

    def test_unsharp_mask(self):
        arr = np.random.rand(20, 20).astype(np.float32)
        f = UnsharpMaskFilter(radius=1.0, amount=2.0)
        out = f.apply(arr)
        assert out.shape == arr.shape

    def test_high_pass_filter(self):
        arr = np.random.rand(20, 20).astype(np.float32)
        f = HighPassFilter(cutoff=2.0)
        out = f.apply(arr)
        assert out.shape == arr.shape


class TestFusionTransforms:
    def test_brovey_fusion(self):
        pan = np.ones((16, 16), dtype=np.float32) * 4.0
        ms = np.ones((4, 16, 16), dtype=np.float32) * 2.0
        f = BroveyPanSharpenTransform(pan_weight=1.0)
        out = f.apply(ms, pan=pan)
        assert out.shape == (4, 16, 16)
        assert np.allclose(out, 4.0, atol=1e-3)

    def test_simple_mean_fusion(self):
        pan = np.ones((16, 16), dtype=np.float32) * 6.0
        ms = np.ones((4, 16, 16), dtype=np.float32) * 2.0
        f = SimpleMeanFusionTransform(pan_weight=0.5)
        out = f.apply(ms, pan=pan)
        assert out.shape == (4, 16, 16)
        assert np.allclose(out, 4.0, atol=1e-3)


class TestSpectralTransforms:
    def test_spectral_indices(self):
        cube = np.zeros((6, 20, 20), dtype=np.float32)
        cube[2] = 0.2  # Red
        cube[3] = 0.8  # NIR
        cube[1] = 0.5  # Green
        cube[5] = 0.1  # SWIR

        ndvi = compute_spectral_index(cube, index_type="NDVI", nir_idx=3, red_idx=2)
        assert np.allclose(ndvi, 0.6, atol=1e-3)

        ndwi = compute_spectral_index(cube, index_type="NDWI", green_idx=1, nir_idx=3)
        assert np.allclose(ndwi, -0.3 / 1.3, atol=1e-3)

        t = SpectralIndexTransform(index_type="NDVI", nir_idx=3, red_idx=2)
        out_t = t.apply(cube)
        assert np.allclose(out_t, 0.6, atol=1e-3)


def test_catalog_export_and_discovery(tmp_path):
    from grdl.discovery.catalog_builder import export_catalog_yaml
    import grdl_eo

    out = export_catalog_yaml("grdl_eo", tmp_path / "catalog.yaml")
    assert out.exists()
    assert grdl_eo.get_catalog_path().exists()

