import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 时间轴
t = np.linspace(0, 80, 200)

# 初始化功率因数数组
pf = np.zeros_like(t)

# 1. 启动阶段 (0~10s): 从0.3线性上升到0.6
mask_start = t <= 10
pf[mask_start] = 0.3 + (0.6 - 0.3) * (t[mask_start] / 10)

# 2. 加速阶段 (10~30s): 从0.6线性上升到0.8
mask_accel = (t > 10) & (t <= 30)
pf[mask_accel] = 0.6 + (0.8 - 0.6) * ((t[mask_accel] - 10) / 20)

# 3. 稳态阶段 (30~60s): 在0.7~0.8之间小幅波动
mask_steady = (t > 30) & (t <= 60)
# 生成小幅波动的随机数，均值0.75，范围0.7~0.8
np.random.seed(42)  # 固定随机种子保证可复现
pf[mask_steady] = 0.75 + 0.05 * np.sin(0.3 * t[mask_steady]) + 0.02 * np.random.randn(len(t[mask_steady]))
pf[mask_steady] = np.clip(pf[mask_steady], 0.7, 0.8)

# 4. 减速阶段 (60~80s): 从0.8线性下降到0.4
mask_decel = t > 60
pf[mask_decel] = 0.8 - (0.8 - 0.4) * ((t[mask_decel] - 60) / 20)

# 绘图
fig, ax = plt.subplots(figsize=(16, 8), dpi=120)
ax.plot(t, pf, color='#1f77b4', linewidth=2.5, label='功率因数')

# 标注阶段分界线
ax.axvline(x=10, color='#c2185b', linestyle='--', linewidth=1.5)
ax.axvline(x=30, color='#ff8c00', linestyle='--', linewidth=1.5)
ax.axvline(x=60, color='#d32f2f', linestyle='--', linewidth=1.5)

# 标注阶段名称
ax.text(5, 0.95, '启动阶段', fontsize=12, color='#c2185b', ha='center')
ax.text(20, 0.95, '加速阶段', fontsize=12, color='#ff8c00', ha='center')
ax.text(45, 0.95, '稳态阶段', fontsize=12, color='#0277bd', ha='center')
ax.text(70, 0.95, '减速阶段', fontsize=12, color='#d32f2f', ha='center')

# 标注阶段转换
ax.text(10, 0.55, '启动→加速', fontsize=10, color='#c2185b', bbox=dict(facecolor='white', alpha=0.8, edgecolor='#c2185b', boxstyle='round,pad=0.3'))
ax.text(30, 0.55, '加速→稳态', fontsize=10, color='#ff8c00', bbox=dict(facecolor='white', alpha=0.8, edgecolor='#ff8c00', boxstyle='round,pad=0.3'))
ax.text(60, 0.55, '稳态→减速', fontsize=10, color='#d32f2f', bbox=dict(facecolor='white', alpha=0.8, edgecolor='#d32f2f', boxstyle='round,pad=0.3'))

# 设置坐标轴
ax.set_xlabel('时间 (s)', fontsize=13)
ax.set_ylabel('功率因数', fontsize=13)
ax.set_title('牵引负荷不同工况下功率因数变化曲线', fontsize=14, pad=20)
ax.set_xlim(0, 80)
ax.set_ylim(0, 1.05)
ax.grid(linestyle=':', alpha=0.7)
ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.show()