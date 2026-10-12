---
id: 13-quality-ehs-and-compliance/script-de-dados-mestre-criar-local-ehs-mds-3sr-362
title: "Script de dados mestre: Criar local EHS – MDS (3SR) (3SR_S4CLD2608_Master_Data_PT_XX)"
description: Portuguese master data script (3SR) for creating an EHS location in the location structure in SAP S/4HANA Cloud Public Edition via app EHFND_UI_LOC_ENTRY.
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/ehs-locations]
aliases: [3SR_S4CLD2608_Master_Data_PT_XX]
keywords: [EHS Locations, ehs location, location structure, master data script, environment health safety, user roles, responsible persons, test procedure, 3SR]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-362
topic: 13-quality-ehs-and-compliance/ehs-locations
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar local EHS – MDS (3SR) (3SR_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **EHS Locations** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar local EHS – MDS (3SR) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893673)

[2 Pré-requisitos 3](#_Toc233893674)

[2.1 Acesso ao sistema 3](#_Toc233893675)

[2.2 Funções 3](#_Toc233893676)

[3 Tabela de síntese 4](#_Toc233893677)

[4 Procedimentos 5](#_Toc233893678)

[4.1 Criar Dados mestre da unidade gerencial EHS – Dados gerais 5](#_Toc233893679)

## Objetivo

Este documento ajuda você a criar uma localização EHS na estrutura de localização. A Localização EHS é um objeto de dados mestre central usado em Environment, Health, and Safety. A criação de localizações EHS organizadas em uma estrutura de localização faz parte da configuração inicial da solução e as localizações são utilizadas em outros processos que fazem parte da solução.

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
| Especialista em segurança do trabalho (Gerente de Incidentes) | SAP_BR_INDUSTRIAL_HYGIENIST | Segurança no local de trabalho | SAP_BR_INDUSTRIAL_HYGIENIST |  |
| Responsável ambiental | SAP_BR_EHS_ENV_MGMT | Environment, Health & Safety | SAP_BR_EHS_ENV_MGMT |  |
| Coordenador de administração de modificações | SAP_BR_CHG_MGMT_COORDINATOR | Administração de modificações | SAP_BR_CHG_MGMT_COORDINATOR |  |

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar Dados mestre da unidade gerencial EHS – Dados gerais](#unique_6) [página ] 5 | Especialista em segurança do trabalhoResponsável ambientalCoordenador de administração de modificações | Administrar localizações(EHFND_UI_LOC_ENTRY) | Uma localização EHS é criada e atribuída à estrutura de localização EHS. |

## Procedimentos

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar Dados mestre da unidade gerencial EHS – Dados gerais

Objetivo

O procedimento a seguir fornece instruções para a criação de uma Unidade Gerencial EHS e sua atribuição a uma estrutura de Unidade Gerencial EHS.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori com uma das seguintes funções:Especialista em segurança do trabalhoResponsável ambientalCoordenador de administração de modificações | O launchpad do SAP Fiori é exibido com as seções e blocos para a função respectiva. |  |
| 2 | Navegue até a Estrutura de localização | Abra Administrar localizações(EHFND_UI_LOC_ENTRY). | A tela Localizações é exibida. Inicialmente, Todas as localizações é definida como o nível superior da estrutura de localização. |  |
| 3 | Criar uma Unidade gerencial | Clique em Editar estrutura de localização.Na tela Estrutura de localização:Selecione a linha Todas as localizações.Clique em Novo.Na tela Criar localização:Insira um <Nome da localização> no campo Localização.Selecione um <Tipo de localização> usando as entradas possíveis para o campo Tipo de localização.Insira a data 01/01/2000 no campo Data de início da revisão.Clique em Salvar.Clique em Voltar para a estrutura de localização.Na tela Estrutura de localização:Salve as entradas. | Uma localização denominada <Nome da localização> é criada e salva na estrutura de localização. |  |
| 4 | Editar uma localização | Na tela Estrutura de localização:Na coluna Nome, clique no link <Nome da localização>. | O app Editar localização é exibido. |  |
| 5 | Adicionar informações básicas | Na tela Localização: <nome da localização>, na guia Informações básicas:Adicione um texto de <descrição da localização> no campo Descrição.Clique em Traduções próximo ao campo Localização. Adicione o texto traduzido para idiomas diferentes.Clique em Traduções próximo ao campo Descrição. Adicione o texto traduzido para idiomas diferentes.Clique em Carregar imagem para adicionar uma imagem à localização.Salve as entradas. | Os dados da localização estão salvos. |  |
| 6 | Adicionar endereço | Na tela Localização: <nome da localização>, na guia Endereço:Insira o <Linha de nome 1> no campo Linha de nome 1.Insira o <Nome linha 2> no campo Nome linha 2.Insira o <nome da rua> no campo Rua .Insira o <código postal> no campo Código postal .Insira o <Nome da cidade> no campo Cidade.Selecione <País/região> no campo País/região usando as entradas possíveis.Selecione <Região> no campo Região usando as entradas possíveis.Use o valor UTC padrão no campo Fuso horário.Insira dados adicionais nos campos Número de telefone, Número de fax, Latitude, Longitude e Altura.Salve as entradas. | Os dados da localização estão salvos. |  |
| 7 | Adicionar pessoa responsável | Esta etapa só é relevante para as seguintes funções:SAP_BR_INDUSTRIAL_HYGIENIST (Especialista em segurança do trabalho)SAP_BR_EHS_ENV_MGMT (Responsável ambiental)Na tela Localização: <nome da localização>, na guia Pessoas responsáveis:Na tabela Pessoas responsáveis pelas funções, selecione o seu <nome de usuário> na coluna Nome usando as entradas possíveis.Na coluna Função, clique em Gerente de incidentes ou Gerente ambiental na lista de opções.Salve as entradas. | Os dados da localização estão salvos. |  |
| 8 | Adicionar documentos | Na tela Localização: <nome da localização>, na guia Documentos:Na tabela Documentos e links, clique em Adicionar arquivo para adicionar um documento ao local.Salve as entradas. | O documento selecionado foi adicionado à tabela.Os dados da localização estão salvos. |  |
|  | Ativar localização | Na tela Localização: <Nome da localização>:clique em Definir status no cabeçalho da página.Selecione a opção Ativo. | A unidade gerencial está ativada.O campo Status é definido para Ativo no cabeçalho da página.Os dados da localização são salvos. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-ehs-location-mds-3sr-359]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-lokation-anlegen-sds-3sr-358]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-361]]
- related-to :: [[13-quality-ehs-and-compliance/ehs-mds-3sr-363]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3SR_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,369 chars in the whole document
