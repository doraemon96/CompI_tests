#! /usr/bin/python 

'''Tests complementarios a practica2.py       '''

'''Para probar nombrar el archivo de practica '''
''' como practica2.py y correr el test con    '''
''' >>>python practica2_test.py               '''

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
            if (id_1 in test_case.values()) and (id_2 in test_case.values()):
                self.assertTrue(len(ans) < len(test_case))   #Une al menos dos conjuntos
#TODO
            


#Test componentes_conexas()
class Test_componentes_conexas(unittest.TestCase):

    test_cases = [
    
    
    
                 ]

    def test(self):
        for test_case in test_cases:
            #Obtengo el resultado de la funcion
            ans = p2.componentes_conexas(test_case)

            #Testeo los tipos del resultado
            self.assertIs(type(ans), type([]))   #Resultado es list
            for e in ans:
                self.assertIs(type(e), type([]))   #Componentes son list
#TODO
