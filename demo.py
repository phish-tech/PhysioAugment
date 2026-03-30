import numpy as np
import matplotlib.pyplot as plt

# 引入我们写好的增强算法模块
from baseline import AddBaselineWander, AddRespirationInterference # <-- 补充导入了呼吸干扰
from artifacts import AddMotionArtifact

def run_demo():
    # 1. 加载真实的 PPG 数据
    print("正在加载 PPG 数据...")
    try:
        clean_ppg = np.load('test_ppg.npy')
    except FileNotFoundError:
        print("错误：找不到 test_ppg.npy，请确保数据在同级目录下！")
        return

    # 截取前 1000 个点用于清晰可视化 (约 10 秒数据)
    plot_length = min(1000, len(clean_ppg))
    clean_ppg_segment = clean_ppg[:plot_length]

    # 2. 实例化增强器 (预留好接口配置)
    augmenter_bw = AddBaselineWander(fs=100, amp_ratio=0.5, p=1.0)
    augmenter_ri = AddRespirationInterference(fs=100, amp_ratio=0.2, p=1.0) # <-- 实例化呼吸干扰
    augmenter_ma = AddMotionArtifact(fs=100, artifact_ratio=1.5, num_artifacts=(1, 2), p=1.0)

    # 3. 分别生成增强后的信号
    print("正在应用数据增强...")
    ppg_with_bw = augmenter_bw(clean_ppg_segment)
    ppg_with_ri = augmenter_ri(clean_ppg_segment) # <-- 生成呼吸干扰信号
    ppg_with_ma = augmenter_ma(clean_ppg_segment)

    # 4. 统一的绘图接口 (改为 4行1列 对比图)
    print("正在生成效果对比图...")
    fig, axes = plt.subplots(4, 1, figsize=(14, 12), sharex=True)

    # 第一张图：原始干净信号
    axes[0].plot(clean_ppg_segment, color='#2ca02c', linewidth=1.5, label='Original Clean PPG')
    axes[0].set_title("PhysioAugment Demo: Original vs Augmented Signals", fontsize=16, fontweight='bold')
    axes[0].legend(loc='upper right')
    axes[0].grid(True, linestyle='--', alpha=0.6)

    # 第二张图：基线漂移
    axes[1].plot(ppg_with_bw, color='#ff7f0e', linewidth=1.5, label='Augmented: Baseline Wander (Low Freq)')
    axes[1].legend(loc='upper right')
    axes[1].grid(True, linestyle='--', alpha=0.6)

    # 第三张图：呼吸干扰 (新增)
    axes[2].plot(ppg_with_ri, color='#1f77b4', linewidth=1.5, label='Augmented: Respiration Interference (Modulation)')
    axes[2].legend(loc='upper right')
    axes[2].grid(True, linestyle='--', alpha=0.6)

    # 第四张图：体动伪影
    axes[3].plot(ppg_with_ma, color='#d62728', linewidth=1.5, label='Augmented: Motion Artifacts (High Freq/Burst)')
    axes[3].set_xlabel("Sample Index", fontsize=12) 
    axes[3].legend(loc='upper right')
    axes[3].grid(True, linestyle='--', alpha=0.6)

    # --- 微调部分：强制全屏显示 ---
    try:
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized() 
    except Exception as e:
        print(f"提示：当前后端不支持自动最大化窗口 ({e})")
    # ----------------------------

    # 调整布局并显示
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_demo()
