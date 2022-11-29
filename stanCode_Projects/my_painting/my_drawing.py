"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLabel
from campy.graphics.gwindow import GWindow
window = GWindow(460, 350, 'inside-out')


def main():
    """
    Hi! How are you today?
    All your feeling matters :)
    """
    happiness()
    sadness()
    label()


def happiness():

    neck = GRect(25, 30)
    window.add(neck, x=230, y=125)
    neck.filled = True
    neck.fill_color = 'lemonchiffon'
    neck.color = 'khaki'

    head = GOval(100, 100)
    window.add(head, x=200, y=30)
    head.filled = True
    head.fill_color = 'lemonchiffon'
    head.color = 'khaki'

    clothes1 = GOval(50, 80)
    window.add(clothes1, 210, 145)
    clothes1.filled = True
    clothes1.fill_color = 'lightgreen'
    clothes1.color = 'lightgreen'

    clothes2 = GRect(35, 40)
    window.add(clothes2, 218, 210)
    clothes2.filled = True
    clothes2.fill_color = 'lightgreen'
    clothes2.color = 'lightgreen'

    clothupper3 = GPolygon()
    clothupper3.add_vertex((150, 195))
    clothupper3.add_vertex((110, 270))
    clothupper3.add_vertex((230, 270))
    window.add(clothupper3)
    clothupper3.filled = True
    clothupper3.fill_color = 'lightgreen'
    clothupper3.color = 'lightgreen'

    clothes4 = GOval(50, 40)
    window.add(clothes4, 205, 230)
    clothes4.filled = True
    clothes4.fill_color = 'lightgreen'
    clothes4.color = 'lightgreen'

    leg2 = GPolygon()
    leg2.add_vertex((146, 247))
    leg2.add_vertex((61, 260))
    leg2.add_vertex((67, 243))
    leg2.add_vertex((62, 241))
    leg2.add_vertex((46, 270))
    leg2.add_vertex((158, 270))
    window.add(leg2)
    leg2.filled = 'True'
    leg2.fill_color = 'lemonchiffon'
    leg2.color = 'khaki'

    leg1 = GPolygon()
    leg1.add_vertex((134, 225))
    leg1.add_vertex((143, 238))
    leg1.add_vertex((116, 272))
    leg1.add_vertex((113, 271))
    leg1.add_vertex((103, 253))
    leg1.add_vertex((108, 249))
    leg1.add_vertex((116, 259))
    window.add(leg1)
    leg1.filled = 'True'
    leg1.fill_color = 'lemonchiffon'
    leg1.color = 'khaki'

    limb = GPolygon()
    limb.add_vertex((230, 150))
    limb.add_vertex((240, 160))
    limb.add_vertex((135, 210))
    limb.add_vertex((130, 205))
    window.add(limb)
    limb.filled = True
    limb.fill_color = 'lemonchiffon'
    limb.color = 'khaki'

    hair1 = GArc(120, 120, 680, 180)
    hair1.filled = True
    hair1.fill_color = 'steelblue'
    hair1.color = 'steelblue'
    window.add(hair1, 205, 20)

    hair2 = GPolygon()
    hair2.add_vertex((277, 25))
    hair2.add_vertex((313, 27))
    hair2.add_vertex((305, 51))
    window.add(hair2)
    hair2.filled = True
    hair2.fill_color = 'steelblue'
    hair2.color = 'steelblue'

    hair3 = GPolygon()
    hair3.add_vertex((218, 39))
    hair3.add_vertex((245, 29))
    hair3.add_vertex((236, 63))
    window.add(hair3)
    hair3.filled = True
    hair3.fill_color = 'steelblue'
    hair3.color = 'steelblue'

    hair4 = GPolygon()
    hair4.add_vertex((245, 60))
    hair4.add_vertex((255, 61))
    hair4.add_vertex((252, 70))
    window.add(hair4)
    hair4.filled = True
    hair4.fill_color = 'steelblue'
    hair4.color = 'steelblue'

    hair5 = GPolygon()
    hair5.add_vertex((269, 70))
    hair5.add_vertex((262, 80))
    hair5.add_vertex((256, 65))
    window.add(hair5)
    hair5.filled = True
    hair5.fill_color = 'steelblue'
    hair5.color = 'steelblue'

    hair6 = GPolygon()
    hair6.add_vertex((269, 75))
    hair6.add_vertex((295, 80))
    hair6.add_vertex((279, 100))
    window.add(hair6)
    hair6.filled = True
    hair6.fill_color = 'steelblue'
    hair6.color = 'steelblue'

    hair7 = GPolygon()
    hair7.add_vertex((285, 85))
    hair7.add_vertex((292, 85))
    hair7.add_vertex((282, 105))
    window.add(hair7)
    hair7.filled = True
    hair7.fill_color = 'steelblue'
    hair7.color = 'steelblue'

    hair8 = GPolygon()
    hair8.add_vertex((293, 90))
    hair8.add_vertex((280, 114))
    hair8.add_vertex((305, 95))
    window.add(hair8)
    hair8.filled = True
    hair8.fill_color = 'steelblue'
    hair8.color = 'steelblue'

    eye_l = GOval(8, 16)
    window.add(eye_l, 220, 68)
    eye_l.filled = True
    eye_l.fill_color = 'steelblue'
    eye_l.color = 'steelblue'

    eye1 = GOval(8, 16)
    window.add(eye1, 240, 75)
    eye1.filled = True
    eye1.fill_color = 'steelblue'
    eye1.color = 'steelblue'

    nose = GOval(5, 5)
    window.add(nose, 230, 90)
    nose.filled = True
    nose.fill_color = 'gold'
    nose.color = 'gold'


