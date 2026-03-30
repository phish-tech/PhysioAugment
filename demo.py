import numpy as np
import matplotlib.pyplot as plt

from core import Compose
from baseline import AddBaselineWander, AddRespirationInterference
from artifacts import AddMotionArtifact

def run_demo():
    try:
        clean_ppg = np.load('test_ppg.npy')[:1000]
    except FileNotFoundError:
        print("错误：找不到 test_ppg.npy 文件！")
        return

    # 1. 单独的增强器（用于展示分解动作）
    aug_baseline = AddBaselineWander(fs=100, amp_ratio=0.5, p=1.0)
    aug_artifact = AddMotionArtifact(fs=100, artifact_ratio=2.0, num_artifacts=(1, 2), p=1.0)
    
    # 2. 终极管道 (全家桶)
    pipeline = Compose([
        AddBaselineWander(fs=100, amp_ratio=0.4, p=1.0),
        AddRespirationInterference(fs=100, amp_ratio=0.3, p=1.0),
        AddMotionArtifact(fs=100, artifact_ratio=1.5, num_artifacts=(1, 2), p=1.0)
    ])

    # 3. 生成各种信号
    sig_baseline = aug_baseline(clean_ppg)
    sig_artifact = aug_artifact(clean_ppg)
    sig_full = pipeline(clean_ppg)


    # 3.5 保存增强后的数据到本地
    print("正在保存增强后的数据...")
    # 保存为炼丹师最爱的 .npy 格式
    np.save('augmented_baseline.npy', sig_baseline)
    np.save('augmented_full_pipeline.npy', sig_full)
    
    # 如果你想分享给用传统 MATLAB 跑信号处理的同事，也可以存为 .mat
    import scipy.io as sio
    sio.savemat('augmented_full_pipeline.mat', {'sig_full': sig_full})
    print("保存完毕！请查看左侧目录。")

    # ... 下面继续是画图的代码 (fig, axes = plt.subplots...) ...

    # 4. 绘制 4 行对比图
    fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)
    
    axes[0].plot(clean_ppg, color='#2ca02c', label='1. Original Clean PPG')
    axes[0].set_title("PhysioAugment: 1D Physiological Signal Augmentation", fontsize=16, fontweight='bold')
    
    axes[1].plot(sig_baseline, color='#ff7f0e', label='2. Low Freq: Baseline Wander')
    axes[2].plot(sig_artifact, color='#9467bd', label='3. High Freq: Motion Artifacts')
    axes[3].plot(sig_full, color='#d62728', label='4. Compose: Full Pipeline (All combined)')

    for ax in axes:
        ax.legend(loc='upper right')
        ax.grid(True, linestyle='--', alpha=0.6)
        
    axes[3].set_xlabel("Sample Index", fontsize=12)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_demo()