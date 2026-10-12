---
id: 03-financial-accounting-and-close/criar-mandato-sepa-mds-bnv-686
title: Criar mandato SEPA – MDS (BNV) (BNV_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data test script (BNV) for SAP S/4HANA Cloud Public Edition 2608: creating, displaying, listing and administering SEPA mandates."
cluster: 03-financial-accounting-and-close
tags: [kb/financial-accounting-and-close, topic/direct-debit-and-sepa-mandates]
aliases: [BNV_S4CLD2608_Master_Data_PT_XX]
keywords: [Direct Debit and SEPA Mandates, sepa mandates, sepa direct debit, master data scripts, mandate display, mandate lists, mandate administration, business roles, test procedures, customer master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-686
topic: 03-financial-accounting-and-close/direct-debit-and-sepa-mandates
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar mandato SEPA – MDS (BNV) (BNV_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Direct Debit and SEPA Mandates** in Financial Accounting and Close. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mandato SEPA – MDS (BNV) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894084)

[2 Pré-requisitos 3](#_Toc233894085)

[2.1 Acesso ao sistema 3](#_Toc233894086)

[2.2 Funções 3](#_Toc233894087)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894088)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894089)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894090)

[3 Tabela de síntese 5](#_Toc233894091)

[4 Procedimentos de teste 6](#_Toc233894092)

[4.1 Criar mandatos SEPA 6](#_Toc233894093)

[4.2 Exibir mandatos SEPA 7](#_Toc233894094)

[4.3 Exibir listas de mandatos SEPA 8](#_Toc233894095)

[4.4 Administrar mandatos SEPA 9](#_Toc233894096)

## Objetivo

Neste documento você encontra uma descrição sobre como criar o mandato SEPA (espaço único de pagamentos em euros) para seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados relevantes para o appliance SAP S/4HANA Cloud Public Edition. Os campos que não são relevantes para o escopo do conteúdo do SAP S/4HANA Cloud Public Edition, uma vez que foram fornecidos pelo SAP Best Practices, não estão descritos neste documento.

Um mandato SEPA é preenchido pelo devedor (um cliente adquirindo mercadorias ou serviços) para autorizar o credor (um comerciante varejista ou fornecedor de serviços) a receber pagamentos por meio de débito direto SEPA. Ao mesmo tempo, o mandato SEPA inclui a autorização do banco do devedor para pagar essas coletas.

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
| Contador da contabilidade de clientes | SAP_BR_AR_ACCOUNTANT | Contabilidade de clientes | SAP_BR_AR_ACCOUNTANT |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre de cliente são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Mandato | Parceiro de negócios | Número do cliente, IBAN e SWIFT/BIC | Só válido para clientes europeus com nota de débito SEPA. | Número do cliente: <seu número> |
| Mandato | Empresa | Empresa | Os dados da empresa podem existir para cada ID da empresa da sua estrutura empresarial para a qual é utilizado o mandato SEPA. | Empresa: seu código |

### Dados mestre obrigatórios e opcionais

A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre do centro de lucro.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Número do cliente | Primeira tela | Obrigatório |  |
| Empresa | Primeira tela | Obrigatório |  |

### Parâmetros principais para a criação de dados

Esta seção descreve alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um mandato SEPA:

Empresa:

Por exemplo, XX10.

Parceiro de negócios – Cliente:

Por exemplo, número do cliente XX100003.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App SAP Fiori | Resultados esperados |
| --- | --- | --- | --- |
| [Criar mandatos SEPA](#unique_9) [página ] 6 | Contador da contabilidade de clientes | Criar mandatos SEPA(FSEPA_M1) | O mandato SEPA é criado. |
| [Exibir mandatos SEPA](#unique_10) [página ] 7 | Contador da contabilidade de clientes | Exibir mandatos SEPA(FSEPA_M3) | O mandato SEPA é exibido. |
| [Exibir listas de mandatos SEPA](#unique_11) [página ] 8 | Contador da contabilidade de clientes | Exibir listas de mandatos SEPA(FSEPA_M4) | A lista de mandatos SEPA é exibida. |
| [Administrar mandatos SEPA](#unique_12) [página ] 9 | Contador da contabilidade de clientes | Administrar mandatos SEPA(F5158) | O mandato SEPA é exibido. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar mandatos SEPA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador da contabilidade de clientes. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar mandatos SEPA(FSEPA_M1). | O app é aberto. |  |
| 3 | Mudar aplicação | Na tela Criar mandato: 1ª tela, selecione Comutar aplicação. Selecione Contabilidade financeira na caixa de diálogo Selecionar aplicação e selecione Continuar. |  |  |
| 4 | ID de pagador | No campo Cliente, insira XX100003. |  |  |
| 5 | ID de recebedor do pagamento | No campo Empresa pagadora, insira XX10 e pressione Enter para continuar.Nota Se uma tela de mandatos for exibida com status ativado, isso significa que esses mandatos já foram criados. Selecione um mandato e clique em Continuar para verificar e alterar o mandato. | A tela Criar mandato: tela detalhada é exibida. |  |
| 6 | Dados suplementares | Selecione Dados suplementares. | Os campos são preenchidos automaticamente. |  |
| 7 | Dados básicos | Na guia Dados básicos, efetue as seguintes entradas:Status: InseridoCampo de seleção mandato B2B: selecionarLocal de assinatura: <localização>Data de assinatura: <Data> |  |  |
| 8 | Pagador | Na guia Pagador, seção Dados bancários do pagador, verifique se os campos IBAN e SWIFT/BIC estão preenchidos.Nota Estes dados fazem parte de seus dados mestre de cliente e já deveriam ter sido criados e disponibilizados. |  |  |
| 9 | Recebedor do pagamento | Na guia Recebedor do pagamento, efetue a seguinte entrada:ID do credor: <ID do credor>: |  |  |
| 10 | Salvar os dados | Salve suas entradas. | A mensagem do sistema Mandato 0000000000## criado é exibida. |  |

### Exibir mandatos SEPA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Já existe um mandato.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador da contabilidade de clientes. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Exibir mandatos SEPA(FSEPA_M3). | O app é aberto. |  |
| 3 | ID de pagador | No campo Cliente, insira XX100003. |  |  |
| 4 | ID de recebedor do pagamento | No campo Empresa pagadora, insira XX10 e pressione Enter para continuar. | A visão Exibir mandato: tela detalhada é exibida. |  |
| 5 | Navegação | Selecione as diferentes guias:Dados básicos, Pagador e/ou Recebedor do pagamento. | As informações são exibidas. |  |
| 6 | Voltar | Clique em Encerrar. |  |  |

### Exibir listas de mandatos SEPA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Já existe um mandato.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador da contabilidade de clientes. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Exibir listas de mandatos SEPA(FSEPA_M4). | O app é aberto. |  |
| 3 | Clicar em Executar | Se uma caixa de diálogo for exibida, selecione Contabilidade financeira na caixa de diálogo Selecionar aplicação e, em seguida, clique em Continuar.Se nenhuma caixa de diálogo for exibida, verifique na guia Seleções técnicas se o campo Aplicação está definido como Contabilidade financeira.Clique em Executar. | É aberta a tela Mandatos que exibe uma lista dos mandatos existentes. |  |
| 4 | Selecionar um mandato | Selecione um Número de referência do mandato. | É exibida a tela Modificar mandatos listando os detalhes do mandato selecionado. |  |
| 5 | Revisar | Embora seja possível alterar os dados do mandato quando necessário, não altere nenhum dado, só revise o mandato. |  |  |
| 6 | Sair | Clique em Continuar duas vezes ou Cancelar para sair. |  |  |

### Administrar mandatos SEPA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Já existe um mandato.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador da contabilidade de clientes. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar mandatos SEPA(F5158). | O app é aberto. |  |
| 3 | Selecionar mandato | No campo Aplicação, selecione Contabilidade financeira. |  |  |
| 4 | Selecionar mandato | No campo Empresa pagadora, insira XX10.Selecione Ir.Selecione a linha que você deseja editar e, em seguida, Editar. | A tela Modificar mandato: detalhe é exibida. |  |
| 5 | Revisar e editar | Revisar e editar todos os campos disponíveis das seguintes guias:Dados básicosPagadorRecebedor do pagamento |  |  |
| 6 | Salvar as entradas | Selecione Salvar para salvar suas entradas. |  |  |

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
- related-to :: [[03-financial-accounting-and-close/crear-mandato-sepa-mds-bnv-684]]
- related-to :: [[03-financial-accounting-and-close/create-sepa-mandate-mds-bnv-683]]
- related-to :: [[03-financial-accounting-and-close/sepa-mandat-anlegen-sds-bnv-682]]
- related-to :: [[03-financial-accounting-and-close/sepa-mds-bnv-685]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNV_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 15,124 chars in the whole document
