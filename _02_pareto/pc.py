import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
from matplotlib.ticker import PercentFormatter

font_path = 'C:/Windows/Fonts/malgunbd.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


df = pd.DataFrame(
	{'defects': [100.0, 50.0, 30.0, 30.0, 20.0, 30.0, 10.0, 10.0]}
)

df.index = ['미스매칭', '찍힘', '쇼트', '오작동', '엣지오염', '훼손', '미작동', '멈춤']

df = df.sort_values(by='defects',ascending=False)

df["cumpercentage"] = df["defects"].cumsum()/df["defects"].sum()*100


fig, ax = plt.subplots()
ax.bar(df.index, df["defects"], color="C0")
ax2 = ax.twinx()
ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
ax2.yaxis.set_major_formatter(PercentFormatter())

ax.tick_params(axis="y", colors="C0")
ax2.tick_params(axis="y", colors="C1")
plt.title(u"Detect 유형별 비율",fontproperties=font_name)
plt.show()