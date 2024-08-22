import matplotlib.pyplot as plt
import numpy as np

# 数据
years = ['2018', '2019', '2020', '2021', '2022', '2023']
house_prices = [120, 125, 130, 140, 145, 150]
rents = [2000, 2200, 2400, 2600, 2800, 3000]

# 设置柱状图的宽度
bar_width = 0.35

# 设置 x 轴位置
index = np.arange(len(years))

# 创建柱状图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制租金柱状图，颜色设为淡绿色
bar2 = ax.bar(index, rents, bar_width, label='Rents (元/月)', color='lightgreen')

# 绘制房价柱状图，颜色设为淡蓝色，位置与租金柱状图并列
bar1 = ax.bar(index + bar_width, house_prices, bar_width, label='House Prices (万元)', color='lightblue')

# 设置图表标题和标签
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Value', fontsize=12, loc='top')
# plt.title('House Prices and Rents Over Time', fontsize=14)

# 设置 x 轴刻度
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(years)

# 添加图例，设置在图表下方，去除边框
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)

# 添加网格线（可选）
# ax.grid(True, linestyle='--', alpha=0.6)

# 设置背景为透明
fig.patch.set_alpha(0.0)
ax.patch.set_alpha(0.0)

# 移除所有边框，保留x轴（底部边框）
for spine in ['top', 'left', 'right']:
    ax.spines[spine].set_visible(False)

# 保留的x轴颜色为黑色
ax.spines['bottom'].set_color('black')

# 保存图表为文件，使用透明背景，并确保图例不被裁剪
plt.savefig('house_prices_and_rents_swapped.png', format='png', transparent=True, bbox_inches='tight', pad_inches=0.1)

# 显示图表
plt.tight_layout()
plt.show()
