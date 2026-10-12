---
id: 11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-mestre-de-transportadoras-mds-4de-410
title: Script de dados mestre - Criar mestre de transportadoras (MDS 4DE) (4DE_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT): step-by-step creation of carrier/freight agent business partners for road, rail, sea, forwarder and air."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/carrier-master-data]
aliases: [4DE_S4CLD2608_Master_Data_PT_XX]
keywords: [Carrier Business Partners, carrier master data, business partner creation, freight agent roles, invoice verification, evaluated receipt settlement, road carriers, rail carriers, sea carriers, air carriers]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-410
topic: 11-inventory-warehouse-and-transportation/carrier-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de transportadoras (MDS 4DE) (4DE_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Carrier Business Partners** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de transportadoras – MDS (4DE) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893746)

[2 Pré-requisitos 3](#_Toc233893747)

[2.1 Acesso ao sistema 3](#_Toc233893748)

[2.2 Funções 3](#_Toc233893749)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893750)

[2.4 Parâmetros principais para a criação de dados 4](#_Toc233893751)

[2.4.1 Agrupamentos 4](#_Toc233893752)

[3 Tabela de síntese 5](#_Toc233893753)

[4 Procedimentos 6](#_Toc233893754)

[4.1 Criar agente de frete parceiro de negócios (rodoviário) para processo de revisão de faturas 6](#_Toc233893755)

[4.2 Criar agente de frete do parceiro de negócios (rodoviário) para o processo de liquidação automática de entrada de mercadorias (LAEM) 9](#_Toc233893756)

[4.3 Criar agente de frete parceiro de negócios (ferroviário) para processo de revisão de faturas 13](#_Toc233893757)

[4.4 Criar agente de frete do parceiro de negócios (ferroviário) para o processo de liquidação automática de entrada de mercadorias (LAEM) 17](#_Toc233893758)

[4.5 Criar agente de frete de parceiro de negócios (marítimo) para processo de verificação de faturas 20](#_Toc233893759)

[4.6 Criar agente de frete do parceiro de negócios (marítimo) para o processo de liquidação automática de entrada de mercadorias (LAEM) 24](#_Toc233893760)

[4.7 Criar agente de frete parceiro de negócios (agente de frete) para processo de revisão de faturas 28](#_Toc233893761)

[4.8 Criar agente de frete do parceiro de negócios (agente de frete) para o processo de faturamento automático de entrada de mercadorias (FAEM) 31](#_Toc233893762)

[4.9 Criar transportadora de parceiro de negócios (aérea) para processo de verificação de faturas 35](#_Toc233893763)

[4.10 Criar transportadora de parceiro de negócios (aéreo) para o processo Faturamento automático de entrada de mercadorias (FAEM) 38](#_Toc233893764)

[5 Anexo 43](#_Toc233893765)

## Objetivo

Este documento fornece uma descrição para a criação de um Parceiro de negócios – Transportadora para o seu sistema SAP S/4HANA. A descrição inclui os segmentos de dados relevantes para a appliance SAP S/4HANA, como funções de Parceiro de Negócios e outros campos relevantes. Os campos que não são relevantes para o escopo do conteúdo do SAP S/4HANA, uma vez que foram fornecidos pelo SAP Best Practices, não estão descritos neste documento.

Uma transportadora é um parceiro de negócios responsável pelo transporte de mercadorias. Uma transportadora pode oferecer serviços aos expedidores ou agentes de frete.

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Especialista em dados mestre - dados do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST | Dados mestre - Parceiros de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios / Governança do parceiro de negócios | SAP_BR_BUPA_MASTER_SPECIALIST / SAP_CA_SPT_MDG_BP_GOV_PC / SAP_CMD_SPT_BP_GOV_PC / SAP_CA_SPT_MDG_BP_WFUSR_PC |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados de compras (administração de materiais) | Organização de compras |  |  |  |
| Empresa | Empresa |  |  |  |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de transportadora de parceiro de negócios.

#### Agrupamentos

Os seguintes agrupamentos são definidos para a transportadora de parceiro de negócios:

| Agrupamento | Intervalo/IDs | Comentários |
| --- | --- | --- |
| Numeração numérica externa (intervalo mais alto) | BP03 |  |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar agente de frete parceiro de negócios (rodoviário) para processo de revisão de faturas](#unique_8) [página ] 6 | Especialista em dados mestre - dados do parceiro de negócios | Atualizar parceiro de negócios(BP) | A transportadora do parceiro de negócios é criada. |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa de processo usado para diferentes processos empresariais: Processo de revisão de faturas e processo de nota de crédito.

### Criar agente de frete parceiro de negócios (rodoviário) para processo de revisão de faturas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. A transportadora está atribuída a uma ordem de transporte (ordem de frete). Este agente de frete é utilizado principalmente no processo de revisão de faturas no qual os montantes da fatura do agente de frete são comparados com os custos de transporte previstos na ordem de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Atualizar parceiro de negócios(BP) | É aberta uma nova janela que exibe a tela Atualizar parceiro de negócios (PN). |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração. Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Nota Valores de exemplo com localização dos EUA para os campos acima:Parceiro de negócios:<17386001>Agrupamento:<numeração numérica externa (intervalo mais alto) (BP03)>Nome: <TM Road Carrier US 1>Critério de pesquisa:<TMROADCARRUS> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima: Forma jurídica: <01 (Corporação) >Salve as entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Clique em Comutar entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua uma nova Função PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar em função PN.Na guia Endereço para função de PN Agente de frete, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade:<nome da cidade>País:<nome do país>Região (estado, província, condado):<nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número):<número do telefone com código de discagem>E-mail: <Endereço de e-mail>Nota Valores de exemplo com localização dos EUA para os campos acima:Rua:<Windgap Ave>Código postal da cidade:<95206>Cidade:<Pittsburgh>País: <EUA>Região (estado, província, país):<PA>Fuso horário:<EST>Idioma: <EN>Telefone (código de discagem + número): <412-264-5632>E-mail: <info@17386001.com> |  |  |
| 7 | Função Inserir dados de transações de pagamento para transportadora | Na guia Transações de pagamento para a função de PN Agente de frete, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve as entradas.Nota Valores de exemplo com localizações dos EUA para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <790133> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN. Em seguida, execute as seguintes etapas:Clique em Compras.Insira o seguinte valor no campo Organização de compras: <organização de compras>Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compradores: <valor Grupo de compradores>Grp.esq.forn.: <valor>Salve as entradas.Nota Valores de exemplo com localização dos EUA para os campos acima:Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função PN Fornecedor (Contab. financeira) (FLVN00) selecionando-a na lista de opções.Modificar na função PNClique em Empresa.Insira a Empresa: <Empresa>Pressione Enter.Insira as seguintes informações na guia respectiva:Fornecedor: Administração de contas.Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Nota Valores de exemplo com localização dos EUA para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Insira as seguintes informações na guia Correspondência de fornecedores:Abreviatura de responsável: <valor>Conta com fornecedor <valor>Nota Valores de exemplo com localização dos EUA para os campos acima:Abreviatura de responsável: <01>Conta com fornecedor <1710-CARR1> |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete do parceiro de negócios (rodoviário) para o processo de liquidação automática de entrada de mercadorias (LAEM)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. A transportadora está atribuída a uma ordem de transporte (ordem de frete). Este agente de frete é usado principalmente para o cenário Liquidação automática de entrada de mercadorias (LAEM), onde a liquidação automática de faturas é efetuada, sem esperar por uma fatura de agente de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Clique em Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios(BP) é exibida. |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função PN é preenchido pelo sistema com a função Parceiro de negócios (Ger.). Mantenha esta configuração.Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Nota Consulte a seção Dados mestre, Dados organizacionais e Outros dados no cenário de 3 EP – Consolidação de transporte baseada na ordem para selecionar os valores corretos.Exemplo de valores para os campos acima:Parceiro de negócios: <17386002>Agrupamento: <Numeração externa (intervalo mais alto) (BP03)>Nome: Faturamento próprio de agente de frete rodoviário TM – USCritério de pesquisa: <TMROADCARRSBUS> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima:Forma jurídica: <01 (Corporação) >Salve as entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Use o comutador entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua a nova função de PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar na função PN.Na guia Endereço, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade: <nome da cidade>País: <nome do país>Região (estado, província, país): <nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número): <número de telefone com o código de discagem>E-mail: <endereço de e-mail>Nota Exemplo de valores para os campos acima:Rua: <E Sweet Ave>Código postal da cidade: <58504>Cidade: <Bismarck>País: <EUA>Região (estado, província, país): <ND>Fuso horário: <MST>Idioma: <EN>Telefone (código de discagem + número): <999 254 3623>E-mail: <info@17386002.com> | A função do parceiro de negócios Agente de frete é adicionada. |  |
| 7 | Inserir dados das transações de pagamento para função Transportadora | Na guia Transações de pagamento, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve as entradas.Nota Exemplo de valores para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <102610> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN.Clique em Compras.Insira o valor no campo Organização de compras: <organização de compras>.Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compras: <valor>Grp.esq.forn.: <valor>AutoEvalGRSetmt Del: <selecione>Salve as entradas.Nota Exemplo de valores para os campos acima:Organização de compras: <1710>Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03>AutoEvalGRSetmt Del: <selecione> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função de PN Fornecedor (cont.financeira) (FLVN00), selecionando-a na lista de opções Modificar na função PN.Clique em Empresa.Insira a Empresa: <Empresa>Pressione Enter.Preencha as seguintes informações na guia Fornecedor: Gerenciamento de contas:Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Nota Exemplo de valores para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Preencha as seguintes informações na guia Fornecedor: Correspondência:Sigla respons.: <valor>Conta com fornecedor <valor>Nota Exemplo de valores para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR2>. |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete parceiro de negócios (ferroviário) para processo de revisão de faturas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. A transportadora está atribuída a uma ordem de transporte (ordem de frete). Este agente de frete é utilizado principalmente no processo de revisão de faturas no qual os montantes da fatura do agente de frete são comparados com os custos de transporte previstos na ordem de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Atualizar parceiro de negócios(BP) | É aberta uma nova janela que exibe a tela Atualizar parceiro de negócios (PN). |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração. Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Valores de exemplo com localização dos EUA para os campos acima:Parceiro de negócios:<17386201>Agrupamento:<numeração numérica externa (intervalo mais alto) (BP03)>Nome: <TM Rail Carrier US 1>Critério de pesquisa:<TMRAILCARRUS1> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima: Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Clique em Comutar entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua uma nova Função PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar em função PN.Na guia Endereço para função de PN Agente de frete, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade:<nome da cidade>País:<nome do país>Região (estado, província, condado):<nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número):<número do telefone com código de discagem>E-mail: <Endereço de e-mail>Valores de exemplo com localização dos EUA para os campos acima:Rua:<Windgap Ave>Código postal da cidade:<95206>Cidade:<Pittsburgh>País: <EUA>Região (estado, província, país):<PA>Fuso horário:<EST>Idioma: <EN>Telefone (código de discagem + número): <412-264-5632>E-mail: <info@17386201.com> |  |  |
| 7 | Função Inserir dados de transações de pagamento para transportadora | Na guia Transações de pagamento para a função de PN Agente de frete, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Valores de exemplo com localizações dos EUA para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <790133> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN. Em seguida, execute as seguintes etapas:Clique em Compras.Insira o seguinte valor no campo Organização de compras: <organização de compras>Clique em Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compradores: <valor Grupo de compradores>Grp.esq.forn.: <valor>Salve suas entradas.Valores de exemplo com localização dos EUA para os campos acima:Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função PN Fornecedor (Contab. financeira) (FLVN00) selecionando-a na lista de opções.Modificar na função PNClique em EmpresaInsira a Empresa: <código da empresa>Pressione Enter.Insira as seguintes informações na guia respectiva:Fornecedor: Administração de contas.Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Valores de exemplo com localização dos EUA para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Insira as seguintes informações na guia Correspondência de fornecedores:Abrev.respons.: <valor>Conta com fornecedor <valor>Valores de exemplo com localização dos EUA para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR201> |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete do parceiro de negócios (ferroviário) para o processo de liquidação automática de entrada de mercadorias (LAEM)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. A transportadora está atribuída a uma ordem de transporte (ordem de frete). Este agente de frete é usado principalmente para o cenário Liquidação automática de entrada de mercadorias (LAEM), onde a liquidação automática de faturas é efetuada, sem esperar por uma fatura de agente de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios(BP) é exibida. |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função PN é preenchido pelo sistema com a função Parceiro de negócios (Ger.). Mantenha esta configuração.Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Consulte a seção Dados mestre, Dados organizacionais e Outros dados no cenário de 3 EP – Consolidação de transporte baseada na ordem para selecionar os valores corretos.Exemplo de valores para os campos acima:Parceiro de negócios: <17386202>Agrupamento: <Numeração externa (intervalo mais alto) (BP03)>Nome: <Faturamento próprio de agente de frete ferroviário TM - US>Critério de pesquisa: <TMRAILCARRSBUS> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima:Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Use o comutador entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua a nova função de PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar na função PN.Na guia Endereço, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade: <nome da cidade>País: <nome do país>Região (estado, província, país): <nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número): <número de telefone com o código de discagem>E-mail: <endereço de e-mail>Exemplo de valores para os campos acima:Rua: <E Sweet Ave>Código postal da cidade: <58504>Cidade: <Bismarck>País: <EUA>Região (estado, província, país): <ND>Fuso horário: <MST>Idioma: <EN>Telefone (código de discagem + número): <999 254 3623>E-mail: <info@17386202.com> | A função do parceiro de negócios Agente de frete é adicionada. |  |
| 7 | Função Inserir dados de transações de pagamento para agente de frete | Na guia Transações de pagamento, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Exemplo de valores para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <102610> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN.Clique em Compras.Insira o valor no campo Organização de compras: <organização de compras>.Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compras: <valor>Grp.esq.forn.: <valor>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar>Salve suas entradas.Exemplo de valores para os campos acima:Organização de compras: <1710>Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função de PN Fornecedor (cont.financeira) (FLVN00), selecionando-a na lista de opções Modificar na função PN.Clique em Empresa.Insira a Empresa: <código da empresa>Pressione Enter.Preencha as seguintes informações na guia Fornecedor: Gerenciamento de contas:Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Exemplo de valores para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Preencha as seguintes informações na guia Fornecedor: Guia Correspondência:Abrev. respons.: <valor>Conta com fornecedor <valor>Exemplo de valores para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR202>. |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete de parceiro de negócios (marítimo) para processo de verificação de faturas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete) como agente de frete executante/emissor da fatura no nível da etapa. Este agente de frete é usado principalmente no processo de verificação de faturas no qual os montantes da fatura do agente de frete são comparados com os custos de transporte previstos calculados na reserva de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Atualizar parceiro de negócios(BP) | É aberta uma nova janela que exibe a tela Atualizar parceiro de negócios (PN). |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração. Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Valores de exemplo com localização dos EUA para os campos acima:Parceiro de negócios:<17386301>Agrupamento:<numeração numérica externa (intervalo mais alto) (BP03)>Nome: <Agente de frete marítimo TM EUA 1>Critério de pesquisa:<TMOCEANCARRUS1> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima: Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Clique em Comutar entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua uma nova Função PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar em função PN.Na guia Endereço para função de PN Agente de frete, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade:<nome da cidade>País:<nome do país>Região (estado, província, condado):<nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número):<número do telefone com código de discagem>E-mail: <Endereço de e-mail>Valores de exemplo com localização dos EUA para os campos acima:Rua:<5301 Waterford at Blue Lagoon>Código postal da cidade:<33126>Cidade:<Miami>País: <EUA>Região (estado, província, condado):<FL>Fuso horário:<EST>Idioma: <EN>Telefone (código de discagem + número): <412-264-5632>E-mail: <info@17386301.com> |  |  |
| 7 | Função Inserir dados de transações de pagamento para transportadora | Na guia Transações de pagamento para a função de PN Agente de frete, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Valores de exemplo com localizações dos EUA para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <790133> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN. Em seguida, execute as seguintes etapas:Clique em Compras.Insira o seguinte valor no campo Organização de compras: <organização de compras>Clique em Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compradores: <valor Grupo de compradores>Grp.esq.forn.: <valor>Salve suas entradas.Valores de exemplo com localização dos EUA para os campos acima:Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função PN Fornecedor (Contab. financeira) (FLVN00) selecionando-a na lista de opções.Modificar na função PNClique em EmpresaInsira a Empresa: <código da empresa>Pressione Enter.Insira as seguintes informações na guia respectiva:Fornecedor: Administração de contas.Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Valores de exemplo com localização dos EUA para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Insira as seguintes informações na guia Correspondência de fornecedores:Abrev.respons.: <valor>Conta com fornecedor <valor>Valores de exemplo com localização dos EUA para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR301> |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete do parceiro de negócios (marítimo) para o processo de liquidação automática de entrada de mercadorias (LAEM)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete) como agente de frete executante/emissor da fatura no nível da etapa. Este agente de frete é usado principalmente para o cenário Liquidação automática de entrada de mercadorias (LAEM), onde a liquidação automática de faturas é efetuada, sem esperar por uma fatura de agente de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios(BP) é exibida. |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função PN é preenchido pelo sistema com a função Parceiro de negócios (Ger.). Mantenha esta configuração.Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Consulte a seção Dados mestre, Dados organizacionais e Outros dados no cenário de 3 EP – Consolidação de transporte baseada na ordem para selecionar os valores corretos.Exemplo de valores para os campos acima:Parceiro de negócios: <17386302>Agrupamento: <Numeração externa (intervalo mais alto) (BP03)>Nome: <Faturamento automático do agente de frete marítimo TM EUA 2>Critério de pesquisa: <TMOCEANCARRSBUS2> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima:Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Use o comutador entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua a nova função de PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar na função PN.Na guia Endereço, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade: <nome da cidade>País: <nome do país>Região (estado, província, país): <nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número): <número de telefone com o código de discagem>E-mail: <endereço de e-mail>Exemplo de valores para os campos acima:Rua: <888 Brannan Street>Código postal da cidade: <94103>Cidade: <San Francisco>País: <EUA>Região (estado, província, país): <CA>Fuso horário: <PST>Idioma: <EN>Telefone (código de discagem + número): <999 254 3623>E-mail: <info@17386302.com> | A função do parceiro de negócios Agente de frete é adicionada. |  |
| 7 | Função Inserir dados de transações de pagamento para agente de frete | Na guia Transações de pagamento, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Exemplo de valores para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <102610> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN.Clique em Compras.Insira o valor no campo Organização de compras: <organização de compras>.Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compras: <valor>Grp.esq.forn.: <valor>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar>Salve suas entradas.Exemplo de valores para os campos acima:Organização de compras: <1710>Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função de PN Fornecedor (cont.financeira) (FLVN00), selecionando-a na lista de opções Modificar na função PN.Clique em Empresa.Insira a Empresa: <código da empresa>Pressione Enter.Preencha as seguintes informações na guia Fornecedor: Gerenciamento de contas:Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Exemplo de valores para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Preencha as seguintes informações na guia Fornecedor: Guia Correspondência:Abrev. respons.: <valor>Conta com fornecedor <valor>Exemplo de valores para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR302>. |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete parceiro de negócios (agente de frete) para processo de revisão de faturas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar um agente de frete de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete). Este agente de frete é usado principalmente para o processo de subcontratação e para a organização da execução do transporte. O agente de frete é pago pelo seu serviço para organizar o transporte.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Atualizar parceiro de negócios(BP) | É aberta uma nova janela que exibe a tela Atualizar parceiro de negócios (PN). |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração. Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Valores de exemplo com localização dos EUA para os campos acima:Parceiro de negócios:<17386401>Agrupamento:<numeração numérica externa (intervalo mais alto) (BP03)>Nome: <Agente de frete TM – EUA>Critério de pesquisa:<TMOCEANFORWUS1> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima: Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Clique em Comutar entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua uma nova Função PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar em função PN.Na guia Endereço para função de PN Agente de frete, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade:<nome da cidade>País:<nome do país>Região (estado, província, condado):<nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número):<número do telefone com código de discagem>E-mail: <Endereço de e-mail>Valores de exemplo com localização dos EUA para os campos acima:Rua:<131 Aberdeen Dr.>Código postal da cidade:<92007>Cidade:<CARDIFF BY THE SEA>País: <EUA>Região (estado, província, condado):<CA>Fuso horário:<PST>Idioma: <EN>Telefone (código de discagem + número): <412-264-5632>E-mail: <info@17386401.com> |  |  |
| 7 | Função Inserir dados de transações de pagamento para transportadora | Na guia Transações de pagamento para a função de PN Agente de frete, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Valores de exemplo com localizações dos EUA para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <790133> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN. Em seguida, execute as seguintes etapas:Clique em Compras.Insira o seguinte valor no campo Organização de compras: <organização de compras>Clique em Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compradores: <valor Grupo de compradores>Grp.esq.forn.: <valor>Salve suas entradas.Valores de exemplo com localização dos EUA para os campos acima:Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função PN Fornecedor (Contab. financeira) (FLVN00) selecionando-a na lista de opções.Modificar na função PNClique em EmpresaInsira a Empresa: <código da empresa>Pressione Enter.Insira as seguintes informações na guia respectiva:Fornecedor: Administração de contas.Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Valores de exemplo com localização dos EUA para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Insira as seguintes informações na guia Correspondência de fornecedores:Abrev.respons.: <valor>Conta com fornecedor <valor>Valores de exemplo com localização dos EUA para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR401> |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar agente de frete do parceiro de negócios (agente de frete) para o processo de faturamento automático de entrada de mercadorias (FAEM)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar um agente de frete de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete). Este agente de frete é usado principalmente para o processo de subcontratação e para a organização da execução do transporte. O agente de frete é pago pelo seu serviço para organizar o transporte. Esse agente de frete é usado principalmente para o cenário Faturamento automático de entrada de mercadorias (FAEM), no qual a liquidação automática de faturas é efetuada sem esperar por uma fatura de agente de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios(BP) é exibida. |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função PN é preenchido pelo sistema com a função Parceiro de negócios (Ger.). Mantenha esta configuração.Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Consulte a seção Dados mestre, Dados organizacionais e Outros dados no cenário de 3 EP – Consolidação de transporte baseada na ordem para selecionar os valores corretos.Exemplo de valores para os campos acima:Parceiro de negócios: <17386402>Agrupamento: <Numeração externa (intervalo mais alto) (BP03)>Nome: <Faturamento próprio de agente de frete TM – EUA>Critério de pesquisa: <TMOCEANFORWSBUS1> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima:Forma jurídica: <01 (Corporação) >Salve suas entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Use o comutador entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua a nova função de PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar na função PN.Na guia Endereço, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade: <nome da cidade>País: <nome do país>Região (estado, província, país): <nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número): <número de telefone com o código de discagem>E-mail: <endereço de e-mail>Exemplo de valores para os campos acima:Rua: <2601 Westheimer Road>Código postal da cidade: <77098>Cidade: <Houston>País: <EUA>Região (estado, província, país): <TX>Fuso horário: <CST>Idioma: <EN>Telefone (código de discagem + número): <999 254 3623>E-mail: <info@17386402.com> | A função do parceiro de negócios Agente de frete é adicionada. |  |
| 7 | Função Inserir dados de transações de pagamento para agente de frete | Na guia Transações de pagamento, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve suas entradas.Exemplo de valores para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <102610> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN.Clique em Compras.Insira o valor no campo Organização de compras: <organização de compras>.Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compras: <valor>Grp.esq.forn.: <valor>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar>Salve suas entradas.Exemplo de valores para os campos acima:Organização de compras: <1710>Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03>Aval.autom.EM fornmto.p/aval. de entrada de mercadorias: <selecionar> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função de PN Fornecedor (cont.financeira) (FLVN00), selecionando-a na lista de opções Modificar na função PN.Clique em Empresa.Insira a Empresa: <código da empresa>Pressione Enter.Preencha as seguintes informações na guia Fornecedor: Gerenciamento de contas:Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Exemplo de valores para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Preencha as seguintes informações na guia Fornecedor: Guia Correspondência:Abrev. respons.: <valor>Conta com fornecedor <valor>Exemplo de valores para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR402>. |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar transportadora de parceiro de negócios (aérea) para processo de verificação de faturas

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete) como agente de frete executante/emissor da fatura no nível da etapa. Este agente de frete é usado principalmente no processo de verificação de faturas no qual os montantes da fatura do agente de frete são comparados com os custos de transporte previstos calculados na reserva de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Atualizar parceiro de negócios(BP) | É aberta uma nova janela que exibe a tela Atualizar parceiro de negócios (PN). |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função de PN é preenchido pelo sistema com a função Parceiro de negócios (geral). Mantenha esta configuração. Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Valores de exemplo com localização dos EUA para os campos acima:Parceiro de negócios:<17386501>Agrupamento:<numeração numérica externa (intervalo mais alto) (BP03)>Nome: <TM Airline US 1>Critério de pesquisa:<TMAIRLINEUS1> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima: Forma jurídica: <01 (Corporação) >Salve as entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Clique em Comutar entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua uma nova Função PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar em função PN.Na guia Endereço para função de PN Agente de frete, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade:<nome da cidade>País:<nome do país>Região (estado, província, condado):<nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número):<número do telefone com código de discagem>E-mail: <Endereço de e-mail>Valores de exemplo com localização dos EUA para os campos acima:Rua:<5301 Waterford at Blue Lagoon>Código postal da cidade:<33126>Cidade:<Miami>País: <EUA>Região (estado, província, condado):<FL>Fuso horário:<EST>Idioma: <EN>Telefone (código de discagem + número): <412-264-5632>E-mail: <info@17386501.com> |  |  |
| 7 | Função Inserir dados de transações de pagamento para transportadora | Na guia Transações de pagamento para a função de PN Agente de frete, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve as entradas.Valores de exemplo com localizações dos EUA para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <790133> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN. Em seguida, execute as seguintes etapas:Clique em Compras.Insira o seguinte valor no campo Organização de compras: <organização de compras>Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compradores: <valor Grupo de compradores>Grp.esq.forn.: <valor>Salve as entradas.Valores de exemplo com localização dos EUA para os campos acima:Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função PN Fornecedor (Contab. financeira) (FLVN00) selecionando-a na lista de opções.Modificar na função PNClique em Empresa.Insira a Empresa: <Empresa>Pressione Enter.Insira as seguintes informações na guia respectiva:Fornecedor: Administração de contas.Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Valores de exemplo com localização dos EUA para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Insira as seguintes informações na guia Correspondência de fornecedores:Sigla respons.: <valor>Conta com fornecedor <valor>Valores de exemplo com localização dos EUA para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR501> |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

### Criar transportadora de parceiro de negócios (aéreo) para o processo Faturamento automático de entrada de mercadorias (FAEM)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar uma transportadora de parceiro de negócios para permitir a execução do transporte. O agente de frete está atribuído a uma ordem de transporte (reserva de frete) como agente de frete executante/emissor da fatura no nível da etapa. Este agente de frete é usado principalmente para o cenário Liquidação automática de entrada de mercadorias (LAEM), onde a liquidação automática de faturas é efetuada, sem esperar por uma fatura de agente de frete.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre – Dados do parceiro de negócios. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Atualizar parceiro de negócios(BP). | A tela Atualizar parceiro de negócios(BP) é exibida. |  |
| 3 | Criar uma Organização de PN | Clique em Organização. | A tela Criar organização é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Parceiro de negócios: <insira um ID do parceiro de negócios que comece com um caractere>Agrupamento: <numeração alfanumérica externa>O campo Criar em função PN é preenchido pelo sistema com a função Parceiro de negócios (Ger.). Mantenha esta configuração.Na guia Endereço, insira as seguintes informações:Nome: <nome da organização>Critério de pesquisa: <critério de pesquisa para parceiro de negócios>Consulte a seção Dados mestre, Dados organizacionais e Outros dados no cenário de 3 EP – Consolidação de transporte baseada na ordem para selecionar os valores corretos.Exemplo de valores para os campos acima:Parceiro de negócios: <17386502>Agrupamento: <Numeração externa (intervalo mais alto) (BP03)>Nome: <TM Airline Self-Billing US 2>Critério de pesquisa: <TMAIRLINESBUS2> |  |  |
| 5 | Inserir dados de identificação | Na guia Identificação da função Parceiro de negócios, insira as seguintes informações:Forma jurídica: <forma jurídica da organização>Exemplo de valores para o campo acima:Forma jurídica: <01 (Corporação) >Salve as entradas. |  |  |
| 6 | Atribuir nova função Agente de frete e inserir dados do endereço | Use o comutador entre Exibir e Modificar para garantir que você esteja no modo de modificação. Atribua a nova função de PN Agente de frete (CRM010), selecionando-a na lista de opções Modificar na função PN.Na guia Endereço, insira as seguintes informações:Rua: <nome da rua>Código postal da cidade: <código postal da cidade>Cidade: <nome da cidade>País: <nome do país>Região (estado, província, país): <nome da região>Fuso horário: <fuso horário>Idioma: <nome do idioma>Telefone (código de discagem + número): <número de telefone com o código de discagem>E-mail: <endereço de e-mail>Exemplo de valores para os campos acima:Rua: <888 Brannan Street>Código postal da cidade: <94103>Cidade: <San Francisco>País: <EUA>Região (estado, província, país): <CA>Fuso horário: <PST>Idioma: <EN>Telefone (código de discagem + número): <999 254 3623>E-mail: <info@17386502.com> | A função do parceiro de negócios Agente de frete é adicionada. |  |
| 7 | Função Inserir dados de transações de pagamento para agente de frete | Na guia Transações de pagamento, insira as seguintes informações:País: <chave do banco>Chave do banco: <chave do banco>Conta bancária: <número da conta bancária>Salve as entradas.Exemplo de valores para os campos acima:País: <EUA>Chave do banco: <150350300>Conta bancária: <102610> |  |  |
| 8 | Atribuir nova função de fornecedor e inserir dados do parceiro de negócios | Atribua nova função de PN Fornecedor (FLVN01) selecionando-a na lista de opções Modificar na função PN.Clique em Compras.Insira o valor no campo Organização de compras: <organização de compras>.Pressione Enter.Preencha as seguintes informações na guia Dados de compras:Moeda da ordem: <nome da moeda>Condições de pagamento: <condições de pagamento>Condições de expedição: <nome da condição de expedição>Grupo de compras: <valor>Grp.esq.forn.: <valor>Faturamto.autom.de entr.mercad: <selecionar>Salve suas entradas.Exemplo de valores para os campos acima:Organização de compras: <1710>Moeda da ordem: <USD>Condições de pagamento: <0004>Condições de expedição: <01>Grupo de compradores: <005>Grp.esq.forn.: <03>Faturamto.autom.de entr.mercad: <selecionar> |  |  |
| 9 | Atribuir nova função de fornecedor FI e inserir dados do parceiro de negócios | Atribua a nova função de PN Fornecedor (cont.financeira) (FLVN00), selecionando-a na lista de opções Modificar na função PN.Clique em Empresa.Insira a Empresa: <Empresa>Pressione Enter.Preencha as seguintes informações na guia Fornecedor: Gerenciamento de contas:Conta de reconciliação: <Número da conta>Chave de ordenação: <valor>Exemplo de valores para os campos acima:Empresa: <1710>Conta de reconciliação: <21100000>Chave de ordenação: <009> |  |  |
| 10 | Inserir dados de correspondência do fornecedor | Preencha as seguintes informações na guia Fornecedor: Correspondência:Sigla respons.: <valor>Conta com fornecedor <valor>Exemplo de valores para os campos acima:Sigla respons.: <01>Conta com fornecedor <1710-CARR502>. |  |  |
| 11 | Salvar os dados | Clique em Salvar. | O sistema exibe uma mensagem indicando que o objeto foi salvo. |  |

## Anexo

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
> Flagged while digesting this document, not verified: Last air carrier section is titled FAEM but its objective and variants refer to LAEM; naming LAEM vs FAEM is inconsistent across sections.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Example data uses US localisation inside a Portuguese-language script; section 4.1 mentions BP numbering 'alfanumérica externa' while the example uses numeric BP03.

> [!warning] Conflict
> Flagged while digesting this document, not verified: Overview table lists only the first segment (road, invoice review) while ten procedures exist.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-carrier-master-mds-4de-407]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-411]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-4de-master-data-script-create-carrier-master-409]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-creacion-de-maestro-de-transportistas-mds-4de]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/4DE_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 66,581 chars in the whole document
