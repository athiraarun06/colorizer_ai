import streamlit as st
from PIL import Image
import cv2
import os

from colorizer import ImageColorizer
from enhancement import enhance_image, sharpen_image


st.set_page_config(
    page_title="colorizer_Ai",
    page_icon="",
    layout="wide"
)


def save_output(image):

    output_dir = "outputs"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(
        output_dir,
        "colorized_output.jpg"
    )

    image_bgr = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )

    cv2.imwrite(output_path, image_bgr)

    return output_path


def convert_image_to_bytes(image):

    from io import BytesIO

    image_pil = Image.fromarray(image)

    buffer = BytesIO()

    image_pil.save(buffer, format="PNG")

    return buffer.getvalue()


st.title("🎨 colorizer_Ai")

st.write(
    "AI-powered historical image colorization system."
)

st.sidebar.title("Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload black and white image",
    type=["jpg", "jpeg", "png"]
)

enable_enhancement = st.sidebar.checkbox(
    "Enable image enhancement"
)

brightness = 0
contrast = 1.0
enable_sharpen = False

if enable_enhancement:

    brightness = st.sidebar.slider(
        "Brightness",
        -50,
        50,
        10
    )

    contrast = st.sidebar.slider(
        "Contrast",
        0.5,
        2.0,
        1.2
    )

    enable_sharpen = st.sidebar.checkbox(
        "Sharpen image"
    )


if uploaded_file is not None:

    original_image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.image(
        original_image,
        use_container_width=True
    )

    if st.button("Colorize Image"):

        try:

            with st.spinner(
                "AI is colorizing image..."
            ):

                colorizer = ImageColorizer()

                colorized_image = colorizer.colorize(
                    original_image
                )

                if enable_enhancement:

                    colorized_image = enhance_image(
                        colorized_image,
                        brightness=brightness,
                        contrast=contrast
                    )

                    if enable_sharpen:

                        colorized_image = sharpen_image(
                            colorized_image
                        )

                save_output(colorized_image)

            st.success(
                "Image colorized successfully!"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "Original Image"
                )

                st.image(
                    original_image,
                    use_container_width=True
                )

            with col2:

                st.subheader(
                    "Colorized Image"
                )

                st.image(
                    colorized_image,
                    use_container_width=True
                )

            st.download_button(
                label="Download Image",
                data=convert_image_to_bytes(
                    colorized_image
                ),
                file_name="colorized_image.png",
                mime="image/png"
            )

        except Exception as e:

            st.error("Something went wrong")

            st.exception(e)

else:

    st.warning(
        "Upload a black and white image"
    )