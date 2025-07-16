TITLE: Install qrcode Python Library
DESCRIPTION: Instructions for installing the qrcode library using pip, including an option for Pillow support for extended image functionality.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_0

LANGUAGE: bash
CODE:
```
pip install qrcode
```

LANGUAGE: bash
CODE:
```
pip install "qrcode[pil]"
```

----------------------------------------

TITLE: Generate Basic QR Code in Python
DESCRIPTION: Demonstrates the simplest way to create a QR code image using the `qrcode.make` shortcut function, saving it as a PNG file.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_2

LANGUAGE: python
CODE:
```
import qrcode
img = qrcode.make('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
```

----------------------------------------

TITLE: Generate Styled QR Code with Customization in Python
DESCRIPTION: Illustrates how to create a styled QR code using `StyledPilImage` in Python, demonstrating the application of custom module drawers (rounded corners), color masks (radial gradient), and embedding an image within the QR code. This functionality requires `qrcode` versions 7.2 or higher.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_11

LANGUAGE: python
CODE:
```
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('Some data')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embedded_image_path="/path/to/image.png")
```

----------------------------------------

TITLE: Generate QR Code with Advanced Options in Python
DESCRIPTION: Illustrates how to use the `qrcode.QRCode` class for fine-grained control over QR code generation, including version, error correction, box size, border, and custom colors.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_3

LANGUAGE: python
CODE:
```
import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
```

----------------------------------------

TITLE: Generate Basic QR Code Images (PNG)
DESCRIPTION: Demonstrates fundamental methods for generating QR code images, including command-line usage to output a PNG file and Python code to create a PNG image using a pure image factory.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_10

LANGUAGE: shell
CODE:
```
qr --factory=png "Some text" > test.png
```

LANGUAGE: python
CODE:
```
import qrcode
from qrcode.image.pure import PyPNGImage
img = qrcode.make('Some data here', image_factory=PyPNGImage)
```

----------------------------------------

TITLE: Generate QR Code from Command Line
DESCRIPTION: How to generate a QR code image directly from the command line using the installed `qr` script, redirecting output to a PNG file.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_1

LANGUAGE: bash
CODE:
```
qr "Some text" > test.png
```

----------------------------------------

TITLE: Customize QR Code Colors in Python
DESCRIPTION: Example of setting custom fill and background colors for a QR code image using RGB tuples with the `make_image` method.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_4

LANGUAGE: python
CODE:
```
img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
```

----------------------------------------

TITLE: QR Code Error Correction Levels
DESCRIPTION: Details the available error correction levels for QR codes, explaining the percentage of errors that can be corrected for each level.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_5

LANGUAGE: APIDOC
CODE:
```
ERROR_CORRECT_L:
    About 7% or less errors can be corrected.
ERROR_CORRECT_M (default):
    About 15% or less errors can be corrected.
ERROR_CORRECT_Q:
    About 25% or less errors can be corrected.
ERROR_CORRECT_H:
    About 30% or less errors can be corrected.
```

----------------------------------------

TITLE: Save QR Code Output to File from Command Line
DESCRIPTION: Provides various command-line methods for saving QR code output to files, including piping ASCII output to a text file and using the `--output` flag for image files, which offers a robust alternative to shell redirection, especially in environments like PowerShell.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_13

LANGUAGE: shell
CODE:
```
qr --ascii "Some data" > "test.txt"
cat test.txt
```

LANGUAGE: shell
CODE:
```
# qr "Some data" > test.png
qr --output=test.png "Some data"
```

----------------------------------------

TITLE: Generate SVG QR Code from Command Line
DESCRIPTION: How to generate QR codes in various SVG formats (path, simple rects, fragment) directly from the command line using the `qr` script.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_6

LANGUAGE: bash
CODE:
```
qr --factory=svg-path "Some text" > test.svg
```

LANGUAGE: bash
CODE:
```
qr --factory=svg "Some text" > test.svg
```

LANGUAGE: bash
CODE:
```
qr --factory=svg-fragment "Some text" > test.svg
```

----------------------------------------

TITLE: Manage QR Code Data and Retrieve ASCII Output in Python
DESCRIPTION: Covers advanced usage of the `qrcode` library in Python, including how to capture the ASCII representation of a QR code into a string using `io.StringIO` and how to clear and update data within an existing `QRCode` object for reuse.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_12

LANGUAGE: python
CODE:
```
import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("Some text")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
```

