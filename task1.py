class Room:
    length=0
    width=0
    height=0
    square=0
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height
        self.doors=[]
        self.windows=[]
        self.square = 2*self.height*(self.width+self.length)

    def add_door(self,door):
        self.doors.append(door)
    def add_window(self,window):
        self.windows.append(window)


    def test(self):
        w = 0
        l=0
        for i in range(0, len(room.doors)):
            w = w + room.doors[i].width
        for i in range(0, len(room.windows)):
            w = w + room.windows[i].width
        for i in range(0, len(room.doors)):
            if room.doors[i].height>self.height:
                l=l+1
        for i in range(0, len(room.windows)):
            if room.windows[i].height+room.windows[i].delta> self.height:
                l = l + 1
        if 2*(self.width+self.length)<w or l>0:
            return "Такая комната существовать не может"
        else:
            return "Такая комната может существовать"


    def wallpaper_area(self):
        square=self.square
        for i in range(0, len(room.doors)):
            if room.doors[i].hidden==0:
                square = square - room.doors[i].square()
        for i in range(0, len(room.windows)):
            square = square - room.windows[i].square()
        return "Площадь обоев составляет " + str(square) + " м^2"

    def illumination(self):
        k = round(self.square / len(self.windows), 2)
        return 'Коэффициент освещенности составляет '+ str(k)


class Frame:
    width=0
    height=0
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def square(self):
        s=self.width*self.height
        return s

class Door(Frame):
    hidden=0 #скрытность=1
    def __init__(self,width,height,hidden):
        Frame.__init__(self,width,height)
        self.hidden=hidden
    def square(self):
        return Frame.square(self)


class Window(Frame):
    delta=0 # высота от пола
    def __init__(self,width,height,delta):
        Frame.__init__(self,width,height)
        self.delta=delta
    def square(self):
        return Frame.square(self)






room=Room(10,20,5)

def win(k):
    for i in range(k):
        h=int(input("Введите высоту окна: "))
        w=int(input("Введите ширину окна: "))
        d=float(input("Введите высоту от пола: "))
        room.add_window(Window(w,h,d))


win(int(input("Введите количество окон: ")))

def do(k):
    for i in range(k):
        h=int(input("Введите высоту двери: "))
        w=int(input("Введите ширину двери: "))
        hid=int(input("Введите, является ли скрытной (скрытая - 1; не скрытая - 0) : "))
        room.add_door(Door(w,h,hid))



do(int(input("Введите количество дверей: ")))


print(room.test())
if room.test()=="Такая комната может существовать":
    print(room.wallpaper_area())
    print(room.illumination())