from gamelib import *
game = Game(800,600,"Survival")

sand=Image("images/sand.jpg",game)
sand.resizeTo(game.width,game.height)
scorpion=Animation("images/scorpion.jpg",3,game,288/3,106/1,5)
bottle=Animation("images/bottle.png",24,game,230/5,516/5)
human=Animation("images/human.png",15,game,440/5,294/3)
snake=Animation("images/snake.png",48,game,960/5,1080/10)
human.y +=220
game.setBackground(sand)              
while not game.over:
  game.processInput()
  game.scrollBackground("down",4)

  human.draw()
  scorpion.move()
  bottle.move()
  snake.move()
  if(keys.Pressed[K_a]):
    human.x -= 4
    human.rotateTo(20)
  if(keys.Pressed[K_d]):
    human.x += 4
    human.rotateTo(-20)


  
  game.update(30)
game.quit()
