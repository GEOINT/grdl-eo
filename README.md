# GRDL-EO

`geoint.org` managed component catalog for Electro-Optical (EO), Multispectral (MSI), Hyperspectral (HSI), and Infrared (IR) image processors built on the [`grdl`](../grdl/) framework.

## Included Components
- **Fusion (`grdl_eo.fusion`)**: `BroveyPanSharpenTransform`, `SimpleMeanFusionTransform`
- **Spectral (`grdl_eo.spectral`)**: `SpectralIndexTransform` (NDVI, NDWI, NDBI, SAVI, RATIO)
- **Edge & Sharpening Filters (`grdl_eo.filters`)**: `SobelFilter`, `LaplacianFilter`, `UnsharpMaskFilter`, `HighPassFilter`

## Catalog Auto-Discovery
`grdl-eo` exports a `catalog.yaml` generated from `@processor_version` and `@processor_tags` decorators and registers `[project.entry-points."grdl.catalogs"]` for automatic federation into `grdl-runtime`.