def sadness():
    feet = GOval(10, 25)
    window.add(feet, 357, 247)
    feet.filled = 'True'
    feet.fill_color = 'skyblue'
    feet.color = 'deepskyblue'

    pants = GPolygon()
    pants.add_vertex((360, 272))
    pants.add_vertex((294, 275))
    pants.add_vertex((298, 245))
    pants.add_vertex((359, 255))
    window.add(pants)
    pants.filled = 'True'
    pants.fill_color = 'steelblue'
    pants.color = 'steelblue'

    clothes1 = GOval(85, 85)
    window.add(clothes1, 255, 190)
    clothes1.color = 'aliceblue'
    clothes1.filled = 'True'
    clothes1.fill_color = 'aliceblue'

    hand = GOval(25, 10)
    window.add(hand, 262, 265)
    hand.filled = 'True'
    hand.fill_color = 'skyblue'
    hand.color = 'deepskyblue'

    clothes2 = GPolygon()
    clothes2.add_vertex((274, 220))
    clothes2.add_vertex((273, 265))
    clothes2.add_vertex((286, 270))
    clothes2.add_vertex((298, 231))
    window.add(clothes2)
    clothes2.color = 'lightblue'
    clothes2.filled = 'True'
    clothes2.fill_color = 'lightblue'

    head = GOval(120, 120)
    window.add(head, x=260, y=100)
    head.filled = True
    head.fill_color = 'skyblue'
    head.color = 'deepskyblue'

    hair1 = GArc(130, 130, 30, 180)
    hair1.filled = True
    hair1.fill_color = 'steelblue'
    hair1.color = 'steelblue'
    window.add(hair1, 260, 100)

    hair2 = GPolygon()
    hair2.add_vertex((262, 131))
    hair2.add_vertex((245, 181))
    hair2.add_vertex((281, 209))
    hair2.add_vertex((307, 155))
    window.add(hair2)
    hair2.filled = True
    hair2.fill_color = 'steelblue'
    hair2.color = 'steelblue'

    hair3 = GPolygon()
    hair3.add_vertex((339, 139))
    hair3.add_vertex((308, 179))
    hair3.add_vertex((294, 173))
    hair3.add_vertex((323, 131))
    window.add(hair3)
    hair3.filled = True
    hair3.fill_color = 'steelblue'
    hair3.color = 'steelblue'

    hair4 = GPolygon()
    hair4.add_vertex((375, 187))
    hair4.add_vertex((384, 186))
    hair4.add_vertex((384, 154))
    hair4.add_vertex((380, 140))
    hair4.add_vertex((373, 127))
    window.add(hair4)
    hair4.filled = True
    hair4.fill_color = 'steelblue'
    hair4.color = 'steelblue'

    eye_l = GOval(8, 8)
    window.add(eye_l, 335, 155)
    eye_l.filled = True
    eye_l.fill_color = 'steelblue'
    eye_l.color = 'steelblue'

    eye_r = GOval(8, 8)
    window.add(eye_r, 360, 160)
    eye_r.filled = True
    eye_r.fill_color = 'steelblue'
    eye_r.color = 'steelblue'

    nose = GOval(5, 5)
    window.add(nose, 350, 170)
    nose.filled = True
    nose.fill_color = 'gold'
    nose.color = 'gold'

    glass_l = GOval(40, 45)
    window.add(glass_l, 310, 135)
    glass_l.color = 'plum'

    glass_r = GOval(40, 45)
    window.add(glass_r, 355, 140)
    glass_r.color = 'plum'


def label():
    title = GLabel('How are you today ?')
    title.font = 'Gill Sans-30'
    window.add(title, x=(window.width-title.width)/2, y=320)
    title.color = 'lightsteelblue'
    title.filled = 'True'
    print((window.width-title.width)/2)


if __name__ == '__main__':
    main()
