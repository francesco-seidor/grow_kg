---
id: 12-production-and-manufacturing/criar-area-de-abastecimento-da-producao-mds-40d-404
title: Criar área de abastecimento da produção – MDS (40D) (40D_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud master data script (40D): create a production supply area via PK05S (quick entry) or F6935 (manage), by plant and storage location."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-supply-areas]
aliases: [40D_S4CLD2608_Master_Data_PT_XX]
keywords: [Production Supply Areas, production supply area, plant and storage location, lean manufacturing, mrp controller, business roles, master data scripts, 40D]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-404
topic: 12-production-and-manufacturing/production-supply-areas
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar área de abastecimento da produção – MDS (40D) (40D_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Production Supply Areas** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar área de abastecimento da produção – MDS (40D) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893770)

[2 Pré-requisitos 3](#_Toc233893771)

[2.1 Acesso ao sistema 3](#_Toc233893772)

[2.2 Funções 3](#_Toc233893773)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893774)

[2.4 Parâmetros obrigatórios e opcionais para criação de dados 4](#_Toc233893775)

[3 Tabela de síntese 5](#_Toc233893776)

[4 Procedimentos de teste 6](#_Toc233893777)

[4.1 Criar área de abastecimento da produção 6](#_Toc233893778)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar uma área de abastecimento da produção para o seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados relevantes para o appliance SAP S/4HANA Cloud Public Edition. Os campos que não são relevantes para o escopo do conteúdo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento.

Uma área de abastecimento da produção criada como descrito aqui pode ser utilizada para os processos de produção.

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
| Planejador de produção - produção enxuta | SAP_BR_PRODN_PLNR_LEAN_MFG | Planejamento de produção - produção enxuta | SAP_BR_PRODN_PLNR_LEAN_MFG |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados da área de abastecimento da produção dependem do centro. | Centro:__________ |
| Todos os dados | Depósito |  | Todos os dados da área de abastecimento da produção dependem do depósito. | Depósito:__________ |

### Parâmetros obrigatórios e opcionais para criação de dados

Registros da área de abastecimento da produção podem se referir a outras parâmetros de entrada. A tabela a seguir fornece uma síntese dos parâmetros de entrada opcionais e obrigatórios que devem ser utilizados para a criação de uma área de abastecimento da produção.

| Objeto de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- |
| Responsável/planejador MRP | Opcional | Pessoa responsável por uma ou mais áreas de abastecimento |

## Tabela de síntese

Este item de escopo consiste da etapa de processo listada na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar área de abastecimento da produção](#unique_8) [página ] 6 | Planejador de produção - produção enxuta | Área de abastecimento da produção - Entrada rápida(PK05S) ou Administrar áreas de abastecimento da produção(F6935) | A área de abastecimento da produção é criada. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar área de abastecimento da produção

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

Opção 1:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador de produção - produção enxuta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Área de abastecimento da produção - Entrada rápida(PK05S). | A tela Editar visões de tabela: 1ª tela é exibida. |  |
| 3 | Inserir código do centro | Na subtela Determinar área de trabalho: entrada, insira o código do Centro e clique em Continuar. |  |  |
| 4 | Navegue até a tela Criar área de abastecimento | Clique em Entradas novas. |  |  |
| 5 | Área de abastecimento | Insira os detalhes da Área de abastecimento e pressione Enter.Área de abastecimento da produção: <área de abastecimento>Depósito: <depósito>Res: <A planejador MRP>Ponto de descarga: <"ponto de descarga A">Nome da área de abastecimento da produção: <Descrição da área de abastecimento da produção> |  |  |
| 6 | Salvar os dados | Clique em Salvar. |  |  |
| 7 | Atualizar outros parâmetros (opcional) | Insira outros parâmetros necessários de acordo com requisitos específicos. Por exemplo:Atualizar o endereço da área de abastecimento da produção via Mais > Ir para > Endereço.Salve as alterações. |  |  |

Opção 2:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador de produção - produção enxuta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar áreas de abastecimento da produção(F6935). | O app é aberto. |  |
| 3 | Criar | Na seção Áreas de abastecimento da produção, clique em Criar. |  |  |
| 4 | Inserir dados | Na caixa de diálogo, efetue as seguintes entradas e clique em Continuar:Área de abastecimento da produção: <área de abastecimento>Centro: <centro>Depósito: <Depósito> |  |  |
| 5 | Inserir dados básicos | Na seção Dados básicos, efetue as seguintes entradas:Responsável: <Um planejador MRP>Ponto de descarga: <"ponto de descarga A"> |  |  |
| 6 | Inserir descrição | Na seção Descrição dependente do idioma, efetue as seguintes entradas:Idioma: <selecione um código de idioma, por exemplo, EN para inglês>Descrição: <Descrição da área de abastecimento da produção> |  |  |
| 7 | Salvar os dados | Clique em Criar. |  |  |
| 8 | Atualizar outros parâmetros (opcional) | Insira outros parâmetros necessários de acordo com requisitos específicos. Por exemplo:Atualizar o endereço da área de abastecimento da produção via Criar endereço.Salve as alterações. |  |  |

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
- related-to :: [[12-production-and-manufacturing/creacion-de-area-de-suministro-de-produccion-mds-40d-402]]
- related-to :: [[12-production-and-manufacturing/create-production-supply-area-mds-40d-401]]
- related-to :: [[12-production-and-manufacturing/mds-40d-403]]
- related-to :: [[12-production-and-manufacturing/mds-40d-405]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/40D_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,484 chars in the whole document
