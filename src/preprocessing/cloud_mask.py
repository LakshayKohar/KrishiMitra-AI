import ee

def mask_clouds(image):
    """
    Mask clouds and cloud shadows using the Sentinel-2 Scene Classification Layer (SCL).
    """

    scl = image.select("SCL")

    # Keep only useful classes
    mask = (
        scl.neq(3)   # Cloud Shadow
        .And(scl.neq(8))   # Cloud Medium Probability
        .And(scl.neq(9))   # Cloud High Probability
        .And(scl.neq(10))  # Thin Cirrus
    )

    return image.updateMask(mask)