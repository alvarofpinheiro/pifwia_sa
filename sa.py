# -*- coding: utf-8 -*-
"""sa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MeaFytbeIw7YE2Hz0EPOmJD0GFOQbsPM
"""

#SA
import random
import math
import matplotlib.pyplot as plt
import numpy as np

TEMPERATURA_MAXIMA = 500.0
TEMPERATURA_MINIMA = 0.01

cidades = cidades_inicial_usando_referencia()

def executar_simulated_annealing():

  # É gerada uma solução inicial aleatoria
  solucao_atual = gerar_solucao_aleatoria()

  # É calculado o fitness da solução incial
  fitness_atual = fitness(solucao_atual)

  # É definido um criterio de parada
  temperatura = TEMPERATURA_MAXIMA

  # print('Fitness Inicial: ', "%.3f" % fitness_atual)

  # --- Função para demonstração visual utilizando matplotlib ---
  # gerar_grafico(cidades, solucao_atual)

  # --- Inicio da execução do algoritimo ---

  # Criterio de parada 
  while temperatura > TEMPERATURA_MINIMA:

    # Uma nova solução é gerada
    nova_solucao = mudar_solucao(solucao_atual)

    # A nova solução é comparada com a anterior
    if fitness(nova_solucao) < fitness(solucao_atual):

      # Caso ela seja melhor a anterior é substituida pela nova
      solucao_atual.clear()
      for j in range(0, NUMERO_DE_CIDADES):
        solucao_atual.append(nova_solucao[j])
      # e o melhor fitness é atualizado
      fitness_atual = fitness(solucao_atual)
    
    # Mesmo que o novo local seja pior que o anterior existe uma chance que o 
    # algoritmo va a ele, isso é feito para aumentar a exploração e evitar 
    # otimos locais
    elif np.exp(((fitness(solucao_atual) - fitness(nova_solucao))/temperatura)) > random.random():
      solucao_atual.clear()
      for j in range(0, NUMERO_DE_CIDADES):
        solucao_atual.append(nova_solucao[j])
      # o fitness é atualizado
      fitness_atual = fitness(solucao_atual)
  
    temperatura -= TEMPERATURA_MINIMA

  # --- Função para demonstração visual utilizando matplotlib ---
  # gerar_grafico(cidades, solucao_atual)

  return fitness_atual