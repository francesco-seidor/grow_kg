---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-material-confi
title: Script de dados mestre - Criar mestre de produtos do tipo Material configurável (MDS 2T7) (2T7_S4CLD2608_Master_Data_PT_XX)
description: "SAP S/4HANA Cloud Public Edition 2608 master data script (PT) 2T7: test steps to create a KMAT configurable material via MM01 or F1602, across all views."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/variant-configuration-master-data]
aliases: [2T7_S4CLD2608_Master_Data_PT_XX]
keywords: [Configurable Materials and Characteristic Display, configurable material, product master data, basic data, sales data, purchasing data, classification, mrp planning data, accounting valuation data, work scheduling]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-284
topic: 02-business-partner-and-product-master-data/variant-configuration-master-data
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo Material configurável (MDS 2T7) (2T7_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Configurable Materials and Characteristic Display** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Material configurável" – MDS (2T7) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893597)

[2 Pré-requisitos 3](#_Toc233893598)

[2.1 Acesso ao sistema 3](#_Toc233893599)

[2.2 Funções 3](#_Toc233893600)

[2.3 Condições empresariais 3](#_Toc233893601)

[2.4 Unidades organizacionais necessárias 4](#_Toc233893602)

[2.5 Dados mestre obrigatórios e opcionais 5](#_Toc233893603)

[2.6 Parâmetros principais para a criação de dados 5](#_Toc233893604)

[2.6.1 Tipo de material e intervalos de numeração 5](#_Toc233893605)

[2.6.2 Setor industrial 6](#_Toc233893606)

[3 Tabela de síntese 7](#_Toc233893607)

[4 Procedimentos de teste 8](#_Toc233893608)

[4.1 Criar dados mestre de produtos – Dados básicos 8](#_Toc233893609)

[4.2 Criar dados mestre de produtos – Dados de vendas / dados do IVA 11](#_Toc233893610)

[4.3 Criar dados mestre do produto – Dados de compras 14](#_Toc233893611)

[4.4 Criar dados mestre do produto – Classificação 16](#_Toc233893612)

[4.5 Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro 18](#_Toc233893613)

[4.6 Criar dados mestre do produto – Planejamento do trabalho 22](#_Toc233893614)

[4.7 Criar dados mestre de produtos - Dados do depósito 23](#_Toc233893615)

[4.8 Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação 26](#_Toc233893616)

[4.9 Criar dados mestre do produto – Cálculo de custos 29](#_Toc233893617)

## Objetivo

O mestre de materiais ou de produtos contém informações referentes a todos os materiais físicos supridos, produzidos, armazenados e vendidos. É também utilizado para gerenciar informações sobre serviços, por exemplo, para compra e venda de serviços por hora.

O mestre de materiais contém informações como o número único de material, nome, tipo de material, unidade de medida, descrições, peso e dimensões. Estas informações de material são utilizadas e armazenadas em transações, como ordens do cliente, remessas, pedidos ou movimentos de mercadorias.

Visto que todas as informações de um material são armazenadas centralmente, as informações mestre do material são organizadas em diferentes visões. Por exemplo, vendas, armazenamento, MRP, cálculo de custos e contabilidade.

Algumas informações em cada material são específicas a determinadas unidades organizacionais. Por exemplo, uma descrição de vendas é específica a uma unidade de vendas (conhecida como área de vendas), um planejador MRP é específico a um certo local (conhecido como centro), ou algumas informações podem ser específicas de um depósito.

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
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Condições empresariais

Para que este script de dados mestre possa ser testado, é necessário cumprir a seguinte condição empresarial:

|  |
| --- |
| Nota O item de escopo 22T - Instalar modelo configurável usando configuração de variantes é um pré-requisito para esse script de dados mestre. |

### Unidades organizacionais necessárias

Alguns segmentos dos dados mestre do material são dependentes das unidades organizacionais da empresa, os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do material (texto breve), número do material, grupo de materiais, unidade de medida básica, etc. | Os dados básicos só existem uma vez para um registro de dados mestre de materiais. | não aplicável |
| Classificação | Independente de unidades organizacionais | Tipo de classe, Classe e Valores de classe | Existem dados de classificação para o tipo de classe para o qual os dados de classificação são utilizados. | não aplicável |
| Dados de vendas | Centro, organização de vendas, canal de distribuição | Dados de imposto, grupo de categorias do item, grupo transp., grupo de carregamento, tempo de preparação da expedição, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de materiais. | Centro:____________Organização de vendas:__________Canal de distribuição:__________ |
| Dados de compras | Centro | Unidade de medida básica, grupo de mercadorias | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de materiais. | Centro:____________ |
| Dados MRP/de planejamento (dados do centro) | Centro, depósito | Tipo de MRP, planejador MRP, tamanho do lote, prazo de entrega planejado, etc. | Podem existir dados do centro para cada ID do centro da sua estrutura da empresa no qual o registro mestre de materiais é usado.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Planejamento do trabalho | Centro | Supervisor de produção e Perfil do plano de produção | Os dados do centro podem existir para toda estrutura empresarial para a qual é usado o registro mestre de materiais. | Centro:_____________ |
| Dados do depósito | Centro, depósito | Número de notas de EM, período máximo de armazenamento, tempo mínimo restante validade, etc. |  | Centro:____________Depósito:__________ |
| Dados contábeis (dados de avaliação) | Área de avaliação (=centro), tipo de avaliação | Classe de avaliação, por preço unitário, controle do preço, etc. | Podem existir dados da área de avaliação para cada ID do centro da sua estrutura empresarial para o qual o registro mestre de materiais é utilizado. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes) | Centro:____________Tipo de avaliação:__________ |
| Cálculo de custos | Centro | Unidade de medida básica, Centro de lucro, Tamanho do lote para cálculo de custos, Classe de avaliação, Controle do preço e Unidade de preço. | Os dados da área de cálculo de custos podem existir para todo ID do centro de sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. | Centro:____________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Esta seção descreve alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais:

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais que 8 dígitos. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão fornece apenas um setor industrial M. Atualmente, isso é visível apenas no SAP GUI.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar dados mestre de produtos – Dados básicos](#unique_12) [página ] 8 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de produtos – Dados de vendas / dados do IVA](#unique_13) [página ] 11 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas (dados de IVA) criados. |
| [Criar dados mestre do produto – Dados de compras](#unique_14) [página ] 14 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de compra criados. |
| [Criar dados mestre do produto – Classificação](#unique_15) [página ] 16 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de material – Classificação criada. |
| [Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro](#unique_16) [página ] 18 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados MRP/de planejamento (dados do centro) criados. |
| [Criar dados mestre do produto – Planejamento do trabalho](#unique_17) [página ] 22 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de material – Planejamento do trabalho criado. |
| [Criar dados mestre de produtos - Dados do depósito](#unique_18) [página ] 23 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados do depósito criados. |
| [Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação](#unique_19) [página ] 26 | Especialista em dados mestre - Dados do produto | Criar material(MM01) ou Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados de avaliação) criados. |
| [Criar dados mestre do produto – Cálculo de custos](#unique_20) [página ] 29 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de material – Cálculo de custos criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar dados mestre de produtos – Dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A visão Selecionar visões é exibida. |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione Dados básicos 1, Dados básicos 2 e clique em Continuar. | A visão Criar material (materiais configuráveis) é exibida. |  |
| 5 | Inserir dados básicos | Na tela Criar material CM-FL-V01 (matérias configuráveis), na guia Dados básicos 1, insira a descrição do material (texto breve).Por exemplo: Empilhadeira |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básica: UNGrupo de mercadorias: L004GrpCtgsItemGer.: 0002 |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs, efetue as seguintes entradas:Peso bruto: 3Unidade de peso: KGPeso líquido: 2 | A guia Dados básicos 2 é exibida. |  |
| 8 | Inserir dados básicos | Na guia Dados básicos 2, você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material? |  |
| 9 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | A visão Criar material (tela inicial) é exibida.Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto. |  |
| 3 | Selecionar Criar novo mestre de produtos | Na visão Administrar dados mestre de produtos, clique em Criar. | Criar registro de dados mestre é exibido. |  |
| 4 | Inserir dados para campos obrigatórios | Na visão Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, CM-FL-V01 …nenhum ID alfanumérico externo … (pelo menos este deve começar com um caractere) ou sem entrada o sistema atribui um ID numérico automaticamentePara maiores informações sobre o Número do produto, veja a seção Tipo de material e intervalos de numeração em Parâmetros principais para a criação de dadosTipo de produto: KMATGrupo de produtos: por exemplo, L004Unidade básica: por exemplo, UNDescrição: Empilhadeira |  |  |
| 5 | Clicar em OK | Na visão Criar registro de dados mestre, clique em OK. | Visão do produto é exibida. |  |
| 6 | Inserir dados básicos | Na visão Produto > Informações gerais > Dados básicos, efetue as seguintes entradas:Setor de atividade: por exemplo, 00 |  |  |
| 7 | Selecionar descrições | Acessar Produto > Informações gerais > Descrições. | A visão Descrições é exibida. |  |
| 8 | Clicar em Adicionar (+) | Na visão Descrições, clique em + (adicionar). | Alguns campos já estão preenchidos. |  |
| 9 | Inserir dados de descrição | Na visão Descrições, efetue as seguintes entradas:Idioma: por exemplo, InglêsDescrição do produto: <sua descrição> |  |  |
| 10 | Selecionar unidade de medida básica | Acesse Produto > Informações gerais > Unidade de medida básica. |  |  |
| 11 | Inserir dados de unidade de medida básica | Na visão Peso, efetue as seguintes entradas:Unidade de peso: por exemplo, KGPeso bruto: por exemplo, 2Peso líquido: por exemplo, 1Nota Se os campos Peso bruto, Unidade de peso ou Peso líquido não forem exibidos como campos de entrada, clique em Ver mais no canto direito. |  |  |
| 12 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos – Dados de vendas / dados do IVA

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, conforme descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, se o seu acesso do usuário disponibilizar o app Criar material.

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: : CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: : KMAT – Materiais configuráveis | Uma nova janela exibe a visão Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione Vendas: Dados organizacionais de vendas 1, Vendas: dados organizacionais de vendas 2 e Vendas: dados gerais/do centro e clique em Continuar. | Uma nova janela exibe os Níveis organizacionais. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas e clique em Continuar:Centro: por exemplo, 1710Organização de vendas: por exemplo, 1710Canal distrib.: por exemplo, 10 | Uma nova janela exibe a visão Criar material (materiais configuráveis).Você recebe a seguinte mensagem de sistema na parte inferior da visão: o material já existe e será ampliado. |  |
| 6 | Inserir dados de vendas | Na visão Criar material CM-FL-V01 (materiais configuráveis), na guia Vendas: organização de vendas 1, insira um valor apropriado para <Classificação fiscal>Em geral, este valor é 1 para totalmente tributável. | A guia Vendas: organização de vendas 2 é exibida.O valor inserido indica que o material é (geralmente) totalmente tributável. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento, efetue a seguinte entrada:Grupo de categorias de item: 0002Grp.estatísticas mat. 1 | Você acessou a próxima guia, Vendas: geral/centro. |  |
| 8 | Inserir dados de vendas | Na guia Vendas: gerais/centro, na seção Dados gerais, insira os seguintes dados:Verificação de disponibilidade: por exemplo, EO |  |  |
| 9 | Inserir dados de vendas | Na seção Dados de expedição (prazos em dias), insira os seguintes dados:Grupo transp.: por exemplo, 0001Grp.carga: por exemplo, 0001 |  |  |
| 10 | Inserir dados de vendas | Na seção Parâmetros gerais de centro, insira os seguintes dados:Centro de lucro: por exemplo, YB110 ou YB111 | É exibida uma nova janela: Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 11 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a janela Dados mestre - produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Clicar em Editar | Clique em Editar.Nota Esta etapa parte do princípio de que você dá prosseguimento a partir da etapa anterior e de que já se encontra no mosaico Administrar dados mestre de produto. Depois de você ter salvo seus dados da seção anterior, o sistema está no Modo de exibição. Para continuar, você tem que estar no Modo de edição. | Modo de edição (os campos estão prontos para a sua entrada). |  |
| 4 | Selecionar as cadeias de distribuição | Na visão Produto, selecione Cadeias de distribuição. | A visão Cadeias de distribuição é exibida. |  |
| 5 | Clicar em Adicionar (+) | Na visão Cadeias de distribuição > Cadeias de distribuição, clique em + (adicionar) | A visão Mestre de produtos – cadeias de distribuição é aberta em Modo de edição. |  |
| 6 | Inserir dados de cadeias de distribuição | Na visão Mestre de produtos – Cadeias de distribuição, efetue as seguintes entradas:DADOS GERAIS – Informações geraisOrganização de vendas: <Nº org.vendas>, por exemplo, 1710Canal de distribuição: por exemplo, 10Centro fornecedor: <Nº do centro>, por exemplo, 1710CRITÉRIOS DE AGRUPAMENTOGrupo de categorias de item: por exemplo, 0002Grupo de classificações contábeis: por exemplo, 03 Produtos acabadosIVAPaís: <código do país>, por exemplo, DECategoria de imposto: TTX1Classificação fiscal: Inserir 1 para material ou 2 para serviçosClassificação fiscal: por exemplo, 1 Imposto total ao usar a condição de imposto UTXJ para US.A classificação fiscal depende de requisitos de país ou região específicos. A classificação fiscal no mestre de materiais e nas tabelas mestre de clientes determinam as entradas da porcentagem do imposto.Só para o Brasil na seção Classificação fiscal, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: Inserir 1 para material ou 2 para serviços |  |  |
| 7 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Dados de compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

|  |
| --- |
| Nota Se você deseja executar o material KMAT com processo de terceiros, amplie a visão de compras. |

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, se o seu acesso do usuário disponibilizar o app Criar material(MM01)Criar material (MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01) | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: : CM-FL-V01Setor industrial: MTipo de material: : KMAT – Materiais configuráveis | Uma nova janela exibe a visão Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na janela Seleção de visões, selecione Compras e, em seguida, Continuar. | Uma nova janela exibe os Níveis organizacionais |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas e clique em Continuar:Centro: por exemplo, 1010 | Uma nova janela exibe a visão Criar material (materiais configuráveis).Você recebe a seguinte mensagem de sistema na parte inferior da visão: o material já existe e será ampliado. |  |
| 6 | Inserir dados de compras | Certifique-se de que as entradas a seguir foram disponibilizadas.Unidade de medida básica: UNGrupo de mercadorias: L004 | A guia Compras é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | Os dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Clicar em Editar | Clique em Editar | Modo de edição (os campos estão prontos para a sua entrada). |  |
| 4 | Clicar em visão de compras | Na visão Mestre de produtos, clique emCompras | A visão Compras é exibida. |  |
| 5 | Inserir dados de compras | Na visão Compras, efetue a seguinte entrada e clique em Salvar.Unidade de medida do pedido: UN | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Classificação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, conforme descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | Uma nova janela exibe a visão Selecionar visão(ões). |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione Classificação e, em seguida, Continuar. | Uma nova janela exibe a visão Tipo de classe (1) |  |
| 5 | Inserir dados dos níveis organizacionais | Na seção Nível de restrição, selecione as seguintes entradas e, em seguida, Continuar:Descrição do tipo de classe: VariantesTipo: 300 | Uma nova janela exibe a visão Classificação. |  |
| 6 | Inserir dados de vendas | Na visão Classificação, em Atribuições, insira os seguintes valores na coluna Classe e clique em Salvar.AVC_CL_ELECADD_V01AVC_CL_REFCSTC_V01AVC_CL_COMMON_V01 | A janela da visão Classificação é exibida.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

|  |
| --- |
| Nota Os campos necessários não estão disponíveis atualmente para este aplicativo. Use a opção 1 (acima) |

### Criar dados mestre de produtos – Dados de planejamento MRP / dados do centro

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (1ª tela), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A visão Selecionar visões é exibida. |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione MRP1, MRP2, MRP3 e MRP4 e clique em Continuar. | A visão Níveis organizacionais é exibida. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Níveis organizacionais, efetue as seguintes entradas:Centro: <código do centro>, por exemplo, 1710Depósito: por exemplo, 171A | A visão Criar material (materiais configuráveis) é exibida.Você chama a seguinte mensagem de sistema na parte inferior da visão: O material já existe e será ampliado. |  |
| 6 | Inserir dados MRP/de planejamento | Na visão Material (materiais configuráveis), na guia MRP 1, na seção Dados gerais, efetue a seguinte entrada:Unidade de medida básica: UN |  |  |
| 7 | Inserir dados MRP/de planejamento | Na seção Procedimento MRP, efetue as entradas seguintes:Tipo de MRP: por exemplo, PDPlanejador MRP: por exemplo, 001 |  |  |
| 8 | Inserir dados MRP/de planejamento | Na seçãoRegra para cálculo do tamanho de lotes, efetue a seguinte entrada:Regra para cálculo do tamanho de lotes: EX | A guia seguinte MRP 2 é exibida. |  |
| 9 | Inserir dados MRP/de planejamento | Na visão Criar material CM-FL-V01 (material configurável), na guia MRP 2, efetue entradas com base em suas necessidades ou pelo menos preencha os campos obrigatórios com valores, por exemplo, tempo de fabricação própria em dias. | A guia seguinte MRP 3 é exibida. |  |
| 10 | Inserir dados MRP/de planejamento | Na visão Criar material (materiais configuráveis), na guia MRP 3, na seção Planejamento, efetue as seguintes entradas:Grupo de estratégias: por exemplo, 25Modo de consumo: por exemplo, 2 |  |  |
| 11 | Inserir dados MRP/de planejamento | Na seção Verificação de disponibilidade, efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EOTempo total reposição por exemplo, 3 | A guia seguinte MRP 4 é exibida. |  |
| 12 | Inserir dados MRP/de planejamento | Na visão Criar material CM-FL-V01 (material configurável), na guia MRP 4 você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 13 | Salvar | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a visão Dados mestre - Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Clicar em Editar | Clique em EditarNota Esta etapa parte do princípio de que você dá prosseguimento a partir da etapa anterior e de que já se encontra no mosaico Administrar dados mestre de produto. Depois de você ter salvo seus dados da seção anterior, o sistema está no Modo de exibição. Para continuar, você tem que estar no Modo de edição. | Modo de edição (os campos estão prontos para a sua entrada). |  |
| 4 | Selecionar dados de centros | Na visão Mestre de produtos, clique em Centros | A visão Centros é exibida. |  |
| 5 | Clicar em Adicionar (+) | Na seção da visão Centros, clique em + (Adicionar) | A visão Centros é aberta no modo de edição. |  |
| 6 | Inserir centros – Dados de informações gerais | Na visão Centro > Dados gerais, efetue as seguintes entradas:Centro: <Nº do centro>, por exemplo, 1710Centro de lucro: por exemplo, YB110 ou YB111Grp.carga: por exemplo, 0001 - Empilhadeira |  |  |
| 7 | Selecionar Centros – Dados MRP | Na visão Centro, clique em Dados MRP. | A visão Dados MRP é exibida. |  |
| 8 | Inserir centros – Dados MRP | Na visão Dados MRP, clique em Dados MRP e efetue as seguintes entradas:Verificação de disponibilidade: por exemplo, EOPrazo de entrega previsto: por exemplo, 3Tempo de processamento da entrada de mercadorias: por exemplo, 1Tipo de MRP: por exemplo, PDPlanejador MRP: por exemplo, 001 |  |  |
| 9 | Selecionar centros – Dados do tamanho do lote | Na visão Dados MRP, selecione Dados do tamanho do lote. | A seção da visão Dados do tamanho do lote é exibida. |  |
| 10 | Inserir Centros – Dados do tamanho do lote | Na visão Dados do tamanho do lote, efetue a seguinte entrada:Regra para cálculo do tamanho de lotes: por exemplo, EX |  |  |
| 11 | Selecionar Centros - Dados de previsão | Na visão Produto > CENTROS, selecione PREVISÃO. | PREVISÃO é exibida |  |
| 12 | Inserir centros - dados de previsão | Na visão PREVISÃO, efetue a seguinte entrada:Tipo de período: por exemplo, F |  |  |
| 13 | Retornar à visão principal | Selecione a seta para voltar para Mestre de produtos. | A visão Mestre de produtos é exibida. |  |
| 14 | Salvar os dados | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Planejamento do trabalho

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, conforme descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | A tela Criar material(MM01) é exibida. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A visão Selecionar visões é exibida. |  |
| 4 | Selecionar Visões | Na janela Selecionar visões, selecione Planejamento do trabalho e clique em Continuar. | A visão Níveis organizacionais é exibida. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, efetue a seguinte entrada e clique em Continuar:Centro: 1710 | É exibida uma nova janela Modificar material CM-FL-V01 (materiais configuráveis). |  |
| 6 | Inserir dados do planejamento do trabalho | Na janela Modificar material CM-FL-V01 (materiais configuráveis), em Dados gerais, insira as entradas a seguir e clique em Salvar.Unidade de medida básica: UNSupervisor de produção: YB3Perfil de plano de Perfil: YB0003 | É exibida uma nova janela: Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material? |  |
| 7 | Salvar os dados | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a janela Dados mestre - produto.Os dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

|  |
| --- |
| Nota Os campos necessários não estão disponíveis atualmente para este aplicativo. Use Opção 1 (acima) e salve suas entradas. |

### Criar dados mestre de produtos - Dados do depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A visão Selecionar visões é exibida. |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2 | É exibida a visão Níveis organizacionais. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: por exemplo, 1710Depósito: por exemplo, 171A | É aberta uma nova janela, mostrando a visão Criar material (materiais configuráveis).Você recebe a seguinte mensagem de sistema na parte inferior da visão: o material já existe e será ampliado. |  |
| 6 | Inserir dados do depósito | Na visão Criar material (materiais configuráveis), na guia Dds.cen./armazmto. 1, na seção Dados gerais, efetue a seguinte entrada:Número de notas de EM: por exemplo, 1 | A guia seguinte exibe os Dds.cen./armazmto.2. |  |
| 7 | Confirmar entradas | Na guia Dds.cen./armazmto 2, você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 8 | Salvar | Na janela Última visão de dados alcançada, selecione Sim. | É exibida a janela Dados mestre - produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Clicar em Editar | Clique em EditarNota Esta etapa parte do princípio de que você dá prosseguimento a partir da etapa anterior e de que já se encontra no mosaico Administrar dados mestre de produto. Depois de você ter salvo seus dados da seção anterior, o sistema está no Modo de exibição. Para continuar, você tem que estar no Modo de edição. | Modo de edição (os campos estão prontos para a sua entrada). |  |
| 4 | Selecionar dados de centros | Na visão Produto, selecione CENTROS.Nota Se não existir registro de dados do centro, siga as etapas na seção anterior Criar dados mestre do produto - dados de planejamento MRP/dados do centro | A visão CENTROS é exibida. |  |
| 5 | Selecionar detalhes do centro | Na visão CENTROS, utilize o ícone de seta para selecionar os dados de centro criados na etapa anterior. | A visão Centro do mestre de produtos é exibida. |  |
| 6 | Navegar para o centro: Depósito | Na visão Mestre de produtos – Centro, navegue para CENTROS > DEPÓSITOS. | A visão Mestre de produtos - CENTROS é aberta em modo de edição. |  |
| 7 | Clicar em Adicionar (+) | Em DEPÓSITOS > Depósitos, selecione + (Adicionar). | A visão Centro - Depósito é aberta no modo de edição. |  |
| 8 | Inserir centro: Dados do depósito | Na visão Depósitos, efetue as seguintes entradas:Depósito:<número do depósito>, por exemplo, 171A |  |  |
| 9 | Retornar à visão principal | Selecione duas vezes a seta para voltar para Mestre de produtos | Volte para a visão Mestre de produtos. |  |
| 10 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre de produtos - Dados contábeis / dados da área de avaliação

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com este procedimento.

Inicie o procedimento assim que salvar as entradas Dados básicos, tal como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A tela Selecionar visões é exibida. |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Contabilidade 1Contabilidade 2 | A visão Níveis organizacionais é exibida. |  |
| 5 | Inserir dados dos níveis organizacionais | Na visão Níveis organizacionais, na seção Nível organizacional, efetue as seguintes entradas:Centro: 1710 | A visão Criar material (materiais configuráveis) é exibida.A informação é exibida na parte inferior da visão: o material já existe e será ampliado. |  |
| 6 | Inserir dados contábeis | Na visão Criar material (materiais configuráveis), na guia Contabilidade 1, seção Dados de avaliação gerais, efetue a seguinte entrada:Classe de avaliação: 7920 |  |  |
| 7 | Inserir dados contábeis | Na seçãoPreços e valores, efetue as seguintes entradas:Preço padrão: 1Preço unid.perc.: 1Ctrl. prç.: S | Você navegou para a guia a seguir, Contabilidade 2. |  |
| 8 | Confirmar entradas | Na guia Contabilidade 2, você não precisa efetuar entradas. | É aberta uma nova janela Última visão de dados alcançada com a mensagem Você está prestes a sair. Deseja salvar primeiro seus dados para este material?. |  |
| 9 | Salvar os dados | Na janela Última visão de dados alcançada, clique em Sim. | É exibida a janela Dados mestre – Produto.Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). |  |  |
| 3 | Clicar em Editar | Clique em EditarNota Esta etapa parte do princípio de que você dá prosseguimento a partir da etapa anterior e de que já se encontra no mosaico Administrar dados mestre de produto. Depois de você ter salvo seus dados da seção anterior, o sistema está no Modo de exibição. Para continuar, você tem que estar no Modo de edição. | Modo de edição (os campos estão prontos para a sua entrada). |  |
| 4 | Selecionar dados da área de avaliação | Na visão Produto, selecione ÁREAS DE AVALIAÇÃO | A visão ÁREAS DE AVALIAÇÃO é exibida. |  |
| 5 | Clicar em Adicionar (+) | Na visão ÁREAS DE AVALIAÇÃO, selecione + (adicionar) | A visão ÁREAS DE AVALIAÇÃO é aberta no modo de edição. |  |
| 6 | Inserir dados da área de avaliação | Na visão ÁREAS DE AVALIAÇÃO > Área de avaliação, efetue as seguintes entradas:Área de avaliação: <número>, por exemplo, 1710Determinação do controle de preço:2Classe de avaliação: por exemplo, 7920 |  |  |
| 7 | Inserir dados da área de avaliação atual | Na visão Avaliação, selecione Período atual e efetue as seguintes entradas:Preço médio móvel: por exemplo, 20Controle de preço: por exemplo, S |  |  |
| 8 | Retornar à visão principal | Selecione a seta para voltar para Mestre de produtos | Volte para a visão Mestre de produtos. |  |
| 9 | Salvar | Clique em Salvar. | O sistema exibe uma notificação indicando que o objeto foi salvo. |  |

### Criar dados mestre do produto – Cálculo de custos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir apresenta instruções para criar dados mestre do produto. Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir a seção anterior, Criar dados mestre de produtos – Dados básicos, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas Dados básicos, conforme descrito no procedimento anterior.

Procedimento: opção 1 – Criar material

Use o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O Criar material(MM01) é exibido. |  |
| 3 | Inserir dados básicos de material | Em Criar material (visão inicial), efetue as seguintes entradas:Material: CM-FL-V01Setor industrial: MNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Se o setor industrial não for oferecido para entrada, o campo é preenchido com no escuro.Tipo de material: KMAT – Materiais configuráveis | A visão Selecionar visões é exibida. | O campo não estará disponível. |
| 4 | Selecionar Visões | Na janela Selecionar visões, selecione Cálculo de custos 1 e Cálculo de custos 2 e clique em Continuar. | A visão Tipo de classe (1) é exibida. |  |
| 5 | Inserir dados dos níveis organizacionais | Na seção Nível organizacional, selecione as seguintes entradas e clique em Continuar:Centro: 1710 | A visão Cálculo de custos 1 é exibida. |  |
| 6 | Inserir dados do cálculo de custos 1 | Na visão Cálculo de custos 1, selecione as entradas a seguir e, em seguida, na guia Cálculo de custos 2.Unidade de medida básica: UNCentro de lucro: YB110Tamanho do lote para cálculo de custos: 100 | A visão Cálculo de custos 2 é exibida.Os dados estão salvos. |  |
| 7 | Inserir dados do cálculo de custos 2 | Na visão Cálculo de custos 2, selecione as entradas a seguir e, em seguida, Continuar para salvar.Classe de avaliação: 7920Controle de preço: SPreço unitário: 1 | Os dados estão salvos. |  |

Procedimento: opção 2 – Administrar dados mestre de produto

|  |
| --- |
| Nota Os campos necessários não estão disponíveis atualmente para este aplicativo. Use Opção 1 (acima) e salve suas entradas. |

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
> Flagged while digesting this document, not verified: Extracted title was 'Objetivo' (first H1), real title is on the cover table

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test steps are examples (plant 1710, profit centers YB110/YB111) and may differ from customer configuration

## Connections
- part-of :: [[_cluster]]
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-configurable-material]]
- related-to :: [[02-business-partner-and-product-master-data/mds-2t7-285]]
- related-to :: [[02-business-partner-and-product-master-data/sap-s-4hana-cloud-public-edition-mds-2t7-283]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-creacion-de-maestro-de-productos-de-tipo-mate-3]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/2T7_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 56,541 chars in the whole document
