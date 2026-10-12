---
id: 14-maintenance-service-and-projects/criar-ponto-de-medicao-mds-5mi-470
title: Criar ponto de medição – MDS (5MI) (5MI_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (5MI) for SAP S/4HANA Cloud Public Edition: configure measuring point category and create measuring points and counters in Fiori."
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/measuring-points-and-counters]
aliases: [5MI_S4CLD2608_Master_Data_PT_XX]
keywords: [Measuring Points and Counters, measuring points, measuring counters, measuring point categories, master data scripts, business roles, maintenance master data, condition-based updates, configuration steps, 5MI]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-470
topic: 14-maintenance-service-and-projects/measuring-points-and-counters
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar ponto de medição – MDS (5MI) (5MI_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Measuring Points and Counters** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar ponto de medição – MDS (5MI) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893811)

[2 Pré-requisitos 3](#_Toc233893812)

[2.1 Acesso ao sistema 3](#_Toc233893813)

[2.2 Funções 3](#_Toc233893814)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893815)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893816)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893817)

[2.5.1 Categoria de ponto de medição: 4](#_Toc233893818)

[3 Tabela de síntese 7](#_Toc233893819)

[4 Procedimento 8](#_Toc233893820)

[4.1 Criar ponto de medição 8](#_Toc233893821)

[4.2 Criar contador de medição 9](#_Toc233893822)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar um registro de dados mestre de ponto de medição para o seu sistema S/4HANA. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo de conteúdo do S/4HANA, fornecido pelo SAP Best Practices, não estão descritos neste documento, embora possam aparecer na interface de usuário (IU).

## Pré-requisitos

Esta seção resume todos os pré-requisitos para a criação de ponto de medição.

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
| Especialista em dados mestre - Administração de manutenção | SAP_BR_MD_SPECIALIST_EAM | Dados mestre - Administração de manutenção | SAP_EAM_SPT_MD_SPECIALIST_PC |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais da empresa. Dados gerais (central) não dependem de uma unidade organizacional ou da empresa. A tabela a seguir oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de receita podem fazer referência a outros dados mestre. A tabela a seguir oferece uma síntese dos objetos de dados mestre, opcionais e obrigatórios, a serem usados em um ponto de medição.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Objeto técnico |  | Obrigatório | Equipamento ou Local de instalação. |
| Característica |  | Obrigatório | As características descrevem as propriedades dos objetos. Os valores de uma característica especificam as propriedades. |

### Parâmetros principais para a criação de dados

Nesta seção, descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um ponto de medição.

#### Categoria de ponto de medição:

A categoria do ponto de medição determina quais dados podem ser atualizados no registro mestre para o ponto de medição. A distinção dos pontos de medição é feita no sistema pela categoria do ponto de medição. Cada categoria de ponto de medição é identificada por uma chave, que é a primeira atribuição que você faz ao ponto de medição ao criá-lo no sistema.

Tabela 2:

| Categoria de ponto de medição: | Descrição |
| --- | --- |
| M | PontoM (geral) |

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O objetivo desta atividade é configurar a categoria de ponto de medição.

Procedimento

Dependendo do ambiente de configuração do SAP S/4HANA Cloud Public Edition, escolha uma das seguintes opções:

Configurar sua solução:

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em configuração - Configuração de processo empresarial. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abra Administrar sua solução (F1241). | A tela Administrar sua solução é exibida. |  |
| 3 | Abrir Configurar sua solução | Clique em Configurar sua solução.Nota Para criar configurações que dependem de país/região para a versão local prevista, clique em Definir versão local.Selecione a área de aplicação como Administração de imobilizadosSelecione a Área de subaplicação como Administração de manutençãoSelecione a linha com o nome do item: Dados mestre | A tela Configurar sua solução é exibida. |  |
| 4 | Abrir Definir categorias de ponto de medição | Em Etapas de configuração, selecione o nome da etapa "Definir categorias de ponto de medição" e clique em Configurar | A telaCategorias de ponto de medição será exibida |  |
| 5 | Ativar condições para EAA (opcional) | Selecione a categoria de ponto de medição "M"Inserir mensagem Intervalo med. como "W"Marque o campo de seleção para Criar notificaçõesClique em Salvar | As condições para EAA foram estabelecidas |  |

SAP Central Business Configuration

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Especialista em configuração - Configuração de processo empresarial. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app | Abrir Atividades de implementação | A tela Administrar sua solução é exibida. |  |
| 3 | Configuração de acesso | Para localizar a atividade na visão de árvore, clique no ícone de pesquisa e selecione a opção PesquisarInsira o Texto do nó/Descrição da atividade: "Definir categorias de ponto de medição" e clicar em Continuar | A atividade na visão de árvore é exibida. |  |
| 4 | Abrir Definir categorias de ponto de medição | Em Etapas de configuração, selecione o nome da etapa "Definir categorias de ponto de medição" e clique em Configurar | A telaCategorias de ponto de medição será exibida |  |
| 5 | Ativar condições para EAA (opcional) | Selecione a categoria de ponto de medição "M"Inserir mensagem Intervalo med. como "W"Marque o campo de seleção para Criar notificaçõesClique em Salvar | As condições para EAA foram estabelecidas |  |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na tabela.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar ponto de medição](#unique_10) [página ] 8 | SAP_BR_MD_SPECIALIST_EAM | App Criar ponto de medição(EAMS_WDA_MP_OIF) | O ponto de medição é criado. |

## Procedimento

Esta seção descreve os procedimentos para cada etapa do processo que pertence a este item de escopo. Você pode também pode usar estes procedimentos para testar a criação de dados mestre.

### Criar ponto de medição

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em dados mestre SAP_BR_MD_SPECIALIST_EAM. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra o app Criar ponto de medição(EAMS_WDA_MP_OIF). | É aberta uma janela exibindo a tela Criar ponto de medição: |  |
| 3 | Inserir detalhes | Insira o seguinte:Ponto de medição/contador: <Ponto de medição>Tipo de objeto de referência: <Objeto técnico> | É exibida uma tela exibindo o objeto de referência. |  |
| 4 | Inserir detalhes do objeto de referência | Insira o seguinte:Objeto técnico:<Nº do equipamento/local de inst.>Pressione Enter ou clique em Continuar. | Criar ponto de medição |  |
| 5 | Dados gerais | Na seção Dados gerais, insira o seguinte:Descrição: <Descrição do ponto de medição>Característica: por exemplo, OPERATING_HOUR/PRESSURECategoria de ponto de medição: M (PontoMed geral) |  |  |
| 6 | Inserir limites de destino e dados do contador | Na seção Limites de destino e Dados do contador, insira o seguinte:Valor fixado: por exemplo, 10 PALimite superior do intervalo: por exemplo, 15 PALimite inferior do intervalo: por exemplo, 5 PA |  |  |
| 7 | Inserir tolerância de medição (opcional) | Na seção Tolerância de medição, insira o seguinte:Tolerância de medição superior: por exemplo, 12 PATolerância de medição inferior: por exemplo, 7 PA |  |  |
| 8 | Atualizar condição (só para atualização baseada em condição) | Na seção Atualizar condição,clique na caixa de seleção para Ativar condição, selecione qualquer condição: Por exemplo, para a condição: VALOR MEDIDO > LIMITE SUPERIORInsira os seguintes detalhesTipo de objeto (tipo de notificação): por exemplo, trabalho reativoPrioridade: Selecione a Prioridade necessária para a notificação a ser criada. Por exemplo, 1 Muito altoAtivo: Clique no campo de seleção para ativar essa condiçãoTexto descritivo: Insira o texto descritivo para a notificação a ser criadaDescrição: Insira a descrição para a notificação a ser criada |  |  |
| 9 | Verificar entradas | Selecione Verificar entradas. | As entradas são verificadas. |  |
| 10 | Salvar os dados | Salve as entradas. | O ponto de medição é criado. |  |

### Criar contador de medição

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como especialista em dados mestre SAP_BR_MD_SPECIALIST_EAM. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra o app Criar ponto de medição (EAMS_WDA_MP_OIF) app. | É aberta uma janela exibindo a tela Criar ponto de medição: |  |
| 3 | Inserir detalhes | Insira o seguinte:Ponto de medição/contador: <Contador>Tipo de objeto de referência: <Objeto técnico> | É exibida uma tela exibindo o objeto de referência. |  |
| 4 | Inserir objeto de referência | Insira o seguinte:Objeto técnico: <Nº Equipamento/Floc>Pressione Enter ou clique em Continuar. | A tela Criar ponto de medição (contador) é aberta. |  |
| 5 | Inserir dados gerais | Na seção Dados gerais, insira o seguinte:Descrição: <Descrição do contador de medição>Categoria de ponto de medição: M (PontoMed geral)Característica: por exemplo, OPERATING_HOUR/PRESSURE | Os dados gerais são atualizados. |  |
| 6 | Inserir limites de destino e dados do contador | Na seção Limites de destino e Dados do contador, insira o seguinte:Leitura de excedente: <Leitura de excedente do contador>Estimativa anual: <Estimativa anual do objeto tecnológico>Unidade do intervalo de medição | Os limites de destino são atualizados. |  |
| 7 | Verificar entradas | Selecione Verificar entradas. | As entradas são verificadas. |  |
| 8 | Salvar os dados | Salve as entradas. | O ponto de medição é criado. |  |

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
- related-to :: [[14-maintenance-service-and-projects/5mi-469]]
- related-to :: [[14-maintenance-service-and-projects/crear-punto-de-medicion-mds-5mi-468]]
- related-to :: [[14-maintenance-service-and-projects/create-measuring-point-mds-5mi-467]]
- related-to :: [[14-maintenance-service-and-projects/mds-5mi-471]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5MI_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 16,189 chars in the whole document
