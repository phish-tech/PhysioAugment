from setuptools import setup, find_packages
import os

# 读取 README.md 作为长描述，展示在 PyPI 或 GitHub 上
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PhysioAugment",
    version="0.1.0",
    author="Boyuan Gu",
    author_email="your.email@example.com",  # 请替换为你的真实邮箱
    description="A lightweight NumPy-based data augmentation library for 1D physiological signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/你的用户名/PhysioAugment",  # 请替换为你的 GitHub 仓库地址
    packages=find_packages(),
    install_requires=[
        "numpy>=1.18.0",
        # 如果你后续在 core 里面用到了 scipy 处理滤波等操作，可以把下面这行取消注释
        # "scipy>=1.4.0", 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.7",
)