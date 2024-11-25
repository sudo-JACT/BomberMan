import player
from game.BomberManGame import *
from unittest import TestCase, main
from unittest.mock import MagicMock, Mock


class TestBomberManMovement(TestCase):

    def setUp(self):
        
        #Prepara l'ambiente per i test
        self.arena = Mock()
        self.arena.size.return_value = (256, 256)
        self.arena.getF.return_value = False
        self.b = player.BomberMan.BomberMan((16, 50), "./imgs/bomberman.png", ["ArrowUp", "ArrowDown", "ArrowLeft", "ArrowRight", "b"], (255, 224), self.arena, 3)
       
    def test_initial_position(self):
        
        # Testa che la posizione iniziale del BomberMan sia corretta
        self.assertEqual(self.b.pos(), (16, 50))

    def test_movimenti(self):

        w,h= self.arena.size()
        self.arena.collisions.return_value = []
        self.arena.previous_keys.return_value = []
        self.arena.current_keys.return_value = ["ArrowUp"]
        self.b.move(self.arena)
    
        self.assertEqual(self.b.pos(), (16, 48))
        
        
        self.arena.collisions.return_value = []
        self.arena.previous_keys.return_value = []
        self.arena.current_keys.return_value = ["ArrowDown"]
        self.b.move(self.arena)
        
        self.assertEqual(self.b.pos(), (16, 50))
        
        
        self.arena.collisions.return_value = []
        self.arena.previous_keys.return_value = []
        self.arena.current_keys.return_value = ["ArrowLeft"]
        self.b.move(self.arena)
        
        self.assertEqual(self.b.pos(), (14, 50))
        
        
        self.arena.collisions.return_value = []
        self.arena.previous_keys.return_value = []
        self.arena.current_keys.return_value = ["ArrowRight"]
        self.b.move(self.arena)
        
        self.assertEqual(self.b.pos(), (16, 50))
        
        

    def m(self):
        
        main()

if __name__ == '__main__':
    main()