# Faça um programa em Python que abra e reproduza o áudio de um arquivo M

from pygame import mixer

mixer.init()
mixer.music.load('desafio 21.mp3')
mixer.music.play()
input('Será que vai?')

# VERSÃO DA AULA ESTAVA DESATUALIZADA.
