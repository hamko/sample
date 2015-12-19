# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import seaborn as sns

fig, ax = plt.subplots()


# メインプロット位置変更
# Matplotlibでは、1つのメインプロットと複数のWidgetsで表現される図を書く
plt.subplots_adjust(left=0.25, bottom=0.25)

# メインプロット
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
s = a0*np.sin(2*np.pi*f0*t)
l, = plt.plot(t, s, lw=2, color='red') # Line2D Objectハンドルlを持っておくと、あとでset_ydataにより変更可能
plt.axis([0, 1, -10, 10])

# スライダー2つ
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)
def update(val): # valって何だろう？今変更されたスライダーの値かな？
    amp = samp.val # Slider.valで現在のスライダーの値が読める
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t)) # 変更
    fig.canvas.draw_idle() # 更新
sfreq.on_changed(update)
samp.on_changed(update)


# ボタン
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
def reset(event): # eventって何だろう？クリックされたか離れたかかな？
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

# ラジオボタン
rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()