LANGUAGE: python
CODE:
```
import qrcode
qr = qrcode.QRCode()
qr.add_data('Some data')
img = qr.make_image()
qr.clear()
qr.add_data('New data')
other_img = qr.make_image()
```

----------------------------------------

TITLE: Convert SVG QR Code Image to String in Python
DESCRIPTION: Example of converting a generated SVG QR code image object into a string representation using the `to_string()` method, specifying the encoding.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_9

LANGUAGE: python
CODE:
```
img.to_string(encoding='unicode')
```

----------------------------------------

TITLE: Generate SVG QR Code with Different Factories in Python
DESCRIPTION: Demonstrates how to generate QR codes as SVG images in Python by specifying different `image_factory` options, including basic rectangles, fragments, and combined paths.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_7

LANGUAGE: python
CODE:
```
import qrcode
import qrcode.image.svg

if method == 'basic':
    # Simple factory, just a set of rects.
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (also just a set of rects)
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory, fixes white space that may occur when zooming
    factory = qrcode.image.svg.SvgPathImage

img = qrcode.make('Some data here', image_factory=factory)
```

----------------------------------------

TITLE: Add Custom Attributes to SVG QR Code in Python
DESCRIPTION: Shows how to pass additional keyword arguments to the underlying ElementTree XML library via `make_image` to fine-tune the root element of the resulting SVG, such as adding CSS classes.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/README.rst#_snippet_8

LANGUAGE: python
CODE:
```
import qrcode
qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(attrib={'class': 'some-css-class'})
```

----------------------------------------

TITLE: Install Image Library Build Dependencies on macOS
DESCRIPTION: This Homebrew command installs common image processing libraries (libjpeg, libtiff, little-cms2, openjpeg, webp) on macOS. These libraries are typically needed to compile Python Imaging Library (PIL) or Pillow, which is a dependency for image manipulation in the project.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/TESTING.rst#_snippet_2

LANGUAGE: Shell
CODE:
```
brew install libjpeg libtiff little-cms2 openjpeg webp
```

----------------------------------------

TITLE: Install Image Library Build Dependencies on Ubuntu
DESCRIPTION: These commands install essential build tools and image processing library development files (libjpeg, zlib) on Ubuntu. These are often required to build Python Imaging Library (PIL) or Pillow from source, which may be necessary if pre-built wheels are not available for your system.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/TESTING.rst#_snippet_1

LANGUAGE: Shell
CODE:
```
sudo apt-get install build-essential python-dev python3-dev
sudo apt-get install libjpeg8-dev zlib1g-dev
```

----------------------------------------

TITLE: Run Project Test Suite with Tox
DESCRIPTION: This section provides commands to execute the project's test suite using Tox, a tool for automating testing in multiple Python environments. You can run Tox directly via Poetry or by entering a Poetry shell first. It also notes how to test against a specific Python version and environment.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/TESTING.rst#_snippet_3

LANGUAGE: Shell
CODE:
```
poetry run tox
# or
poetry shell
tox
```

----------------------------------------

TITLE: Run Code Formatting Check with Ruff
DESCRIPTION: This command uses Ruff to check and enforce code formatting standards for the `qrcode` directory. Running this ensures that the codebase adheres to predefined style guidelines, improving readability and consistency.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/TESTING.rst#_snippet_4

LANGUAGE: Shell
CODE:
```
ruff format qrcode
```

----------------------------------------

TITLE: Install Python Project Development Dependencies
DESCRIPTION: This command installs all development dependencies for the `python-qrcode` project using Poetry. It ensures that all necessary packages for testing and development are available in the project's virtual environment.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/TESTING.rst#_snippet_0

LANGUAGE: Shell
CODE:
```
poetry install --with dev
```

----------------------------------------

TITLE: Install Project Dependencies with Poetry
DESCRIPTION: Ensures all necessary maintainer dependencies for the project are installed using Poetry's `install` command.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/PACKAGING.rst#_snippet_0

LANGUAGE: bash
CODE:
```
poetry install
```

----------------------------------------

TITLE: Execute Project Release Process with Poetry
DESCRIPTION: Initiates the full release process for the project by running the `fullrelease` command via Poetry, prompting for user input as needed.
SOURCE: https://github.com/lincolnloop/python-qrcode/blob/main/PACKAGING.rst#_snippet_1

LANGUAGE: bash
CODE:
```
poetry run fullrelease
```
