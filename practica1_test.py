#! /usr/bin/python 

'''Tests complementarios a practica1.py       '''

'''Para probar nombrar el archivo de practica '''
''' como practica1.py y correr el test con    '''
''' >>>python practica1_test.py                 '''

import unittest
import tempfile
import practica1 as p1

#Test leer_grafo_stdin()
#  En caso de TypeError borrar los mensajes a stdout
#  "raw_input('ingrese algo:')" reescribirlo como
#  "raw_input()" por problemas de testing.
class Test_leer_grafo_stdin(unittest.TestCase):

    test_cases = [
                  ['2', 'A', 'B', 'A B', 'B B']
                  ['3', 'a', 'b', 'c', 'a b', 'b c']
                  ['1', '1', '1 1']
                 ]

    def test(self):
        for test_case in test_cases:
            #Manipulo el caso de testing
            test_verts = test_case[1:int(test_case[0])]
            test_edges = test_case[int(test_case[0])+1, len(test_case)]
            p1.raw_input = lambda : _follow(test_case)
            #Obtengo el resultado de la funcion
            ans = p1.leer_grafo_stdin()
            res_verts = ans[0]
            res_edges = ans[1]            

            #Testeo los tipos del resultado
            self.assertIs(type(ans), type(()))    #Resultado es tupla
            self.assertIs(type(res_verts), type([]))  #Fst elem es lista
            self.assertIs(type(res_edges), type([]))  #Snd elem es lista
            #Testeo los vertices del resultado
            for v in test_verts:
                self.assertIn(v, res_verts)
            #Testeo las aristas del resultado
            for e in test_edges:
                self.assertIn((e[0], e[2]), res_edges)



class Test_lista_a_incidencia(unittest.TestCase):

    test_cases = [
                  (['A','B','C'], [('A','B'),('B','C')])
                  (['A','B','C'], [('A','B')])
                  (['A','B','C','D','E'], [('A','B'),('B','E'),('E','D'),('C','A')])
                 ]

    def test(self):
        for test_case in test_cases:
            #Manipulo el caso de testing
            test_verts = test_case[0]
            test_edges = test_case[1]
            #Obtengo el resultado de la funcion
            ans = p1.lista_a_incidencia(test_case)
            
            #Testeo los tipos del resultado
            self.assertIs(type(ans), type([]))
            self.assertEquals(len(ans), len(test_
