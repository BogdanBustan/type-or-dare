from typing import NewType, Literal, Annotated, overload
import numpy as np
from numpy.typing import NDArray

# Define our image types
BWNumpyImage = NewType(
    'BWNumpyImage',
    Annotated[NDArray, "Single channel grayscale image, shape: (H, W)"]
)

ColorNumpyImage = NewType(
    'ColorNumpyImage',
    Annotated[NDArray, "RGB image with 3 channels, shape: (H, W, 3)"]
)

ImageMode = Literal["bw", "color"]


# Overloads to help IDE understand return types
@overload
def load_image(mode: Literal["bw"]) -> BWNumpyImage: ...


@overload
def load_image(mode: Literal["color"]) -> ColorNumpyImage: ...


# Actual implementation
def load_image(mode: ImageMode) -> BWNumpyImage | ColorNumpyImage:
    # Simulate loading an image
    if mode == "bw":
        array = np.zeros((100, 100))
        return BWNumpyImage(array)
    else:
        array = np.zeros((100, 100, 3))
        return ColorNumpyImage(array)


# Usage
bw_img = load_image("bw")  # IDE knows this is BWNumpyImage
color_img = load_image("color")  # IDE knows this is ColorNumpyImage


# Type checking examples
def process_bw(img: BWNumpyImage) -> None:
    print(f"Processing BW image of shape {img.shape}")


def process_color(img: ColorNumpyImage) -> None:
    print(f"Processing color image of shape {img.shape}")


# These will work with proper type checking
process_bw(bw_img)
process_color(color_img)

# # These would raise type errors
# process_bw(color_img)    # Type error!
# process_color(bw_img)    # Type error!