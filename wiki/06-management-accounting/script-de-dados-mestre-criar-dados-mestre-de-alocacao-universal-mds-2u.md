---
id: 06-management-accounting/script-de-dados-mestre-criar-dados-mestre-de-alocacao-universal-mds-2u
title: "Script de dados mestre: Criar dados mestre de alocação universal - MDS (2US) (2US_S4CLD2608_Master_Data_PT_XX)"
description: Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (2US) for creating planned/actual universal allocation cycles for cost centers and profit centers.
cluster: 06-management-accounting
tags: [kb/management-accounting, topic/universal-allocation]
aliases: [2US_S4CLD2608_Master_Data_PT_XX]
keywords: [Universal Allocation Cycles, universal allocation, planned cost allocation, actual cost allocation, profit center distribution, allocation cycle upload, master data, business roles, overhead cost controlling, 2US]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-290
topic: 06-management-accounting/universal-allocation
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar dados mestre de alocação universal - MDS (2US) (2US_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Universal Allocation Cycles** in Management Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar dados mestre de alocação universal - MDS (2US) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893586)

[2 Pré-requisitos 3](#_Toc233893587)

[2.1 Acesso ao sistema 3](#_Toc233893588)

[2.2 Funções 3](#_Toc233893589)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893590)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893591)

[3 Tabela de síntese 5](#_Toc233893592)

[4 Procedimentos de teste 6](#_Toc233893593)

[4.1 Alocações planejadas 6](#_Toc233893594)

[4.1.1 Administrar ciclos de avaliação de custos indiretos planejados 6](#_Toc233893595)

[4.1.2 Editar ciclos de alocação de custos indiretos reais 8](#_Toc233893596)

[4.2 Alocações reais 10](#_Toc233893597)

[4.2.1 Administrar ciclos de avaliação de custos indiretos reais 10](#_Toc233893598)

[4.2.2 Editar ciclos de avaliação de custos indiretos reais 12](#_Toc233893599)

[4.3 Alocação de centros de lucro de plano 14](#_Toc233893600)

[4.3.1 Administrar ciclos de distribuição de centros de lucro planejados 14](#_Toc233893601)

[4.4 Alocação de centros de lucro real 16](#_Toc233893602)

[4.4.1 Administrar ciclos de distribuição de centros de lucro reais 16](#_Toc233893603)

## Objetivo

A alocação universal cobre avaliações/distribuições planejadas e reais de centros de custo no controlling dos custos indiretos por meio de várias combinações de emissor e receptor de montantes, porcentagens e partes. Esses dados mestre dão suporte ao planejamento anual por meio da redistribuição do custo via alocação predefinida e ciclos de distribuição em uma empresa específica. Alocando elementos de custo a centros de custo no controlling dos custos indiretos, você consegue controlar seus custos e comparar os custos planejados com os reais. Além disso, há suporte a avaliações/distribuições planejadas e reais de centros de lucro.

Este script oferece alguns exemplos gerais da criação de dados mestre com alocação universal, mas você pode adaptá-lo de acordo com as necessidades da sua empresa utilizando as diversas combinações de emissor/receptor de montantes, porcentagens e partes.

Este documento fornece um procedimento detalhado para testar o item de escopo após a ativação da solução, refletindo o escopo predefinido da solução. Cada etapa do processo, relatório ou item está coberto em uma seção própria que fornece as interações do sistema (etapas de teste) em uma visão de tabela. As etapas que não estão no escopo do processo, mas que são necessárias para teste, estão marcadas de modo correspondente. É necessário adicionar etapas específicas do projeto.

|  |
| --- |
| Nota Os valores deste script de teste (notação decimal, formatos de data etc.) são apresentados na notação padrão dos EUA. Se o sistema de teste estiver configurado para usar uma notação diferente, insira os valores apropriados. |

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
| Controlador – Custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT | Contabilidade de custos indiretos | SAP_BR_OVERHEAD_ACCOUNTANT |  |
| Contador divisional | SAP_BR_DIVISION_ACCOUNTANT |  |  |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura de sua empresa. Os dados mestre representam centros de custo e grupos de centros de custo, dependendo do foco operacional da sua empresa.

| Objeto de dados | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Área de contabilidade de custos | Dados gerais | Obrigatório |  |
| Empresa | Unidades organizacionais | Obrigatório |  |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre do centro de custo e do grupo de centros de custo podem fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados na alocação.

| Objeto de dados mestre | Obrigatório/opcional | Comentários |
| --- | --- | --- |
| Centro de custo | Obrigatório |  |
| Classe de custo | Obrigatório |  |
| Índice estatístico | Opcional |  |
| Centro de lucro | Obrigatório |  |

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

Alocações planejadas

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar ciclos de avaliação de custos indiretos planejados](#unique_8) [página ] 6 | Controlador - custos indiretos | Administrar alocações(F3338A) | Os custos são alocados para grupos de centros de custo, centros de custo ou intervalos de valores. |
| [Editar ciclos de alocação de custos indiretos reais](#unique_9) [página ] 8 | Controlador - custos indiretos | Administrar alocações(F3338A) | Os ciclos de alocação de custos indiretos planejados são editados. |

Alocações reais

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar ciclos de avaliação de custos indiretos reais](#unique_10) [página ] 10 | Controlador - custos indiretos | Administrar alocações(F3338A) | Os custos são alocados para grupos de centros de custo, centros de custo ou intervalos de valores. |
| [Editar ciclos de avaliação de custos indiretos reais](#unique_11) [página ] 12 | Controlador - custos indiretos | Administrar alocações(F3338A) | Os ciclos de alocação de custos indiretos reais são editados. |

Alocações planejadas de centro de lucro

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar ciclos de distribuição de centros de lucro planejados](#unique_12) [página ] 14 | Contador divisional | Administrar alocações(F3338A) | A alocação planejada de centro de lucro é criada. |

Alocação real de centro de lucro

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Administrar ciclos de distribuição de centros de lucro reais](#unique_13) [página ] 16 | Contador divisional | Administrar alocações(F3338A) | A distribuição de centros de lucro é criada. |

## Procedimentos de teste

### Alocações planejadas

#### Administrar ciclos de avaliação de custos indiretos planejados

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Nesse exemplo, o ciclo de avaliação de custos indiretos planejados utiliza classes de custo secundário para alocar custos de um centro de custo ou de um grupo de centros de custo para outro centro de custo ou grupo de centros de custo segundo uma porcentagem fixa na mesma empresa.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Criar cabeçalho de ciclo | Clique no botão Criar e selecione Criar novo ciclo. | A caixa de diálogo Criar novo ciclo é exibida.Nota O upload em massa de ciclos de alocação é possível para a criação de novas alocações e/ou novos segmentos por meio do app Administrar alocação usando o botão Carregar/baixar modelo. Você pode baixar um modelo em branco ou selecionar um ciclo de alocação existente para baixar como modelo. |  |
| 4 | Insira valores | Efetue as seguintes entradas e clique no botão Criar:Ciclo de alocação: <insira um ID de ciclo que comece com Z>Contexto de alocação: <centros de custo>Tipo de alocação:Alocação de custos indiretosLedger: 0LVálido até: 31/12/2030Descrição do ciclo: <insira uma descrição do ciclo>Empresa: 1010Real/planejado: planejadoCategoria do plano: PLN | A visão <novo ciclo> é exibida. |  |
| 5 | Inserir dados de segmento | Na seção inferior da visão Novo ciclo de alocação, na seção Segmentos, clique no botão Criar, efetue as seguintes entradas na janela Criar novo segmento e clique no botão Criar:Nome de segmento: <insira um segmento comece com Z>Descrição do segmento: <insira uma descrição> | A visão <novo segmento> é exibida. |  |
| 6 | Inserir regras | Selecione o novo segmento e clique na seta à direita.Na guia Regras, efetue as seguintes entradas:Conta de alocação de sobretaxas: 94201000Regra de emissor: montantes lançadosRegra receptor: porcentagens fixasPorcentagem em %: 100Moeda: <insira a moeda local> |  |  |
| 7 | Inserir detalhes do emissor | Na guia Emissores, efetue as seguintes entradas:Número da conta:Modifique o valor na coluna Tipo de valor para GrupoNa coluna Grupo, utilize a lista de opções para selecionar 10_CE na seguinte visão Selecionar: número da contaCentro de custo: 10101101 |  |  |
| 8 | Inserir detalhes do receptor | Na seção Receptores, clique em Adicionar. Na visão Adicionar receptores, selecione Centro de custo e, em seguida, Adicionar. Efetue as seguintes entradas:Centro de custosModifique o valor na coluna Tipo de valor para GrupoNa coluna Grupo, use a lista de opções para selecionar 1010300 na seguinte visão Selecionar: centro de custo |  |  |
| 9 | Base receptor | Na guia Base receptor, clique no botão ... (Opções adicionais) e selecione Distribuir igualmente. | Você verá que os montantes são distribuídos igualmente. |  |
| 10 | Salvar | Clique no botão Salvar. | Os dados estão salvos. |  |

#### Editar ciclos de alocação de custos indiretos reais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Essa atividade demonstra a capacidade de trabalhar com alocações que possuem uma grandes quantidade de dados utilizando modelos.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Inserir valores | Efetue as seguintes entradas e clique no botão Ir:Contexto de alocação: <centros de custo>Empresa: 1010Ledger:0LCiclo de alocação: <o ciclo que acabou de criar> | A visão Ciclos de alocação é exibida. |  |
| 4 | Detalhes do ciclo de alocação | Selecione o seu ciclo de alocação e selecione a seta na direita para ir aos detalhes. Clique no botão Editar. | A visão Administrar alocações é exibida. |  |
| 5 | Seção Segmentos | Role para abaixo até a seção Segmentos, selecione o seu segmento e escolha > (Detalhes) na direita. |  |  |
| 6 | Base receptor | Na guia Base receptor, selecione Carregar/baixar valores. | A visão Carregar valores do receptor é exibida. |  |
| 7 | Carregar valores do receptor | Selecione Baixar modelo com valores. Baixe e salve o arquivo. |  |  |
| 8 | Atualizar porcentagens | No arquivo, atualize a coluna de porcentagem com os valores como mostrado abaixo:Centro de custoPorcentagem001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | As porcentagens são atualizadas. |  |
| 9 | Base receptor | Volte para a guia Base receptor e faça o seguinte:Escolha Carregar/baixar valores.Na visão Carregar valores do receptor, selecione Navegar. Selecione o arquivo salvo. A tela indica se os valores podem ser carregados ou se são necessárias correções. Clique em Confirmar.Clique em Salvar para salvar o ciclo de alocação. | Você pode ver agora que os dados foram atualizados de acordo com o carregamento do arquivo csv. |  |

### Alocações reais

#### Administrar ciclos de avaliação de custos indiretos reais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

O ciclo de alocação de custos indiretos reais utiliza classes de custo secundário para alocar custos de um centro de custo ou de um grupo de centros de custo para outro centro de custo ou grupo de centros de custo segundo uma porcentagem fixa na mesma empresa.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Criar cabeçalho de ciclo | Clique no botão Criar e selecione Criar novo ciclo. | A caixa de diálogo Criar novo ciclo é exibida. |  |
| 4 | Insira valores | Efetue as seguintes entradas e clique no botão Criar:Ciclo de alocação: <insira um ID de ciclo que comece com Z>Contexto de alocação: <centros de custo>Empresa:1010Tipo de alocação:Alocação de custos indiretosLedger: 0LVálido até: 31/12/2030Descrição do ciclo: <insira uma descrição do ciclo>Empresa: 1010Real/planejado: real | A visão Alocação: criar ciclo de rateio plano: dados do cabeçalho é exibida. |  |
| 5 | Inserir dados de segmento | Na seção inferior da visão Novo ciclo de alocação, em Segmentos, selecione o botão Adicionar e efetue as seguintes entradas na janela Criar novo segmento:Nome de segmento: <insira um segmento comece com Z>Descrição do segmento: <insira uma descrição> | A visão Criar um novo ciclo é exibida. |  |
| 6 | Inserir regras | Selecione o novo segmento e clique na seta à direita.Na guia Regras, efetue as seguintes entradas:Conta de alocação de custos indiretos: 94201000Regra de emissor: montantes lançadosRegra receptor: porcentagens fixas |  |  |
| 7 | Inserir detalhes do emissor | Na guia Emissores, efetue as seguintes entradas:Número da conta:Modifique o valor na coluna Tipo de valor para GrupoNa coluna Grupo, use a lista de opções para pesquisar e selecionar 10_CE na seguinte visão Selecionar: número da contaCentro de custo: 10101101Nota Além dos centros de custo padrão e das contas do Razão, agora você pode usar atributos de lançamento contábil específicos, como moeda, área funcional, centro de lucro e segmento, para permitir uma seleção de alocação mais granular na regra do emissor. Para isso, clique no botão Adicionar e selecione as opções desejadas. |  |  |
| 8 | Inserir detalhes do receptor | Na guia Receptores, clique no botão + (Adicionar).Selecione o centro de custo e clique no botão Adicionar.Efetue a seguinte entrada:Centro de custosModifique o valor na coluna Tipo de valor para GrupoNa coluna Grupo, utilize a lista de opções para pesquisar e selecionar 1010300 na seguinte visão Selecionar: centro de custo |  |  |
| 9 | Base receptor | Na guia Base receptor, clique no botão ... (Opções adicionais) e selecione Distribuir igualmente. | Você verá que os montantes são distribuídos igualmente. |  |
| 10 | Salvar | Clique no botão Salvar. | Os dados estão salvos. |  |

#### Editar ciclos de avaliação de custos indiretos reais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Essa atividade demonstra a capacidade de trabalhar com alocações que possuem uma grandes quantidade de dados utilizando modelos.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Controlador - custos indiretos. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Inserir valores | Efetue as seguintes entradas e clique no botão Ir:Contexto de alocação: <centros de custo>Empresa: 1010Ledger:0LCiclo de alocação: <o ciclo que acabou de criar> | A visão Ciclos de alocação é exibida. |  |
| 4 | Detalhes do ciclo de alocação | Selecione o seu ciclo de alocação e selecione a seta na direita para ir aos detalhes. | A visão Administrar alocações é exibida. |  |
| 5 | Seção Segmentos | Role para abaixo até a seção Segmentos, selecione o seu segmento e escolha > (Detalhes) na direita. |  |  |
| 6 | Base receptor | Na guia Base receptor, selecione o Carregar/baixar valores. | A visão Carregar valores do receptor é exibida. |  |
| 7 | Carregar valores do receptor | Selecione Baixar modelo com valores. Baixe e salve o arquivo. |  |  |
| 8 | Atualizar porcentagens | No arquivo, atualize a coluna de porcentagem com os valores como mostrado abaixo:Centro de custoPorcentagem001010110150010101201500101012025001010130150010101302150010101401150010101501150010101601150010101602001010170120 | As porcentagens são atualizadas. |  |
| 9 | Base receptor | Volte para a guia Base receptor e faça o seguinte:Escolha Carregar/baixar valores.Na visão Carregar valores do receptor, selecione Navegar. Selecione o arquivo salvo. A tela indica se os valores podem ser carregados ou se são necessárias correções. Clique em Confirmar.Clique em Salvar para salvar o ciclo de alocação. | Você pode ver agora que os dados foram atualizados de acordo com o carregamento do arquivo csv. |  |

### Alocação de centros de lucro de plano

#### Administrar ciclos de distribuição de centros de lucro planejados

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Este exemplo mostra a distribuição planejada de saldos da conta de balancetes para e a partir de vários centros de lucro.

Pré-requisito

É preciso que uma conta do Razão para compensação de alocação esteja disponível. Crie a compensação de alocação do Razão 29500000 CO usando o Razão 29500100 como referência. Para obter detalhes sobre como criar o Razão, consulte Criar conta do Razão e classe de custo – MDS (BNG).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador divisional. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Criar cabeçalho de ciclo | Clique no botão Criar e selecione Criar novo ciclo. | A caixa de diálogo Criar novo ciclo é exibida. |  |
| 4 | Inserir valores | Efetue as seguintes entradas e clique no botão Criar:Ciclo de alocação: <insira um ID de ciclo que comece com Z>Contexto de alocação: <centros de lucro>Empresa:1010Tipo de alocação:distribuiçãoLedger: 0LVálido até: 31/12/2030Descrição do ciclo: <insira uma descrição do ciclo>Empresa: 1010Real/planejado: planejadoCategoria do plano: PLN | A visão Administrar alocações é exibida. |  |
| 5 | Inserir dados de segmento | Na seção inferior da visão Administrar alocações, na seção Segmentos, clique no botão Criar e efetue as seguintes entradas na janela Criar novo segmento:Nome de segmento: <inserir outro segmento que comece com ZD>Descrição do segmento: <insira uma descrição>Clique em OK. |  |  |
| 6 | Inserir regras | Na guia Regras, efetue as seguintes entradas:Moeda:<insira a moeda local>Regra do emissor:montantes fixosPorcentagem em %: 100Regras do receptor: porcentagens fixasSelecione a guia Emissores. |  |  |
| 7 | Inserir detalhes do emissor | Na guia Emissores, efetue as seguintes entradas:Número da conta:29500000Centro de lucro: YB600Clique na guia Base do emissor. |  |  |
| 8 | Base do emissor | Efetue a seguinte entrada:Montante: 100000Selecione a guia Receptores. |  |  |
| 9 | Inserir detalhes do receptor | Na seção Receptores, clique em + (Adicionar). Na visão Adicionar receptores, selecione Centro de lucro. Clique no botão Adicionar e efetue as seguintes entradas:Tipo de valor: intervaloEntrada individual/de: YB700Valor Até: YB800Clique na guia Base receptor. |  |  |
| 10 | Base receptor | Na guia Base receptor, clique no botão ... (Opções adicionais) e selecione Distribuir igualmente. | Você verá que os montantes são distribuídos igualmente. |  |
| 11 | Salvar | Clique no botão Salvar. | A distribuição de centros de lucro de plano é criada. |  |

### Alocação de centros de lucro real

#### Administrar ciclos de distribuição de centros de lucro reais

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Contexto

Este exemplo mostra a distribuição real de saldos da conta de balancetes para e a partir de vários centros de lucro.

Pré-requisito

É preciso que uma conta do Razão para compensação de alocação esteja disponível. Crie a compensação de alocação do Razão 29500000 CO usando o Razão 29500100 como referência. Para obter detalhes sobre como criar o Razão, consulte Criar conta do Razão e classe de custo – MDS (BNG).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Contador divisional. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar alocações(F3338A). | A visão Administrar alocações é exibida. |  |
| 3 | Criar cabeçalho de ciclo | Clique no botão Criar e selecione Criar novo ciclo. | A caixa de diálogo Criar novo ciclo é exibida. |  |
| 4 | Inserir valores | Efetue as seguintes entradas e clique no botão Criar:Ciclo de alocação: <insira um ID de ciclo que comece com Z>Contexto de alocação: <centros de lucro>Empresa:1010Tipo de alocação:distribuiçãoLedger: 0LVálido até: 31/12/2030Descrição do ciclo: <insira uma descrição do ciclo>Empresa: 1010Real/planejado: real | A visão Alocação: Criar ciclo de distribuição planejado: dados de cabeçalho é exibida. |  |
| 5 | Inserir dados de segmento | Na seção inferior da visão Gerenciar alocações, na seção Segmentos, selecione o botão Adicionar e efetue as seguintes entradas na janela Criar novo segmento:Nome de segmento: <inserir outro segmento que comece com ZD>Descrição do segmento: <insira uma descrição> | A visão Alocação: Criar ciclo de distribuição planejado: dados de cabeçalho é exibida. |  |
| 6 | Inserir regras | Selecione o segmento recém-criado e clique no sinal > à direita. Na guia Regras, efetue as seguintes entradas:Moeda:<insira a moeda local>Regra do emissor: montantes fixosPorcentagem em %: 100Regras do receptor: porcentagens fixasSelecione a guia Emissores. |  |  |
| 7 | Inserir detalhes do emissor | Na guia Emissores, efetue as seguintes entradas:Número da conta:29500000Centro de lucro: YB600Clique na guia Base do emissor. |  |  |
| 8 | Base do emissor | Efetue a seguinte entrada:Montante: 100000Selecione a guia Receptores. |  |  |
| 9 | Inserir detalhes do receptor | Na seção Receptores, clique em + (Adicionar). Na visão Adicionar receptores, selecione Centro de lucro. Clique no botão Adicionar e efetue as seguintes entradas:Tipo de valor: intervaloEntrada individual/de: YB700Valor Até: YB800Clique na guia Base receptor. |  |  |
| 10 | Base receptor | Na guia Base receptor, clique no botão ... (Opções adicionais) e selecione Distribuir igualmente. | Você verá que os montantes são distribuídos igualmente. |  |
| 11 | Salvar | Clique no botão Salvar. | A distribuição de centros de lucro é criada. |  |

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
- related-to :: [[06-management-accounting/create-universal-allocation-master-data-mds-2us-287]]
- related-to :: [[06-management-accounting/mds-2us-289]]
- related-to :: [[06-management-accounting/mds-2us-291]]
- related-to :: [[06-management-accounting/script-de-datos-maestros-crear-datos-maestros-de-asignacion-universal]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2US_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 29,416 chars in the whole document
