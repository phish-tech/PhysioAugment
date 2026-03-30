import numpy as np

class AddBaselineWander:
    """模拟基线漂移 (Baseline Wander)"""
    def __init__(self, fs=100, amp_ratio=0.3, freq_range=(0.05, 0.3), p=0.5):
        self.fs = fs
        self.amp_ratio = amp_ratio
        self.freq_range = freq_range
        self.p = p

    def __call__(self, x):
        if np.random.rand() > self.p:
            return x
        
        x = np.asarray(x)
        n_samples = len(x)
        t = np.arange(n_samples) / self.fs
        
        signal_max_amp = np.max(np.abs(x)) if np.max(np.abs(x)) > 1e-5 else 1.0
        wander_amp = self.amp_ratio * signal_max_amp
        
        f = np.random.uniform(self.freq_range[0], self.freq_range[1])
        phase = np.random.uniform(0, 2 * np.pi)
        baseline_wander = wander_amp * np.sin(2 * np.pi * f * t + phase)
        
        f2 = np.random.uniform(self.freq_range[0] * 0.1, self.freq_range[0])
        baseline_wander += (wander_amp * 0.5) * np.sin(2 * np.pi * f2 * t + np.random.uniform(0, 2 * np.pi))
        
        return x + baseline_wander


class AddRespirationInterference:
    """模拟呼吸干扰 (Respiration Interference)"""
    def __init__(self, fs=100, amp_ratio=0.3, resp_freq_range=(0.2, 0.4), p=0.5):
        self.fs = fs
        self.amp_ratio = amp_ratio
        self.resp_freq_range = resp_freq_range
        self.p = p

    def __call__(self, x):
        if np.random.rand() > self.p:
            return x
            
        x = np.asarray(x)
        n_samples = len(x)
        t = np.arange(n_samples) / self.fs
        
        f_resp = np.random.uniform(self.resp_freq_range[0], self.resp_freq_range[1])
        signal_max_amp = np.max(np.abs(x)) if np.max(np.abs(x)) > 1e-5 else 1.0
        amp = self.amp_ratio * signal_max_amp
        
        phase_1 = np.random.uniform(0, 2 * np.pi)
        interference = amp * np.sin(2 * np.pi * f_resp * t + phase_1)
        
        phase_2 = np.random.uniform(0, 2 * np.pi)
        interference += (amp * 0.2) * np.sin(2 * np.pi * (f_resp * 2) * t + phase_2)
                       
        return x + interference