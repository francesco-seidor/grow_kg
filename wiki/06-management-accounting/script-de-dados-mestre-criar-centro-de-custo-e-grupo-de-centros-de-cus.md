---
id: 06-management-accounting/script-de-dados-mestre-criar-centro-de-custo-e-grupo-de-centros-de-cus
title: Script de dados mestre - Criar centro de custo e grupo de centros de custo (MDS BNM) (BNM_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition master data script (BNM): create cost centers and cost center groups, plus where-used analysis, dated 02-07-26."
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/cost-centers-and-groups]
aliases: [BNM_S4CLD2608_Master_Data_PT_XX]
keywords: [Cost Centers and Cost Center Groups, cost center master data, cost center groups, standard hierarchy, cost accounting, global hierarchies, cost center where-used list, business roles, organizational units, master data integration]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-638
topic: 06-management-accounting/cost-centers-and-groups
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar centro de custo e grupo de centros de custo (MDS BNM) (BNM_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Cost Centers and Cost Center Groups** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar centro de custo e grupo de centros de custo – MDS (BNM) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894077)

[2 Pré-requisitos 3](#_Toc233894078)

[2.1 Acesso ao sistema 3](#_Toc233894079)

[2.2 Funções 3](#_Toc233894080)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894081)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233894082)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233894083)

[3 Tabela de síntese 5](#_Toc233894084)

[4 Procedimentos de teste 6](#_Toc233894085)

[4.1 Criar dados mestre do centro de custo 6](#_Toc233894086)

[4.2 Criar dados mestre do grupo de centros de custo 8](#_Toc233894087)

[4.3 Análise 10](#_Toc233894088)

[4.3.1 Lista de utilizações - Dados reais de centros de custo 10](#_Toc233894089)

[5 Anexo 12](#_Toc233894090)

[5.1 Replicação do centro de custo do SAP S/4HANA Cloud Public Edition para o SAP Master Data Integration (opcional) 12](#_Toc233894091)

## Objetivo

Centros de custo representam áreas de responsabilidade de unidades organizacionais às quais custos financeiros podem ser atribuídos. A divisão de uma organização em centros de custo permite que você siga vários objetivos.

A atribuição de custos a centros de custos permite que você determine onde os custos incorrem na organização.

Se planejar custos no nível do centro de custo, você pode verificar a eficiência dos custos no ponto onde os custos incorrem.

Se deseja atribuir custos indiretos de maneira precisa a produtos, serviços ou segmentos de mercado individuais, você precisa realizar alocações adicionais de custos para os centros de custo envolvidos diretamente na criação dos produtos ou serviços. A partir destes centros de custo, você pode então utilizar diferentes métodos para atribuir as atividades e os custos aos produtos, serviços e segmentos de mercado relevantes.

Isto permite que você avalie produtos semiacabados e acabados no controlling de custos do produto (CO-PC) e calcule as margens de contribuição na demonstração de resultados (CO-PA)

Grupos de centros de custo representam uma estrutura hierárquica de centros de custo conhecida como hierarquia padrão. Cada centro de custo criado deve ser atribuído a um grupo na hierarquia padrão. Isto assegura que a hierarquia padrão contenha todos os centros de custo no grupo de controlling. Ao analisar a hierarquia padrão, o sistema SAP inclui automaticamente todos os centros de custo.

Observe que os centros de custo podem ser atribuídos a qualquer número de grupos alternativos. No entanto, grupos alternativos não podem ser criados na atualização da hierarquia padrão.

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

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura de sua empresa. Os dados mestre representam centros de custo e grupos de centros de custo, dependendo do foco operacional da sua empresa.

| Objeto de dados | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de contabilidade de custos | Dados gerais | Obrigatório |  |
| Empresa | Unidades organizacionais | Obrigatório |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do centro de custo e do grupo de centros de custo podem fazer referência a outros dados mestre. A tabela seguinte oferece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados do centro de custo.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de hierarquia | Unidades organizacionais | Obrigatório |  |
| Divisão | Unidades organizacionais | Opcional |  |
| Área funcional | Unidades organizacionais | Opcional |  |
| Centro de lucro | Unidades organizacionais | Obrigatório |  |

### Parâmetros principais para a criação de dados

Este item de escopo não tem condições empresariais.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar dados mestre do centro de custo](#unique_9) [página ] 6 | Controlador - custos indiretos | Administrar centros de custo - Versão antiga(F1443A) | Os centros de custo podem ser criados de acordo com os novos requisitos empresariais. |
| [Criar dados mestre do grupo de centros de custo](#unique_10) [página ] 8 | Controlador - custos indiretos | Administrar hierarquias de contabilidade global(F2918) ou Administrar grupos de centros de custo(F1024) | Os grupos de centros de custo podem ser criados de acordo com os novos requisitos empresariais. |
| [Lista de utilizações - Dados reais de centros de custo](#unique_11) [página ] 10 | Controlador - custos indiretos | Administrar centros de custo - Versão antiga(F1443A) |  |

## Procedimentos de teste

Esta seção descreve os procedimentos para cada etapa do processo que pertence a este item de escopo. Você pode também pode usar estes procedimentos para testar a criação de dados mestre.

### Criar dados mestre do centro de custo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

|  |
| --- |
| Nota Nó de hierarquia padrão 1~A partir da edição 2502, para novas instalações do cliente, a hierarquia padrão será fornecida usando a funcionalidade de hierarquia global com o valor de 1~. Os clientes anteriores podem continuar usando o valor da hierarquia padrão baseada em conjuntos de 0001.Ao criar o primeiro centro de custo no sistema produtivo, você deve inserir o valor 1~ na lista de opções de pesquisa no campo Nó de hierarquia padrão. Isso estabelece o nó de nível superior 1~ na hierarquia padrão. Assim que o primeiro centro de custo no sistema for criado, o nó de hierarquia padrão 1~ também é criado automaticamente. A partir da edição 25092, o conteúdo padrão do SAP S/4HANA Cloud Public Edition Public Edition é sempre fornecido com a hierarquia padrão 1~ e deve ser usado como o nível superior. |

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar centros de custo - Versão antiga(F1443A). | O app é aberto. |  |
| 3 | Criar um novo centro de custo | Selecione Criar para criar um novo centro de custo. |  |  |
| 4 | Inserir novo centro de custo | Na guia Informações gerais, efetue as seguintes entradas:Centro de custo: <texto>Nome: <texto>Descrição: <texto>Responsável: <responsável>Válido desde:<01/01/2017>Válido até:<31/12/9999>Categoria do centro de custo: <tipo de centro de custo>Opcionalmente, você pode modificar os valores propostos para datas válidas e selecionar uma referência dos dados mestre do centro de custo existentes. | É aberta uma nova seção exibindo as Informações gerais. |  |
| 5 | Inserir dados organizacionais de centro de custo | Na seção Unidades organizacionais, na tela Centro de custo, efetue as seguintes entradas:Nó de hierarquia padrão: <1~>Empresa: <empresa>Área funcional: <área funcional>Centro de lucro: <Centro de lucro>Somente para PSM:Nota Se você tiver Administração do Setor Público (PSM) instalado, esses campos estarão disponíveis para entrada após a seleção da empresa PSM.Fundos: <fundo>Atribuição fixa de fundo: <sim/não>Subsídio: <subsídio>Atribuição fixa do subsídio: <sim/não>Atribuição fixa de área funcional: <sim/não>Nota O campo de seleção Atribuição fixa para a área funcional, fundo e subsídio público será exibido somente depois de inserir os respectivos dados mestre.Transporte de orçamento de centro de custo: <centro de custos>Perfil de controle de disponibilidade de orçamento: <perfil>Controle de disponibilidade de orçamento está ativo: <sim/não> | A seleção é rolada, exibindo dados organizacionais. |  |
| 6 | Criar | Selecione Criar. | O centro de custo é criado. |  |

### Criar dados mestre do grupo de centros de custo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Pré-requisito

Para este capítulo, os dados básicos para o material já devem estar preenchidos como descrito no capítulo: [Criar dados mestre do centro de custo](#unique_9) [página ] 6. Inicie este procedimento depois de salvar as entradas de dados mestre, como descrito no capítulo anterior.

|  |
| --- |
| Nota Administrar hierarquias de contabilidade global(F2918) ou Administrar grupos de centros de custo(F1024) podem ser usados ao criar hierarquias alternativas, mas apenas um método (Grupos de hierarquias globais ou Grupos baseados em conjuntos) deve ser selecionado. Ambos os métodos estão descritos nas etapas abaixo.Os clientes existentes podem continuar usando o app Administrar grupos de centros de custo(F1024) relacionado a grupos baseados em conjuntos até que eles migrem completamente e marquem o status da migração como Concluído usando a função de especialista BPC por meio deste caminho: Configuração de processo empresarial > Contabilidade > Configurações gerais: Migrar grupos baseados em conjuntos para hierarquias globais (F6228).Os dados mestre de demonstração do grupo de centros de custo fornecidos pela SAP também são criados usando grupos baseados em conjuntos e também podem ser convertidos.Você pode encontrar mais informações sobre a conversão de Grupo de centros de custo em Hierarquia global via: [https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT](https://help.sap.com/docs/SAP_S4HANA_CLOUD/c56f622a2edf491b9f1b596b55587009/635e615de9a848eb9129edb0da88cbcc.html?state=DRAFT). |

Procedimento: Opção 1 – Grupos de hierarquia global

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar hierarquias de contabilidade global(F2918). | O app é aberto. |  |
| 3 | Clicar em Criar | Na seção Lista de hierarquias, clique em Criar. | A tela Nova hierarquia é exibida. |  |
| 4 | Inserir nova hierarquia de centros de custo | Na tela Nova hierarquia, efetue as seguintes entradas e clique em Criar:Tipo: Hierarquia de centros de custoID da hierarquia: <qualquer ID de até 10 caracteres>Atenção O comprimento total do ID da hierarquia e do ID do nó não pode exceder 14 caracteres.Área de contabilidade de custos: A000Descrição da hierarquia: <qualquer descrição>Válido desde: <Data atual> |  |  |
| 5 | Editar nova hierarquia de custos | Na tela Lista de hierarquias, clique no ícone de detalhes > e selecione Editar para sua hierarquia de centros de custo recém-criada.Selecione a hierarquia de centros de custo recém-criada, clique em Mais no lado direito da tela e, em seguida, selecione Entrada rápida.Na tela Entrada rápida, selecione Centro de custo e efetue a seguinte entrada:ID: <selecione os centros de custo que deseja adicionar usando a função de pesquisa>Clique em OK quando terminar e selecione Salvar.Volte para a tela Hierarquia de centros de custo e selecione Ativar. | A hierarquia de centros de custo recém-criada está agora ativada. |  |

Procedimento: Opção 2 – Grupos baseados em conjuntos

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar grupos de centros de custo(F1024). | O app é aberto. |  |
| 3 | Criar um novo grupo de centros de custo | No painel Lista de resultados: grupo de centros de custo, selecione Novo. |  |  |
| 4 | Inserir novo grupo de centros de custo | Na tela Grupo de centros de custo: nova, efetue as seguintes entradas:Área de contabilidade de custos: <A000>Grupo de centros de custo: <grupo de centros de custo>Clique em Continuar e efetue a seguinte entrada:Nome: <nome>Clique em Salvar.Como alternativa, escolha uma referência dos grupos de centros de custos existentes. | A tela Grupos de centros de custo: novo é exibida. |  |
| 5 | Inserir dados organizacionais de centro de custo | Na tela Grupos de centros de custo: nova, efetue as seguintes entradas:No nível superior, você pode criar dados mestre novos com Novo:novo grupo inferior: <grupo de centros de custo>Nos níveis inferiores, você pode adicionar com Novo:novo grupo inferior: <grupo de centros de custo>Novo grupo do mesmo nível: <grupo de centros de custo>No nível superior, você pode adicionar dados mestre existentes com Adicionar:Adicionar grupo inferior: <grupo de centros de custo>Adicionar centro de custo: <centro de custos>Adicionar área de centro de custo: <centros de custo>Nos níveis inferiores, você pode adicionar com Novo:novo grupo inferior: <grupo de centros de custo>Novo grupo do mesmo nível: <grupo de centros de custo>Adicionar centro de custo: <centro de custos>Adicionar área de centro de custo: <centros de custo> | Os novos dados mestre são exibidos na tela Grupos de centros de custos: novo. |  |
| 6 | Salvar os dados | Clique em Salvar. | O grupo de centros de custo é criado e salvo. |  |

### Análise

#### Lista de utilizações - Dados reais de centros de custo

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Esta atividade permite ver onde os centros de custo são utilizados em outros dados mestre como tipo de atividade, centros de lucro e alocações de custos reais.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. |  |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar centros de custo - Nova versão(F1443B). | A tela Administrar centros de custo é exibida. |  |
| 3 | Inserir critérios de seleção | Efetue a seguinte entrada e clique em Ir:Centro de custo: <seu centro de custo |  |  |
| 4 | Lista de utilizações | Selecione o centro de custo desejado e clique em Lista de utilizações.Selecione uma opção na lista de opções. Por exemplo, Em todos os objetos. | Um relatório é exibido, mostrando os locais em que os centros de custo vêm sendo usados. Para mais detalhes, selecione o tipo de objeto de dados mestre e continue a pesquisa. |  |

|  |
| --- |
| Nota O app Lista de utilizações - Centros de custo(F3549) também pode servir para determinar onde os centros de custo estão sendo usados atualmente. |

## Anexo

### Replicação do centro de custo do SAP S/4HANA Cloud Public Edition para o SAP Master Data Integration (opcional)

Este link descreve a replicação de dados mestre do centro de custo do SAP S/4HANA Cloud Public Edition por meio do SAP Master Data Integration para outras aplicações na nuvem, como o SAP SuccessFactors:[https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html](https://help.sap.com/viewer/6b39bd1d0e5e4099a5b65d835c29c696/LATEST/en-US/decbb94c95fa421ead9101e4c43683f7.html).

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
- related-to :: [[06-management-accounting/create-cost-center-and-cost-center-group-mds-bnm-635]]
- related-to :: [[06-management-accounting/mds-bnm-637]]
- related-to :: [[06-management-accounting/mds-bnm-639]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-centro-de-coste-y-grupo-de-centros-de-c]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNM_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 21,038 chars in the whole document
