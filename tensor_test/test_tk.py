import tkinter as tk
import redis

window = tk.Tk()
# window.title("Frame参数说明")
# window.iconbitmap("./image/icon.ico")
smtc = {
    'horizontal_cmd':['maintain heading', 'heading towards target', 'crank 30deg', 'crank 50deg', 'turn 90deg to target', 'turn 180 to target'],
    'vertical_cmd':['turn 180 to targetmaintain height', 'steer towards target', 'dive 10deg', 'dive 30deg', 'climb 10deg', 'climb 20deg'],
    'vel_cmd':['300', '600', '900'],
    'ny_cmd':['5.5', '8'],
    'maneuver_target':['0', '1', '2', '3'],
    'action_shoot_target':['0', '1'],
    'view control':['q', 'w']
}
player = 'player'+'0'
action = [0,0,0,0,0]
# r = redis.Redis(host='127.0.0.1')
def send_action(event):
    manunver = event.widget.cget('text')
    type = event.widget.master.children['!label'].cget('text')
    index = list(smtc.keys()).index(type)
    value = smtc[type].index(manunver)
    action[index] = value
    # r.put(player,action)
    print(action)

for i, type in enumerate(smtc.keys()):
    frame = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1,
    )
    frame.grid(row=7, column=i, padx=7, pady=7)
    tk.Label(frame, text=type).pack()

    for j,manunver in enumerate(smtc[type]):
        but = tk.Button(master=frame, text=manunver)
        but.bind('<Button-1>', send_action)
        but.pack()

window.mainloop()