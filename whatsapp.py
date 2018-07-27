##ZÉ VI: Módulo WhatsApp
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Ze-VI/wiki
##2018

import discord                                                      #Biblioteca para trabalhar com o discord
from WFAPI import *     #Importamos as funções relacionadas ao WFAPI

def whatsapp_qr(driver):
    return gerar_qr(driver)

def whatsapp_whats(driver, destinatario,*mensagem):
    #driver         - Conexão com o Chrome
    #destinatario   - Quem deve receber nossa mensagem
    #*mensagem      - Vetor com as palavras da nossa frase
    
    frase=''                            #Variável pra guardar a frase que vai twitar
    for palavra in mensagem:            #Vamos montar a frase, o discord pega as palavras separadas como argumentos       
        frase=frase+' '+palavra

    enviar_msg(driver,destinatario,frase)
    return 'Mensagem enviada!'

def whatsapp_mensagens(driver,tamanho_max):
    while True:
        try:
            (contatos,mensagens)=novas_msgs(driver,tamanho_max)
            texto=''
            k=0
            for contato in contatos:
                texto=texto+contato+':\n'
                tam=len(mensagens[k])
                for n in range(tam-1,-1,-1):
                    texto=texto+mensagens[k][n]+'\n'
                texto=texto+'\n'
                k=k+1
            if (len(contatos)>0):
                print('O texto é:\n'+texto)
                return texto
            else:
                print('Sem mensagem.')
                return ('Sem novas mensagens.')
        except:
            print('Checando de novo.')


def whatsapp_contato(driver,contato):
    while True:
        try:
            (mensagens)=ult_msgs(driver,contato)
            driver.get("https://web.whatsapp.com")  #Reabrimos a pagina para não ficar em nenhuma conversa aberta

            texto=contato+':\n'
            tam=len(mensagens)
            for n in range(tam-1,-1,-1):
                texto=texto+mensagens[n]+'\n'
                texto=texto+'\n'
            
            if (len(mensagens)>0):
        #        print('O texto é:\n'+texto)
                return texto
            else:
       #         print('Sem mensagem.')
                return ('Sem mensagens não respondidas.')
        except:
            print('Checando de novo.')

print ('Módulo do WhatsApp importado.')