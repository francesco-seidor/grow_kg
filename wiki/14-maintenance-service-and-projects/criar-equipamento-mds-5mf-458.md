---
id: 14-maintenance-service-and-projects/criar-equipamento-mds-5mf-458
title: Criar equipamento - MDS (5MF) (5MF_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud master data script (5MF): creating equipment master data with Criar objeto técnico and installing it at a functional location."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/equipment]
aliases: [5MF_S4CLD2608_Master_Data_PT_XX]
keywords: [Equipment Master Records, equipment master, technical objects, master data scripts, test procedures, plant maintenance, business roles, organizational units, mandatory master data, functional location]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-458
topic: 14-maintenance-service-and-projects/equipment
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar equipamento - MDS (5MF) (5MF_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Equipment Master Records** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar equipamento – MDS (5MF) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893846)

[2 Pré-requisitos 3](#_Toc233893847)

[2.1 Acesso ao sistema 3](#_Toc233893848)

[2.2 Funções 3](#_Toc233893849)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893850)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893851)

[3 Tabela de síntese 5](#_Toc233893852)

[4 Parâmetros principais para a criação de dados 6](#_Toc233893853)

[4.1 Categoria de objeto técnico: 6](#_Toc233893854)

[5 Procedimento 7](#_Toc233893855)

[5.1 Criar equipamento 7](#_Toc233893856)

## Objetivo

Neste documento, você encontra um procedimento detalhado sobre como criar registros de dados mestre de equipamentos para o seu sistema SAP S/4HANA. Isso inclui os segmentos de dados que são relevantes para os dados mestre funcionarem em um ambiente de sistema normal. Este documento fornece também informações sobre quais segmentos de dados e campos necessitam de valores de entrada.

Os campos que não são relevantes para o escopo de conteúdo do SAP S/4HANA, fornecido pelo SAP Best Practices, não estão descritos neste documento, embora possam aparecer na interface de usuário (IU).

## Pré-requisitos

Esta seção resume todos os pré-requisitos para a criação de um equipamento.

### Acesso ao sistema

O teste deve ser conduzido com o seguinte sistema:

Tabela 1:

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (espaço) | ID (espaço) |
| --- | --- | --- | --- |
| Planejador de manutenção | SAP_BR_MD_SPECIALIST_EAM | Planejador de manutenção | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A tabela a seguir oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados de equipamentos dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados do equipamento podem fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um equipamento.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de trabalho de manutenção | Na interface do usuário (IU) mestre de equipamentos, guia Dados organizacionais, você encontra a entrada do centro de trabalho de manutenção na seção de responsabilidades. | Opcional | O sistema usa o centro de trabalho de manutenção como parâmetro para determinar alguns valores, como preparação, máquina ou mão de obra. |
| Centro de custos | Na interface do usuário (IU) do mestre de equipamentos, guia Dados organizacionais, você encontra a entrada do centro de custo na seção de responsabilidades. | Opcional | O sistema usa o centro de custo como parâmetro para o cálculo de custos. |

## Tabela de síntese

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar equipamento](#unique_8) [página ] 7 | SAP_BR_MD_SPECIALIST_EAM | Criar objeto técnico(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)) | O equipamento é criado. |

## Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um equipamento.

### Categoria de objeto técnico:

Os usos possíveis podem ser:

- Maquinário
- Dispositivo
- Meios auxiliares de produção
- Equipamento do cliente

Tabela 2:

| Categoria de objeto técnico: | Descrição |
| --- | --- |
| M | Máquinas |

## Procedimento

### Criar equipamento

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta etapa de teste, você atualiza um registro para um equipamento que está montado em um local de instalação.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como SAP_BR_MD_SPECIALIST_EAM. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar objeto técnico(EAMS_WDA_TECHOBJ_OIF (EAMS_WDA_TECHOBJ_OIF_CFG_V2)). | É aberta uma janela exibindo Criar objeto técnico: 1ª tela. |  |
| 3 | Criar equipamento | Na tela Criar objeto técnico, selecione o Tipo de objeto técnico: Equipamento.Na tela seguinte, insira o seguinte:Tipo de objeto técnico: equipamentoObjeto técnico: deixar em brancoVálido desde: data de hojeCategoria de objeto técnico: M (padrão do sistema técnico)Clique em Continuar. |  |  |
| 4 | Atualizar dados gerais | Na tela Criar objeto técnico: <ID do equipamento>, na seção Dados gerais, insira o seguinte:Descrição: por exemplo, válvula de isolamento manual>Tipo de objeto: por exemplo, 9400>Data de início das atividades: por exemplo, <data de hoje>País/região produtora: por exemplo, US>Mês/ano de construção: por exemplo, 04/2011Número da peça do fabricante: por exemplo, HZZ-TD B4>Nº de série do fabricante: por exemplo, HZZ-TD B4/66>Valor de aquisição/moeda: por exemplo, 10.000,00/ USD >Data de aquisição: por exemplo, 04/10/2011 >Opcionalmente, atualize outros dados gerais, em seguida, navegue para a seção Dados da unidade gerencial. | A tela Criar objeto técnico: dados gerais é exibida. |  |
| 5 | Atualizar dados do local | Na seção Dados do local, insira o seguinte:Centro de manutenção: por exemplo, 1710 para US>Local: por exemplo, YB_1701 para US>Área operacional: por exemplo, YOH para US>Nota os objetos técnicos que pertencem à mesma estrutura devem ter o mesmo centro atribuído. Como alternativa, você pode deixar a informação sobre o centro em branco para todos os objetos técnicos.Opcionalmente, atualize outros detalhes, tais como informações de endereço. | A tela Criar objeto técnico: dados do local é exibida. |  |
| 6 | Atualizar dados organizacionais | Na seção Dados organizacionais, insira o seguinte:Grupo de planejamento: por exemplo, 920 para US>Centro de planejamento: por exemplo, 1710 para US>Centro de trabalho de manutenção: por exemplo, RES-0100 para US>Centro de trabalho: por exemplo, 1710 para US>Centro de custo: por exemplo, 17101701 para US>Opcionalmente, você pode atualizar informações adicionais, por exemplo, informações do parceiro e outras, na seção Dados organizacionais. | A tela Criar objeto técnico: dados organizacionais é exibida. |  |
| 7 | Salvar equipamento | Opcionalmente, você pode atualizar informações adicionais para outras seções.Clique no botão Verificar entradas.Clique em Salvar. | O equipamento é criado. |  |
| 8 | Instalar equipamento no local de instalação | Na tela Modificar objeto técnico: <ID do equipamento>, navegue para a seção Estrutura.Selecione Modificar estrutura: Montar.Na tela Modificar local de instalação, insira o seguinte:Objeto técnico superior: por exemplo< 1710>Posição: <deixar em branco>Data/hora de montagem: <mantenha a proposta do sistema>Clique em OK.Clique em Salvar. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/crear-equipo-mds-5mf-456]]
- related-to :: [[14-maintenance-service-and-projects/create-equipment-mds-5mf-455]]
- related-to :: [[14-maintenance-service-and-projects/equipment-anlegen-sds-5mf-454]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mf-457]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MF_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 11,815 chars in the whole document
