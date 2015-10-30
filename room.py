import mcpi.block as block

class Room(object):
	def draw_room(self, mc):
		#clear the area
		mc.setBlocks(-20,0,-20,20,64,20,block.AIR)
		
		#walls
		mc.setBlocks(-20,0,-20,-20,20,20,block.BRICK_BLOCK)
		mc.setBlocks(-20,0,20,20,20,20,block.BRICK_BLOCK)
		mc.setBlocks(20,0,20,20,20,-20,block.BRICK_BLOCK)
		mc.setBlocks(20,0,-20,-20,20,-20,block.BRICK_BLOCK)
		
		#floor
		mc.setBlocks(-20,-1,-20,20,-1,20,block.BRICK_BLOCK)
		
		#ceiling
		mc.setBlocks(-20,20,-20,20,20,20,block.BRICK_BLOCK)

	def set_lighting(self, mc):
		mc.setBlocks(-10, 0, 12, 10, 0, 12, block.TORCH)
		mc.setBlocks(-11, 0, 12, -11, 19, 12, block.BRICK_BLOCK)
		mc.setBlocks(-10, 1, 12, -10, 19, 12, block.TORCH)
		mc.setBlocks(11, 0, 12, 11, 19, 12, block.BRICK_BLOCK)
		mc.setBlocks(10, 1, 12, 10, 19, 12, block.TORCH)
	
		mc.setBlocks(-10, 13, 12, 10, 13, 12, block.BRICK_BLOCK)
		mc.setBlocks(-10, 13, 13, 10, 13, 13, block.TORCH)
	
		mc.setBlock(-10, 0, -10, block.TORCH)
		mc.setBlock(10, 0, -10, block.TORCH)