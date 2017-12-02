"""
Тест для проверки взаимообратности действия алгоритма

"""


def test_vice_versa(ROT13):
	if (ROT13(ROT13('pythonist wannabe')) == 'pythonist wannabe'):  
		return 1
	else:
		return 0

