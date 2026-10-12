---
id: 09-subscription-billing-and-contract-accounting/script-de-dados-mestre-criar-dados-mestre-do-produto-para-faturamento
title: Script de dados mestre - Criar dados mestre do produto para faturamento baseado em consumo (3JA) (3JA_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese master data script (3JA) for SAP S/4HANA Cloud Public Edition: create configurable material with variant pricing for consumption-based billing."
cluster: 09-subscription-billing-and-contract-accounting
tags: [kb/subscription-billing-and-contract-accounting, topic/variant-configured-products-in-provider-contracts]
aliases: [3JA_S4CLD2608_Master_Data_PT_XX]
keywords: [Variant-Configured Products in Provider Contracts, product master data, consumption-based billing, configurable material, characteristics, classes, configuration profile, material classification, variant pricing, sales data]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-326
topic: 09-subscription-billing-and-contract-accounting/variant-configured-products-in-provider-contracts
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar dados mestre do produto para faturamento baseado em consumo (3JA) (3JA_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Variant-Configured Products in Provider Contracts** in Subscription Billing and Contract Accounting. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar dados mestre do produto para faturamento baseado em consumo – MDS (3JA) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893634)

[2 Pré-requisitos 3](#_Toc233893635)

[2.1 Acesso ao sistema 3](#_Toc233893636)

[2.2 Funções 3](#_Toc233893637)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893638)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893639)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893640)

[2.5.1 Agrupamentos e intervalos de numeração 4](#_Toc233893641)

[2.5.2 Setor industrial 5](#_Toc233893642)

[3 Tabela de síntese 6](#_Toc233893643)

[4 Procedimentos de teste 7](#_Toc233893644)

[4.1 Criar mestre de materiais configurável - Dados básicos 7](#_Toc233893645)

[4.2 Criar característica 8](#_Toc233893646)

[4.3 Criar classe 10](#_Toc233893647)

[4.4 Criar perfil de configuração 12](#_Toc233893648)

[4.5 Criar mestre de materiais – Classificação 13](#_Toc233893649)

[4.6 Criar determinação de preço variante 14](#_Toc233893650)

[4.7 Criar dados mestre de produtos – Dados de vendas / dados do IVA 15](#_Toc233893651)

## Objetivo

Neste documento você encontra uma descrição sobre como criar um registro de dados mestre de materiais para o seu sistema SAP S/4HANA Cloud Public Edition. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo de conteúdo do SAP S/4HANA Cloud Public Edition não estão descritos neste documento, embora possam aparecer na IU.

Um registro mestre do produto com determinação de preços variante criado da forma aqui descrita pode ser utilizado para o faturamento baseado em consumo.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via SAP Fiori Launchpad. O administrador do sistema fornece a você o URL para acessar os vários aplicativos atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Modelador de configuração de produto | SAP_BR_PRODUCT_CONFIG_MODELER | Configuração de variantes | SAP_BR_PRODUCT_CONFIG_MODELER |  |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do material (texto breve), número do material, grupo de materiais, unidade de medida básica etc. | Os dados básicos só existem uma vez para um registro de dados mestre de materiais. | n/a |
| Dados de vendas | Centro, organização de vendas, canal de distribuição | Dados do imposto, grupo de categorias do item etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. | Centro: ____________ Organização de vendas: __________ Canal de distribuição: __________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre pode fazer referência a outros dados mestre. A tabela a seguir fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem usados em um registro de dados mestre.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais:

#### Agrupamentos e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

#### Setor industrial

O conteúdo padrão fornece apenas um setor industrial M. Atualmente, isso é visível apenas no SAP GUI

## Tabela de síntese

Este registro mestre é composto por vários segmentos fornecidos na tabela a seguir.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar mestre de materiais configurável - Dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de materiais – Dados básicos criados. |
| [Criar característica](#unique_12) [página ] 8 | Modelador de configuração de produto | Administrar características(CT04) | A característica é criada. |
| [Criar classe](#unique_13) [página ] 10 | Modelador de configuração de produto | Administrar classes(CL02) | A classe é criada. |
| [Criar perfil de configuração](#unique_14) [página ] 12 | Modelador de configuração de produto | Ambiente de modelagem VC(PMEVC) | O perfil de configuração é criado. |
| [Criar mestre de materiais – Classificação](#unique_15) [página ] 13 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de material – Classificação criada. |
| [Criar determinação de preço variante](#unique_16) [página ] 14 | Modelador de configuração de produto | Ambiente de modelagem VC(PMEVC) | A condição da variante é mapeada para um valor da característica. |
| [Criar dados mestre de produtos – Dados de vendas / dados do IVA](#unique_17) [página ] 15 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de materiais – Dados de vendas (dados de IVA) criados. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa do processo que faz parte deste registro mestre.

### Criar mestre de materiais configurável - Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nessa etapa do processo, você cria visão de dados básicos para o mestre de materiais.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <CBPTS001>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada será necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A tela Selecionar visões é exibida. |  |
| 4 | Selecionar visões | Na tela Seleção de visões, clique em Dados básicos 1 e Dados básicos 2. Em seguida, clique em Continuar. | A tela Criar material (materiais configuráveis) é exibida. |  |
| 5 | Inserir dados básicos | Na tela Criar material CBPTS001 (materiais configuráveis), na guia Dados básicos 1, insira a descrição do material (texto breve).Por exemplo, insira <Ferramentas baseadas no consumo>. |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as entradas seguintes:Unidade de medida básica: <UN>GrpCtgsItemGer.: <0003> |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue a seguinte entrada:Unidade de peso: KGSelecione a guia Dados básicos 2. |  |  |
| 8 | Inserir dados básicos | Na guia Dados básicos 2, você não precisa efetuar entradas.Pressione Enter. | A tela Última visão de dados alcançada é exibida com a mensagem: O processamento será encerrado. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Na tela Última visão de dados alcançada, clique em Sim. | É exibida a tela Criar material (1ª tela).Os dados básicos são criados e salvos. |  |

### Criar característica

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta etapa de processo você cria uma característica.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Abra Administrar dados mestre de cliente. | Abra Administrar características(CT04). | O app é aberto. | Tela comum para o modo de criação, modificação e exibição. |
| 3 | Inserir nome da característica | Efetue a seguinte entrada e clique em Criar:Característica: <CATEGORY> | A tela Criar característica é exibida. | O valor no campo Válido desde é preenchido automaticamente.Se a característica <CATEGORY> já existir, crie a característica <CATEGORY>_Vnn, em que nn é o número sequencial. |
| 4 | Inserir dados básicos | Na guia Dados básicos, efetue as seguintes entradas:A seção Dados básicos:Descrição: <Category>Status: Liberado (padrão)A seção Formato:Tipo de dados: Formato de caracteresNúmero de características: <15>Considerar maiúsculas/minúsculas: <desmarcado>A seção Avaliação:Selecione o botão de rádio Valor individual.Desmarque a caixa de seleção Restringível. |  |  |
| 5 | Inserir valores | Na guia Valores, na seção Valores permitidos, efetue as entradas a seguir.Valor caract.:<STANDARD><HIGH_END>Descrição:<Ferramentas elétricas standard><Ferramentas elétricas de alto nível>Marque a caixa de seleção Valor padrão para o valor <STANDARD>. |  |  |
| 6 | Salvar a característica | Clique em Salvar. | A característica é criada. |  |
| 7 | Criar outra característica | Efetue a seguinte entrada e clique em Criar:Característica: <CATEGORY_VARCOND> |  |  |
| 8 | Inserir dados básicos | Na guia Dados básicos, efetue as seguintes entradas:A seção Dados básicos:Descrição: <Chave de condição de variante>Status: Liberado (padrão)A seção Formato:Tipo de dados: Formato de caracteresNúmero de características: <26>Considerar maiúsculas/minúsculas: <selecionado>A seção Avaliação:Selecione o botão de rádio Valores múltiplos.Desmarque a caixa de seleção Restringível. |  |  |
| 9 | Inserir dados adicionais | Na guia Dados adicionais, efetue as seguintes entradas:A seção Referência ao campo de tabela:Nome da tabela: SDCOMNome do campo: VKONDA seção Comportamento para avaliação:Não disponível para entrada: <desmarcado> |  |  |
| 10 | Salvar a característica | Clique em Salvar. |  |  |

### Criar classe

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta etapa de processo, você cria uma classe com o tipo de classe - 300.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar classes(CL02). | O app é aberto. | Tela comum para o modo de criação, modificação e exibição. |
| 3 | Inserir nome de classe | Efetue as seguintes entradas e clique em Criar:Classe: <CATEGORY>Tipo de classe: 300 | A tela Criar classe é exibida. | O valor no campo Válido desde é preenchido automaticamente.Se a classe <CATEGORY> já existir, crie a classe <CATEGORY>_Vnn, em que nn é o número sequencial. |
| 4 | Inserir dados básicos | Na guia Dados básicos, efetue as seguintes entradas:Na seção Dados básicos:Descrição: <Categoria de ferramentas elétricas>Status: Liberado (padrão)Na seção Mesma classificação:Clique no botão de rádio Não verificar (padrão). |  | Se você usar a mesma classificação, então pode selecionar o método de verificação (mensagem de aviso, erro, nenhuma). |
| 5 | Inserir característica | Na guia Caract., efetue as seguintes entradas:Caract.: <CATEGORY>Caract.: <CATEGORY_VARCOND> |  |  |
| 6 | Salvar a classe | Clique em Salvar. | A classe é criada. |  |

### Criar perfil de configuração

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta etapa do processo, você cria um perfil de configuração.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Ambiente de modelagem VC(PMEVC). | O app é aberto. |  |
| 3 | Inserir dados de modelo de configuração | Na tela inicial, efetue as seguintes entradas e clique em Inserir modelo:Material: <CBPTS001>Tipo de classe: 300 (padrão) | A tela de configuração é exibida. |  |
| 4 | Criar perfil de configuração | Na seção Objeto, clique com o botão direito em <CBPTS001> e selecione Criar perfil de configuração.Na caixa de diálogo Criar perfil de configuração, efetue a seguinte entrada.Perfil de configuração: <CBPT_CP_V01>Selecione Continuar. | A tela Perfil de configuração é exibida no painel direito e a guia Dados básicos é selecionada. |  |
| 5 | Salvar o perfil de configuração | Selecione Salvar. | O perfil de configuração é criado. |  |

### Criar mestre de materiais – Classificação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nesta etapa do processo, você cria a visão de classificação para o mestre de materiais.

Pré-requisito

Você deve completar as etapas da seção anterior, [Criar mestre de materiais configurável - Dados básicos](#unique_11) [página ] 7, antes de continuar com esta seção. Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <CBPTS001>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido no escuro.Tipo de material: KMAT – Materiais configuráveis | A tela Seleção de visões é exibida. |  |
| 4 | Selecionar visões | Na tela Seleção de visões, selecione Classificação e, em seguida, Continuar. | A tela Tipo de classe (1) é exibida. |  |
| 5 | Inserir tipo de classe | Na seção Nível de restrição, selecione as seguintes entradas e em seguida Continuar:Descrição do tipo de classe: VariantesTipo: 300 | A tela Classificação é exibida. |  |
| 6 | Inserir dados de classificação | Na tela Classificação, na guia Atribuições, insira os dados a seguir na coluna Classe e clique em Salvar.<CATEGORY>Sob os valores para a classe CATEGORY – objeto <CBPTS001>, insira os valores a seguir na coluna Valor e clique em Salvar.<STANDARD><HIGH_END> | Seus dados são salvos. |  |

### Criar determinação de preço variante

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

A condição da variante é mapeada para um valor da característica.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Modelador de configuração de produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Ambiente de modelagem VC(PMEVC). | O app é aberto. |  |
| 3 | Inserir dados de modelo de configuração | Na 1ª tela, efetue as seguintes entradas e clique em Inserir atualização do modelo:Material: <CBPTS001>Tipo de classe: 300 (padrão) | A tela de configuração é exibida. |  |
| 4 | Criar determinação de preço variante | Na seção Objeto, clique duas vezes em <CBPTS001> e selecione a guia Determinação do preço de variante no painel direito.Selecione Modificar e efetue as seguintes entradas:Característica: <CATEGORY>Valor car.: <HIGH_END>Cond. variante: <HIGH_END> |  |  |
| 5 | Salvar a configuração | Selecione Salvar. | A determinação de preços variante é criada. |  |

### Criar dados mestre de produtos – Dados de vendas / dados do IVA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Nessa etapa do processo, você cria visão de dados de venda para o mestre de materiais.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: <CBPTS001>Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A tela Seleção de visões é exibida. |  |
| 4 | Selecionar Visões | Na tela Seleção de visões, clique em Vendas: dados organizacionais de vendas 1, Vendas: Dados organizacionais de vendas 2 e Vendas: dados gerais/do centro e, em seguida, clique em Continuar. | É exibida a tela Níveis organizacionais. |  |
| 5 | Inserir dados dos níveis organizacionais | Na tela Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas e clique em Continuar:Centro: Por exemplo, <1010>.Organização de vendas: Por exemplo, <1010 para o centro 1010>.Canal distrib.: Por exemplo, <10>. | A tela Criar material (materiais configuráveis) é exibida.Você chama a seguinte mensagem de sistema na parte inferior da tela: o material já existe e será ampliado. |  |
| 6 | Inserir dados de vendas | Na tela Criar material CBPTS001 (materiais configuráveis), na guia Vendas: organização de vendas 1, insira um valor apropriado para a Classificação fiscalEm geral, este valor é 1 para totalmente tributável.Pressione Enter. | A guia Vendas: organização de vendas 2 é exibida.O valor inserido indica que o material é (geralmente) totalmente tributável. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento, efetue a seguinte entrada e pressione Enter:Grupo de categorias de item <0003> | A guia Vendas: geral/centro é exibida. |  |
| 8 | Inserir dados de vendas | Na guia Vendas: geral/centro, na seção Dados gerais, efetue a seguinte entrada e pressione Enter:Verificação de disponibilidade: Por exemplo, <NC>. | A tela Última visão de dados alcançada é exibida com a mensagem: O processamento será encerrado. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Clique em Sim na tela Última visão de dados alcançada. | A tela Dados mestre – Produto é exibida.Os dados estão salvos. |  |

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
- related-to :: [[09-subscription-billing-and-contract-accounting/master-data-script-create-product-master-for-consumption-based-billing]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-325]]
- related-to :: [[09-subscription-billing-and-contract-accounting/mds-3ja-327]]
- related-to :: [[09-subscription-billing-and-contract-accounting/script-de-datos-maestros-creacion-de-maestro-de-productos-para-factura]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3JA_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 26,524 chars in the whole document
