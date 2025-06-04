import pyautogui
import time

# pyautogui.click -> clicar em algo
# pyautogui.press -> apertar a tecla
# pyautogui.write -> escrever um texto

pyautogui.PAUSE = 0.5

#Passo1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

#Passo2: Fazer login
pyautogui.click(x=475, y=375)
# Para saber onde o mouse está basta usar o comando 'time.sleep(5)' e 'print(pyautogui.position())' e olhar no terminal.
pyautogui.write("programadorsenior@gmail.com")
# Preencher a senha
pyautogui.press("tab")
pyautogui.write("minhasenha")
# Apertar botão de logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

#Passo3: Importar a base de dados.
import pandas
tabela=pandas.read_csv("produtos.csv")
# Criar uma variável. Nesse caso é 'tabela'.
print(tabela)

#Passo4: Cadastrar um produto.
for linha in tabela.index: 
    pyautogui.click(x=497, y=258)
    time.sleep(3)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) #string=texto -> str()
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preço_unitario = str(tabela.loc[linha, "preço_unitario"])
    pyautogui.write(preço_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)

    if obs != "nan": #'!=' significa diferente
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

#Passo5: Repetir para os outros produtos.

