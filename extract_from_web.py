import os
import wget

# https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp
url_serie = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-"
file_extension = ".csv"
download_folder = "downloads/series"

# Lista o nome dos arquivos da base: Série Histórica de Preços de Combustíveis e de GLP
file_names = [
    "2004-01", "2004-02", "2005-01", "2005-02", "2006-01", "2006-02", "2007-01", "2007-02", "2008-01", "2008-02",
    "2009-01", "2009-02", "2010-01", "2010-02", "2011-01", "2011-02", "2012-01", "2012-02", "2013-01", "2013-02",
    "2014-01", "2014-02", "2015-01", "2015-02", "2016-01", "2016-02", "2017-01", "2017-02", "2018-01", "2018-02",
    "2019-01", "2019-02", "2020-01", "2020-02", "2021-01", "2021-02", "2022-01", "2022-02"
]

# Verifica se a pasta de downloads existe, caso contrário, cria-a
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# For each arquivos da base histórica de Preços
for name in file_names:
    url = url_serie + name + file_extension
    filename = os.path.join(download_folder, name + file_extension)

    try:
        wget.download(url, filename)
        print("Download concluído:", filename)
    except Exception as e:
        print("Ocorreu um erro ao tentar baixar o arquivo:", filename)
        print(e)

# ------------------------------------------------------------------------------------------------------------------- #

# Tenta baixar o arquivo da base de exportação
url_imp_exp = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/ie/petroleo/importacoes-exportacoes-petroleo-2000-2022.csv"
alias = "imp_and_exp_petroleo"

try:
    wget.download(url_imp_exp)
    print("Download concluído:", alias)
except Exception as e:
    print("Ocorreu um erro ao tentar baixar o arquivo:", alias)
    print(e)

# ------------------------------------------------------------------------------------------------------------------- #

# Produção por Poços
url_serie = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-producao-de-petroleo-e-gas-natural-por-poco/producao-por-poco-"
file_extension = ".zip"
download_folder = "downloads"

# Lista o nome dos arquivos da base: Série Histórica de Preços de Combustíveis e de GLP
file_names = [
    "2005"
]

# For each arquivos da base histórica de Preços
for name in file_names:
    url = url_serie + name + file_extension
    filename = os.path.join(download_folder, name + file_extension)

    try:
        wget.download(url, filename)
        print("Download concluído:", filename)
    except Exception as e:
        print("Ocorreu um erro ao tentar baixar o arquivo:", filename)
        print(e)
