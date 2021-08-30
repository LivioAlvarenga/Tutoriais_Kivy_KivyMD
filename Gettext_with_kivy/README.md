# Criando um arquivo python multi language com gettext

# Etapa 1: Colocando a função _() nas strings a serem traduzidas

Adicione a função **_()**

~~~python
print(_('Hello! What is your name?'))
print(_('Well, %s, I am thinking of a number between 1 and 20.') % (myName))
print(_('Good job, %s! You guessed my number in %s guesses!') % (myName, guessesTaken))
~~~

**Obs:** Não consegui fazer funcionar com f string e nem com .format( ). Os códigos abaixo não funcionam:

~~~python
print(_('Well, {}, I am thinking of a number between 1 and 20.').format(myName))

print(_(f'Well, {myName}, I am thinking of a number between 1 and 20.'))
~~~

---

# Etapa 2: pygettext --> gerar arquivo.pot

Extraia as strings usando **pygettext.py**.

O pygettext é um programa que vem no python, normalmente ele fica em:

>_C:\Users\Avell\AppData\Local\Programs\Python\Python39\Tools\i18n\pygettext.py_

pygettext.py sabe como analisar o código-fonte Python, ele encontrará
todas essas strings entre a função _() e produzirá um arquivo "pot".

1. Abra o terminal;
1. Va para pasta raiz de onde esta o arquivo.py que deseja traduzir.
1. Digite o comando abaixo:

python + **path\pygettext.py** + **-d** + **nome_do_arquivo** + **nome_arquivo.py a ser traduzido**

* Exemplo para um único arquivo .py
>python C:\Users\Avell\AppData\Local\Programs\Python\Python39\Tools\i18n\pygettext.py -d base main.py

* Exemplo para vários arquivos .py
>python C:\Users\Avell\AppData\Local\Programs\Python\Python39\Tools\i18n\pygettext.py -d base *.py

* Caso deseje gerar o arquivo em diretório diferente, é so colocar o path mais nome do arquivo, segue exemplo:

>python C:\Users\Avell\AppData\Local\Programs\Python\Python39\Tools\i18n\pygettext.py -d locales\base *.py

Segue exemplo de arquivo.pot:
![arquivo_pot](imagens\arquivo_pot.png)

Para este arquivo geramos .pot de dois arquivos .py main1 e main2

---

# Etapa 3: Estrutura de pastas

Esta deve ser a estrutura de pasta a ser usada:
    
    locales (pasta)
        pt_BR (pasta)
            LC_MESSAGES (pasta)
                pt_BR.mo (gerado pelo Poedit)
                pt_BR.po (gerado pelo Poedit)
        en_US (pasta)
            LC_MESSAGES (pasta)
                en_US.mo (gerado pelo Poedit)
                en_US.po (gerado pelo Poedit)
        base.pot
    main1.py
    main2.py

---

# Etapa 4: Poedit --> gerar arquivos .mo e .po

site download: <https://poedit.net/>

1. Abra Poedit;
1. Selecione Arquivo> Novo do arquivo POT / PO ... e selecione seu arquivo.pot que gerou com pygettext;
1. Informe o idioma de tradução;
1. Preencha as traduções;
1. E agora salve o arquivo em sua pasta formatada para gettext. Salvar criará o arquivo .po (um arquivo de texto legível por humanos idêntico ao arquivo.pot original, exceto com as traduções) e um arquivo.mo (uma versão legível por máquina que o gettext módulo lerá). Esses arquivos devem ser salvos na estrutura de pastas acima para gettext poder encontrá-los.

---

# Etapa 5: Adicione o código gettext ao seu programa

~~~python
import gettext
from os.path import normpath, join, dirname

path = normpath(join(dirname(__file__), 'locales'))

es = gettext.translation ('en_US', localedir=path, languages​​=['en_US'])

es.install()

_ = es.gettext

~~~
O primeiro argumento '**_en_US_**' é o arquivo.mo. O **_localedir_** é o local do diretório da pasta local que você criou. Este pode ser um _caminho relativo ou absoluto_. A '**_en_US_**' string descreve a pasta dentro da pasta local. A pasta LC_MESSAGES é um nome padrão.

O **_install()_** método fará com que todas as **_()** chamadas retornem a string traduzida em inglês. Se você quiser voltar ao português (idioma padrão):

---

# Criando uma função para gettext

~~~python
from gettext import translation
from os.path import normpath, join, dirname


def set_language(lang: str, path: str = 'locales'):
    """Habilita tradução multilanguage para biblioteca gettext (padrão I18N).

    Obs.: lang tem que ser igual a pasta dentro de locales e igual ao arquivo .po, ex:

    lang = en_US path = locales

    locales\\en_US\\LC_MESSAGES\\en_US.mo

    Todo arquivo .mo deve estar contido em pasta LC_MESSAGES!

    Args:
        lang (str): Indica que as traduções serão encontradas em arquivos nomeados lang + ".mo"
        path (str, optional): Path arquivos de tradução. Defaults to 'locales'.

    Returns:
        gettex.translation: Instancia de gettext.translation
    """
    lan_gettext = translation(
        lang,
        localedir=normpath(join(dirname(__file__), path)),
        languages=[lang],
        fallback=True,
    )
    lan_gettext.install()

    return lan_gettext


'''
# !Explicando uso de translation:
    lang = nome do arquivo .mo, ex: en_US.mo
    localedir = diretorio locales
        'c:\\Users\\Avell\\OneDrive\\DEV\\Python_Tutorial\\gettext\\Tutorial_1\\locales'
        Boa pratica usar normpath(join(dirname(__file__), path), sendo path = locales
    languages = nome do diretorio do idioma apos locales. Boa pratica deixar com mesmo do
        arquivo.mo. A def set_language funciona assim.
    fallback = Por padrão, o fallback é False. Se o padrão for usado e uma solicitação for
        feita para usar uma tradução não existente, uma exceção será levantada. Ao usar
        fallback=True, a string não traduzida (como existe no arquivo de origem) é usada
        em seu lugar. Usando pelo menos algumas palavras em MAIÚSCULAS, as mensagens ainda
        podem ser lidas (em inglês), enquanto nos dá uma pista de que uma tradução está
        faltando (da versão em inglês).
'''
~~~

Usando esta função basta colocar nos arquivos .py que geraram o .pot

~~~python
from language import set_language

_ = set_language('en_US').gettext


def print_some_strings():

    print('\n')
    print(_("Oi, este é um tutorial do uso de gettext"))
    print('\n')
    print(_("Vamos traduzir este texto para inglês."))
~~~

---

# Bibliográfia:

* <https://inventwithpython.com/blog/2014/12/20/translate-your-python-3-program-with-the-gettext-module/>
* <https://wiki.python.org.br/TraduzindoSeuPrograma>
* <https://phrase.com/blog/posts/translate-python-gnu-gettext/>
---