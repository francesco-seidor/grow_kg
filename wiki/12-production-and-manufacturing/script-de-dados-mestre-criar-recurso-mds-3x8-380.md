---
id: 12-production-and-manufacturing/script-de-dados-mestre-criar-recurso-mds-3x8-380
title: "Script de dados mestre: Criar recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_PT_XX)"
description: Portuguese master data/test script (3X8) for creating a resource (category 0008 processing unit) with app F6176 in SAP S/4HANA Cloud Public Edition 2608.
cluster: 12-production-and-manufacturing
tags: [kb/production-and-manufacturing, topic/process-resources-and-master-recipes]
aliases: [3X8_S4CLD2608_Master_Data_PT_XX]
keywords: [Process Manufacturing Resources and Master Recipes, resources, resource creation, resource types, capacity planning, default value keys, business roles, master recipes, process manufacturing, 3X8]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-380
topic: 12-production-and-manufacturing/process-resources-and-master-recipes
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar recurso - MDS (3X8) (3X8_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Process Manufacturing Resources and Master Recipes** in Production and Manufacturing. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar recurso – MDS (3X8) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893692)

[2 Pré-requisitos 3](#_Toc233893693)

[2.1 Acesso ao sistema 3](#_Toc233893694)

[2.2 Funções 3](#_Toc233893695)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893696)

[2.4 Dados mestre obrigatórios e opcionais 3](#_Toc233893697)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893698)

[2.5.1 Categoria de recurso 4](#_Toc233893699)

[3 Tabela de síntese 5](#_Toc233893700)

[4 Procedimentos de teste 6](#_Toc233893701)

[4.1 Criar recurso 6](#_Toc233893702)

[5 Anexo 9](#_Toc233893703)

[5.1 Criar receita mestre 9](#_Toc233893704)

## Objetivo

Um recurso significa meios de produção e pessoas envolvidas em um processo de produção que têm capacidades atribuídas. Os recursos são divididos em categorias de recurso, tais como linha de produção, mão de obra e armazenamento.

Com a utilização de recursos, você pode:

- Criar uma estrutura de rede de recursos para definir a sequência dos recursos utilizados
- Definir uma hierarquia de recursos para agrupar recursos para avaliação
- Classificar os recursos para definir a sua aptidão para um objetivo ou uso em uma operação

## Pré-requisitos

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
| Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC | Engenharia de produção - produção por processos | SAP_BR_PRODN_ENG_PROC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Todos os dados | Centro |  | Todos os dados de recursos dependem do centro. | Centro:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados de recurso podem consultar outros dados mestre. A tabela a seguir oferece uma síntese de objetos de dados mestre opcionais e obrigatórios a serem utilizados em um recurso.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Chave de valor padrão | Na IU de recursos, guia de dados básicos, você encontra a entrada da chave de valor padrão na seção Atualização de valores padrão. | Obrigatório | O sistema utiliza valores padrão como parâmetros com o valor padrão de origem em fórmulas para calcular o tempo de execução, as necessidades de capacidade e os custos.Você utiliza a chave de valor padrão para atribuiir um ID de parâmetro a valores padrão. Este ID de parâmetro identifica o valor padrão em uma fórmula. Você pode utilizar o ID de parâmetro para determinar a palavra-chave para um valor padrão, como a preparação, a máquina ou a mão-de-obra. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um recurso.

#### Categoria de recurso

A categoria de recurso determina o tipo de dados a ser atualizado no registro mestre do recurso. Principais recursos de diferenciação de acordo com sua categoria (por exemplo, rede de recursos, unidade de processo).

| Categoria de recurso | Descrição |
| --- | --- |
| 0008 | Unidade de processamento |

## Tabela de síntese

Este item de escopo consiste em várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| Criar recurso | Engenharia de produção - produção por processos | Administrar recursos(F6176) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar recurso

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Engenharia de produção - produção por processos | A página Início é exibida. |  |
| 2 | Abrir o app SAP Fiori | Selecione Administrar recursos(F6176). |  |  |
| 3 | Selecionar Criar | Clique em Criar. | É exibida uma nova tela Criar recurso: 1ª tela. |  |
| 4 | Inserir código do centro | Insira Código do centro. | A tela Criar organização é exibida. |  |
| 5 | Inserir ID do recurso | Insira o ID do recurso.Nota O comprimento de campo do ID do recurso é menor que 8. |  |  |
| 6 | Categoria de recurso | Selecione a categoria de recurso:<0008> unidade de processamento |  |  |
| 7 | Selecionar dados básicos | Clique no botão Dados básicos na parte superior esquerda da tela. | A tela Criar recurso: dados básicos é exibida. |  |
| 8 | Inserir dados | Na guia Dados básicos, insira os seguintes dados:Descrição: <insira a descrição>Pessoa responsável: <pessoa responsável ou pessoa responsável pelo centro>Utilização: <008>Chave de valor padrão: <YBP1> |  |  |
| 9 | Inserir os valores padrão | Na guia Valores padrão, insira os seguintes dados;Chave de controle: <YBP4>Unidade de valor padrão da máquina: <H>Unidade de valor padrão de trabalho: <H> |  |  |
| 10 | Definir as fórmulas de capacidade e processamento | Na guia capacidades, insira os seguintes dados:Categoria de capacidade: <001(máquina/002(pessoa)>Configurar fórmula: <YBPI01>Fórmula de processamento: <YBPI02> | Pressione Enter. A tela Criar capacidade de recurso: cabeçalho é exibida. |  |
| 11 | Instalar capacidade de recurso | Na seção Capacidade de recurso: Cabeçalho, insira os seguintes dados:Descrição da categoria da capacidade: <adicionar uma descrição>Responsável pela capacidade: Selecione F4 para procurar pela pessoa responsável pelo centro.ID do calendário de fábrica: <calendário para seu país>Versão ativa: <1>Unidade básica de capacidade: por exemplo, DHora de início:Hora final:Duração de intervalos:Tempo da operação:Utilização de capacidades: <100>Nº capacids. indiv.: <10>Relevante para programação finita: <X>Planejamento a longo prazo: <X>Pode ser utilizado por várias operações: <X>Pressione Enter. | Pressione Enter. A tela volta para a síntese de capacidades. |  |
| 12 | Inserir dados de programação | Na guia Programação, insira os seguintes dados:Categoria de capacidade: <001(máquina/002(pessoa)>Tempo de setup: <YBPI01>Duração de processamento: <YBPI02> |  |  |
| 13 | Inserir dados do cálculo de custos | Na guia Cálculo de custos, insira os seguintes dados:Centro de custo: <centro de custo de produção para seu código de empresa>Tipo de atividade (máquina): <3>Fórmula (máquina): <YBPI01>Tipo de atividade （trabalho）: <11>Fórmula （trabalho）: <YBPI02>Unidade de atividade: selecione a UM necessária, por exemplo, H |  |  |
| 14 | Salvar os dados | Salve as entradas. |  |  |

## Anexo

### Criar receita mestre

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Receita mestre |  |  | Para executar esta atividade, execute o script de teste Criar receita mestre (3X9). |

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
- related-to :: [[12-production-and-manufacturing/crear-recurso-mds-3x8-378]]
- related-to :: [[12-production-and-manufacturing/master-data-script-create-resource-mds-3x8-377]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-379]]
- related-to :: [[12-production-and-manufacturing/mds-3x8-381]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3X8_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 11,633 chars in the whole document
