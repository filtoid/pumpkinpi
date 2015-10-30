import mcpi.minecraft as minecraft
import mcpi.block as block
from room import Room

mc = minecraft.Minecraft.create('127.0.0.1')
room = Room()
room.draw_room(mc)
room.set_lighting(mc)


#make the pumpkin
orangeWool = block.Block(35,1)
greyWool = block.Block(35,8)

def clear_pumpkin():
	#Body of pumpkin
	mc.setBlocks(-5,0,15,5,0,15, orangeWool)
	mc.setBlocks(-8,1,15,8,1,15, orangeWool)
	mc.setBlocks(-9,3,15,9,2,15, orangeWool)
	mc.setBlocks(-10,7,15,10,4,15, orangeWool)
	mc.setBlocks(-9,9,15,9,7,15, orangeWool)
	mc.setBlocks(-8,10,15,8,10,15, orangeWool)
	mc.setBlocks(-5,11,15,5,11,15, orangeWool)
	
	#Stalk
	mc.setBlocks(-1,12,15,1,12,15, greyWool)
	mc.setBlocks(0,13,15,2,13,15, greyWool)
	mc.setBlocks(1,14,15,2,14,15, greyWool)

clear_pumpkin()

#Insert Code Here
def make_pumpkin():
	#eyes
	mc.setBlocks(-3,8,15,-2,7,15, block.AIR)
	mc.setBlocks(2,8,15,3,7,15, block.AIR)
	
	#mouth
	mc.setBlocks(-4,4,15,-4,3,15, block.AIR)
	mc.setBlocks(-4,3,15,-1,3,15, block.AIR)
	mc.setBlocks(-2,2,15,2,2,15, block.AIR)
	mc.setBlocks(1,3,15,4,3,15, block.AIR)
	mc.setBlocks(4,4,15,4,3,15, block.AIR)

make_pumpkin()

