---
id: 17-leasing-and-real-estate/script-de-dados-mestre-criar-objeto-de-locacao-mds-7ad-524
title: Script de dados mestre - Criar objeto de locação (MDS 7AD) (7AD_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (7AD) for SAP S/4HANA Cloud Public Edition 2608: creating generic lease objects (usable/rentable, intercompany), prerequisites and test steps."
cluster: 17-leasing-and-real-estate
tags: [kb/leasing-and-real-estate, topic/real-estate-contracts-and-leasing]
aliases: [7AD_S4CLD2608_Master_Data_PT_XX]
keywords: [Real Estate Rental Objects and Lease Accounting, generic lease objects, usable objects, rentable objects, intercompany leasing, usage categories, usage types, number ranges, measurements, real estate architecture objects]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-524
topic: 17-leasing-and-real-estate/real-estate-contracts-and-leasing
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar objeto de locação (MDS 7AD) (7AD_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Real Estate Rental Objects and Lease Accounting** in Leasing and Real Estate. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar objeto de locação – MDS (7AD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233893875)

[2 Pré-requisitos 4](#_Toc233893876)

[2.1 Acesso ao sistema 4](#_Toc233893877)

[2.2 Funções 4](#_Toc233893878)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893879)

[2.4 Dados mestre obrigatórios e opcionais 5](#_Toc233893880)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233893881)

[2.5.1 Categoria de utilização 5](#_Toc233893882)

[2.5.2 Tipos de utilização e intervalos de numeração 6](#_Toc233893883)

[2.5.3 ID de propriedade 7](#_Toc233893884)

[2.5.4 ID do portfólio 7](#_Toc233893885)

[2.5.5 Medições 8](#_Toc233893886)

[2.5.6 Tipo de objeto arquitetônico do bem imóvel e intervalo de numeração 9](#_Toc233893887)

[2.5.7 Hierarquia de objetos arquitetônicos do bem imóvel 9](#_Toc233893888)

[2.6 Etapas preliminares 9](#_Toc233893889)

[2.6.1 Validar disponibilidade do serviço MDI 9](#_Toc233893890)

[3 Tabela de síntese 10](#_Toc233893891)

[4 Procedimento de teste 11](#_Toc233893892)

[4.1 Criar objeto utilizável sem estrutura de portfólio 11](#_Toc233893893)

[4.2 Criar objeto utilizável com estrutura de portfólio 12](#_Toc233893894)

[4.3 Criar objeto locável sem estrutura de portfólio 14](#_Toc233893895)

[4.4 Alterar objeto locável com estrutura de portfólio 15](#_Toc233893896)

[4.5 Criar objeto locável interempresarial com estrutura de portfólio 15](#_Toc233893897)

[4.6 Criar objeto locável interempresarial sem estrutura de portfólio 17](#_Toc233893898)

[4.7 Criar objeto utilizável interempresarial com estrutura de portfólio 18](#_Toc233893899)

[4.8 Criar objeto utilizável interempresarial sem estrutura de portfólio 19](#_Toc233893900)

## Objetivo

Um objeto de locação genérico pode ser um objeto utilizável ou locável.

Um objeto utilizável é um objeto alugado ou de propriedade de uma empresa e define o escopo para utilização própria ou contrato de locação externo ou interempresarial. O objeto utilizável pode estar sujeito a um contrato de aluguel de bens imóveis. A empresa atua de uma perspectiva do cliente.

Um objeto locável é um objeto que pode ser alugado por uma empresa a um locatário externo ou empresa afiliada. O objeto locável pode estar sujeito a um contrato de locação de bens imóveis. A empresa atua do ponto de vista do fornecedor.

Os objetos de locação genéricos são utilizados nos diferentes cenários da seguinte forma:

a) Objetos alugados externos ou próprios

Você define objetos alugados externos ou próprios como objetos utilizáveis. Para isso, você pode utilizar a categoria de utilização Objeto utilizável com estrutura de carteira (UP) ou Objeto utilizável sem estrutura de carteira (UW). Os objetos utilizáveis são necessários para todos os processos subsequentes.

b) Objetos de contrato de locação externos

Os objetos de contrato de locação externos são definidos como objetos locáveis Para isso, você pode utilizar a categoria de utilização Objeto de locação com estrutura de carteira (RP) ou Objeto de locação sem estrutura de carteira (RW). Cada objeto locável precisa de uma relação com um objeto utilizável. Por isso, você precisa primeiro criar um objeto utilizável (consulte a)).

c) Objetos de locação interempresariais

Para configurar um processo de locação interempresarial, os seguintes objetos são necessários:

1. Objeto utilizável (alugado externo ou próprio) (consulte a))
2. Objeto locável interempresarial (categoria de utilização Objeto locável interempresarial com estrutura de carteira (I3) ou Objeto locável interempresarial sem estrutura de carteira (I4)) relacionado a um objeto utilizável (consulte 1.) dentro da empresa locadora
3. Objeto utilizável interempresarial (categoria de utilização Objeto utilizável interempresarial com estrutura de carteira (I1) ou Objeto utilizável interempresarial sem estrutura de carteira (I2)) na empresa locatária relacionado a um objeto locável interempresarial dentro da empresa locadora (consulte 2.)

Em seguida, você pode continuar com 2. e 3. para configurar um processo de locação interempresarial adicional para uma terceira empresa ou com b) para criar um objeto de contrato de locação externo. O objeto locável interempresarial adicional ou o objeto locável externo, nesse caso, tem uma relação com o objeto utilizável interempresarial.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Responsável de bens imóveis - administração de localizações | SAP_BR_RE_SPECIALIST_LOCAT | Gerenciamento de locais de atividade | SAP_FIN_SPT_RE_LOCATION_PC |  |
| Especialista de contrato - leasing | SAP_BR_RECM_SPECIALIST | Gestão de contratos de leasing / Gerenciamento de contratos de leasing - Aluguel baseado no faturamento | SAP_BR_RECM_SPECIALIST / SAP_BR_RECM_SALES_REPORTER |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura da sua empresa. Os dados mestre representam objetos utilizáveis, dependendo do foco operacional da sua empresa.

| Objeto de dados | Usado em segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Empresa | Dados gerais | Obrigatório |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de objetos utilizáveis e locáveis podem fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um registro de dados utilizável/locável.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de custo | Objeto da classificação contábil | Obrigatório | Centro de custo ou elemento PEP |
| Elemento PEP | Objeto da classificação contábil | Obrigatório | Centro de custo ou elemento PEP |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um objeto de locação genérico.

#### Categoria de utilização

As categorias de utilização determinam o tipo e o comportamento empresarial de um objeto de locação genérico. As seguintes categorias de utilização são suportadas:

1. Objeto utilizável com estrutura de portfólio (UP) – Esses objetos utilizáveis requerem a utilização do serviço Master Data Integration no BTP (MDI) para estabelecer a relação com objetos de arquitetura de bens imóveis fornecidos por uma aplicação externa.
2. Objeto utilizável sem estrutura de portfólio (UW) – para esses objetos utilizáveis, não é possível uma relação com objetos de arquitetura de bens imóveis.
3. Objeto locável com estrutura de portfólio (RP) – Esses objetos locáveis requerem a utilização do serviço Master Data Integration no BTP (MDI) para estabelecer a relação com objetos de arquitetura de bens imóveis fornecidos por uma aplicação externa.
4. Objeto locável sem estrutura de portfólio (RW) – Para esses objetos locáveis, não é possível uma relação com objetos de arquitetura de bens imóveis.
5. Objeto locável interempresarial com estrutura de portfólio (I3) – Esses objetos locáveis são utilizados em um cenário de locação interempresarial e requerem a utilização do serviço Master Data Integration no BTP (MDI) para estabelecer a relação com objetos de arquitetura de bens imóveis fornecidos por uma aplicação externa.
6. Objeto locável interempresarial sem estrutura de portfólio (I4) – Esses objetos locáveis são usados em um cenário de locação interempresarial sem uma relação com objetos de arquitetura de bens imóveis.
7. Objeto utilizável interempresarial com estrutura de portfólio (I1) – Esses objetos utilizáveis são usados em um cenário de contrato de aluguel interempresarial e requerem uma relação com um objeto locável da categoria de utilização Objeto locável interempresarial com estrutura de portfólio (I3).
8. Objeto utilizável interempresarial sem estrutura de portfólio (I2) – Esses objetos utilizáveis são usados em um cenário de contrato de aluguel interempresarial e requerem uma relação com um objeto locável da categoria de utilização Objeto locável interempresarial sem estrutura de portfólio (I4).

#### Tipos de utilização e intervalos de numeração

Para cada categoria de utilização, podem ser definidos diferentes tipos de utilização para diferenciar os objetos e o respectivo comportamento empresarial dentro da categoria. Os tipos de utilização determinam os intervalos de numeração para os IDs do registro mestre do objeto. Você não pode alterar posteriormente a atribuição ou os IDs. Se um tipo de utilização estiver atribuído a um intervalo de numeração interno, você não pode inserir o ID do registro mestre manualmente. Neste caso, deixe o campo em branco, uma vez que o sistema seleciona automaticamente um número do intervalo de numeração numérico atribuído.

Os seguintes tipos de utilização e intervalos de numeração correspondentes estão predefinidos:

| Tipo de utilização | Categoria de utilização | Intervalo de numeração | Comentários |
| --- | --- | --- | --- |
| DP/hardware (SU01) | Objeto utilizável sem estrutura de portfólio (UW) | 010000000 – 019999999 |  |
| Instalações e equipamentos (SU02) | Objeto utilizável sem estrutura de portfólio (UW) | 020000000 – 029999999 |  |
| Máquinas (SU03) | Objeto utilizável sem estrutura de portfólio (UW) | 030000000 – 039999999 |  |
| Veículos (SU04) | Objeto utilizável sem estrutura de portfólio (UW) | 040000000 – 049999999 |  |
| Equipamento de escritório (SU05) | Objeto utilizável sem estrutura de portfólio (UW) | 050000000 – 059999999 |  |
| Edifício de escritórios (SU06) | Objeto utilizável com estrutura de portfólio (UP) | 060000000 – 069999999 | Somente objetivo de demonstração |
| Varejo (SU07) | Objeto utilizável com estrutura de portfólio (UP) | 070000000 – 079999999 | Somente objetivo de demonstração |
| Residencial (SU08) | Objeto utilizável com estrutura de portfólio (UP) | 080000000 – 089999999 | Somente objetivo de demonstração |
| Escritório (SR01) | Objeto locável com estrutura de portfólio (RP) | 1000000000 – 1099999999 | Somente objetivo de demonstração |
| Loja (SR02) | Objeto locável com estrutura de portfólio (RP) | 1100000000 – 1199999999 | Somente objetivo de demonstração |
| Apartamento (SR03) | Objeto locável com estrutura de portfólio (RP) | 1200000000 – 1299999999 | Somente objetivo de demonstração |
| Veículos (SR04) | Objeto locável sem estrutura de portfólio (RW) | 1300000000 – 1399999999 | Somente objetivo de demonstração |
| LO escritório ICO (SRI1) | Objeto locável interempresarial com estrutura de portfólio (I3) | 3100000000 – 3199999999 | Somente objetivo de demonstração |
| LI escritório ICO (SUI1) | Objeto utilizável interempresarial com estrutura de portfólio (I1) | 3000000000 – 3099999999 | Somente objetivo de demonstração |
| LO Instalações e equipamentos ICO (SRI2) | Objeto locável interempresarial sem estrutura de portfólio (I4) | 6100000000 – 6199999999 | Somente objetivo de demonstração |
| LI Instalações e equipamentos ICO (SUI2) | Objeto utilizável interempresarial sem estrutura de portfólio (I2) | 6000000000 – 6099999999 | Somente objetivo de demonstração |

Para configurar intervalos de numeração e tipos de utilização, use as seguintes SSCUIs:

- Definir intervalos de numeração para objetos de locação genéricos (ID: 106591)
- Definir tipos de utilização para objetos de locação genéricos (ID: 106592)

#### ID de propriedade

Os objetos utilizáveis podem estar sujeitos a diferentes controles legais. O tipo de controle legal deve ser atualizado usando o atributo ID de propriedade. Os valores da característica do ID de propriedade podem ser definidos na configuração.

Os seguintes IDs de propriedade estão predefinidos:

- Contrato de aluguel (S001)
- Propriedade (S002)

Para configurar IDs de propriedade, use SSCUI: Definir IDs de propriedade para objetos utilizáveis (ID: 106593).

#### ID do portfólio

Os objetos utilizáveis do tipo de utilização 'Objeto utilizável sem estrutura de portfólio (UW)' podem ser agrupados por um ID de portfólio. Os valores da característica do ID do portfólio podem ser definidos na configuração.

Os seguintes IDs de portfólio para subagrupamento de equipamento de escritório e veículos estão predefinidos para fins de demonstração:

- Automóvel a diesel (S401)
- Automóvel a gasolina (S402)
- Automóvel elétrico (S403)
- Eletrodomésticos de escritório (S501)
- Móveis de escritório (S502)
- Soluções de montagem (S503)

Para configurar IDs de portfólio, use a SSCUI: Definir IDs de portfólio para objetos utilizáveis (ID: 106594).

#### Medições

Objetos utilizáveis e/ou locáveis podem ter medições. Com base nessas medições, os montantes da condição podem ser calculados em contratos. As medições de diferentes tipos podem ser somadas até uma medição total.

Os seguintes tipos de medição estão predefinidos para fins de demonstração:

| Tipo de medição | Unidade padrão | Medição da área | Medição total | Comentários |
| --- | --- | --- | --- | --- |
| Área do escritório (SG11) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Área de reunião (SG13) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Despensa (SF04) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Banheiro (SD01) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Sala técnica (SC04) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Elevador (SA02) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Corredor (SE01) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Loja (SG22) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Espaço habitacional (SG41) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Hall de entrada (SE02) | Metro quadrado (M2) | X |  | Totalizado para área utilizável (ST99) |
| Vaga de estacionamento (SK01) | Metro quadrado (M2) | X |  |  |
| Área utilizável (ST99) | Metro quadrado (M2) | X | X |  |

Para configurar tipos de medição e medições totais, use as seguintes SSCUIs:

- Definir tipos de medição (ID: 105394)
- • Definir medições totais (ID: 105395)

#### Tipo de objeto arquitetônico do bem imóvel e intervalo de numeração

Os objetos de locação genéricos da categoria de utilização 'Objeto utilizável com estrutura de portfólio (UP)' ou 'Objeto locável com estrutura de portfólio (RP)' se referem a objetos arquitetônicos do bem imóvel fornecidos por uma aplicação externa por meio do serviço de integração de dados mestre no BTP (MDI). Para fins de sincronização, devem ser configurados tipos de objeto arquitetônico do bem imóvel. O tipo de objeto arquitetônico do bem imóvel determina a categoria do objeto arquitetônico e o intervalo de numeração usado no sistema.

Os seguintes tipos de objeto arquitetônico do bem imóvel e intervalos de numeração correspondentes estão predefinidos para fins de demonstração:

| Tipos de objeto arquitetônico | Categoria de objetos arquitetônicos | Intervalos de numeração | Comentários |
| --- | --- | --- | --- |
| Local (S1SI) | Local (1) | 10000000 – 19999999 |  |
| Edifício (S2BU) | Edifício (2) | 20000000 – 29999999 |  |
| Terreno (S2LA) | Terreno (3) | 30000000 – 39999999 |  |
| Andar (S3FL) | Outros (99) | 40000000 – 49999999 |  |
| Sala (S4RO) | Outros (99) | 50000000 – 59999999 |  |

Para configurar intervalos de numeração e tipos de objeto arquitetônico do bem imóvel, use as seguintes SSCUIs:

- Definir intervalo de numeração para objeto arquitetônico (ID: 106628)
- Definir tipo de objeto arquitetônico (ID: 106629)

#### Hierarquia de objetos arquitetônicos do bem imóvel

Com base nos tipos de objeto arquitetônico, uma hierarquia pode ser definida. Esta hierarquia é usada no sistema de relatórios.

Para configurar uma hierarquia de tipos de objeto arquitetônico, use a SSCUI: Definir tipos de objeto arquitetônico superior permitido (ID: 106630).

### Etapas preliminares

#### Validar disponibilidade do serviço MDI

Se você quiser criar objetos utilizáveis/locáveis com estrutura de portfólio (categoria de utilização UP e RP), será necessária uma conexão com uma aplicação externa que forneça objetos arquitetônicos de bens imóveis por meio do serviço de integração de dados mestre no BTP (MDI).

Para instruções de configuração e pré-requisitos, consulte o item de escopo 77V – Integração de dados mestre para administração de contratos e locações.

## Tabela de síntese

Este item de escopo consiste em vários processos, indicados nas tabelas a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Diagrama de processo | Funções empresariais | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar objeto utilizável sem estrutura de portfólio](#unique_17) [página ] 11 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objetos utilizáveis |  |
| [Criar objeto utilizável com estrutura de portfólio](#unique_18) [página ] 12 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objetos utilizáveis |  |
| [Criar objeto locável sem estrutura de portfólio](#unique_19) [página ] 14 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objeto locável |  |
| [Alterar objeto locável com estrutura de portfólio](#unique_20) [página ] 15 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objeto locável |  |
| [Criar objeto locável interempresarial com estrutura de portfólio](#unique_21) [página ] 15 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objeto locável |  |
| [Criar objeto locável interempresarial sem estrutura de portfólio](#unique_22) [página ] 17 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objeto locável |  |
| [Criar objeto utilizável interempresarial com estrutura de portfólio](#unique_23) [página ] 18 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objetos utilizáveis |  |
| [Criar objeto utilizável interempresarial sem estrutura de portfólio](#unique_24) [página ] 19 | Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações | Administrar objetos utilizáveis |  |

## Procedimento de teste

### Criar objeto utilizável sem estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objetos utilizáveis | Abra Administrar objetos utilizáveis. | A tela Administrar objetos utilizáveis é exibida. |  |
| 3 | Criar objetos utilizáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto utilizável: <seu nome de objeto>Categoria de utilização: Objeto utilizável sem estrutura de portfólio (UW)Tipo de utilização de objeto utilizável: <selecione um tipo de utilização, por exemplo, Veículos (SU04)>Empresa: <selecione uma empresa, por exemplo, Empresa (1010) >Objeto utilizável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:ID de portfólio (opcional): <selecione um ID de portfólio, por exemplo, Carro a diesel (S401)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>ID de propriedade: <selecione um ID de propriedade, por exemplo, Locação (S001)>Início da validade: <data a partir da qual seu objeto é válido, por exemplo, a data atual>Fim da validade: <data até a qual o seu objeto é válido>Na seção Objeto de classificação contábil principal, selecione Criar e efetue as seguintes entradas:Tipo de objeto do objeto atribuído: <selecione um tipo de objeto, por exemplo, Centro de custo (KS)>Objeto de classificação contábil: <seu objeto de classificação contábil>Nota Um objeto de classificação contábil principal deve ser atribuído para toda a validade do objeto. O objeto de classificação contábil pode ser alterado durante a validade do objeto. No entanto, não podem ocorrer sobreposições ou lacunas. Os objetos utilizáveis que pertencem ao mesmo ID de portfólio podem usar os mesmos objetos de classificação contábil principal ou diferentes. Um objeto de classificação contábil principal usado para um ID de portfólio não pode ser usado como objeto de classificação contábil principal em outro ID de portfólio.Clique em Aplicar.Opcional:Para a seção Medição, clique em Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Criar. | O objeto utilizável é criado. |  |

### Criar objeto utilizável com estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objetos utilizáveis | Abra Administrar objetos utilizáveis. | A tela Administrar objetos utilizáveis é exibida. |  |
| 3 | Criar objetos utilizáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto utilizável: <seu nome de objeto>Categoria de utilização: Objeto utilizável com estrutura de portfólio (UP)Tipo de utilização de objeto utilizável: <selecione um tipo de utilização, por exemplo, Edifício de escritórios (SU06)>Empresa: <selecione uma empresa, por exemplo, Empresa (1010) >Objeto utilizável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:Nº de objeto de edifício/terreno: <selecione o objeto de arquitetura (edifício/terreno) ao qual o objeto utilizável se refere (objeto superior)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>ID de propriedade: <selecione um ID de propriedade, por exemplo, Locação (S001)>Início da validade: <data a partir da qual seu objeto é válido, por exemplo, a data atual>Fim da validade: <data até a qual o seu objeto é válido>Na seção Objeto de classificação contábil principal, selecione Criar e efetue as seguintes entradas:Tipo de objeto do objeto atribuído: <selecione um tipo de objeto, por exemplo, Centro de custo (KS)>Objeto de classificação contábil: <seu objeto de classificação contábil>Nota Um objeto de classificação contábil principal deve ser atribuído para toda a validade do objeto. O objeto de classificação contábil pode ser alterado durante a validade do objeto. No entanto, não podem ocorrer sobreposições ou lacunas. Os objetos utilizáveis que pertencem ao mesmo edifício ou terreno podem usar os mesmos ou diferentes objetos de classificação contábil principais. Um objeto de classificação contábil principal usado para um edifício ou terreno não pode ser usado como o objeto de classificação contábil principal em outro edifício ou terreno.Clique em Aplicar.Na seção Utilização obj.arquitetônico, selecione Criar e efetue as seguintes entradas.Nota Objetos requerem o uso do serviço Master Data Integration no BTP (MDI) para estabelecer a relação com objetos arquitetônicos de bens imóveis fornecidos por uma aplicação externa.Tipo de objeto arquitetônico: <selecione o tipo de objeto de arquitetura, por exemplo, Edifício (S2BU)>Número de objeto arquitetônico: <selecione o objeto arquitetônico representado pelo objeto utilizável>Nota Você pode agrupar vários objetos arquitetônicos de bens imóveis em um objeto utilizável.Opcional:Na seção Status do sistema, selecione Bloquear para configuração interempresarial se você quiser evitar que os objetos locáveis (RP) sincronizados a partir de uma solução de administração de bens imóveis de terceiros sejam atribuídos automaticamente a objetos utilizáveis, desde que a configuração interempresarial não esteja concluída.Seu objeto utilizável tem o status Somente locação interempresarial, o que impede uma locação externa.Selecione Desbloquear para configuração interempresarial depois de ter concluído a configuração interempresarial.Para a seção Medição, clique em Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Criar. | O objeto utilizável é criado. |  |

### Criar objeto locável sem estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objeto locável | Abra Administrar objeto locável. | A tela Administrar objetos locáveis é exibida. |  |
| 3 | Criar objetos locáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto locável: <seu nome de objeto>Categoria de utilização: Objeto locável sem estrutura de portfólio (RW)Tipo de utilização do objeto locável: <selecione um tipo de utilização, por exemplo, Veículos (SR04)>Empresa: <selecione uma empresa, por exemplo, Empresa (1010) >Objeto locável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:Categoria de objeto locável: <selecione uma categoria de objeto locável, por exemplo, Externo (E)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Início da validade: <data a partir da qual seu objeto é válido, por exemplo, a data atual>Fim da validade: <data até a qual o seu objeto é válido>Na seção Atribuição de objeto utilizável, selecione Criar e efetue as seguintes entradas.Objeto utilizável: <atribua o objeto utilizável ao qual o objeto locável se refere>Clique em Aplicar.Opcional:Para a seção Medição, clique em Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Criar. | O objeto locável é criado. |  |

### Alterar objeto locável com estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objeto locável | Abra Administrar objeto locável. | A tela Administrar objetos locáveis é exibida. |  |
| 3 | Alterar objetos locáveis | Procure o objeto locável com o ID do objeto.Selecione o objeto locável. Clique em Editar e efetue as entradas a seguir.Na seção Informações gerais:Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Na seção Atribuição de objeto utilizável, a seguinte entrada pode ser criada ou atualizada:Objeto utilizável: <atribua o objeto utilizável ao qual o objeto locável se refere>Nota Considere que só pode existir uma atribuição aqui.Clique em Aplicar.Opcional:Na seção Medição, a seguinte entrada pode ser criada ou atualizada:Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Salvar. | O objeto locável é alterado. |  |

### Criar objeto locável interempresarial com estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objeto locável | Abra Administrar objeto locável. | A tela Administrar objetos locáveis é exibida. |  |
| 3 | Criar objetos locáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto locável: <seu nome de objeto>Categoria de utilização: Objeto locável interempresarial com estrutura de portfólio (I3)Tipo de utilização do objeto locável: <selecione um tipo de utilização, por exemplo, LO Office ICO (SRI1)>Empresa: <selecione uma empresa, por exemplo, Empresa (1010) >Objeto locável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:Nº de objeto de edifício/terreno obrigatório:Nº de objeto de edifício/terreno: <selecione o objeto de arquitetura (edifício/terreno) ao qual o objeto locável interempresarial se refere (objeto superior)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Início da validade: <data a partir da qual seu objeto é válido, por exemplo, a data atual>Fim da validade: <data até a qual o seu objeto é válido>Na seção Atribuição de objeto utilizável, efetue as seguintes entradas.Objeto utilizável: <atribuir o objeto utilizável pode ser um objeto utilizável interempresarial (I1) ou um objeto utilizável não interempresarial (UP) ao qual o objeto locável interempresarial se refere>Clique em Aplicar.Na seção Utilização de objeto de arquitetura, selecione Criar e efetue as seguintes entradas.Tipo de objeto arquitetônico: <selecione o tipo de objeto arquitetônico, por exemplo, Sala (S4RO)>Número de objeto arquitetônico: <selecione o objeto arquitetônico representado pelo objeto utilizável>Utilização baseada em medição: <como padrão, Sim>Clique em Entrar em tela inteira na parte superior direita. Em Medição de utilização arquitetônica, clique em Criar e efetue as seguintes entradas:Tipo de medição: <seu tipo de medição>, por exemplo, Área do escritório (SG11)Montante: Seu montanteInício da validade: <data a partir da qual o seu objeto é válido>Fim da validade: <data até a qual o seu objeto é válido>Clique em Aplicar.Clique em Criar. | O objeto locável é criado. |  |

### Criar objeto locável interempresarial sem estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objeto locável | Abra Administrar objeto locável. | A tela Administrar objetos locáveis é exibida. |  |
| 3 | Criar objetos locáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto locável: <seu nome de objeto>Categoria de utilização: Objeto locável interempresarial sem estrutura de portfólio (I4)Tipo de utilização do objeto locável: <selecione um tipo de utilização, por exemplo, Instalações e equipamentos LO> ICO (SRI2)>Empresa: <selecione uma empresa, por exemplo, Empresa (1010) >Objeto locável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Início da validade: <data a partir da qual seu objeto é válido, por exemplo, a data atual>Fim da validade: <data até a qual o seu objeto é válido>Na seção Atribuição de objeto utilizável, selecione Criar e efetue as seguintes entradas.Objeto utilizável: <Atribuir o objeto utilizável - pode ser um objeto utilizável interempresarial (I2) ou um objeto utilizável não interempresarial (UW) ao qual o objeto locável interempresarial se refere>Clique em Aplicar.Opcional:Para a seção Medição, clique em Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Criar. | O objeto locável é criado. |  |

### Criar objeto utilizável interempresarial com estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objetos utilizáveis | Abra Administrar objetos utilizáveis. | A tela Administrar objetos utilizáveis é exibida. |  |
| 3 | Criar objetos utilizáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto utilizável: <seu nome de objeto>Categoria de utilização: Objeto utilizável interempresarial com estrutura de portfólio (I1)Tipo de utilização de objeto utilizável: <selecione um tipo de utilização, por exemplo, CA Escritório ICO (SUI1)>Empresa: <selecione uma empresa, por exemplo, Empresa (1020) >Objeto utilizável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:Nº de objeto de edifício/terreno: <selecione o objeto de arquitetura (edifício/terreno) ao qual o objeto utilizável interempresarial se refere (objeto superior)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Nota A Data de início da validade e a Data do fim da validade serão determinadas a partir do Objeto locável interempresarial atribuído.Na seção Objeto de classificação contábil principal, selecione Criar e efetue as seguintes entradas:Tipo de objeto do objeto atribuído: <selecione um tipo de objeto, por exemplo, Centro de custo (KS)>Objeto de classificação contábil: <seu objeto de classificação contábil>Nota Um objeto de classificação contábil principal deve ser atribuído para toda a validade do objeto. O objeto de classificação contábil pode ser alterado durante a validade do objeto. No entanto, não podem ocorrer sobreposições ou lacunas. Os objetos utilizáveis que pertencem ao mesmo edifício ou terreno podem usar os mesmos ou diferentes objetos de classificação contábil principais. Um objeto de classificação contábil principal usado para um edifício ou terreno não pode ser usado como o objeto de classificação contábil principal em outro edifício ou terreno.Clique em Aplicar.Na seção Atribuição de objeto locável interempresarial, selecione Criar e efetue as seguintes entradas.Objeto locável interempresarial: <atribua o objeto locável interempresarial ao qual o objeto utilizável interempresarial ao qual ele se refere>Clique em Aplicar.Nota O escopo do contrato de aluguel interempresarial é limitado ao escopo alugado pela empresa afiliada. Um objeto locável interempresarial da empresa arrendadora deve ser atribuído.Opcional:Na seção Status do sistema, selecione Bloquear para configuração interempresarial se você quiser evitar que os objetos locáveis (RP) sincronizados a partir de uma solução de administração de bens imóveis de terceiros sejam atribuídos automaticamente a objetos utilizáveis, desde que a configuração interempresarial não esteja concluída.Seu objeto utilizável interempresarial tem o status Somente locação interempresarial, o que impede uma locação externa.Selecione Desbloquear para configuração interempresarial depois de ter concluído a configuração interempresarial.Para a seção Medição, selecione Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Selecione Criar. | O objeto utilizável é criado. |  |

### Criar objeto utilizável interempresarial sem estrutura de portfólio

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista de contrato - leasing ou Responsável de bens imóveis - administração de localizações. | A página Início é exibida. |  |
| 2 | Abrir Administrar objetos utilizáveis | Abra Administrar objetos utilizáveis. | A tela Administrar objetos utilizáveis é exibida. |  |
| 3 | Criar objetos utilizáveis | Clique em Criar e efetue as entradas a seguir.Na seção Cabeçalho:Nome do objeto utilizável: <seu nome de objeto>Categoria de utilização: Objeto utilizável interempresarial sem estrutura de portfólio (I2)Tipo de utilização de objeto utilizável: <selecione um tipo de utilização, por exemplo, LI Instalações e equipamentos ICO (SUI2)>Empresa: <selecione uma empresa, por exemplo, Empresa (1020) >Objeto utilizável: <seu ID de objeto no caso de intervalo de numeração externo, caso contrário, deixe o campo em branco>Na seção Informações gerais:ID de portfólio (opcional): <selecione um ID de portfólio, por exemplo, Eletrodomésticos de escritório (S501)>Grupo de autorizações (opcional): <selecione um grupo de autorizações (este campo só é visível se um grupo de autorizações estiver configurado)>Nota A Data de início da validade e a Data do fim da validade serão determinadas a partir do Objeto locável interempresarial atribuído.Na seção Objeto de classificação contábil principal, selecione Criar e efetue as seguintes entradas:Tipo de objeto do objeto atribuído: <selecione um tipo de objeto, por exemplo, Centro de custo (KS)>Objeto de classificação contábil: <seu objeto de classificação contábil>Nota Um objeto de classificação contábil principal deve ser atribuído para toda a validade do objeto. O objeto de classificação contábil pode ser alterado durante a validade do objeto. No entanto, não podem ocorrer sobreposições ou lacunas. Os objetos utilizáveis que pertencem ao mesmo edifício ou terreno podem usar os mesmos ou diferentes objetos de classificação contábil principais. Um objeto de classificação contábil principal usado para um edifício ou terreno não pode ser usado como o objeto de classificação contábil principal em outro edifício ou terreno.Clique em Aplicar.Na seção Atribuição de objeto locável interempresarial, selecione Criar e efetue as seguintes entradas.Objeto locável interempresarial: <atribua o objeto locável interempresarial ao qual o objeto utilizável interempresarial ao qual ele se refere>Nota O escopo do contrato de aluguel interempresarial é limitado ao escopo alugado pela empresa afiliada. Um objeto locável interempresarial da empresa arrendadora deve ser atribuído.Clique em Aplicar.Opcional:Para a seção Medição, selecione Criar e efetue as seguintes entradas.Tipo de medição: <selecione um tipo de medição>Montante: <montante da medição>Clique em Aplicar.Clique em Criar. | O objeto utilizável é criado. |  |

Typographic Conventions

| Type Style | Description |
| --- | --- |
| Example | Words or characters quoted from the screen. These include field names, screen titles, pushbuttons labels, menu names, menu paths, and menu options.Textual cross-references to other documents. |
| Example | Emphasized words or expressions. |
| EXAMPLE | Technical names of system objects. These include report names, program names, transaction codes, table names, and key concepts of a programming language when they are surrounded by body text, for example, SELECT and INCLUDE. |
| Example | Output on the screen. This includes file and directory names and their paths, messages, names of variables and parameters, source text, and names of installation, upgrade and database tools. |
| Example | Exact user entry. These are words or characters that you enter in the system exactly as they appear in the documentation. |
| <Example> | Variable user entry. Angle brackets indicate that you replace these words and characters with appropriate entries to make entries in the system. |
| EXAMPLE | Keys on the keyboard, for example, F2 or ENTER. |

|  |
| --- |
|  |
| www.sap.com/contactsap |
| © 2026 SAP SE or an SAP affiliate company. All rights reserved.No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company. The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components of other software vendors. National product specifications may vary.These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty. SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company) in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies. See [www.sap.com/copyright](http://www.sap.com/copyright) for additional trademark information and notices. |

<!-- image omitted: SAP Logo -->

## Connections
- part-of :: [[_cluster]]
- related-to :: [[17-leasing-and-real-estate/create-rental-object-master-data-script-7ad-521]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-523]]
- related-to :: [[17-leasing-and-real-estate/sap-s-4hana-cloud-public-edition-mds-7ad-525]]
- related-to :: [[17-leasing-and-real-estate/script-de-datos-maestros-crear-objeto-de-alquiler-mds-7ad-522]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/7AD_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 43,866 chars in the whole document
