import pandas as pd
import cv2
import numpy as np

img = cv2.imread('images.jpeg')
imgWidth = img.shape[1] - 40
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv("colors(1).csv", header=None, names=index)

r = g = b = xpos = ypos = 0


def getRGBvalue(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    xpos = x
    ypos = y
    b, g, r = img[y, x]
    b = int(b)
    g = int(g)
    r = int(r)


def colorname(B, G, R):
    minimum = 10000
    cname = ""
    for i in range(len(df)):
        d = abs(B - int(df.loc[i, "B"])) + abs(G - int(df.loc[i, "G"])) + abs(R - int(df.loc[i, "R"]))
        if d < minimum:
            minimum = d
            cname = df.loc[i, "color_name"] + " Hex: " + df.loc[i, "hex"]
    return cname


cv2.namedWindow('image')
cv2.setMouseCallback('image', getRGBvalue)

while True:
    img_copy = img.copy()  
    cv2.rectangle(img_copy, (20, 20), (imgWidth, 60), (b, g, r), -1)
    text = colorname(b, g, r) + '  R=' + str(r) + '  G=' + str(g) + '  B=' + str(b)
    if r + g + b >= 600:
        cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(img_copy, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('image', img_copy)

    if cv2.waitKey(20) & 0xFF == 27:  
        break

cv2.destroyAllWindows()

