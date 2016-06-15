###########Created by Sourabh Saini##############
import socket
import tkinter, re
from tkinter import *

root = Tk()
root.geometry("50x50")
root.resizable(False,False)
root.wm_attributes("-topmost", True)
root.wm_geometry('+' + str(1316) + '+' + str(718))
root.overrideredirect(True)
#root.attributes('-alpha', 0.4) in Windows
root.wait_visibility(root)
root.wm_attributes('-alpha',0.6)


class Drag:
    ''' Makes a window dragable. '''
      
    def __init__ (root, par, dissable=None, releasecmd=None) :

        root.Par        = par
        root.Dissable   = dissable

        root.ReleaseCMD = releasecmd

        root.Par.bind('<Button-1>', root.relative_position)
        root.Par.bind('<ButtonRelease-1>', root.drag_unbind)


    def relative_position (root, event) :

        cx, cy = root.Par.winfo_pointerxy()

        _filter = re.compile(r"(\d+)?x?(\d+)?([+-])(\d+)([+-])(\d+)")

        pos = root.Par.winfo_geometry()

        filtered = _filter.search(pos)
        x = int(filtered.group(4))
        y = int(filtered.group(6))
        
        #x, y = 1300, 700

        root.OriX = x
        root.OriY = y

        root.RelX = cx - x
        root.RelY = cy - y

        root.Par.bind('<Motion>', root.drag_wid)

    def drag_wid (root, event) :

        cx, cy = root.Par.winfo_pointerxy()

        d = root.Dissable

        if d == 'x' :
            x = root.OriX
            y = cy - root.RelY
        elif d == 'y' :
            x = cx - root.RelX
            y = root.OriY
        else:
            x = cx - root.RelX
            y = cy - root.RelY

        if x < 0 :
            x = 0

        if y < 0 :
            y = 0

        root.Par.wm_geometry('+' + str(x) + '+' + str(y))

    def drag_unbind (root, event) :

        root.Par.unbind('<Motion>')

        if root.ReleaseCMD != None :
            root.ReleaseCMD()


    def dissable (root) :

        root.Par.unbind('<Button-1>')
        root.Par.unbind('<ButtonRelease-1>')
        root.Par.unbind('<Motion>')

root.Drag = Drag(root)

REMOTE_SERVER = "www.google.com"
def is_connected():
      try:
        # see if we can resolve the host name -- tells us if there is a DNS listening.
        host = socket.gethostbyname(REMOTE_SERVER)
        # connect to the host -- tells us if the host is actually reachable.
        s = socket.create_connection((host, 80), 2)
        root["bg"]="green"
      except:
        root["bg"]="red"
      root.after(1000, is_connected)

is_connected()
root.mainloop()
   
###########Created by Sourabh Saini##############
