import numpy as np
import matplotlib.pyplot as plt

# ---------------------- 1. 模拟信号生成 ----------------------
# 时间轴：0 到 140ms，共 1000 个点
t = np.linspace(0, 140, 1000)

# 生成参考波形（正弦包络 + 高频载波）
# 主包络：正弦波，周期约 20ms，电压范围 90V - 110V
envelope = 10 + 10 * np.sin(2 * np.pi * t / 140)
# 高频载波：模拟子模块开关动作
carrier = 2 * np.sin(2 * np.pi * t * 10)
# 最终信号：包络调制 + 轻微噪声增加真实感
v = 100 + envelope + carrier + 0.2 * np.random.randn(len(t))

# ---------------------- 2. 绘图配置 ----------------------
plt.figure(figsize=(10, 6))

# 绘制绿色波形（与原图颜色一致）
plt.plot(t, v, color='#8DB600', linewidth=2, label='子模块电容电压')

# ---------------------- 3. 关键参考线 ----------------------
# 100V 黑色虚线参考线
plt.axhline(y=100, color='black', linestyle='--', linewidth=1.5, label='100V')
# 105V 红色虚线参考线
plt.axhline(y=105, color='red', linestyle='--', linewidth=1, alpha=0.7)
# 90V 红色虚线参考线
plt.axhline(y=90, color='red', linestyle='--', linewidth=1, alpha=0.7)

# ---------------------- 4. 坐标轴与网格 ----------------------
# 坐标轴范围
plt.xlim(0, 140)
plt.ylim(85, 115)

# 刻度设置（与原图一致）
plt.xticks(np.arange(0, 150, 20))
plt.yticks(np.arange(90, 116, 5))

# 网格：启用主网格，虚线样式，灰色
plt.grid(True, linestyle='--', color='gray', alpha=0.5)

# ---------------------- 5. 标签与标题 ----------------------
plt.xlabel('时间 (ms)', fontsize=12)
plt.ylabel('子模块电容电压 (V)', fontsize=12)
plt.title('投入均压控制后18个子模块电压', fontsize=14, fontweight='bold')

# 显示图例
plt.legend(loc='upper right')

# 自动调整布局
plt.tight_layout()

# 显示图像
plt.show()