---
id: 12-production-and-manufacturing/script-de-dados-mestre-criar-meio-auxiliar-de-producao-mds-5cp-440
title: Script de dados mestre - Criar meio auxiliar de produção - MDS (5CP) (5CP_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (5CP) for SAP S/4HANA Cloud: creating production resources/tools (MAP/PRT) and assigning them to routings and production orders."
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/production-resources-tools]
aliases: [5CP_S4CLD2608_Master_Data_PT_XX]
keywords: [Production Resources/Tools (PRTs), production resources tools, master data script, material PRT creation, equipment PRT creation, document PRT creation, routing assignment, production order assignment, business roles, prt status]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-440
topic: 12-production-and-manufacturing/production-resources-tools
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar meio auxiliar de produção - MDS (5CP) (5CP_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Production Resources/Tools (PRTs)** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar meio auxiliar de produção - MDS (5CP) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893825)

[2 Pré-requisitos 3](#_Toc233893826)

[2.1 Acesso ao sistema 3](#_Toc233893827)

[2.2 Funções 3](#_Toc233893828)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893829)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893830)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893831)

[2.5.1 Status MAP 4](#_Toc233893832)

[2.5.2 Chave de controle MAP 5](#_Toc233893833)

[3 Tabela de síntese 6](#_Toc233893834)

[4 Procedimentos 7](#_Toc233893835)

[4.1 Criar meios auxiliares de produção 7](#_Toc233893836)

[4.1.1 Criar MAP de material 7](#_Toc233893837)

[4.1.2 Criar outros MAPs 8](#_Toc233893838)

[4.1.3 Criar documento MAP 9](#_Toc233893839)

[4.1.4 Criar MAP de equipamento 10](#_Toc233893840)

[4.2 Atribuir MAP no roteiro (opcional) 12](#_Toc233893841)

[4.3 Atribuir MAP na ordem de produção (opcional) 13](#_Toc233893842)

[5 Anexo 16](#_Toc233893843)

## Objetivo

Neste documento você encontra uma descrição sobre como criar um registro de dados mestre com recursos/ferramentas de produção para seu sistema SAP S/4HANA Cloud Private Edition. Ao contrário de máquinas e imobilizados, os MAPs (meios auxiliares de produção) são recursos operacionais móveis (não estacionários) que são necessários para executar uma atividade e podem ser utilizados repetidamente.

Existem várias categorias de meios auxiliares de produção disponíveis. A categoria determina as características e funções empresariais que um MAP pode ter.

Você pode criar seu próprio MAP seguindo as instruções deste script de dados mestre.

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
| Supervisor de produção - produção discreta | SAP_BR_PRODN_SUPERVISOR_DISC | Administração de produção - produção discreta | SAP_BR_PRODN_SUPERVISOR_DISC |  |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |
| Designer | SAP_BR_DESIGN_ENGINEER | Administração de documentos | SAP_BR_DESIGN_ENGINEER |  |
| Planejador de manutenção | SAP_BR_MAINTENANCE_PLANNER | Planejamento de manutenção | SAP_BR_MAINTENANCE_PLANNER |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre do material são dependentes das unidades organizacionais da empresa, os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados dependem do centro. | Centro:____________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados do roteiro de referência podem fazer referência a outros dados mestre. A tabela a seguir oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um roteiro de referência.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Roteiro | Atribuir MAP no roteiro | Opcional | Vamos supor que você tem um roteiro e quer atribuir um MAP a ele. |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre MAP:

#### Status MAP

O status MAP controla a utilização de meios auxiliares de produção. Dependendo de seu status, um meio auxiliar de produção pode ser liberado para várias tarefas na atualização do MAP.

| Status MAP | Descrição |
| --- | --- |
| 01 | Data de criação |
| 02 | Liberado para planejamento de utilização MAP |
| 03 | Liberado para produção |

#### Chave de controle MAP

A chave de controle MAP determina se os MAPs são atribuídos a uma lista de tarefas ou a uma ordem são incluídos nas seguintes funções empresariais:

| Perfil de controle MAP | Descrição |
| --- | --- |
| 1 | Todas as funções |
| 2 | Imprimir |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar MAP de material](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01) |  |
| [Criar outros MAPs](#unique_12) [página ] 8 | Engenheiro de produção - produção discreta | Administrar meios auxiliares de produção(F7653) |  |
| [Criar documento MAP](#unique_13) [página ] 9 | Designer | Administrar documentos(F2733) |  |
| [Criar MAP de equipamento](#unique_14) [página ] 10 | Planejador de manutenção | Criar objeto técnico(W0029) |  |
| [Atribuir MAP no roteiro (opcional)](#unique_15) [página ] 12 | Engenheiro de produção - produção discreta | Modificar roteamento(CA02) |  |
| [Atribuir MAP na ordem de produção (opcional)](#unique_16) [página ] 13 | Supervisor de produção - produção discreta | Modificar ordem de produção(CO02) |  |

## Procedimentos

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Criar meios auxiliares de produção

#### Criar MAP de material

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como criar um MAP de material.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | É exibida a página Início. |  |
| 2 | Abrir o app SAP Fiori | Abra Criar material(MM01). | É aberta uma nova janela exibindo Criar material (1ª tela). |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <Número do material>, por exemplo, PRT_01Tipo de material: Meios auxiliares de produçãoClique em Seleção de visões. | A visão Selecionar visões é exibida. |  |
| 4 | Clicar em Visões | Na tela Seleção de visões, selecione:Visão básicaMeios auxiliares de produçãoOutras visões necessáriasClique em Continuar. |  |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro: <código do centro>, por exemplo, 1010Pressione Enter. |  |  |
| 6 | Inserir dados básicos da visão | Na guia Dados básicos 1, insira os seguintes dados:Descrição: <MAP do conjunto acabado>Unidade de medida básica: <Unid.>Selecione a guia Meio auxiliar de produção . | Os dados básicos são salvos. |  |
| 7 | Inserir dados de meio auxiliar de produção | Na guia Meio auxiliar de produção , insira os seguintes dados:Utilização MAP: <009>Perfil de controle MAP: <1>Clique em Salvar. | A tela volta para a 1ª tela.O material PRT_01 é criado. |  |

#### Criar outros MAPs

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como criar um MAP diverso.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar meios auxiliares de produção(F7653). | O app é aberto. |  |
| 3 | Selecionar Criar | Selecione Criar. | É aberta uma nova janela que exibe a tela Criar MAP. |  |
| 4 | Inserir nome | Efetue as seguintes entradas:Meio auxiliar de produção: <Nome>, por exemplo, PRT_02Selecione Dados básicos. | A tela Criar meio auxiliar de produção: Dados básicos é exibida. |  |
| 5 | Inserir dados básicos | Forneça uma descrição para o MAP criado:Procure a dica de Descrição do meio auxiliar de produção e insira: <Diversos PRT 02>Na seção Dados básicos, efetue as seguintes entradas:Status: <03>Utilização MAP: <009>Unidade de medida básica: <Unid.>Clique em Salvar. | A tela volta para a 1ª tela.O meio auxiliar de produção é criado. |  |

#### Criar documento MAP

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como criar um documento MAP.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Designer. | É exibida a página Início. |  |
| 2 | Abrir o app SAP Fiori | Abra Administrar documentos(F2733). | É aberta uma nova janela exibindo Administrar documentos. |  |
| 3 | Criar o documento | Selecione Criar.Na tela Documento, efetue as entradas abaixo:Tipo de documento: <SPP>Descrição do documento: <PRT_03>Selecione Criar. | O documento é criado.Anote o número do documento. |  |
| 4 | Editar o documento | Clique em Editar no canto superior direito.Na seção Dados do documento , modifique o Status do documento para Em processamento.Na seção Originais , selecione Carregare, em seguida, anexe um documento PRT do seu PC.Clique em Salvar. | O documento está salvo. |  |
| 5 | Liberar o documento | Clique em Editar no canto superior direito.Na seção Dados do documento , modifique o Status do documento para Liberado.Clique em Salvar. | O documento está salvo. |  |

#### Criar MAP de equipamento

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como criar um MAP de equipamento.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador de manutenção. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar objeto técnico(W0029). | O app é aberto. |  |
| 3 | Criar equipamento | Na tela Criar objeto técnico, selecione o Tipo de objeto técnico: Equipamento.Na tela seguinte, insira o seguinte:Tipo de objeto técnico: EquipamentoObjeto técnico: deixar em brancoVálido desde: data de hojeCategoria de objeto técnico: P (Meio auxiliar de produção)Clique em Continuar. |  |  |
| 4 | Atualizar dados gerais | Na tela Criar objeto técnico: <ID do equipamento>, na seção Dados gerais, insira o seguinte:Descrição: <por exemplo, equipamento MAP>Opcionalmente, atualize outros dados gerais, em seguida, navegue para a seção Dados MAP. | A tela Criar objeto técnico: dados gerais é exibida. |  |
| 5 | Atualizar dados MAP | Na seção Dados MAP, insira o seguinte:Utilização da lista de tarefas: 009 (todos os tipos de lista de tarefas)Chave de controle: 1 (Todas as funções)Opcionalmente, atualize mais detalhes. Por exemplo, você pode criar um ponto de medição atribuído com algumas características e, em seguida, anexar o ponto de medição no campo Ponto de medição e marcar o campo de seleção para o campo Registros de carga. | A tela Criar objeto técnico: Dados do local é exibida. |  |
| 6 | Salvar equipamento | Opcionalmente, você pode atualizar informações adicionais para outras seções.Clique em Salvar. | O equipamento é criado. Anote o número do equipamento. |  |

### Atribuir MAP no roteiro (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como atribuir material MAP, diversos MAPs, documento MAP ou equipamento MAP no roteiro. Você pode atribuir diferentes tipos de recursos de produção e ferramentas às listas de tarefas e ordens de produção para as quais são necessários. Os MAPs atribuídos à lista de tarefas serão copiados automaticamente para a ordem de produção.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenheiro de produção - produção discreta. | É exibida a página Início. |  |
| 2 | Abrir o app SAP Fiori | Abra Modificar roteamento(CA02). | É aberta uma nova janela exibindo Modificar roteiro: 1ª tela. |  |
| 3 | Inserir material | Efetue as seguintes entradas e clique em Continuar:Material: <Número do material>Centro: <código do centro>, por exemplo, 1010 | A tela Modificar roteiro: síntese de operações é exibida. |  |
| 4 | Selecionar operação | Marque um item e selecione Operações.Selecione uma operação à qual deseja atribuir MAP. Em seguida, selecione MAP. | A tela Modificar roteiro: síntese MAP é exibida. |  |
| 5 | Atribuir material MAP | Se não houver MAP na operação, efetue as seguintes entradas no diálogo: Modificar roteiro: Novos MAPs.Se já existirem, selecione Material, efetue as seguintes entradas e pressione a marca de seleção verde:Nº item MAP: <0010>Material: <número do material>, por exemplo, PRT_01Centro: <código do centro>, por exemplo, 1010 | O meio auxiliar de produção do material está atribuído à operação. |  |
| 6 | Atribuir outros MAP | Selecione Outro, efetue as seguintes entradas e pressione a marca de seleção verde:Nº item MAP: <0020>Meios auxiliares de produção: <nome>, por exemplo, PRT_02 | Vários MAPs estão atribuídos à operação. |  |
| 7 | Atribuir documento MAP | Selecione Documento, efetue as seguintes entradas e pressione a marca de seleção verde:Nº item MAP: <0030>Documento: <número do documento criado na etapa anterior>Tipo de documento: <SPP>Documento parcial: <000>Versão do documento: <00>Quantidade: 1 unid.PerfCtrl.: <1> | O meio auxiliar de produção do documento está atribuído à operação. |  |
| 8 | Atribuir equipamento MAP | Clique em Equipamento, efetue as seguintes entradas e selecione a marca de seleção verde:Equipamento. <número do equipamento criado na etapa anterior> |  |  |
| 9 | Salvar as modificações | Clique em Salvar. | O roteiro é salvo. |  |

### Atribuir MAP na ordem de produção (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Este capítulo mostra como atribuir material MAP, diversos MAPs, MAPs diversos, documento MAP ou equipamento MAP para uma operação em uma ordem de produção. Certifique-se de ter uma ordem de produção criada antecipadamente. Você também pode atribuir MAPs na guia de síntese de operações durante a criação da ordem.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Supervisor de produção - produção discreta. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Modificar ordem de produção(CO02). | É aberta uma nova janela que exibe a tela Modificação da ordem de produção: 1ª tela. |  |
| 3 | Inserir informações da ordem | Efetue as seguintes entradas e clique em Continuar:Ordem: <Número da ordem> | A tela Criação da ordem de produção: modificar é exibida. |  |
| 4 | Selecionar uma operação | Selecione Operações.Na tabela Síntese de operações , marque o campo de seleção para uma operação, por exemplo, Operação 0010, e selecione MAP. | Uma nova caixa de diálogo Modificação da ordem de produção: Novas entradas de PRT será exibida, se não houver MAP na operação.Se já existir alguma, a tabela Síntese de meios auxiliares de produção será exibida. |  |
| 5 | Atribuir material MAP | Se não houver MAP na operação, efetue as seguintes entradas no diálogo Modificação da ordem de produção: Novas entradas de MAP:Se já existir, selecione + na parte inferior da Síntese de meios auxiliares de produção e efetue as seguintes entradas:Número do item: por exemplo, 0010Material: por exemplo, PRT_01Centro: por exemplo, 1010Selecione a marca de seleção verde. | O meio auxiliar de produção do material está atribuído à operação. |  |
| 6 | Atribuir outros MAP | Selecione + na parte inferior da Síntese de meios auxiliares de produção e selecione Outros. Em seguida, efetue as seguintes entradas:Número do item: por exemplo, 0020PRT: por exemplo, PRT_02Selecione a marca de seleção verde. | Vários MAPs estão atribuídos à operação. |  |
| 7 | Atribuir MAP do documento | Selecione + na parte inferior da Síntese de meios auxiliares de produção e selecione Documento. Em seguida, efetue as seguintes entradas:Número do item: <0030>Documento: <número do documento criado na etapa anterior>Tipo de documento: <SPP>Documento parcial: <000>Versão do documento: <00>Quantidade: 1 unid.Chave de controle: <1>Selecione a marca de seleção verde. | O meio auxiliar de produção do documento está atribuído à operação. |  |
| 8 | Atribuir equipamento MAP | Clique em + na parte inferior da Síntese de meios auxiliares de produção e clique em Equipamento. Em seguida, efetue as seguintes entradas:Equipamento:<número do equipamento criado na etapa anterior>Perfil de controle: 1 (Todas as funções)Selecione a marca de seleção verde. |  |  |

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
> Flagged while digesting this document, not verified: Purpose text refers to 'SAP S/4HANA Cloud Private Edition' while the title and rest of the document say Public Edition

## Connections
- part-of :: [[_cluster]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-production-resources-tools-mds-5cp-437]]
- related-to :: [[12-production-and-manufacturing/master-data-script-mds-5cp-japanese-439]]
- related-to :: [[12-production-and-manufacturing/mds-5cp-441]]
- related-to :: [[12-production-and-manufacturing/script-de-datos-maestros-creacion-de-medios-auxiliares-de-fabricacion]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5CP_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 23,536 chars in the whole document
