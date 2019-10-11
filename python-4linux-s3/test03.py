from unittest import TestCase, main

def eh_impar(num):
    try:
        if int(num) % 2 != 0:
            return True
        else:
            return False
    except Exception:
        return None

class Impar(TestCase):
    def test_impar(self):
        self.assertEqual(eh_impar(3), True)
        self.assertEqual(eh_impar(172937), True)
        self.assertEqual(eh_impar(24216), False)
        self.assertEqual(eh_impar('273923'), True)
        self.assertEqual(eh_impar('181282'), False)
        self.assertEqual(eh_impar('sohuhjbweol'), None)

if __name__=='__main__':
    main()