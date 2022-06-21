from setuptools import setup

setup(
    name="swinir",
    py_modules=["swinir"],
    install_requires=["timm", "numpy", "torch", "opencv-python-headless", "pillow"],
)
