# 🏥 Aplicativo Hospitalar:

<details>
    <summary>Como instalar</summary>

## Instalação de Venv Python e Pacotes com Requirements.txt

**Objetivo:** Este guia visa auxiliar na instalação de um ambiente virtual Python (venv) e na instalação dos pacotes necessários para o seu projeto, utilizando o arquivo requirements.txt.

**Pré-requisitos:**

* Python instalado em seu sistema operacional.
* Arquivo requirements.txt com a lista de pacotes a serem instalados.

**Etapas:**

**1. Criar e ativar o ambiente virtual:**

* Abra um terminal ou prompt de comando e navegue até o diretório raiz do seu projeto.
* Execute o seguinte comando para criar o ambiente virtual:

```
    python3 -m venv ./venv
```
Para ativar basta executar o comando de acordo com o sistema operacional:
- Unix or MacOS: ``source ./venv/Scripts/activate``
- Windows PowerShell: ``./venv/Scripts/Activate.ps1``


**2. Instalar pacotes a partir do requirements.txt:**

Utilize o comando pip para instalar os pacotes listados no requirements.txt:
```
    pip install -r requirements.txt
```

E para executar o programa desenvolvido basta executar:
```
    python ./main.py
```

Recursos adicionais:

- Documentação oficial do venv: https://docs.python.org/3/tutorial/venv.html
- Documentação oficial do pip: https://packaging.python.org/installing/

</details>


<details>
  <summary>Objetivos</summary>

- Deverá possibilitar ao usuário o controle completo (inserção, edição, exclusão e consulta) das entidades: paciente, procedimento e consulta.
- ⁠Considere que para registrar uma consulta, deverá armazenar: paciente, lista de procedimentos realizados e data.
- ⁠Deverá gerenciar os logs da aplicação, relacionados a cada evento realizado.
- ⁠Os dados poderão ser armazenados em algum tipo de arquivo a escolha.
- ⁠Considerem a exclusão de um paciente e/ou procedimento também da consulta relacionado ao(s) mesmo(s).

</details>

<details>
  <summary>Decisões técnicas</summary>

- Foi optado pela utilização de arquivos json para armazenar os dados.
- Para leitura/manipulação do arquivo json está sendo utilizada a biblioteca pandas.
</details>

Integrantes: [Joao Beltrami](https://github.com/jbeltrami), [Marcelo Zaguette Jr.]() e [Murilo Ferris](https://github.com/Murilaom)