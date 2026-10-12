---
id: 06-management-accounting/criar-tipo-de-atividade-e-hierarquia-de-tipo-de-atividade-mds-bnn-644
title: Criar tipo de atividade e hierarquia de tipo de atividade – MDS (BNN) (BNN_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (BNN) for SAP S/4HANA Cloud Public Edition: create activity types and activity type hierarchies, change log and where-used list."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/activity-types]
aliases: [BNN_S4CLD2608_Master_Data_PT_XX]
keywords: [Activity Types and Activity Type Hierarchies, activity types, activity type hierarchies, master data scripts, cost accounting, cost accounting area, secondary cost elements, change log, where-used list, business roles]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-644
topic: 06-management-accounting/activity-types
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar tipo de atividade e hierarquia de tipo de atividade – MDS (BNN) (BNN_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Activity Types and Activity Type Hierarchies** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar tipo de atividade e hierarquia de tipo de atividade – MDS (BNN) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894055)

[2 Pré-requisitos 3](#_Toc233894056)

[2.1 Acesso ao sistema 3](#_Toc233894057)

[2.2 Funções 3](#_Toc233894058)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894059)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894060)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894061)

[2.6 Etapas preliminares 4](#_Toc233894062)

[2.6.1 Configurações do usuário - definir área de contabilidade de custos 4](#_Toc233894063)

[3 Tabela de síntese 6](#_Toc233894064)

[4 Procedimentos de teste 7](#_Toc233894065)

[4.1 Criar dados mestre do tipo de atividade 7](#_Toc233894066)

[4.2 Criar dados mestre de hierarquia de tipos de atividade 8](#_Toc233894067)

[4.3 Análise 9](#_Toc233894068)

[4.3.1 Log de modificações - Tipo de atividade 9](#_Toc233894069)

[4.3.2 Lista de utilizações – Tipos de atividade 10](#_Toc233894070)

## Objetivo

Tipos de atividade representam as atividades produzidas por um centro de custo em uma área de contabilidade de custos. Os tipos de atividade são utilizados para planejar e alocar as atividades registradas e medidas em unidades de atividade. As quantidades de atividade são avaliadas com uma tarifa atualizada no centro de custo.

Os tipos de atividade são utilizados da seguinte forma:

Para determinar o resultado com base na quantidade de um centro de custo. Os volumes de atividade planejados da produção e centros de custo de serviços devem ser reconciliados com o plano mestre de produção na logística. Isto determina o volume de atividade planejado e a capacidade planejada.

Para controlar os volumes de atividade dos centros de custo. Isto permite a medição do índice de operação ou o grau de utilização de um centro de custo.

Além do planejamento manual dos volumes de atividade, você também pode utilizar automaticamente a alocação de atividade indireta para volumes de atividade planejados.

Hierarquias de tipos de atividade também são úteis no planejamento. Uma vez que não existe nenhuma ferramenta de seleção múltipla disponível para tipos de atividade, as atividades podem ser agrupadas em hierarquias de tipos de atividade para permitir o planejamento de diversos tipos de atividade de uma só vez.

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
| Controlador - custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT | Contabilidade de custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura da sua empresa. Os dados mestre representam tipos de atividade e hierarquias de tipos de atividade, dependendo do foco operacional da sua empresa.

| Objeto de dados | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de contabilidade de custos | Dados gerais | Obrigatório |  |

### Dados mestre obrigatórios e opcionais

Valores propostos

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura de sua empresa. Os dados mestre dependem do foco operacional da sua empresa.

O processo empresarial é ativado com os dados mestre específicos desta organização; são fornecidos exemplos na seção seguinte.

Os registros de hierarquia de tipo de atividade e de tipos de atividade podem se referir a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados do tipo de atividade.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Classe de custo | Dados gerais | Obrigatório | Classe de custo secundário (tipo de classe de custo '43') |
| Conta do Razão |  | Obrigatório | Para casse de custo secundário (tipo de classe de custo '43') |

### Parâmetros principais para a criação de dados

Este item de escopo não tem condições empresariais.

### Etapas preliminares

#### Configurações do usuário - definir área de contabilidade de custos

| Nº da etapa | Nome da etapa | Instrução | Resultado esperado | Aprovado/Reprovado/Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar logon no launchpad do SAP Fiori | Efetue o logon no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Selecione Configurações | Selecione Configurações no menu de contexto do usuário. | Surge a janela Configuração do usuário. |  |
| 3 | Selecione Valores padrão | Selecione Valores padrão na janela. | Surge a janela Valores padrão. |  |
| 4 | Inserir dados | No campo Área de contabilidade de custos, insira <valor ACC> e depois selecione Gravar. | A área de contabilidade de custos, por exemplo, A000, está definida para o seu usuário. |  |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do tipo de atividade](#unique_10) [página ] 7 | Controlador - custos indiretos | Administrar tipos de atividade(F1605A) | Os tipos de atividade podem ser criados de acordo com os novos requisitos empresariais. |
| [Criar dados mestre de hierarquia de tipos de atividade](#unique_11) [página ] 8 | Controlador - custos indiretos | Administrar hierarquias de contabilidade global(F2918) | As hierarquias de tipos de atividade podem ser criados de acordo com os novos requisitos empresariais. |
| [Log de modificações - Tipo de atividade](#unique_12) [página ] 9 | Controlador - custos indiretos | Log de modificações - Tipos de atividade(F3866) |  |
| [Lista de utilizações – Tipos de atividade](#unique_13) [página ] 10 | Controlador - custos indiretos | Administrar tipos de atividade (versão 2)(F1605A) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos para cada etapa do processo que pertence a este item de escopo. Você pode também pode utilizar estes procedimentos para testar a criação de dados mestre.

### Criar dados mestre do tipo de atividade

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar tipos de atividade(F1605A). | O app é aberto. |  |
| 3 | Clicar em Criar | Selecione Criar. |  |  |
| 4 | Inserir dados do tipo de atividade | Na tela Novo tipo de atividade: novo, na guia Dados gerais, efetue as seguintes entradas:Inserir tipo de atividade: Texto de descriçãoUnidade de atividade: <unidade de atividade>Nome: <nome>Descrição do tipo de atividade: <insira uma descrição>Válido desde: <data atual>Fim da validade: <data do fim do ano>Categoria de centro de custo: <tipo de centro de custo>Categoria do tipo de atividade: <categoria do tipo de atividade>Classe de custo de alocação: Por exemplo, 94304000.Indicador de preço: <indicador de preço> | A seção Dados gerais e várias guias são exibidas.Nota Você pode encontrar abaixo os valores recomendados pela SAP para SAP S/4HANA Cloud Public Edition (como outros, embora visíveis, podem não ser suportados):Categoria do tipo de atividade: somente 1 (entrada manual, alocação manual) é suportado.Indicador de preço: Somente 3 (o preço é definido manualmente) é suportado.Categoria do tipo de atividade real: deve ficar em branco.Indicador de preço real: deve estar em branco por padrão. Somente se você tiver ativado o item de escopo 33Q - Cálculo de custo real, deve usar 5 ou 7 (para obter detalhes sobre esses dois valores, consulte a seção no script de teste de 33Q). |  |
| 5 | Salvar os dados | Selecione Criar. | O tipo de atividade é criado e salvo. |  |

### Criar dados mestre de hierarquia de tipos de atividade

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Você preencheu e salvou os dados básicos para o material como descrito em [Criar dados mestre do tipo de atividade](#unique_10) [página ] 7.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar hierarquias de contabilidade global(F2918). | O app é aberto. |  |
| 3 | Clicar em Criar | Na seção Lista de hierarquias, clique em Criar. | A tela Nova hierarquia é exibida. |  |
| 4 | Inserir nova hierarquia de tipos de atividade | Na tela Nova hierarquia, efetue as seguintes entradas e clique em Criar:Tipo: Hierarquia de tipos de atividadesID da hierarquia: <qualquer ID de até 10 caracteres>Atenção O comprimento total do ID da hierarquia e do ID do nó não pode exceder 14 caracteres.Área de contabilidade de custos: A000Descrição da hierarquia: <qualquer descrição> |  |  |
| 5 | Editar nova hierarquia de tipos de atividade | Na tela Lista de hierarquias, clique no ícone de detalhes > e clique em Editar para sua hierarquia de tipos de atividade recém-criada.Selecione a hierarquia de tipos de atividade recém-criada, clique em Mais no lado direito da tela e selecione Entrada rápida.Na tela Entrada rápida, selecione Tipo de atividade e efetue a seguinte entrada:ID: <selecione os tipos de atividade que deseja adicionar usando a função de pesquisa>Clique em OK quando terminar e selecione Salvar.Volte para a tela Hierarquia de tipos de atividade e selecione Ativar. | A hierarquia de tipos de atividade recém-criada está agora ativada. |  |

### Análise

#### Log de modificações - Tipo de atividade

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta atividade, você vai executar o log de modificações para tipos de atividade.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Log de modificações - Tipos de atividade(F3866). | A caixa de diálogo Log de modificações – Tipos de atividade é exibida. |  |
| 3 | Inserir critérios de seleção | Efetue as seguintes entradas:Tipo de atividade: <Qualquer tipo de atividade> |  |  |
| 4 | Selecionar | Clique em Ir. | É exibido um relatório mostrando o histórico detalhado de modificações. |  |

#### Lista de utilizações – Tipos de atividade

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta atividade permite ver onde os tipos de atividade são usados em outros dados mestre, por exemplo, centros de lucro e alocações de custos reais.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar tipos de atividade (versão 2)(F1605A). | O app é aberto. |  |
| 3 | Inserir critérios de seleção | Efetue as seguintes entradas:Tipo de atividade: <Qualquer tipo de atividade> |  |  |
| 4 | Lista de utilizações | Selecione o centro de custo desejado e, em seguida, Lista de utilizações – Tipos de atividade. | É exibido um relatório mostrando onde os tipos de atividade estão sendo usados no momento. Para obter detalhes, selecione o tipo de objeto de dados mestre e continue a pesquisa. |  |

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
- related-to :: [[06-management-accounting/leistungsart-und-leistungsartenhierarchie-anlegen-sds-bnn-640]]
- related-to :: [[06-management-accounting/master-data-script-create-activity-type-and-activity-type-hierarchy-bn]]
- related-to :: [[06-management-accounting/mds-bnn-643]]
- related-to :: [[06-management-accounting/mds-bnn-645]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNN_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 17,739 chars in the whole document
