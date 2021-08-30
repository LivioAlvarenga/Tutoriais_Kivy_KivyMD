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
