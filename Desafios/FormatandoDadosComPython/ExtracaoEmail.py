entrada = input()

def extrair_dominios(emails):
    lista_emails = emails.split(';')
    dominios = [email.split('@')[1] for email in lista_emails]
    return dominios

print(extrair_dominios(entrada))