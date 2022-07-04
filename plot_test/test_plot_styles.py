from matplotlib import pyplot as plt
styles = plt.style.available

for style in styles:
    plt.style.use(style) # 设置主题
    plt.figure(figsize=(5,5))
    # sinplot()
    plt.title(style)
    plt.show()