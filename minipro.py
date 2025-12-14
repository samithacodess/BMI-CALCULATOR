import csv
import wx
from sklearn.tree import DecisionTreeClassifier

# LOAD DATASET

X = []
y = []

f=open("dataset_8symptoms_final.csv", "r")
reader = csv.reader(f)
next(reader)
for row in reader:
        y.append(row[0])
        X.append([int(row[1]), int(row[2]), int(row[3]),int(row[4]),int(row[5]),int(row[6]),int(row[7]),int(row[8])])

model = DecisionTreeClassifier()
model.fit(X, y)

# RESULT WINDOW

def show_result_window(result):
    frame1 = wx.Frame(None, title="Prediction", size=(400,200))
    p = wx.Panel(frame1)
    p.SetBackgroundColour("light blue")

    lbl = wx.StaticText(p,label=f"Predicted Disease:\n{result}", pos=(100,40))
    lbl.SetFont(wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

    ok = wx.Button(p,label="OK", pos=(160,120))
    ok.Bind(wx.EVT_BUTTON,lambda x:frame1.Close())

    frame1.Centre()
    frame1.Show()

# -------------------------
# MAIN WINDOW
# -------------------------
app = wx.App()
frame = wx.Frame(None, title="Disease Predictor", size=(1600,880))

# --- Load background image ---
bg = wx.Image("bg.png", wx.BITMAP_TYPE_ANY)
bg = bg.Scale(1600,800,wx.IMAGE_QUALITY_HIGH)
bg_bitmap = wx.Bitmap(bg)

# --- Paint background ---
def paint_background(event):
    dc = wx.PaintDC(frame)
    dc.DrawBitmap(bg_bitmap,0,0)

frame.Bind(wx.EVT_PAINT, paint_background)

# -------------------------
# WIDGETS DIRECTLY ON FRAME
# -------------------------

title = wx.StaticText(frame, label="Disease Prediction System", pos=(550,20))
title.SetFont(wx.Font(28, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
title.SetForegroundColour("black")

subtitle = wx.StaticText(frame, label="Select your Symptoms:", pos=(600, 160))
subtitle.SetFont(wx.Font(24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
subtitle.SetForegroundColour("black")

# Checkboxes
cb1 = wx.CheckBox(frame, label="Fever", pos=(600,220),size=(200,20))
cb2 = wx.CheckBox(frame, label="Body Pain", pos=(600,260),size=(200,20))
cb3 = wx.CheckBox(frame, label="Vomiting", pos=(600,300),size=(200,20))
cb4 = wx.CheckBox(frame, label="Cough", pos=(600,340),size=(200,20))
cb5 = wx.CheckBox(frame, label="Cold", pos=(600,380),size=(200,20))
cb6 = wx.CheckBox(frame, label="Headache", pos=(600,420),size=(200,20))
cb7 = wx.CheckBox(frame, label="Fatigue", pos=(600,460),size=(200,20))
cb8 = wx.CheckBox(frame, label="Diarrhea", pos=(600,500),size=(200,20))

for cb in (cb1, cb2, cb3, cb4, cb5, cb6, cb7, cb8):
    cb.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    cb.SetForegroundColour("black")

# Predict button
def on_predict(event):
    s1 = 1 if cb1.GetValue() else 0
    s2 = 1 if cb2.GetValue() else 0
    s3 = 1 if cb3.GetValue() else 0
    s4 = 1 if cb4.GetValue() else 0
    s5 = 1 if cb5.GetValue() else 0
    s6 = 1 if cb6.GetValue() else 0
    s7 = 1 if cb7.GetValue() else 0
    s8 = 1 if cb8.GetValue() else 0
    prediction = model.predict([[s1, s2, s3, s4, s5, s6, s7, s8]])[0]
    show_result_window(prediction)

btn = wx.Button(frame, label="Predict Disease", size=(220,50), pos=(650,550))
btn.SetFont(wx.Font(20,wx.FONTFAMILY_SWISS,wx.FONTSTYLE_NORMAL,wx.FONTWEIGHT_NORMAL))
btn.SetBackgroundColour("#2e7d32")
btn.SetForegroundColour("black")
btn.Bind(wx.EVT_BUTTON, on_predict)

# --- SHOW EVERYTHING ---
frame.Show()
app.MainLoop()
