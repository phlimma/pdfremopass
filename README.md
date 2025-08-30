# pdfremopass
Script para remover recursivamente senhas de PDFs que pedem constantemente por senha para serem abertos.

# Como usar

### 1) Salvar o script em um arquivo, como por exemplo:

`pdfremopass.py`

### 2) Executar no terminal ou clicando duas vezes (dependendo do SO):

`python pdfremopass.py`

### 3) Informar a senha quando solicitado.

# Notas:

A mesma senha será testada em todos os PDFs encontrados.

PDFs sem senha serão ignorados.

Resultados:

* Se a senha estiver correta → será criado um novo PDF no mesmo diretório com _semsenha no nome.

* Se a senha estiver incorreta → o arquivo será ignorado.

Ao final basta pressionar Enter para encerrar o script.
