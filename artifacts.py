import numpy as np

class AddMotionArtifact:
    """模拟体动伪影 (Motion Artifact)"""
    def __init__(self, fs=100, artifact_ratio=1.5, num_artifacts=(1, 3), p=0.5):
        self.fs = fs
        self.artifact_ratio = artifact_ratio
        self.num_artifacts = num_artifacts
        self.p = p

    def __call__(self, x):
        if np.random.rand() > self.p:
            return x
            
        x_aug = np.array(x, copy=True)
        n_samples = len(x_aug)
        
        n_artifacts = np.random.randint(self.num_artifacts[0], self.num_artifacts[1] + 1)
        signal_max_amp = np.max(np.abs(x)) if np.max(np.abs(x)) > 1e-5 else 1.0
        
        for _ in range(n_artifacts):
            center = np.random.randint(0, n_samples)
            width_samples = np.random.randint(int(0.1 * self.fs), int(0.6 * self.fs))
            width_samples = max(width_samples, 2)
            
            t = np.arange(n_samples)
            sigma = width_samples / 4.0 
            envelope = np.exp(-0.5 * ((t - center) / sigma) ** 2)
            
            noise = np.random.randn(n_samples) * signal_max_amp * self.artifact_ratio
            artifact_component = envelope * noise
            
            x_aug += artifact_component
            
        return x_aug