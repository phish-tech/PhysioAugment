# PhysioAugment

[English](README.md) | [简体中文](README_zh-CN.md)

[![Python >= 3.7](https://img.shields.io/badge/Python->=3.7-blue.svg)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Required-orange.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**PhysioAugment** 是一个轻量级、纯 NumPy 实现的数据增强库，专为 1D 生理信号（如 PPG、ECG、呼吸信号等）量身定制。

在深度学习模型训练中，高质量的数据增强对提升模型的鲁棒性至关重要。与图像领域的丰富工具箱不同，针对 1D 生理信号的轻量化增强工具相对匮乏。PhysioAugment 旨在填补这一空白，提供一套即插即用、高度可定制的增强流水线。

## ✨ 核心特性

* **纯 NumPy 实现**：极致轻量，无需安装庞大的深度学习框架即可运行。
* **贴合真实场景**：内置多种真实的生理信号噪声与干扰模型（如基线漂移、呼吸干扰、体动伪影）。
* **面向深度学习优化**：采用类似 PyTorch `transforms.Compose` 的 API 设计，可无缝接入现有的 Dataloader 和训练流水线。
* **概率控制**：支持为每种增强操作设置触发概率（`p`），方便构建多样化的训练批次。

## 📦 安装指南

你可以通过 pip 直接从 GitHub 安装最新版本：

```bash
pip install git+[https://github.com/phish-tech/PhysioAugment.git](https://github.com/phish-tech/PhysioAugment.git)
```

或者，将代码克隆到本地进行开发（推荐使用可编辑模式）：

```bash
git clone [https://github.com/phish-tech/PhysioAugment.git](https://github.com/phish-tech/PhysioAugment.git)
cd PhysioAugment
pip install -e .
```

## 🚀 快速开始

PhysioAugment 的 API 设计非常直观。你可以使用 `Compose` 将多个增强操作串联起来：

```python
import numpy as np
from core import Compose, AddMotionArtifact
from baseline import AddBaselineWander, AddRespirationInterference

# 1. 初始化数据增强流水线
augment_pipeline = Compose([
    AddBaselineWander(fs=100, amp_ratio=0.3, p=0.8),          # 添加基线漂移 (80% 概率)
    AddRespirationInterference(fs=100, amp_ratio=0.2, p=0.5), # 添加呼吸干扰 (50% 概率)
    AddMotionArtifact(fs=100, artifact_ratio=1.5, p=0.3)      # 添加体动伪影 (30% 概率)
])

# 2. 准备你的 1D 信号数据 (例如长度为 1000 的 PPG 信号)
# x = np.load('your_signal.npy')
x = np.sin(2 * np.pi * 1.5 * np.arange(1000) / 100) # 模拟信号

# 3. 应用数据增强
augmented_x = augment_pipeline(x)
```

## 🛠️ 支持的增强方法

目前版本包含以下核心增强模块（更多模块持续更新中）：

### 1. `AddBaselineWander` (基线漂移)
模拟由传感器位移或温度变化引起的低频基线漂移。
* **`fs`**: 采样率
* **`amp_ratio`**: 漂移幅度相对于原信号的比例
* **`freq_range`**: 漂移频率的范围 (默认 0.05Hz - 0.3Hz)
 <img width="1901" height="309" alt="image" src="https://github.com/user-attachments/assets/a31926a1-b332-46d8-924a-ed4711c149b1" />


### 2. `AddRespirationInterference` (呼吸干扰)
模拟生理信号中不可避免的呼吸调制效应。
* **`resp_freq_range`**: 典型呼吸频率范围 (默认 0.2Hz - 0.4Hz)
<img width="1898" height="232" alt="image" src="https://github.com/user-attachments/assets/a092c0c7-5f91-40ac-82dc-662f40e5c70d" />


### 3. `AddMotionArtifact` (体动伪影)
模拟由用户剧烈运动产生的突发性、高振幅噪声。
* **`artifact_ratio`**: 伪影强度
* **`num_artifacts`**: 生成伪影的数量区间
<img width="1913" height="323" alt="image" src="https://github.com/user-attachments/assets/31ef2fd7-f68b-454b-a690-6b5c06c14ef4" />

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 协议开源。欢迎在你的研究或项目中免费使用。如果你觉得这个库对你有帮助，欢迎点个 ⭐️ Star！
