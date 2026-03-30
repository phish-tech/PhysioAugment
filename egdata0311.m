% 1. 加载原始的 mat 数据
load('sub01_sit_01.mat');

% 注意：请把下面的 'raw_data' 替换为你在 MATLAB 工作区 (Workspace) 里看到的真实变量名
% 2. 提取第一行 (假设原矩阵是 M行 x N列，且第一行是我们要的信号)
signal_1d = dataMatrix(1, :);

% 3. 剥离其他所有信息，单独保存这个 1D 数组
save('test_ecg.mat', 'signal_1d');