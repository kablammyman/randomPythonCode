from random import randint

print "No Mince Pie"
print "-----------------"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZ"
VOWELS = "AEIOU"
COLORS = ["red", "pink", "rose", "off red", "light red", "dark red"];
print "You are in a ship flying through space. You crash land"
print "You land on a planet"

planetName = ""
for x in range(1,10):
	planetName += CONSONANTS[ randint(0,20) ]
	planetName += VOWELS[ randint(0,4) ]
print "The name of the planet is " + planetName
print "The planet has "+str(randint(0,10))+" moons."
print "The sky is "+COLORS [ randint(0,5) ] +" and the grass is "+COLORS[randint(0,5)];
a = input( "Would you like to go North, South, East or West? " )
print "You go "+str(a)+" and fall into a wormhole."
print "When you come out the stars all look different."
#130 GOTO 30
 