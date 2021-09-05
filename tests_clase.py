import unittest
from romanClass import RomanNumber

class RomanNumberClassTest(unittest.TestCase):
    def test_crear_Numero_romano(self):
        
        uno = RomanNumber(1)
        self.assertEqual(uno.valor, 1)
        self.assertEqual(uno.cadena, 'I')
        
        with self.assertRaises(ValueError):
            cuatromil = RomanNumber(4000)
            
        dos = RomanNumber('II')
        self.assertEqual(dos.valor, 2)
        self.assertEqual(dos.cadena, 'II')
        
        with self.assertRomanNumber(ValueError):
            cuatromil = RomanNumber ('MMM')
        
    def test_metodos_magicos_representacion(self):
        uno = RomanNumber(1)
        dos = RomanNumber(2)
        
        self.assertEqual(uno, "I")
        
    def test_metodos_magicos_comparaciones(self):
        uno = RomanNumber(1)
        dos = RomanNumber(2)
        
        self.assertEqual(uno, 1)
        self.assertEqual(uno, 1.0)
        self.assertEqual(uno, 1.1)
        self.assertEqual(uno, 'I')
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {})
        
        self.assertNotEqual(uno, 2)
        self.assertNotEqual(uno, 1.1)
        self.assertNotEqual(uno, 2.1)
        self.assertNotEqual(uno, 'II')
        with self.assertRaises(ValueError):
            self.assertEqual(uno, {})
            
        self.assertTrue(dos > uno)
        self.assertTrue(dos > 1)
        self.assertTrue(dos > 1.3)
        self.assertFalse(dos > 'DI')
        with self.assertRaises(ValueError):
            dos > {}
        
        self.assertTrue(dos >= uno)
        self.assertTrue(dos >= 1)
        self.assertTrue(dos >= 1.3)
        self.assertFalse(dos >= 'DI')
        with self.assertRaises(ValueError):
            dos > {}
        
        self.assertFalse(dos < uno)
        self.assertFalse(dos < 1)
        self.assertFalse(dos < 1.3)
        self.assertTrue(dos < 'DI')
        with self.assertRaises(ValueError):
            dos > {}
        
        self.assertFalse(dos <= uno)
        self.assertFalse(dos <= 1)
        self.assertFalse(dos <= 1.3)
        self.assertTrue(dos <= 'DI')
        with self.assertRaises(ValueError):
            dos > {}
            
    def metodos_magicos_aritmeticos(self):
        uno = RomanNumber(1)
        
        self.assertEqual(RomanNumber(2), uno + 1)
        
        with self.assertRaises(RomanNumber):
            
            


        