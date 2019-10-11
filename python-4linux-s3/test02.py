from unittest import TestCase, main

def soma(x, y):
    return x + y

class TestSoma(TestCase):
    def test_soma(self):
        self.assertEqual(soma(2,2), 4)
        self.assertNotEqual(soma(4,2), 7)

if __name__=='__main__':
    main()