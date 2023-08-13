import streamlit as st  # StreamlitのWebアプリ機能のためのインポート。
import pandas as pd  # データ操作のためのpandasのインポート。
import matplotlib.pyplot as plt  # プロットのためのmatplotlibのインポート。
import seaborn as sns  # 高度なプロットのためのseabornのインポート。

# Streamlitアプリのタイトルを設定。
st.title("Palmer's Penguins")
# タイトルの下にマークダウンテキストを追加。
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

# x軸の変数を選択するためのドロップダウンメニューを作成。
selected_x_var = st.selectbox('What do want the x variable to be?',
  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
# y軸の変数を選択するためのドロップダウンメニューを作成。
selected_y_var = st.selectbox('What about the y?',
  ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])

# ユーザーが自身のペンギンのCSVファイルをアップロードするオプションを提供。
penguin_file = st.file_uploader('Select Your Local Penguins CSV')
# ユーザーがファイルをアップロードした場合、そのファイルはpandasデータフレームに読み込まれる。
if penguin_file is not None:
  penguins_df = pd.read_csv(penguin_file)
# ファイルがアップロードされなかった場合、アプリは停止する。
else:
  st.stop()

# seabornのプロットの背景スタイルを設定。
sns.set_style('darkgrid')
# 各ペンギンの種類に対して特定のマーカーを設定。
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
# seabornを使用して散布図を作成。
fig, ax = plt.subplots()
ax = sns.scatterplot(data = penguins_df, x = selected_x_var,
  y = selected_y_var, hue = 'species', markers = markers,
  style = 'species')
# x軸とy軸のラベルおよびタイトルを設定。
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins")
# Streamlitアプリにプロットを表示。
st.pyplot(fig)
