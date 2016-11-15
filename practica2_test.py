#! /usr/bin/python 

'''Tests complementarios a practica2.py       '''

'''Para probar nombrar el archivo de practica '''
''' como practica2.py y correr el test con    '''
''' >>>python practica2_test.py                 '''

import unittest
import tempfile
import practica2 as p2

#Test make_set()
class Test_make_set(unittest.TestCase):

    test_cases = [
                  []
                  []
                  []
                 ]

    def test(self):
        for test_case in test_cases:
            #Obtengo el resultado de la funcion
            ans = p2.make_set(test_case)

            self.assertIs(type(ans), type({}))   #Resultado es dict
            self.assertEquals(len(ans), len(test_case))   #Preserva tamaños 
            for elem in test_case:
                self.assertIn(elem, ans)   #Estan todos en el disjointSet
                #Una key tiene que tener un valor univocamente asosciado
                value = ans[elem]
                for k,v in ans:
                    if v == value:
                        self.assertEquals(elem, k)


#Test find()
class Test_find(unittest.TestCase):

    test_cases = [



                 ]
    
    def test(self):
        for test_case in test_cases:
            #Manipulo el caso de testing
            test_
#TODO


#Test union()
class Test_union(unittest.TestCase):

    test_cases = [



                 ]

    def test(self):
        for test_case in test_cases:
            id_1 = test_case[0]
            id_2 = test_case[1]
            dset = test_case[2]
            #Obtengo el resultado de la funcion
            ans = p2.union(id_1, id_2, dset)

            self.assertIs(type(ans), type({}))   #Resultado es dict
            self.assertTrue(len(ans) < len(dset))   #Achica tamaño
            
