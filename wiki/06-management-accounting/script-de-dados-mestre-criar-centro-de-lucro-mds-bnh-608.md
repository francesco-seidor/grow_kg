---
id: 06-management-accounting/script-de-dados-mestre-criar-centro-de-lucro-mds-bnh-608
title: "Script de dados mestre - Criar centro de lucro (MDS, BNH) (BNH_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese master data script (scope BNH) for creating a profit center in SAP S/4HANA Cloud Public Edition: prerequisites, mandatory fields and test steps."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/profit-centers]
aliases: [BNH_S4CLD2608_Master_Data_PT_XX]
keywords: [Profit Centers and Profit Center Reorganization, profit center master data, profit center creation, business roles, controlling area, validity periods, mandatory master data fields, master data scripts, BNH]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-608
topic: 06-management-accounting/profit-centers
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar centro de lucro (MDS, BNH) (BNH_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Profit Centers and Profit Center Reorganization** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar centro de lucro – MDS (BNH) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894013)

[2 Pré-requisitos 3](#_Toc233894014)

[2.1 Acesso ao sistema e funções 3](#_Toc233894015)

[2.2 Unidades organizacionais necessárias 3](#_Toc233894016)

[2.3 Dados mestre obrigatórios e opcionais 4](#_Toc233894017)

[2.4 Parâmetros principais para a criação de dados 5](#_Toc233894018)

[3 Tabela de síntese 6](#_Toc233894019)

[4 Procedimentos de teste 7](#_Toc233894020)

[4.1 Criar dados mestre do centro de lucro 7](#_Toc233894021)

## Objetivo

Um centro de lucro é uma unidade organizacional na contabilidade que reflete uma estrutura orientada à administração da organização com a finalidade de controle interno. A divisão da empresa em centros de lucro permite que você determine o lucro de áreas de responsabilidade internas e delegue a responsabilidade a unidades descentralizadas.

Os dados mestre de um centro de lucro incluem o nome do centro de lucro, a área de contabilidade de custos à qual ele está atribuído e o período de validade do centro de lucro, assim como como as informações sobre a pessoa responsável pelo centro de lucro, a atribuição do centro de lucro a um nó da hierarquia padrão e os dados necessários para a comunicação (endereço, número de telefone, etc.).

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema e funções

Conduzir o teste nos seguintes sistemas:

| Sistema | Detalhes |
| --- | --- |
| SAP S/4HANA Cloud Public Edition | ID do sistema: ###Mandante: ### |

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Contador divisional | SAP_BR_DIVISION_ACCOUNTANT | Contabilidade divisional | SAP_BR_DIVISION_ACCOUNTANT |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre de cliente são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados básicos do centro de lucro | Área de contabilidade de custosGrupo de centros de lucroSegmento | Nome, Texto descritivo, Período de validade, Usuário responsável, Responsável | Os grupos de centros de lucro permitem que o controlador se enderece a todo o grupo de centros de lucro fornecendo o nome do grupo em vez dos nomes individuais dos centros de lucro, por exemplo, no customizing ou nos relatórios. Nos relatórios, isso permite uma análise dos índices da contabilidade de custos em um nível agregado.Normalmente o segmento não é lançado de forma explícita. Os dados são derivados de objetos da classificação contábil, como centros de lucro. Por sua vez, normalmente o centro de lucro não é lançado de forma explícita. Os dados são derivados de objetos primários da classificação contábil, como centros de custo, ordens internas, etc. | Área de contabilidade de custos:____________Grupo de centros de lucro:____________Segmento:____________ |
| Atribuição de centro de lucro a empresa | Empresa | Empresa | Os dados da empresa podem existir para cada ID da empresa da sua estrutura empresarial para a qual é utilizado o registro mestre do centro de lucro. | Empresa:____________ |

### Dados mestre obrigatórios e opcionais

A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre do centro de lucro.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de contabilidade de custos | Dados básicos do centro de lucro | Obrigatório | Uma área de contabilidade de custos de referência pode ser utilizada para criar um novo centro de lucro. |
| Centro de lucro | Dados básicos do centro de lucro | Obrigatório | Um centro de lucro de referência pode ser utilizado para criar um novo centro de lucro. |
| Início da validade | Dados básicos do centro de lucro | Obrigatório |  |
| Fim da validade | Dados básicos do centro de lucro | Obrigatório |  |
| Nome | Dados básicos do centro de lucro | Obrigatório |  |
| Texto descritivo | Dados básicos do centro de lucro | Opcional |  |
| Usuário responsável | Dados básicos do centro de lucro | Opcional |  |
| Responsável | Dados básicos do centro de lucro | Obrigatório |  |
| Grupo de centros de lucro | Dados básicos do centro de lucro | Obrigatório |  |
| Departamento | Dados básicos do centro de lucro | Opcional |  |
| Segmento | Dados básicos do centro de lucro | Opcional | Se o centro de lucro for válido para uma empresa dos EUA, recomenda-se o preenchimento do campo do segmento; dessa forma, é possível executar os relatórios do segmento. |
| Esquema de planejamento | Dados básicos do centro de lucro | Opcional |  |
| Campos de endereço e comunicação | Dados de endereço e comunicação do centro de lucro | Estes são todos opcionais |  |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre do centro de lucro:

Área de contabilidade de custos: A000

## Tabela de síntese

Este item de escopo consiste em várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do centro de lucro](#unique_8) [página ] 7 | Contador divisional | Administração de centros de lucro - Versão antiga(F3516) | É aberta uma nova janela exibindo a tela Dados mestre para centro de lucro. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre do centro de lucro

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador divisional. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administração de centros de lucro - Versão antiga(F3516). | A tela Dados mestre para centro de lucro é exibida. |  |
| 3 | Procurar centro de lucro | Procure pelo centro de lucro.Clique em Ir. | Uma lista de centros de lucro é exibida na tela. |  |
| 4 | Adicionar centro de lucro | Clique em Criar. | A tela Centro de lucro: nova é exibida. |  |
| 5 | Inserir novos dados do centro de lucro | Na seção Novo centro de lucro, insira os seguintes dados:Centro de lucro: <nome>, por exemplo, YBXXXNota O comprimento máximo é de 10 caracteres. Não use caracteres especiais como %, !, $, &, @ etc. Eles causam queda do app e não podem ser excluídos.Válido desde: <Data de início da validade>Válido até: <Data de fim da validade>Nome: <qualquer descrição>Responsável: <nome da pessoa responsável> |  |  |
| 6 | Inserir dados básicos | Na guia Unidade organizacional, insira os seguintes dados:Nó de hierarquia padrão: <grupo de centros de lucro>Segmento: <segmento> |  |  |
| 7 | Atribuição de empresa | Marque ou desmarque o campo de seleção para atribuir empresas ao novo centro de lucro. |  |  |
| 8 | Salvar os dados | Salve suas entradas. |  |  |
| 9 | Definir novo período de validade (opcional) | Clique em Editar.No centro de lucro criado, clique em Período de validade > Novo período de validade.Efetue entradas nos campos Válido desde e Válido até e selecione um período de dados de origem.Clique em Criar.Nota Se o novo período de validade se sobrepuser ao atual, o tempo sobreposto será excluído do período atual.Se existir uma lacuna entre o novo período de validade e outros períodos, o sistema impedirá esta ação. |  |  |
| 10 | Modificar campos dependentes de tempo (opcional) | Você pode modificar os campos dependentes de tempo a seguir no novo período de validade.DepartamentoResponsável do CLUsuário responsávelTítuloNomeNome 2Nome 3Nome 4Código de bloqueioClique em Salvar.Nota Se você modificar campos que não são dependentes de tempo, as modificações serão aplicadas em todos os períodos de validade.Se não houver diferença entre o novo período e o anterior ou seguinte, o novo período será agrupado com o atual. | É criado um novo período de validade.Os registros de modificação são exibidos na seção Log de modificações. |  |

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
- related-to :: [[06-management-accounting/create-profit-center-mds-bnh-605]]
- related-to :: [[06-management-accounting/mds-bnh-607]]
- related-to :: [[06-management-accounting/mds-bnh-609]]
- related-to :: [[06-management-accounting/profitcenter-anlegen-sds-bnh-604]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNH_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 13,131 chars in the whole document
