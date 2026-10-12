---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-fornecedores-mds-bne-590
title: Script de dados mestre - Criar mestre de fornecedores - MDS (BNE) (BNE_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data test script for creating supplier master (general, company code, purchasing org data) via Fiori apps BP and F1053A."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/supplier-master]
aliases: [BNE_S4CLD2608_Master_Data_PT_XX]
keywords: [Supplier Master Data, general supplier data, company code data, purchasing organization data, business partner grouping, business partner roles, account groups, business roles, withholding tax, country-specific fields]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-590
topic: 02-business-partner-and-product-master-data/supplier-master
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de fornecedores - MDS (BNE) (BNE_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Supplier Master Data** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de fornecedores - MDS (BNE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893990)

[2 Pré-requisitos 3](#_Toc233893991)

[2.1 Acesso ao sistema 3](#_Toc233893992)

[2.2 Funções 3](#_Toc233893993)

[2.3 Etapas preliminares 3](#_Toc233893994)

[2.4 Unidades organizacionais necessárias 4](#_Toc233893995)

[2.5 Dados mestre obrigatórios e opcionais 5](#_Toc233893996)

[2.6 Parâmetros principais para a criação de dados 5](#_Toc233893997)

[2.6.1 Agrupamento de parceiros de negócios e intervalos de numeração 5](#_Toc233893998)

[2.6.2 ID do parceiro de negócios 6](#_Toc233893999)

[2.6.3 Função do parceiro de negócios 6](#_Toc233894000)

[2.6.4 Grupo de contas 7](#_Toc233894001)

[3 Tabela de síntese 8](#_Toc233894002)

[4 Procedimentos de teste 9](#_Toc233894003)

[4.1 Criar dados mestre do fornecedor – Dados gerais 9](#_Toc233894004)

[4.2 Criar dados mestre do fornecedor – Dados da empresa 15](#_Toc233894005)

[4.3 Criar dados mestre do fornecedor – Dados da organização de compras 22](#_Toc233894006)

## Objetivo

Contexto empresarial

Um fornecedor é um parceiro de negócios que fornece e vende mercadorias e serviços à sua organização. Um parceiro de negócios pode ser, simultaneamente, um cliente e um fornecedor, por exemplo, o seu fornecedor também compra mercadorias a você.

Um mestre de fornecedores retém informações sobre o fornecedor como, por exemplo, o nome, o endereço, os dados bancários, os detalhes de imposto e as preferências de faturamento. A informação sobre o fornecedor é utilizada e armazenada em transações, como ordens do cliente, remessas e faturas.

Algumas informações sobre o fornecedor são específicas de uma determinada empresa (conhecida como empresa) ou unidade de compras (conhecida como organização de compras) dentro de sua organização.

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
| Especialista em dados mestre - dados do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST | Dados mestre - Parceiros de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |  |

### Etapas preliminares

Contexto

Nesta etapa você atribui as funções do capítulo “Funções” ao usuário de teste, necessárias para a replicação de dados. Antes de executar esta etapa, certifique-se de ter criado e adicionado as funções necessárias para o objeto específico para a replicação de dados.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori com suas credenciais de usuário. | A Tela inicial é exibida. |  |
| 2 | Acesse o app SAP Fiori | Clique em Atualizar usuários empresariais. |  |  |
| 3 | Inserir nome do usuário | Insira o nome do usuário fornecido pelo seu administrador do sistema, em seguida clique em Ir. |  |  |
| 4 | Selecionar usuário | Selecione o usuário na lista. |  |  |
| 5 | Editar | Clique em Editar. |  |  |
| 6 | Adicionar funções do usuário | Clique em Adicionar funções empresariais, insira a função empresarial necessária no campo Procurar e pressione Enter. |  |  |
| 7 | Selecionar funções empresariais | Selecione as Funções empresariais necessárias e, em seguida, clique em OK. |  |  |
| 8 | Salvar | Clique em Salvar. | As funções do usuário foram salvas. |  |
| 9 | Página inicial | Volte para a Página inicial da SAP. | A página inicial é exibida. |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre do fornecedor são dependentes das unidades organizacionais da empresa, os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados gerais/centrais | Independente de unidades organizacionais | ID, nome, endereço, conta bancária, número de identificação fiscal, etc. | Os dados centrais só existem uma vez para um registro de dados mestre do fornecedor. | não aplicável |
| Dados da empresa | Empresa | Conta de reconciliação, condições de pagamento, responsável, etc. | Os dados da empresa podem existir para cada ID da empresa da sua estrutura empresarial para a qual é utilizado o registro mestre do fornecedor. | Empresa:____________ |
| Dados de compras | Organização de compras | Moeda da ordem, condições de pagamento, grupo de compradores, condições de expedição | Os dados de compras podem existir para todas as organizações de compras para as quais é utilizado o registro de dados mestre do fornecedor. | Organização de compras:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do fornecedor podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre do fornecedor.

|  |
| --- |
| Nota Verifique Nota Fiscal Brasil – JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de cliente. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Mestre de bancos | Na IU do parceiro de negócios você encontra a entrada dos dados da conta bancária na seção Transações de pagamento. | Opcional | Se você deseja atualizar as contas bancárias do fornecedor, deve criar o mestre de bancos do banco correspondente. No registro mestre de clientes, você pode depois inserir o número da conta real juntamente com os dados mestre do banco. |
| Conta de reconciliação | Na IU do parceiro de negócios, você encontra a entrada dos dados da conta de conciliação Empresa > Gerenciamento de contas do fornecedor | Obrigatório | Para a conta de reconciliação, vcoê insere o número da conta do Razão a partir do livro auxiliar da contabilidade de clientes (CC).A conta do Razão que você insere deve ser criada antes de poder utilizá-la no registro mestre do fornecedor. |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de fornecedor:

#### Agrupamento de parceiros de negócios e intervalos de numeração

Os agrupamentos de parceiros de negócios determinam os intervalos de numeração para os IDs do parceiro de negócios. Você não pode modificar posteriormente a atribuição ou os IDs. Se um agrupamento de parceiros de negócios estiver atribuído a um intervalo de numeração interno, você não pode inserir o ID do parceiro de negócios manualmente. Neste caso, deixe o campo em branco, uma vez que o sistema seleciona automaticamente um número do intervalo de numeração numérico atribuído.

Os agrupamentos de parceiros de negócios seguintes e os intervalos de numeração correspondentes estão definidos para os parceiros de negócios (clientes, fornecedores, contatos, empregados, etc.):

| Agrupamento de parceiros de negócios | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| BP01 | Intervalo de numeração numérico externo (inferior):1 – 999999 | Utilize este agrupamento, por exemplo, para migrar registros de dados mestre numéricos |
| BP02 | Intervalo de numeração numérico interno para utilização padrão:1000000 – 9999999 | Se não for inserido nenhum grupo de parceiros de negócios, é utilizado este intervalo de numeração por padrão. |
| BP03 | Intervalo de numeração numérico externo (superior):10000000 – 999999999 | Reservado para objetos de dados mestre de amostra da SAP. |
| BPAB | Intervalo de numeração alfanumérico externo:A – ZZZZZZZZZZ | Este intervalo deve iniciar com um caractere. |
| BPEE | Intervalo de numeração numérico interno:9980000000 – 9999999999 | Reservado para parceiros de negócios utilizados como Empregados. |

#### ID do parceiro de negócios

ID do parceiro de negócios

Estão disponíveis as seguintes opções para a atribuição do identificador (ID) do parceiro de negócios:

- Insira um ID com um agrupamento de parceiros de negócios para a numeração externa. Por exemplo

| Agrupamento de parceiros de negócios | Entradas possíveis para o ID do parceiro de negócios |
| --- | --- |
| BP01 | Qualquer número dentro do intervalo correspondente 1 - 999999 |
| BPAB | Qualquer combinação alfanumérica até 10 caracteres, se você começar com um caractere, por exemplo, Z-TEST01 |

Se você não indicou o agrupamento de parceiros de negócios e deixa o ID do parceiro de negócios em branco, o sistema aceita o próximo número livre do agrupamento de parceiros de negócios BP02. Este agrupamento é definido como agrupamento padrão para os IDs numéricos internos do parceiro de negócios.

#### Função do parceiro de negócios

Função do parceiro de negócios

A função do parceiro de negócios determina os direitos e responsabilidades de cada parceiro em uma transação empresarial.

Exemplos para funções de parceiro em Compras: fornecedor, emissor da fatura, fornecedor de mercadorias, etc.

#### Grupo de contas

Os grupos de contas são parâmetros de controle principais para a criação de segmentos de dados ERP de um registro mestre de fornecedor. Atualmente, o único grupo de contas suportado para os dados mestre de fornecedor é SUPL.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do fornecedor – Dados gerais](#unique_14) [página ] 9 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do fornecedor(F1053A) | Mestre de fornecedores – Dados gerais criados. |
| [Criar dados mestre do fornecedor – Dados da empresa](#unique_15) [página ] 15 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do fornecedor(F1053A) | Mestre de fornecedores – Dados da empresa criados. |
| [Criar dados mestre do fornecedor – Dados da organização de compras](#unique_16) [página ] 22 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) ou Administrar dados mestre do fornecedor(F1053A) | Mestre de fornecedores – Dados de compras criados. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre do fornecedor – Dados gerais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do fornecedor. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Criar uma organização do parceiro de negócios | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas e clique em OK:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com uma letra>Agrupamento: Selecione, por exemplo, Numeração alfanumérica externa.O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração.Nota Para obter mais informações, consulte o capítulo anterior [Agrupamento de parceiros de negócios e intervalos de numeração](#unique_9) [página ] 5. |  |  |
| 5 | Inserir dados de endereço | Na guia Endereço, na seção Nome, insira os seguintes dados:Título: <empresa>Nome: <nome> |  |  |
| 6 | Inserir critério de pesquisa | Na guia Endereço, na seção Critério de pesquisa, insira um ou mais critérios de pesquisa para o fornecedor. |  |  |
| 7 | Inserir dados de endereço | Na seção Endereço padrão, na subseção Endereço, insira o endereço. |  |  |
| 8 | Inserir fuso horário e zona de transporte | Na seção Endereço, escolha Mais campos. Insira os seguintes dados:Fuso horário: <fuso horário>Zona de transporte: <zona de transporte> |  |  |
| Somente para a Tailândia | Inserir dados de endereço (somente Tailândia) | Na seção Endereço, selecione Mais e insira os seguintes dados:Código do edifício: <edifício>Sala: <nº da sala>Andar: <nº do andar>Rua 2: <Moo>Rua 3: <Soi/Travessa>Rua: <estrada>Número: <não>Cidade diferente: <subdistrito>Bairro: <bairro/zona>Cidade: <província>Código postal: <Código postal> |  |  |
| 9 | Inserir dados de comunicação | Na guia Endereço, seção Comunicação, insira os seguintes dados:Idioma: <selecione o idioma preferido do fornecedor>Telefone: <Número de telefone>E-mail: <endereço de e-mail> |  |  |
| 10 | Inserir dados de identificação | Na guia Identificação na seção Dados organizacionais, insira os seguintes dados para o fornecedor:Forma jurídica: <Forma jurídica> |  |  |
| Só para o Japão | Inserir os dados do setor (somente Japão) | Na guia Identificação na seção Setores industriais, selecione o botão Todos os sistemas setoriais. Insira os seguintes dados:Sistema de setor industrial: Selecione Banco do Japão.Setor industrial: <selecione um número de setor>Setor industr.padrão: <não selecionado> |  |  |
| Só para o Japão | Inserir número de identificação fiscal (somente Japão) | Pressione Enter para a confirmação.Atenção Se você selecionar a configuração incorreta, não será possível atualizar os dados Japão: dado Meu número. |  |  |
| Só para o Japão | Inserir dados do número de identificação fiscal longo (somente Japão) | Na guia Identificação, na seção Números de identificação fiscal longos, insira os seguintes dados:Categoria: JP4 – Número de identificação fiscal de IVA JapãoNúmero de identificação fiscal longo: <Número da empresa do parceiro de negócios> |  |  |
| 11 | Inserir contas bancárias | Na guia Transações de pagamento, na seção Dados bancários, insira os seguintes dados para o fornecedor:País/Região: <País/região>Chave do banco: <chave do banco>Conta bancária: <conta bancária>Atenção As chaves do banco devem ser definidas previamente. Use as entradas possíveis para obter mais informações sobre as entradas permitidas neste campo. |  |  |
| 12 | Salvar os dados | Salve as entradas. |  |  |

Procedimento: opção 2 – Administrar dados mestre de cliente

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do fornecedor(F1053A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do fornecedor(F1053A). | O app é aberto. |  |
| 3 | Clicar em Criar | Na seção Fornecedores escolha Criar > Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Na seção Dados gerais insira os dados seguintes e selecione OK:Parceiro de negócios: Por exemplo, Z … (ou seja, qualquer ID alfanumérico externo, pois tem de começar com uma letra).Agrupamento: Por exemplo, <Numeração alfanumérica externa>.Título: Por exemplo, Empresa (0003)Nome 1: <insira um nome> | A tela Fornecedor novo é exibida. |  |
| 5 | Inserir dados básicos | Na tela Fornecedor novo, na guia Dados básicos, efetue as seguintes entradas:Na seção Informações do fornecedor, insira os seguintes dados:Grupo de contas de referência, grupo de autorizações do fornecedor etc.: Selecione a partir das entradas possíveis.Na seção Dados organizacionais, insira os seguintes dados:Obrigação de IVA, divisão fiscal, bloqueio de pagamento etc.: Marque os indicadores relevantes.Nota Para obter mais informações sobre agrupamentos de PNs e como eles estão relacionados à numeração de ID, consulte o capítulo anterior [Agrupamento de parceiros de negócios e intervalos de numeração](#unique_9) [página ] 5.Na seção Informações adicionais, insira os dados seguintes:Bloquear função: Selecione a partir das entradas possíveis.Centro: Selecione a partir das entradas possíveis.Chave de instruções: Selecione a partir das entradas possíveis. |  |  |
| 6 | Selecionar funções | Na tela Fornecedor novo, selecione a guia Funções. | Você navega para a seção Funções. |  |
| 7 | Clicar em Criar | Na seção Funções, clique em Criar e selecione uma função a partir das entradas possíveis:Função de parceiro de negócios: Por exemplo, FLVN01.Um mestre fornecedor deve ser criado com a função de parceiro de negócios FLVN00 (fornecedor FI) ou com a função de parceiro de negócios FLVN01 (fornecedor com dados de compras) ou com as duas funções. A função de parceiro de negócios FLVN00 (fornecedor FI) é usada na contabilidade financeira e a função de parceiro de negócios FLVN01 (fornecedor com dados de compras) é usada em vendas.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. | A função é adicionada. |  |
| 8 | Inserir funções adicionais (opcional) | Repita as etapas 6 e 7 para adicionar outras funções.Função de parceiro de negócios: Por exemplo, FLVN00. | Depois de você ter Inserido todas as funções de parceiro de negócios, elas são exibidas na seção Funções na tela Novo mestre. |  |
| 9 | Selecionar endereço padrão | Na tela Mestre fornecedor – Fornecedor novo, selecione a guia Endereço e vá para a seção Endereço padrão. | Você navega para a seção Endereço padrão. |  |
| 10 | Inserir dados de endereço | Na seção Endereço – Endereço padrão, efetue entradas para todos os campos relevantes de acordo com suas necessidades. Por exemplo:Rua: <nome da rua>Número: <número para o endereço>Código postal: <código postal para o endereço>Cidade: <Cidade>País/Região: <Código do país/região>Nota (Se aplica somente aos Estados Unidos) Quando você cria um Parceiro de negócios localizado nos Estados Unidos, o código do domicílio fiscal é determinado automaticamente. No entanto, você tem que inserir o endereço correto e completo, uma vez que o domicílio é derivado com base nas entradas de País (EUA), Estado e Código postal.Na seção Endereço – Comunicação padrão, efetue as seguintes entradas:Idioma: <idioma>:Telefone: <insira o campo conforme necessário>E-mail: por exemplo, contact@Z.comClique em Criar.Na seção Endereço – Detalhes de endereço, selecione a entrada de endereço.Na tela Novo endereço, na guia Utilizações de endereço, verifique se as seguintes informações são exibidas:Tipo de endereço: XXDEFAULT |  |  |
| 11 | Retornar à tela principal | Clique em Aplicar.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. |  |  |
| 12 | Selecionar contas bancárias | Na tela Mestre fornecedor – Fornecedor novo…, selecione a guia Contas bancárias. | Você navega para a seção Contas bancárias. |  |
| 13 | Clicar em Criar | Na tela Mestre fornecedor – Contas bancárias, selecione Criar. | A nova conta bancária é adicionada. |  |
| 14 | Inserir dados do banco | Insira os seguintes dados para a nova conta bancária:ID: Por exemplo, BNK1.País/região do banco: <Código do país/região>Chave do banco: <chave do banco>Número da conta: <Número da conta>Efetue entradas para todos os outros campos de acordo com suas necessidades. |  |  |
| 15 | Retornar à tela principal | Clique em Aplicar.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. |  |  |
| 16 | Selecionar número de identificação fiscal (opcional) | Na tela Mestre fornecedor – Fornecedor novo, na guia Identificação, selecione NÚMEROS DE IDENTIFICAÇÃO FISCAL. | Você navega para a seção NÚMEROS DE IDENTIFICAÇÃO FISCAL. |  |
| 17 | Selecione Criar (opcional) | Na seção Mestre de fornecedores – Novo fornecedor – NÚMERO DE IDENTIFICAÇÃO FISCAL…, selecione Criar. |  |  |
| 18 | Inserir dados de número de identificação fiscal (opcional) | Na seção Números de identificação fiscal, efetue as seguintes entradas:Categoria de imposto: <código de imposto>Número de identificação fiscal: <número de identificação fiscal>Nota Os números de identificação fiscal inseridos dependem de requisitos de país/região específicos.Selecione a categoria correta aplicável ao país/região do cliente. Por exemplo, para um parceiro de negócios alemão, você atualiza um valor para a categoria DE1, que representa o número de identificação fiscal de IVA usado habitualmente (Umsatzsteuer-Identifikationsnummer).Efetue entradas apenas para os campos necessários, caso contrário, clique em Excluir para remover o conjunto de dados (vazio). |  |  |
| 19 | Retornar à tela principal | Selecione a seta para voltar.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. |  |  |
| 20 | Clicar em Criar | Na seção Mestre fornecedor – Fornecedor novo – Categorias de imposto, selecione Criar. | A tela Categorias de imposto é exibida. |  |
| 21 | Inserir dados de categorias de imposto (opcional) | Efetue as seguintes entradas:Código de imposto: Por exemplo, IVA de compra IVA .Débito automático desde: <Data>Débito automático até : <Data> |  |  |
| 22 | Inserir textos (opcional) | Na tela Textos efetue as seguintes entradas:Idioma: Por exemplo, ENID: por exemplo, 01.Texto descritivo: <Insira um texto descritivo> |  |  |
| 23 | Inserir dados de fornecedor adicionais (opcional) | Vá para Dados básicos > Dados de fornecedor adicionais e selecione Criar.Adicione os dados necessários como descrito nas etapas acima.Nota Este cenário destina-se a atribuições múltiplas de fornecedores aos mesmos parceiros de negócios e, por isso, são aplicáveis os mesmos dados mestre descritos nas etapas acima referidas.Se forem necessários dados adicionais, como os dados de compras e os dados da Empresa, consulte as seções anteriores que contêm descrições semelhantes. |  |  |
| 24 | Salvar os dados | Clique em Criar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do fornecedor – Dados da empresa

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do fornecedor. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre do fornecedor – Dados gerais](#unique_14) [página ] 9, para prosseguir com este capítulo.

Siga o procedimento depois de ter salvo as entradas dos dados gerais, tal como descrito no capítulo anterior, na tela Exibir organização: <Nome do fornecedor>.

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Comutar para modo de modificação | Selecione Comutar entre exibição e modificação para ativar o modo de modificação. |  |  |
| 4 | Modificar função de parceiro de negócios | No campo Modificar em função de PN, selecione o seguinte valor:Fornecedor (contabilidade financeira)Nota A chave técnica para esta função de parceiro de negócios é FLVN00. |  |  |
| 5 | Abrir dados da empresa | Selecione Empresa na tela. | A tela Empresa é exibida. |  |
| 6 | Inserir empresa | Insira a Empresa. por exemplo, 1010. |  |  |
| Somente para a Rússia | Inserir dados contábeis do fornecedor – Sede (só para Rússia) | Na guia Fornecedor: Administração de contas, na seção Administração de contas, insira uma das seguintes opções:163107701 como sede para o PN de IVA 163117701163107701 como sede para o PN de IVA 163117701163107701 como sede para PN de imposto de imobiliário 163127701163107702 como sede para PN de imposto imobiliário 163127702 |  |  |
| 7 | Inserir dados contábeis do fornecedor | Na guia Fornecedor: Administração de contas, na seção Administração de contas, insira os seguintes dados:Conta de reconciliação: <21100000> (contas a pagar nacionais)Chave de ordenação: <Chave de ordenação>Indicador de minoria: <Indicador de minoria> (os valores do indicador de minoria são definidos usando a etapa de configuração: Definir indicadores de minoria)Nota Poderão existir outras contas de reconciliação do Razão para fornecedores estrangeiros ou afiliadas. |  |  |
| Só para o Japão | Inserir dados contábeis do fornecedor – Imposto retido na fonte (somente Japão) | Na guia Fornecedor: Na guia Administração de contas da seção Imposto retido na fonte, insira os seguintes dados, se este fornecedor for relevante para imposto retido na fonte:Chave de país/região IRF: <JP> (Japão) |  |  |
| Só para a Polônia | Inserir fornecedor: Imposto retido na fonte (só para a Polônia) | Na guia Fornecedor: Imposto retido na fonte, na seção Tipos de imposto retido na fonte, efetue as seguintes entradas:Atribua o Tipo de imposto retido na fonte e informações do Código de imposto retido na fonte para o parceiro de negócios.Insira o Motivo de isenção (DT), a Porcentagem de isenção (por exemplo, 100%), o Número de isenção e o Intervalo de validade para os códigos de imposto retido na fonte relevantes para o contrato/acordo de tributação dupla. |  |  |
| 8 | Inserir dados de pagamento do fornecedor | Na guia Fornecedor: Transações de pagamento, na seção Dados de pagamento, efetue a seguinte entrada:Condições de pagamento: <condições de pagamento>Nota As condições de pagamento definidas nesta etapa podem ser anuladas pelas condições de pagamento definidas no nível das compras. |  |  |
| 9 | Inserir dados de pagamento do fornecedor | Na guia Fornecedor: Transações de pagamento, na seção Transações de pagamento automáticas, insira os seguintes dados:Formas de pagamento: <Formas de pagamento>Banco da empresa: <Banco da empresa>Nota Pressione F4 para abrir a seleção no campo Formas de pagamento. |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Na guia Fornecedor: Correspondência, na seção Correspondência, insira os seguintes dados:Conta com fornecedor <Conta com fornecedor> |  |  |
| Só para o Japão | Imposto retido na fonte (somente Japão) | Na guia Imposto retido na fonte efetue a seguinte entrada, se este fornecedor for relevante para o imposto retido na fonte.Tipo de imposto retido na fonte: <Tipo de imposto retido na fonte>Código de imposto retido na fonte: <Código de imposto retido na fonte>Assunto: <selecionado>. |  |  |
| Só para o Japão | Japão: Meu número (somente Japão) | Selecione Dados gerais. Na guia Ampliação específica do país efetue a seguinte entrada, se este parceiro de negócios não for uma pessoa física:Nº da empresa: <Nº da empresa>Na guia Ampliação específica do país, efetue as seguintes entradas, se este fornecedor for uma pessoa física.Selecione Válido desde, Válido até e clique em Exibir.Status: <Status>Comprovante para identidade: <Comprovante para identidade>Comprovante para número: <Comprovante para número>Retenção até: <Retenção até>Selecione Visualizar sem proteção para inserir o Nº individual. |  |  |
| Só para a Tailândia | Código de filial (só para a Tailândia) | Abra os dados gerais e, na guia Ampliação específica do país , atualize os dados de código da filial, com o endereço e o código de filial padrão para este parceiro de negócios.Para o endereço do código da filial, clique em Endereço e insira os seguintes dados:Nome (primeiras duas linhas): <Nome do contribuinte>País: THCódigo do edifício: <nome edif./Localidade>Sala: <nº da sala>Andar: <andar>Rua 2: <Moo>Rua 3: <Trok/Soi>Rua: <estrada>Número: <não>Outra cidade: <Tumbol/Sub-zona>Bairro: <bairro/zona>Cidade: <província>Código postal: <Código postal>Telefone: <Número de telefone>Nota Caso haja mais de um código de filial para um parceiro de negócios, você deverá atualizar cada código de filial junto com o endereço para cada código de filial. Você também deve definir um código de filial que é normalmente usado pelo parceiro de negócios como padrão. |  |  |
| Somente para a Rússia | Atributos do pagamento de imposto (somente Rússia) | Na guia Ampliação específica do país, efetue as seguintes entradas para o parceiro de negócios.Para o imposto imobiliário BP 163107701 e 163107702, insira os seguintes valores:Tipo de pagamento: Pagamentos a orçamentoStatus do pagador: 01Código de orçamento: 182 1 06 02010 02 1000 110Para pagamento da Folha de pagamento BP 163107703, insira os seguintes valores:Tipo de pagamento: Pagamentos a orçamentoPara o IVA BP 163117701 e 163117702, insira os seguintes valores:Tipo de pagamento: Pagamentos a orçamentoStatus do pagador: 01Código de orçamento: 18210301000011000110Para o imposto imobiliário BP 163127701 e 163127702, insira os seguintes valores:Tipo de pagamento: Pagamentos a orçamentoStatus do pagador: 01Código de orçamento: 18210602010021000110 |  |  |
| Só para a Arábia Saudita | Fornecedor: Ampliação espec. de país (só para Arábia Saudita) | Na guia Fornecedor: ampliação específica de país, clique em Inserir linha para adicionar os Certificados de fornecedor. |  |  |
| 11 | Salvar os dados | Salve as entradas. | A entrada no campo Modificar na função do PN é alterada de Fornecedor FI (novo) para Fornecedor FI (definido). |  |

Informação sobre o imposto retido na fonte (somente Brasil)

Use a tabela seguinte para determinar as entradas de imposto retido na fonte na etapa anterior somente para o Brasil.

Para a organização empresarial:

| Tipo de imposto retido na fonte | Código do imposto retido na fonte | assunto | Comentários |
| --- | --- | --- | --- |
| GA | GA | X | para 4,65% |
| PA | PA | X | Só para PIS |
| CA | CA | X | só para COFINS |
| SA | SA | X | só para CSSL |
| RA | RA | X | só para IRPJ (por meio de TAXBRA) |
| IR | R1 a R3 | X | só para IRPJ (por meio de FI) |
| IW | IW | X | para ISS |
| IJ | I1 a I2 | X | para INSS PJ |

Para pessoa física:

| Tipo de imposto retido na fonte | Código do imposto retido na fonte | assunto | Comentários |
| --- | --- | --- | --- |
| ID | R0 a R5 | X | para INSS PF |
| IN | N1 | X | para INSS PR |

Procedimento: opção 2 – Administrar dados mestre de cliente

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do fornecedor(F1053A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do fornecedor(F1053A). | O app é aberto. |  |
| 3 | Inserir detalhes do fornecedor | A partir das entradas possíveis, selecione Parceiro de negócios. Além disso, você pode selecionar mais detalhes, como Rua.Clique em Ir. |  |  |
| 4 | Selecionar fornecedor | Selecione um fornecedor na lista de resultados. | É exibida a tela Fornecedor. |  |
| 5 | Clicar em Editar | Clique em Editar.Nota Esta etapa parte do princípio de que você está continuando a partir da etapa anterior e já acessou Dados mestre - Mestre fornecedor > Administrar mestre fornecedor. Depois de você ter salvo seus dados gerais da seção anterior, o sistema está no modo de exibição. Para continuar, você tem que estar no modo de edição. | A tela Administrar mestre fornecedor é exibida no modo de edição (os campos estão prontos para suas entradas). |  |
| 6 | Selecionar Empresas | Na tela Administrar fornecedor, selecione Empresas. |  |  |
| 7 | Clicar em Criar | Na seção Empresas, clique em Criar. | Uma visão de detalhes é exibida no modo de edição. |  |
| 8 | Inserir dados da empresa | Na seção Empresas, selecione uma entrada para abrir uma visão detalhada. Efetue as seguintes entradas:Na guia Dados gerais:Empresa: insira a empresa, por exemplo, 1710.Na guia Correspondência:Responsável: Por exemplo: 01 Sra. Smith.Conta no fornecedor: <Conta no fornecedor>Na guia Finanças:Finanças – ContabilidadeConta de reconciliação: por exemplo, 21100000 – contas a pagar nacionais.Chave de ordenação: Por exemplo, 009 número de documento externo.Grupo minoritário: <Grupo minoritário> (válido somente para a função FLVN00 - Fornecedor (contabilidade financeira). Os valores do grupo de minorias são definidos usando a etapa de configuração: Definir indicadores de minoria.)Finanças – Dados de pagamentoCondições de pagamento: por exemplo, 0001.Finanças – Transações de pagamento automáticasFormas de pagamento: Por exemplo, E débito direto.Na guia Dados de advertência:Procedimento de advertência, Bloqueio de advertências, Destinatário da advertência, Responsável pela advertência: Selecione nas entradas possíveis.Nível de advertência: por exemplo, 0.Última advertência: Por exemplo, 10.02.2020Procedimento judicial de advertência de: por exemplo, 11.02.2020.Na guia Textos:Na seção Textos , clique em Criar e efetue as seguintes entradas:Idioma: Por exemplo, ENID: por exemplo, 01.Texto descritivo: <Insira um texto descritivo> |  |  |
| 9 | Retornar à tela principal | Selecione Criar e clique em Aplicar.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. |  |  |
| 10 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

### Criar dados mestre do fornecedor – Dados da organização de compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do fornecedor. Os apps disponíveis dependem de sua função atribuída. Por isso, são fornecidas duas opções.

Pré-requisito

Você deve concluir o capítulo anterior, [Criar dados mestre do fornecedor – Dados gerais](#unique_14) [página ] 9, para prosseguir com este capítulo.

Siga o procedimento depois de ter salvo as entradas dos dados gerais, tal como descrito no capítulo anterior, na tela Exibir organização: <Nome do fornecedor>.

Procedimento: opção 1 - Atualizar parceiro de negócios

Siga este procedimento quando seu acesso de usuário oferece a você o app Atualizar parceiro de negócios(BP).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Atualizar parceiro de negócios(BP). | O app é aberto. |  |
| 3 | Comutar para modo de modificação | Selecione Comutar entre exibição e modificação para ativar o modo de modificação. |  |  |
| 4 | Modificar função de parceiro de negócios | No campo Modificar em função de PN, selecione o seguinte valor:FornecedorNota A chave técnica para esta função de parceiro de negócios é FLVN01. |  |  |
| 5 | Abrir dados da organização de compras | Selecione Compras na tela. | A tela Organização de compras é exibida. |  |
| 6 | Inserir dados de compras | Insira os seguintes dados e pressione Enter:Organização de compras: <Organização de compras> |  |  |
| 7 | Inserir dados de compras | Na guia Dados de compras, na seção Condições, insira os dados seguintes:Moeda da ordem: <Moeda da ordem>Condições de pagamento: <Condições de pagamento> |  |  |
| 8 | Inserir dados de compras | Na guia Dados de compras, na seção Dados de controle, insira os seguintes dados:Condições de expedição: <Condições de expedição>Revisão de faturas baseada EM: <Revisão de faturas baseada na EM> |  |  |
| 9 | Inserir dados de compras | Na guia Dados de compras, na seção Valores propostos para material, insira os seguintes dados:Grupo de compradores: <grupo de compradores>Prazo de entrega previsto: <Prazo de entrega previsto> |  |  |
| 10 | Inserir dados de funções de parceiro | Na guia Funções do parceiro, na seção Funções do parceiro, verifique se existe a entrada LF (ou entrada VN quando o idioma de login for inglês). |  |  |
| 11 | Salvar os dados | Salve as entradas. |  |  |

Procedimento: opção 2 – mestre de fornecedores

Siga este procedimento quando seu acesso de usuário oferece a você o app Administrar dados mestre do fornecedor(F1053A).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do fornecedor(F1053A). | O app é aberto. |  |
| 3 | Clicar em Editar | Clique em Editar.Nota Esta etapa parte do princípio de que você está continuando a partir da etapa anterior e já acessou Dados mestre - Mestre fornecedor > Mestre fornecedor. Depois de você ter gravado seus dados da seção anterior, o sistema está no Modo de exibição. Para continuar, você tem que estar no modo de edição. | A tela Mestre fornecedor é exibida no modo de edição (os campos estão prontos para suas entradas). |  |
| 4 | Selecionar Organizações de compras | Na tela Mestre fornecedor ..., selecione ORGANIZAÇÕES DE COMPRAS. | A seção Mestre fornecedor – COMPRAS é exibida. |  |
| 5 | Clicar em Criar | Na seção Mestre fornecedor – COMPRAS, selecione Criar. | A tela Nova organização de compras... é exibida no modo de edição. |  |
| 6 | Inserir dados da organização de compras | Na tela Nova organização de compras, efetue as seguintes entradas:Na guia Dados gerais:Organização de compras: <código da organização de compras>Grupo de compradores: por exemplo, 001.Na guia COMPRAS:Para a coluna Condições:Moeda da ordem: <código da moeda>Valor mínimo da ordem: <Valor mínimo da ordem>Condições de pagamento: por exemplo, 0001.Controle de dados da determinação do preço: Por exemplo, <data atual>.Para a coluna Dados de controle:Condição de expedição: por exemplo, 01.Pedido automático: <Pedido automático>Revisão de faturas baseada na entrada de mercadorias (campo de seleção) |  |  |
| 7 | Inserir dados de funções de parceiro | Nota Algumas funções de parceiro estão predeterminadas com base na customização para grupos de contas e organizações de compras selecionadas.Para adicionar mais Funções do parceiro, na guia Funções do parceiro, selecione Criar. Você pode selecionar a partir das seguintes funções:VN – FornecedorGS – Fornecedor de mercadoriasMN – Centro de produção |  |  |
| 8 | Inserir detalhes da organização de compras | Na guia Texto, selecione Criar e insira os detalhes da organização de compras. |  |  |
| 9 | Retornar à tela principal | Clique em Aplicar.Nota Certifique-se de que a mensagem do sistema Esboço gravado é exibida na parte inferior da tela, antes de você retornar à tela principal. |  |  |
| 10 | Salvar os dados | Clique em Salvar. | Uma mensagem do sistema indica que o objeto foi salvo. |  |

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

## Suspected conflicts

> [!warning] Conflict
> Flagged while digesting this document, not verified: Note refers to Brazil nota fiscal JD0 'for customer master data' and the option 2 headings say 'Administrar dados mestre de cliente' although the content concerns suppliers; FLVN01 is described as used in 'sales' rather than purchasing.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-supplier-master-mds-bne-sap-s-4hana-cloud-pu]]
- related-to :: [[02-business-partner-and-product-master-data/mds-bne-591]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-bne-589]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-proveedores-bne-588]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNE_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 45,570 chars in the whole document
