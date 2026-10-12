---
id: 12-production-and-manufacturing/script-de-dados-mestre-criar-versao-de-producao-mds-bld-572
title: "Script de dados mestre: Criar versão de produção - MDS (BLD) (BLD_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese master data script for SAP S/4HANA Cloud Public Edition: creating and editing a production version (F6400, F2568), with roles and required master data."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-versions]
aliases: [BLD_S4CLD2608_Master_Data_PT_XX]
keywords: [Production Versions, master data scripts, editing production versions, bill of materials, task lists, material master, business roles, plant organizational data, production engineering, BLD]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-572
topic: 12-production-and-manufacturing/production-versions
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar versão de produção - MDS (BLD) (BLD_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Production Versions** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar versão de produção – MDS (BLD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893968)

[2 Pré-requisitos 3](#_Toc233893969)

[2.1 Acesso ao sistema 3](#_Toc233893970)

[2.2 Funções 3](#_Toc233893971)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893972)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893973)

[3 Tabela de síntese 5](#_Toc233893974)

[4 Procedimentos de teste 6](#_Toc233893975)

[4.1 Criar versão de produção 6](#_Toc233893976)

[4.2 Editar versão de produção (opcional) 9](#_Toc233893977)

## Objetivo

Criar versão de produção

Neste documento, você encontra uma descrição sobre como criar uma versão e produção para seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados relevantes para o appliance SAP S/4HANA Cloud Public Edition. Os campos não relevantes para o escopo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento.

Uma versão de produção criado como descrita aqui pode ser utilizada para o processamento de processos de produção.

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
| Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC | Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados para uma versão de produção dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados da versão de produção podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em uma versão de produção.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material | A versão de produção é criada para cada material e centro. | Obrigatório | Na Versão de produção: tela Processamento em massa, insira o Material.Para a criação de material, você pode seguir as etapas no script de dados mestre: Criar mestre de produtos do tipo "Matéria-prima" – MDS - BNR, Criar mestre de produtos do tipo "Produto semiacabado" – MDS - BNS ou Criar mestre de produtos do tipo "Produto acabado" – MDS - BNT. |
| Lista técnica | Os dados mestre de lista técnica para o material são atribuídos na versão de produção. | Obrigatório | Na Versão de produção: processamento em massa, Lista técnica alternativa e Utilização da lista técnica devem ser inseridas.Para a criação da lista técnica, você pode seguir as etapas no script de dados mestre: Criar lista técnica de materiais para produção e vendas – MDS - BNK. |
| Lista de tarefas | Um plano de tarefas para o material é atribuído na versão de produção. | Obrigatório | Na Versão de produção: processamento em massa, Tipo de lista de tarefas, Grupo e Numerador de grupos devem ser inseridos.Para a criação da lista de tarefas, você pode seguir as etapas no script de dados mestre: Criar roteiro – MDS - BNL ou Criar receita mestre – MDS - 3X9. |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar versão de produção](#unique_8) [página ] 6 | Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos | Versões de produção de processo(F6400) ou Administrar versões de produção(F2568) |  |
| [Editar versão de produção (opcional)](#unique_9) [página ] 9 | Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos | Versões de produção de processo(F6400) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar versão de produção

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

É possível executar esta etapa com diferentes apps do SAP Fiori. Existem três opções que você pode utilizar. Você pode escolher qualquer uma delas.

Opção 1

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Versões de produção de processo(F6400). | O app é aberto. |  |
| 3 | Inserir campos de seleção | Efetue as seguintes entradas e clique em Ir:Material: <Inserir número do material>Centro: <Inserir centro> |  |  |
| 4 | Verificar propostas de versão de produção | Na guia Propostas de versão de produção, você pode encontrar as propostas para criar uma nova versão de produção se a combinação de lista técnica/lista de tarefas correspondente ainda não existir.Você pode examinar os detalhes da proposta selecionando a proposta e efetuar possíveis alterações. | Nota Etapa de configuração (ID: 105965) foi introduzida para configurar as regras para a proposta de versão de produção. |  |
| 5 | Aceitar proposta | Selecione a proposta de versão de produção e escolha Aceitar proposta. |  |  |
| 6 | Confirmação | Na caixa de diálogo Confirmação, escolha OK. | Uma nova versão de produção é criada com base nos parâmetros propostos. Você pode encontrá-la na guia Versões de produção existentes. |  |

Opção 2

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Versões de produção de processo(F6400). | O app é aberto. |  |
| 3 | Inserir campos de seleção | Efetue as seguintes entradas e clique em Ir:Material: <Inserir número do material>Centro: <Inserir centro> |  |  |
| 4 | Selecionar guia | Escolha a guia Versões de produção existentes. |  |  |
| 5 | Criar | Selecione Criar. Na caixa de diálogo Criar versão de produção, efetue as seguintes entradas e escolha Criar.Material: <Inserir número do material>Centro: <Inserir centro>Versão de produção: <um número de 4 dígitos>Descrição da versão de produção: <descrição> |  |  |
| 6 | Parâmetros de entrada | Insira os parâmetros necessários e escolha Criar:Início da validade: <hoje>Fim da validade: <31/12/9999>Tamanho mínimo do lote: <1>Tamanho máximo do lote: <999999999>Seção Lista de tarefas:Tipo de lista de tarefas: <Selecione o tipo de lista de tarefas para o material>Grupo de listas de tarefas: <Selecione o grupo para o material>Contador da lista de tarefas: <Selecione o contador de grupos para o material>Seção Lista técnica:LT alternativa: <Selecione a lista técnica alternativa para o material>Utilização da lista técnica: <Selecione a utilização da lista técnica do mestre de listas técnicas para o material> | A versão de produção é criada. |  |

Opção 3

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar versões de produção(F2568). | A visão Versão de produção: processamento em massa é exibida. |  |
| 3 | Inserir código do centro | Insira Código do centro. |  |  |
| 4 | Inserir material | Inserir Material.Pressione Enter. |  |  |
| 5 | Versão de produção | Insira os itens de linha da versão de produção e depois pressione Enter.Material: <Inserir número do material>Versão de produção <um número de 4 dígitos>Válido desde: <hoje>Válido até: <31/12/9999>Do tamanho do lote: <1>Ao tamanho do lote: <999999999>LT alternativa: Pressione F4 para selecionarLT Alternativa para o material.Utilização da lista técnica: Pressione F4 para selecionar Utilização da LT do mestre de lista técnica para o material.Grupo: <Insira o grupo para o material>Contador de grupos: <Insira o contador de grupos para o material>Tipo: <Selecione o tipo de lista de tarefas para o material> |  |  |
| 6 | Salvar os dados | Clique em Salvar. | A versão de produção é criada. |  |

### Editar versão de produção (opcional)

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
| 1. | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta ou Engenharia de produção - produção por processos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Versões de produção de processo(F6400). | O app é aberto. |  |
| 3 | Inserir campos de seleção | Efetue a seguinte entrada e clique em Ir:Material: <Inserir número do material>Centro: <Inserir centro> |  |  |
| 4 | Navegar até a guia Versões de produção existentes | Vá para a guia Versões de produção existentes. |  |  |
| 5 | Editar versão de produção | Selecione a versão de produção que você quer alterar e selecione Editar na tela Versão de produção.Efetue as alterações necessárias nos campos, dependendo das suas necessidades.Nota Para efetuar alterações semelhantes em várias versões de produção, pode efetuar a seleção múltipla na guia Versões de produção existentes e selecionar Edição em massa.Na caixa de diálogo Edição em massa, você pode efetuar as alterações necessárias nos campos listados. |  |  |
| 6 | Salvar | Clique em Salvar. | A versão de produção é atualizada com sucesso. |  |

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
- related-to :: [[12-production-and-manufacturing/fertigungsversion-anlegen-sds-bld-568]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-version-mds-bld-569]]
- related-to :: [[12-production-and-manufacturing/mds-bld-571]]
- related-to :: [[12-production-and-manufacturing/mds-bld-573]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BLD_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 15,200 chars in the whole document
