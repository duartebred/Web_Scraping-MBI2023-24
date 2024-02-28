**Exemplo prático da utilização de técnicas de Web Scraping para a adição de informação a bases de dados MYSQL**

Neste repositório apresenta-se a proposta de solução para as fichas-exemplo disponibilizadas pelo Professor Jorge Gustavo Rocha para a aplicação de téncicas de web scrapping com vista a capturar dados da base de dados GenBank com vista à população de tabelas de uma base de dados MySQL com informação básica sobre genes.

Estas fichas utilizam como base os exemplos disponibilizados pelo Professor Jorge Gustavo Rocha no seu [repositório](https://github.com/jgrocha/m8-ferramentas).

Esta implementação visa replicar o código e acrescentar um conjunto de automatismos com vista a criar uma ferramenta de web scrapping mais autónoma. O objetivo passa por ir buscar uma ou mais sequências biológicas online e que depois essas sequências sejam guardadas em base de dados. O resultado será um programa que saca dados do Genbank e guarda os mesmos na base de dados.

Explicação do raciocínio e desafios:

- ir buscar dados de sequências biológicas online ao Genbank. Depois de se sacar os dados do Genbank, onde é que os mesmos são guardados? Em lado nenhum. Os dados são mostrados (com print), mas não são guardados. Podem ser facilmente guardados num documento, mas não estão a ser guardados em base de dados.

- Portanto, pega-se num documento e insere-se os dados do mesmo na base de dados. Os dados são lidos de um documento local. Não são lidos do site Genbank.


A implementação das funções foi desenvolvida por [Duarte Velho](https://github.com/duartebred) (PG53481).
