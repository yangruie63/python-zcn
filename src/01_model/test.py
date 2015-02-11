 # -*- coding: utf-8 -*-
from mymodel import People,Man,Woman,onDate

p = People('yangrui',25)
p.printPeople();

m = Man('yangrui',28,18)
m.printPeople();

w = Woman('xiaohong',25,'C')
w.printPeople();

onDate(m,w)