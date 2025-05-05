#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init() # inicializa o pygame
pygame.mixer.init() # inicializa o mixer do pygame
pygame.mixer.music.load('desafios/21.mp3') # carrega o arquivo mp3, no caso não tem arquivo, mas se tivesse o nome do arquivo seria '21.mp3'
pygame.mixer.music.play() # toca o arquivo mp3
pygame.event.wait() # espera o evento de tocar a música acabar