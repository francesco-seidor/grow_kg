---
id: 12-production-and-manufacturing/criar-roteiro-mds-bnl-632
title: Criar roteiro - MDS (BNL) (BNL_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud master data script (BNL): creating a production routing (roteiro) for discrete manufacturing in Administrar itinerários (F5425)."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/routings-and-reference-operation-sets]
aliases: [BNL_S4CLD2608_Master_Data_PT_XX]
keywords: [Routings and Reference Operation Sets, routing, discrete manufacturing, master data scripts, test procedures, operation control keys, external operations, business roles, organizational units, mandatory master data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-632
topic: 12-production-and-manufacturing/routings-and-reference-operation-sets
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar roteiro - MDS (BNL) (BNL_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Routings and Reference Operation Sets** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar roteiro – MDS (BNL) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894017)

[2 Pré-requisitos 3](#_Toc233894018)

[2.1 Acesso ao sistema 3](#_Toc233894019)

[2.2 Funções 3](#_Toc233894020)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894021)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894022)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894023)

[2.5.1 Utilização 4](#_Toc233894024)

[3 Tabela de síntese 6](#_Toc233894025)

[4 Procedimentos de teste 7](#_Toc233894026)

[4.1 Criar roteiro 7](#_Toc233894027)

## Objetivo

Um roteiro de produção define o processo de produção de um material. Ele contém as etapas de operação ou de trabalho a serem executadas durante a produção. Ele define o uso de materiais e centros de custo. Forma um modelo para uma ordem de produção e é a base para o cálculo de custos do produto.

Um roteiro é definido para um produto acabado ou produto semiacabado e é específico de um local de produção (conhecido como centro). Ele se aplicação a um determinado tamanho de lote e consiste de uma série de operações, cada uma delas alocada a um centro de trabalho.

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
| Engenheiro de produção - produção discreta | SAP_BR_PRODN_ENG_DISC | Engenharia de produção - produção discreta | SAP_BR_PRODN_ENG_DISC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados para um roteiro dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados do roteiro podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um roteiro.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material |  | Obrigatório | Conclua o seguinte script de teste como pré-requisito antes de executar as etapas do processo:Criar mestre de produtos do tipo "Matéria-prima" – MDS (BNR)Criar mestre de produtos do tipo "Produto semiacabado" – MDS (BNS)Criar mestre de produtos do tipo "Produto acabado" – MDS (BNT) |
| Centro de trabalho | Na tela Criar roteiro: síntese de operações, selecione um centro de trabalho para uma operação interna | Obrigatório, (opcional) | O centro de trabalho não é um campo de entrada obrigatório para uma operação externa.Se for necessário, execute o script de teste Criar roteiro – MDS (BNL). |
| Lista técnica |  | Opcional | Execute o script de teste Criar lista técnica de materiais para produção e vendas – MDS (BNK). |
| Registro info para compras |  | (Obrigatório) | Para uma operação externa, você pode utilizar um registro info de compras para capturar todos os dados relevantes de fornecimento |
| Grupo de materiais |  |  |  |
| Classe de custo |  |  |  |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um roteiro:

#### Utilização

| Categoria do centro de trabalho | Descrição |
| --- | --- |
| 1 | Produção |
| 2 | Engenharia/design |
| 3 | Universal |

## Tabela de síntese

Este item de escopo consiste da etapa de processo listada na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar roteiro](#unique_10) [página ] 7 | Engenheiro de produção - produção discreta | Administrar itinerários(F5425) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar roteiro

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar itinerários(F5425). | O app é aberto. |  |
| 3 | Clicar em Criar | Clique em Criar. | É aberta uma nova janela que exibe a tela Criar roteiro. |  |
| 4 | Configurar a tela Criar roteiro | Insira os seguintes dados na tela Criar roteiro:Material: <Número do material acabado/semiacabado>Centro: <Nº de seu centro>Clique em Continuar. | A tela Criar roteiro: detalhes do cabeçalho é exibida. |  |
| 5 | Configurar a tela Criar roteiro: detalhes do cabeçalho | Insira os seguintes dados na tela Criar roteiro: detalhes do cabeçalho é exibida.Utilização: <1 para produção>Status: <4 liberado geral>Do tamanho do lote - ao tamanho do lote: <Inserir intervalo do tamanho do lote e unidade de medida> |  |  |
| 6 | Configurar a tela Criar roteiro: síntese de operações | Selecione Operação. A tela Criar roteiro: síntese de operações é exibida.Insira os seguintes dados na tela Criar roteiro: síntese de operações:Centro de trabalho: necessário para operações internas, (em branco) para operações externasChave de controle: <YBP1/YBP2/YBP3/YBP5>YBP1 para a operação interna sem entrada de mercadorias automáticaYBP2 para a operação externa (subcontratação de PP)YBP3 para a operação interna com entrada de mercadorias automáticaYBP4 para marco da produção por processosDescrição: <insira uma descrição para a operação>E depois clique duas vezes em sua operação inserida. |  |  |
| 7 | Configuração de operação externa para a seção de processamento externo | Insira os seguintes dados na tela Criar roteiro: detalhes da operação.Registro info para compras: necessário para operações internas, (em branco) para operações externasGrupo de mercadorias: L002/L003Classe de custo: <classe de custo relevante para seu país>Organização de compras: <organização de compras>. |  |  |
| 8 | Configuração de operação interna para a seção de valor padrão | Insira os seguintes dados na tela Detalhes da operação da criação do roteiro:Setup: <tempo de setup>Máquina: <tempo da operação da máquina>Trabalho: <tempo de trabalho> |  |  |
| 9 | Adicionar mais operações | Repita as etapas anteriores para cada operação. |  |  |
| 10 | Selecionar um componente | Selecione Alocação de componente na parte superior da visão e marque um componente. | A visão Síntese de componentes de material é exibida. |  |
| 11 | Criar uma nova atribuição | Selecione Nova atribuição. | É exibida a caixa de diálogo Nova atribuição. |  |
| 12 | Atribuir à lista de operações/atividades | Selecione a Lista Oper./ativ. |  |  |
| 13 | Selecionar operação | Selecione uma operação e pressione Enter. |  |  |
| 14 | Atribuir outros componentes | Repita as etapas anteriores para outros componentes. |  |  |
| 15 | Salvar os dados | Salve as entradas. | O roteiro é criado. |  |

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
> Flagged while digesting this document, not verified: Step 7 (external operation setup) says the purchasing info record is required for internal operations and blank for external ones, contradicting section 2.4 and the step title, which tie the purchasing info record to external operations.

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/arbeitsplan-anlegen-sds-bnl-628]]
- related-to :: [[12-production-and-manufacturing/creacion-de-hoja-de-ruta-mds-bnl-630]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-routing-mds-bnl-629]]
- related-to :: [[12-production-and-manufacturing/mds-bnl-631]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNL_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 11,814 chars in the whole document
