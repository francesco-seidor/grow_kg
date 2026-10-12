---
id: 11-inventory-warehouse-and-transportation/script-de-dados-mestre-criar-dados-mestre-de-administracao-de-lotes-2z
title: Script de dados mestre - Criar dados mestre de administração de lotes (2ZW) (2ZW_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (2ZW): test steps to create batch management master data, search and derivation strategies."
cluster: 11-inventory-warehouse-and-transportation
tags: [kb/inventory-warehouse-and-transportation, topic/batch-management-master-data]
aliases: [2ZW_S4CLD2608_Master_Data_PT_XX]
keywords: [Batch Management Master Data, batch management, batch characteristics, batch classes, sort sequences, batch search strategies, batch derivation, master data scripts, business roles, test procedures]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-302
topic: 11-inventory-warehouse-and-transportation/batch-management-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar dados mestre de administração de lotes (2ZW) (2ZW_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Batch Management Master Data** in Inventory, Warehouse and Transportation. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar dados mestre de administração de lotes – MDS (2ZW) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893621)

[2 Pré-requisitos 3](#_Toc233893622)

[2.1 Acesso ao sistema 3](#_Toc233893623)

[2.2 Funções 3](#_Toc233893624)

[3 Tabela de síntese 4](#_Toc233893625)

[4 Procedimentos de teste 5](#_Toc233893626)

[4.1 Criar característica 5](#_Toc233893627)

[4.2 Criar classe 6](#_Toc233893628)

[4.3 Criar sequência de ordenação 7](#_Toc233893629)

[4.4 Criar registro de estratégia de pesquisa de lotes para administração de estoques 8](#_Toc233893630)

[4.5 Criar registros de estratégia de pesquisa de lotes para produção 10](#_Toc233893631)

[4.6 Criar registro de estratégia de pesquisa de lotes para vendas e distribuição 12](#_Toc233893632)

[4.7 Criar estratégia de derivação para material emissor 14](#_Toc233893633)

[4.8 Criar estratégia de derivação para material receptor 15](#_Toc233893634)

## Objetivo

Os dados mestre de administração de lotes incluem especificações de lote, sequências de ordenação (regras de ordenação) e registros de estratégia de pesquisa de lotes na determinação de lote.

As especificações de lote descrevem as propriedades técnicas, físicas e químicas de um lote. Você grava especificações de lote, por exemplo status do lote ou potência de ingrediente ativo, como características no sistema de classificação.

Você pode utilizar o sistema de classificação para atribuir as especificações de material ao material de um lote. Estas especificações de material estão atribuídas à mesma classe dos lotes dos materiais. Assim, você pode gravar os valores fixados de um lote com o respectivo intervalo de tolerância. Estes valores fixados são, por exemplo, utilizados no controle de qualidade ou durante a transação de entrada de mercadorias, se forem necessários para uma classificação imediata de um lote. Os valores também são utilizados para a verificação de usabilidade.

No material, você grava intervalos de destino para todas as características. Como lote pertence à mesma classe do material, o lote recebe automaticamente as características do material. Para cada lote, você insere os valores atuais exatos.

A determinação de lote ocorrendo em diferentes processos (administração de estoques, produção, vendas e distribuição) tem critérios diferentes. As sequências de ordenação e os registros de estratégia de pesquisa de lotes são necessários para atualizar os critérios.

A sequência de ordenação indica se os lotes no resultado da pesquisa da determinação de lote são ordenados em ordem crescente ou decrescente de valores da característica.

Em uma estratégia de pesquisa de lotes para a determinação de lote, você pode definir os valores de acordo com os quais o sistema deve encontrar lotes, incluindo atributos para o processo (por exemplo, tipo de movimento, tipo de ordem ou centro) e número do material. Somente quando os registros de condições forem cumpridos, esses lotes poderão ser mais ordenados e determinados com base em sequências de ordenação e especificações de lote.

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
| Responsável pela lista técnica | SAP_BR_BOM_ENGINEER | Listas técnicas | SAP_BR_BOM_ENGINEER |  |
| Especialista em dados mestre - dados do lote | SAP_BR_BATCH_MASTER_SPCLST | Dados mestre - Lote | SAP_BR_BATCH_MASTER_SPCLST |  |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar característica](#unique_6) [página ] 5 | Responsável pela lista técnica | Administrar características(CT04) | A característica é criada. |
| [Criar classe](#unique_7) [página ] 6 | Responsável pela lista técnica | Administrar classes(CL02) | A classe é criada. |
| [Criar sequência de ordenação](#unique_8) [página ] 7 | Especialista em dados mestre - dados do lote | Criar sequência de ordenação(CU70) | A sequência de ordenação é criada. |
| [Criar registro de estratégia de pesquisa de lotes para administração de estoques](#unique_9) [página ] 8 | Especialista em dados mestre - dados do lote | Administrar estratégias de pesquisa - Administração de estoques(MBC2) | Os registros de estratégia de pesquisa de lotes são criados. |
| [Criar registros de estratégia de pesquisa de lotes para produção](#unique_10) [página ] 10 | Especialista em dados mestre - dados do lote | Administrar estratégias de pesquisa - Produção(COB2) | Os registros de estratégia de pesquisa de lotes são criados. |
| [Criar registro de estratégia de pesquisa de lotes para vendas e distribuição](#unique_11) [página ] 12 | Especialista em dados mestre - dados do lote | Administrar estratégias de pesquisa - Vendas e distribuição(VCH2) | Os registros de estratégia de pesquisa de lotes são criados. |
| [Criar estratégia de derivação para material emissor](#unique_12) [página ] 14 | Especialista em dados mestre - dados do lote | Administrar estratégias de derivação - Emissor(DVS2) | A estratégia de derivação para o material emissor é criada. |
| [Criar estratégia de derivação para material receptor](#unique_13) [página ] 15 | Especialista em dados mestre - dados do lote | Administrar estratégias de derivação - Destinatário(DVR2) | A estratégia de derivação para o material receptor é criada. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar característica

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de característica.

Procedimento

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar características(CT04).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Responsável pela lista técnica. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar características(CT04). | A tela Características é exibida.Nota Tela comum para o modo de criação, modificação e exibição. |  |
| 3 | Inserir nome de característica | Insira o seguinte e clique em Criar.Característica: <seu nome de característica> | As opções de tela Dados básicos são exibidas.Nota O valor no campo Início da validade é preenchido automaticamente. |  |
| 4 | Inserir dados básicos | Insira o seguinte e clique em Salvar:Seção Dados básicos:Descrição: <Insira sua descrição>Status: Liberado (padrão)Seção Formato:Tipo de data: <Selecione um formato>Seção Avaliação de valor:Selecione o botão de rádio Valor individual. | Nota Outros campos para formato selecionado são necessários na seção Formato. Atualizar de forma correspondente. |  |
| 5 | Inserir valores para verificação | Na guia Valores, na seção Intervalo de valores, insira os valores permitidos para esta característica. |  |  |
| 6 | Salvar a característica | Clique em Salvar. | A característica é criada. |  |

### Criar classe

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de classe.

Pré-requisito

Você deve completar a seção anterior, [Criar característica](#unique_6) [página ] 5, antes de continuar com esta seção.

Procedimento

Siga o procedimento abaixo caso seu acesso de usuário ofereça o app Administrar classes(CL02).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Responsável pela lista técnica. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar classes(CL02). | A tela Classe é exibida.Nota É uma tela comum para o modo de criação, alteração e exibição. |  |
| 3 | Inserir nome de classe | Efetue as seguintes entradas e clique em Criar:Classe: <nome da classe>Tipo de classe: 023 | A tela Criar classe é exibida.Nota O campo Início da validade é preenchido automaticamente com um valor. |  |
| 4 | Inserir dados básicos | Na guia Dados básicos, efetue as seguintes entradas:Na seção Dados básicos:Descrição: <descrição de classe>Status: Liberado |  |  |
| 5 | Inserir característica Guia | Selecione a guia Caract., efetue a seguinte entrada para atribuir características que você criou para esta classe, e pressione Enter:Na coluna Caract. :Caract.: <nome da característica> | Os campos Descrição e Tipo de dados das características são preenchidos automaticamente com valores. |  |

### Criar sequência de ordenação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de sequência de ordenação.

Pré-requisito

Você deve concluir a seção Criar característica antes de continuar com esta seção.

Procedimento

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar sequência de ordenação(CU70).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar sequência de ordenação(CU70). | A tela Criar sequência de ordenação é exibida. |  |
| 3 | Inserir nome da sequência de ordenação | Efetue as seguintes entradas e selecione o ícone Criar:Sequência de ordenação: <Nome da sequência de ordenação> | A tela Criar sequência de ordenação: Dados básicos é exibida. |  |
| 4 | Inserir dados básicos | Atualize a descrição ao lado do Nome da sequência de ordenação e selecione Características.Descrição: <Ordenar denominação subsequente> | A tela Criar sequência de ordenação: Características é exibida. |  |
| 5 | Inserir detalhes da sequência de ordenação | Clique em Novas entradas para atualizar as seguintes colunas e clique em Salvar:Característica: <nome da característica>Ordem crescente: XOrdem decrescente: ‘ ’ | A sequência de ordenação é criada.Nota Você pode indicar uma ordenação crescente ou decrescente. |  |

### Criar registro de estratégia de pesquisa de lotes para administração de estoques

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento fornece instruções para a criação de estratégias de pesquisa para determinação de lote.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | O launchpad do SAP Fiori é exibido. | Abra Administrar estratégias de pesquisa - Administração de estoques(MBC2). | A tela Modificar estratégia de pesquisa de lotes: 1ª tela é exibida. |  |
| 3 | Inserir tipo de estratégia | Efetue as seguintes entradas e selecione Modificar:Tipo de estratégia: <tipo de estratégia, por exemplo, YB11>Nota o tipo de estratégia é configurável pela IU de configuração self-service. | O pop-up combinação de chaves é exibido. |  |
| 4 | Selecionar combinação de chaves | No pop-up combinação de chaves, selecione uma das seguintes opções e escolha Selecionar:Tipo de movimento/centro/materialCentro/materialTipo de movimento/materialTipo de movimento/centroTipo de movimento | A tela Modificar PN: Número do lote (YB11): Seleção é exibida. | As Combinações de chaves são dependentes do Tipo de estratégia que você escolhe. Se houver somente uma combinação de chaves na sua estratégia selecionada, o popup não será exibido. |
| 5 | Inserir sua seleção | Para indicar seus registros, insira os seguintes atributos que são exibidos com base na combinação de chaves selecionada e clique em Executar:Tipo de movimento de mercadorias: <Tipo de movimento de mercadorias>Centro: <centro>Material: <Número do material> | A tela Modificar PN: Número do lote (YB11): Entrada rápida é exibida. |  |
| 6 | Inserir seu registro da estratégia em detalhes | Para criar um novo registro, você deve inserir as seguintes entradas e clicar em Salvar:Material: <Número do material>Se necessário, você também pode indicar os seguintes atributos para cada registro:Nº de partições de loteModificações permitidasDiálogo determinação de loteExibir UMQuantidade propostaFornecimento excessivo permitidoTipo de seleção |  |  |
| 7 | Atualizar critérios de seleção (opcional) | Para atualizar mais detalhadamente os critérios de seleção para o valor da característica do lote do material em um registro, selecione o registro e clique em critérios de seleção. | A tela Modificar PN: Classificação é exibida. |  |
| 8 | Atualizar sequência de ordenação (opcional) | Para atualizar a sequência de ordenação para registros específicos, selecione o registro clique em Ordenar. | A tela Modificar PN: Número do lote (YB11): Regra de ordenação é exibida. |  |

### Criar registros de estratégia de pesquisa de lotes para produção

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento fornece instruções para a criação de estratégias de pesquisa para determinação de lote.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar estratégias de pesquisa - Produção(COB2). | A tela Modificar estratégia de pesquisa de lotes: 1ª tela é exibida. |  |
| 3 | Inserir tipo de estratégia | Efetue as seguintes entradas e selecione Modificar:Tipo de estratégia: <tipo de estratégia, por exemplo, YB11>Nota O tipo de estratégia é configurável pela IU de configuração self-service. | A tela Modificar PN: Número do lote (YB11): Seleção é exibida.Nota A combinação de chaves não é mostrada porque há apenas uma combinação de chaves configurada para YB11 na produção |  |
| 4 | Inserir sua seleção | Para indicar seus registros, insira os seguintes atributos que são exibidos com base na combinação de chaves selecionada e clique em Executar:Tipo de ordem: <Tipo de ordem>Centro: <centro>Material: <Número do material> | A tela Modificar PN: Número do lote (YB11): Entrada rápida é exibida. | As Combinações de chaves são dependentes do Tipo de estratégia que você escolhe. Se houver somente uma combinação de chaves na sua estratégia selecionada, o popup não será exibido. |
| 5 | Inserir seu registro da estratégia em detalhes | Para criar um novo registro, você deve inserir as seguintes entradas e clicar em Salvar:Material: <Número do material>Se necessário, você também pode indicar os seguintes atributos para cada registro:Nº de partições de loteModificações permitidasDiálogo determinação de loteExibir UMQuantidade propostaFornecimento excessivo permitidoTipo de seleção |  |  |
| 6 | Atualizar critérios de seleção (opcional) | Para atualizar mais detalhadamente os critérios de seleção para o valor da característica do lote do material em um registro, selecione o registro e clique em critérios de seleção. | A tela Modificar PN: Classificação é exibida. |  |
| 7 | Atualizar sequência de ordenação (opcional) | Para atualizar a sequência de ordenação para registros específicos, selecione o registro clique em Ordenar. | A tela Modificar PN: Número do lote (YB11): Regra de ordenação é exibida. |  |

### Criar registro de estratégia de pesquisa de lotes para vendas e distribuição

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento fornece instruções para a criação de estratégias de pesquisa para determinação de lote.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar estratégias de pesquisa - Vendas e distribuição(VCH2). | A tela Modificar estratégia de pesquisa de lotes: 1ª tela é exibida. |  |
| 3 | Inserir tipo de estratégia | Efetue as seguintes entradas e selecione Modificar:Tipo de estratégia: <tipo de estratégia, por exemplo, YB11>Nota o tipo de estratégia é configurável pela IU de configuração self-service. | O pop-up combinação de chaves é exibido. |  |
| 4 | Selecionar combinação de chaves | No pop-up combinação de chaves, selecione uma das seguintes opções e escolha selecionar:Cliente/MaterialMaterial | A tela Modificar PN: Número do lote (YB11): Seleção é exibida. | As Combinações de chaves são dependentes do Tipo de estratégia que você escolhe. Se houver somente uma combinação de chaves na sua estratégia selecionada, o popup não será exibido. |
| 5 | Inserir sua seleção | Para indicar seus registros, insira os seguintes atributos que são exibidos com base na combinação de chaves selecionada e clique em Executar:Cliente: <ID do cliente>Material: <Número do material> | A tela Modificar PN: Número do lote (YB11): Entrada rápida é exibida. |  |
| 6 | Inserir seu registro da estratégia em detalhes | Para criar um novo registro, você deve inserir as seguintes entradas e clicar em Salvar:Material: <Número do material>Se necessário, você também pode indicar os seguintes atributos para cada registro:Nº de partições de loteModificações permitidasDiálogo determinação de loteExibir UMQuantidade propostaFornecimento excessivo permitidoTipo de seleção |  |  |
| 7 | Atualizar critérios de seleção (opcional) | Para atualizar mais detalhadamente os critérios de seleção para o valor da característica do lote do material em um registro, selecione o registro e clique em critérios de seleção. | A tela Modificar PN: Classificação é exibida. |  |
| 8 | Atualizar sequência de ordenação (opcional) | Para atualizar a sequência de ordenação para registros específicos, selecione o registro clique em Ordenar. | A tela Modificar PN: Número do lote (YB11): Regra de ordenação é exibida. |  |

### Criar estratégia de derivação para material emissor

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de registros de estratégia usados para determinar atributos para o material emissor durante a derivação do lote.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar estratégias de derivação - Emissor(DVS2). | A tela Derivação – modificar estratégia de pesquisa: 1ª tela é exibida. |  |
| 3 | Inserir tipo de estratégia | Efetue as seguintes entradas e clique em Modificar:Tipo de estratégia: <Tipo de estratégia> | O pop-up combinação de chaves é exibido. | Antes disso, você precisa concluir as seguintes etapas de configuração com base em suas necessidades:Intervalos de numeração para derivação do loteDeterminação de lotes emissores na derivação do lote |
| 4 | Selecionar combinação de chaves | No pop-up combinação de chaves, selecione uma das seguintes opções e escolha Selecionar:<Combinação de chaves 1><Combinação de chaves 2>… | A tela Modificar <tipo de estratégia>: A tela Seleção é exibida. | As Combinações de chaves são dependentes do Tipo de estratégia que você escolhe. |
| 5 | Inserir sua seleção | Para indicar seus registros, insira os seguintes atributos que são exibidos com base na Combinação de chaves escolhida e clique em Executar:Material emissor:<ID do material emissor><Campo-chave>: <Valor-chave>… | A tela Modificar <tipo de estratégia>: Entrada rápida é exibida. |  |
| 6 | Inserir registro da estratégia | Para criar um novo registro, você deve inserir as seguintes entradas e clicar em Salvar:Material emissor: <ID do material emissor>Para atualizar ainda mais os detalhes do material emissor, selecione um registro e clique em Detalhes. | A tela Modificar <tipo de estratégia>: Detalhes é exibida. |  |
| 7 | Atualizar detalhes de registro de estratégia | Na seção Atributos enviados (campos/caracts.), efetue as seguintes entradas e clique em Salvar:Atributo: <ID do material emissor>Campo: <selecionado por padrão>Característica: <não selecionado por padrão> |  |  |

### Criar estratégia de derivação para material receptor

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de registros de estratégia que são usados para determinar atributos para o material receptor durante a derivação do lote.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - dados do lote. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar estratégias de derivação - Destinatário(DVR2). | A tela Derivação – modificar estratégia de pesquisa: 1ª tela é exibida. |  |
| 3 | Inserir tipo de estratégia | Efetue as seguintes entradas e clique em Modificar:Tipo de estratégia: <Tipo de estratégia> | O pop-up combinação de chaves é exibido. | Antes disso, você precisa concluir as seguintes etapas de configuração com base em suas necessidades:Intervalos de numeração para derivação do loteDeterminação de lotes receptores na derivação do lote |
| 4 | Selecionar combinação de chaves | No pop-up combinação de chaves, selecione uma das seguintes opções e escolha Selecionar:<Combinação de chaves 1><Combinação de chaves 2>… | A tela Modificar <tipo de estratégia>: A tela Seleção é exibida. | As Combinações de chaves são dependentes do Tipo de estratégia que você escolhe. |
| 5 | Inserir sua seleção | Para indicar seus registros, insira os seguintes atributos que são exibidos com base na Combinação de chaves escolhida e clique em Executar:Material receptor: <ID do material receptor><Campo-chave>: <Valor-chave>… | A tela Modificar <tipo de estratégia>: Entrada rápida é exibida. |  |
| 6 | Inserir registro da estratégia | Para criar um novo registro, você deve inserir as seguintes entradas e clicar em Salvar:Material receptor: <ID do material receptor>Para atualizar ainda mais os detalhes do material receptor, selecione um registro e clique em Detalhes. | A tela Modificar <tipo de estratégia>: Detalhes é exibida. |  |
| 7 | Atualizar detalhes de registro de estratégia | Na guia Atributos, na seção Atributos recebidos (campos/características), insira as seguintes entradas e clique em Salvar:Atributo: <ID do material receptor>Campo: <selecionado por padrão>Característica: <não selecionado por padrão>Para atualizar as regras de cada atributo, selecione um atributo e clique na guia Regras. Em seguida, atualize as seguintes regras:Regras para controle de derivaçãoCampo emissor vazioSobregravar recep.Níveis na lista utilizações loteReceptor não enviaRegras para seleção de valores se existir mais de um emissorComparativoBooleanoCaracterísticas com vários valores |  |  |

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
- related-to :: [[11-inventory-warehouse-and-transportation/master-data-script-create-batch-management-master-data-mds-2zw-299]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-301]]
- related-to :: [[11-inventory-warehouse-and-transportation/mds-2zw-303]]
- related-to :: [[11-inventory-warehouse-and-transportation/script-de-datos-maestros-crear-datos-maestros-de-gestion-de-lotes-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2ZW_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 30,463 chars in the whole document
