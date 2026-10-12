---
id: 10-procurement/criar-registro-info-para-compras-mds-bhd-566
title: Criar registro info para compras – MDS (BHD) (BHD_S4CLD2608_Master_Data_PT_XX)
description: "Script de dados mestre (PT) do SAP S/4HANA Cloud Public Edition 2608: testes para criar e modificar registros info para compras, incl. consignação, subcontratação, pipeline e massa."
cluster: 10-procurement
tags: [kb/procurement, topic/purchasing-info-records]
aliases: [BHD_S4CLD2608_Master_Data_PT_XX]
keywords: [Purchasing Info Records, consignment info records, subcontracting info records, pipeline info records, mass changes info records, mass price changes, numbering ranges, business roles, required master data, tax codes]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-566
topic: 10-procurement/purchasing-info-records
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar registro info para compras – MDS (BHD) (BHD_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Purchasing Info Records** in Procurement. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar registro info para compras – MDS (BHD) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893986)

[2 Pré-requisitos 3](#_Toc233893987)

[2.1 Acesso ao sistema 3](#_Toc233893988)

[2.2 Funções 3](#_Toc233893989)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893990)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893991)

[2.5 Parâmetros principais para a criação de dados 4](#_Toc233893992)

[2.5.1 Intervalos de numeração 4](#_Toc233893993)

[3 Tabela de síntese 5](#_Toc233893994)

[4 Procedimentos de teste 6](#_Toc233893995)

[4.1 Criar registro info para compras 6](#_Toc233893996)

[4.2 Criar registro info para compras para consignação 8](#_Toc233893997)

[4.3 Criar registro info para compras para subcontratação 10](#_Toc233893998)

[4.4 Criar registro info para compras em pipeline 12](#_Toc233893999)

[4.5 Modificações em massa do registro info para compras 15](#_Toc233894000)

[4.6 Modificações de preço em massa para registro info para compras 16](#_Toc233894001)

[5 Anexo 18](#_Toc233894002)

[5.1 Recursos relevantes 18](#_Toc233894003)

## Objetivo

Um registro info para compras contém informação específica a um material e o fornecedor do material.

Ele contém informações como o preço cobrado pelo fornecedor, a sua quantidade de ordem padrão e as tolerâncias para entrega excessiva e incompleta. É utilizado na transação do pedido.

A informação é específica a uma determinada unidade de compras (conhecida como organização de compras) e a um local específico (conhecido como um centro) dentro de sua organização.

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
| Comprador | SAP_BR_PURCHASER | Compras / Determinação da fonte de suprimento e contratação | SAP_MM_SPT_PURCHASING_PC / SAP_MM_SPT_SOURCING_PC |  |

### Unidades organizacionais necessárias

A estrutura organizacional e os dados mestre da sua empresa foram criados no seu sistema ERP durante a implementação. A estrutura organizacional reflete a estrutura da sua empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Dados de compras | Organização de compras | Grupo de compradores, grupo de materiais, tempo de processamento da EM, etc. | Os dados de compras podem existir para cada organização de compras, para a qual o material é utilizado em processos de compras. | Organização de compras:__________ |

### Dados mestre obrigatórios e opcionais

Os registros info para compras podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro info para compras.

| Objeto de dados mestre | Utilizado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Material |  | Obrigatório | Para inserir o material, crie primeiro os dados mestre de materiais. |
| Fornecedor |  | Obrigatório | Para inserir o fornecedor, crie primeiro os dados mestre de fornecedores. |

### Parâmetros principais para a criação de dados

Nesta seção é fornecida uma descrição para os parâmetros básicos que influenciam o comportamento de um registro info para compras e que são sempre necessários para a criação de um registro info para compras.

#### Intervalos de numeração

Os seguintes intervalos de numeração estão definidos para o registro info para compras:

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Numérico interno | Intervalo de numeração numérico interno para utilização padrão:5300000000 – 5399999999 | Este intervalo de numeração é utilizado quando o sistema atribui automaticamente um valor numérico a um material. |
| Numeração externa | Intervalo de numeração numérico externo (superior):5400000000 – 5499999999 | Este intervalo de numeração está reservado para uma atribuição externa de números de numeração. |

## Tabela de síntese

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Criar registro info para compras](#unique_10) [página ] 6 | Comprador | Administrar registros info para compras(F1982) | Os registros info para compras foram criados. |
| [Criar registro info para compras para consignação](#unique_11) [página ] 8 | Comprador | Administrar registros info para compras(F1982) | O registro info para compras de em consignação é criado. |
| [Criar registro info para compras para subcontratação](#unique_12) [página ] 10 | Comprador | Administrar registros info para compras(F1982) | O registro info para compras de subcontratação é criado. |
| [Criar registro info para compras em pipeline](#unique_13) [página ] 12 | Comprador | Administrar registros info para compras(F1982) | O registro info para compras para o pipeline é criado. |
| [Modificações em massa do registro info para compras](#unique_14) [página ] 15 | Comprador | Modificações em massa registros info p/compras(F2667) | As modificações em massa do registro info para compras são aplicadas. |
| [Modificações de preço em massa para registro info para compras](#unique_15) [página ] 16 | Comprador | Modificações de preços: Registros info. | As modificações em massa de preços do registro info para compras são aplicadas. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Criar registro info para compras

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info para compras(F1982). | A tela Administrar registros info para compras(F1982) é exibida. |  |
| 3 | Abrir Novo registro info para compras | Clique em Criar. | A tela Registro info para compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas:Categoria de registro info para compras: <padrão>Organização de compras: <organização de compras>Fornecedor: <fornecedor>Material: <Material>Centro: <centro>Grupo de compradores: <grupo de compradores> | Os dados do cabeçalho são adicionados. |  |
| 5 | Inserir informações gerais | Efetue as seguintes entradas:Disponível desde: DD/MM/AAAADisponível até: DD/MM/AAAA | Informações gerais são adicionadas. |  |
| 6 | Inserir dados de compras | Efetue as seguintes entradas:Incoterm: <Incoterm>Local incoterm 1: <Localização de Incoterm1> | Dados de compras são adicionados. |  |
| 7 | Inserir dados de remessa e quantidade | Efetue as seguintes entradas:Prazo de entrega em dias: <XX dias>Limite de tolerância para fornecimento incompleto em %: <XX>Limite de tolerância para fornecimento excessivo %: <XX>Código de imposto: <Código de imposto>Nota Quando o TDT (imposto dependente do tempo) é ativado por meio da Etapa de configuração 101016 (Definir códigos de imposto para vendas e compras) para o país da empresa e o código de imposto é indicado, o campo Início de validade da taxa de imposto é obrigatório. É possível inserir a data atual, que será ajustada à data de início de validade do código de imposto de acordo com a configuração na Etapa de Configuração.Quando o RITA (Registro para tributação indireta no exterior) é ativado, o país de identificação fiscal é atualizado para a empresa na Etapa de configuração 103464 (Ativar RITA e atualizar países de identificação fiscal) e o código de imposto é indicado, o campo País do imposto é obrigatório. Nele, o ID do país da empresa é indicado como valor proposto, mas é possível modificá-lo para o ID de país válido, que é atualizado na Etapa de configuração de modo correspondente.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Unidade de medida do pedido: <Unidade do pedido>Quantidade de pedido normal: <Quantidade padrão do pedido>Selecione as seguintes entradas, se necessário:Fornecimento ilimitadoRevisão de faturas baseada na entrada de mercadoriasNenhum faturamento automático de entrada de mercadoriasObrigatoriedade de confirmação da ordemControle de confirmação | Dados de remessa e quantidade são adicionados. |  |
| 8 | Inserir dados da condição | Na seção Condição, selecione o ícone Criar. Insira os seguintes dados:Válido desde: <data do início de validade>Montante: <Montante>Unidade de preço: <unidade de determinação do preço>Válido até: <fim da validade>Moeda: <Moeda>Clique em Aplicar. | Dados de condição são adicionados. |  |
| 9 | Inserir dados de referência (opcional) | Opcionalmente, você pode inserir dados de referência. | Os dados de referência são adicionados. |  |
| 10 | Salvar os dados | Clique em Criar. | Um registro info para compras é salvo. |  |

### Criar registro info para compras para consignação

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info para compras(F1982) | A tela Administrar registros info para compras é exibida. |  |
| 3 | Abrir Novo registro info para compras | Clique em Criar. | A tela Registro info para compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas:Categoria de registro info para compras:< Consignação>Organização de compras: <Organização de compras>Fornecedor: <fornecedor>Material: <material>Centro: <centro>Grupo de compradores: <grupo de compradores> | Os dados do cabeçalho são adicionados. |  |
| 5 | Inserir informações gerais | Efetue as seguintes entradas:Disponível desde: DD/MM/AAAADisponível até: DD/MM/AAAA | Informações gerais são adicionadas. |  |
| 6 | Inserir dados de compras | Efetue as seguintes entradas:Incoterm: <Incoterm>Local incoterm 1: <Localização de Incoterm1> | Dados de compras são adicionados. |  |
| 7 | Inserir dados de remessa e quantidade | Efetue as seguintes entradas:Prazo de entrega em dias: <XX dias>Abaixo da tolerância de remessa em %: <XX>Acima da tolerância de remessa em %: <XX>Código de imposto: <Código de imposto>Nota Quando o TDT (imposto dependente do tempo) é ativado via Etapa de configuração SSCUI 101016 (Definir códigos de imposto para vendas e compras) no país da empresa e o código de imposto é indicado, o campo Início de validade de taxa de imposto é obrigatório. É possível inserir a data atual, que será ajustada à data de início de validade do código de imposto de acordo com a configuração na Etapa de Configuração.Quando o RITA (Registro para tributação indireta no exterior) é ativado, o país de identificação fiscal é atualizado para a empresa na Etapa de configuração 103464 (Ativar RITA e atualizar países de identificação fiscal) e o código de imposto é indicado, o campo País do imposto é obrigatório. Nele, o ID do país da empresa é indicado como valor proposto, mas é possível modificá-lo para o ID de país válido, que é atualizado na Etapa de configuração de modo correspondente.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Unidade do pedido: <Unidade do pedido>Quantidade padrão do pedido: <Quantidade da ordem padrão> | Dados de remessa e quantidade são adicionados. |  |
| 8 | Inserir dados da condição | Na seção Condição, selecione o ícone Criar. Insira os seguintes dados:Início da validade: <Data do início de validade>Montante: <montante>Unidade de preço: <Unidade de determinação do preço>Fim da validade: <Fim da validade>Moeda:<Moeda>Clique em Aplicar. | Dados de condição são adicionados |  |
| 9 | Inserir dados de referência (opcional) | Opcionalmente, você pode inserir dados de referência. | Os dados de referência são adicionados. |  |
| 10 | Salvar os dados | Clique em Criar. | Um registro info para compras é salvo. |  |

### Criar registro info para compras para subcontratação

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info para compras(F1982). | A tela Administrar registros info para compras (F1982) é exibida. |  |
| 3 | Abrir Novo registro info para compras | Clique em Criar. | A tela Registro info para compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas:Categoria de registro info para compras:<Subcontratação>Organização de compras: <organização de compras>Fornecedor: <fornecedor>Material: <material>Centro: <centro>Grupo de compradores: <grupo de compradores> | Os dados do cabeçalho são adicionados. |  |
| 5 | Inserir informações gerais | Efetue as seguintes entradas:Disponível desde: DD/MM/AAAADisponível até: DD/MM/AAAA | Informações gerais são adicionadas. |  |
| 6 | Inserir dados de remessa e quantidade | Efetue as seguintes entradas:Prazo de entrega em dias: <XX dias>Abaixo da tolerância de remessa em %: <XX>Acima da tolerância de remessa em %: <XX>Código de imposto: <Código de imposto>Nota Quando o TDT (imposto dependente do tempo) é ativado por meio da Etapa de configuração 101016 (Definir códigos de imposto para vendas e compras) para o país da empresa e o código de imposto é indicado, o campo Início de validade da taxa de imposto é obrigatório. É possível inserir a data atual, que será ajustada à data de início de validade do código de imposto de acordo com a configuração na Etapa de Configuração.Quando o RITA (Registro para tributação indireta no exterior) é ativado, o país de identificação fiscal é atualizado para a empresa na Etapa de configuração 103464 (Ativar RITA e atualizar países de identificação fiscal) e o código de imposto é indicado, o campo País do imposto é obrigatório. Nele, o ID do país da empresa é indicado como valor proposto, mas é possível modificá-lo para o ID de país válido, que é atualizado na Etapa de configuração de modo correspondente.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Unidade do pedido: <Unidade do pedido>Quantidade padrão do pedido: <Quantidade padrão do pedido> | Dados de remessa e quantidade são adicionados. |  |
| 7 | Inserir dados da condição | Na seção Condição, selecione o ícone Criar. Insira os seguintes dados:Início da validade: <Data do início de validade>Montante: <montante>Unidade de preço: <Unidade de determinação do preço>Fim da validade: <Fim da validade>Moeda: <Moeda>Clique em Aplicar. | Dados de condição são adicionados. |  |
| 8 | Inserir dados de referência (opcional) | Opcionalmente, você pode inserir dados de referência. | Os dados de referência são adicionados. |  |
| 9 | Salvar os dados | Clique em Criar. | Um registro info para compras é salvo. |  |

### Criar registro info para compras em pipeline

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar registros info para compras(F1982). | O app é aberto. |  |
| 3 | Abrir Novo registro info para compras | Clique em Criar. | A tela Registro info para compras é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas:Categoria de registro info para compras: <Pipeline>Organização de compras: <Organização de compras>Fornecedor: <fornecedor>Material: <Material pipeline>Centro: <Centro>Grupo de compradores: <grupo de compradores>Grupo de mercadorias: <grupo de mercadorias> | Os dados do cabeçalho são adicionados. |  |
| 5 | Inserir informações gerais | Efetue as seguintes entradas:Disponível desde: DD/MM/AAAADisponível até: DD/MM/AAAA | Informações gerais são adicionadas. |  |
| 6 | Inserir dados de compras | Efetue as seguintes entradas:Incoterm: <Incoterm>Local incoterm 1: <Local incoterm 1> | Dados de compras são adicionados. |  |
| 7 | Inserir dados de remessa e quantidade | Efetue as seguintes entradas:Prazo de entrega em dias: <XX dias>Limite de tolerância para fornecimento incompleto em %: <XX>Limite de tolerância para fornecimento excessivo %: <XX>Código de imposto: <código de imposto>Nota Quando o TDT (imposto dependente do tempo) é ativado por meio da Etapa de configuração 101016 (Definir códigos de imposto para vendas e compras) para o país da empresa e o código de imposto é indicado, o campo Início de validade da taxa de imposto é obrigatório. É possível inserir a data atual, que será ajustada à data de início de validade do código de imposto de acordo com a configuração na Etapa de Configuração.Quando o RITA (Registro para tributação indireta no estrangeiro) é ativado, o país de notificação de imposto é atualizado para a empresa na Etapa de configuração 103464 (Ativar RITA e atualizar países de notificação de imposto) e o código de imposto é indicado, o campo País do imposto é obrigatório. Nele, o ID do país da empresa é indicado como valor proposto, mas é possível modificá-lo para o ID de país válido, que é atualizado na etapa de configuração de modo apropriado.Nota Dependendo do ambiente de configuração, as etapas de configuração podem ser acessadas em Configurar sua solução no Launchpad do SAP Fiori ou no app Business Processes Configuration na experiência em projetos do SAP Central Business Configuration.Unidade de medida do pedido: <Unidade de medida do pedido>Quantidade padrão do pedido: <Quantidade padrão do pedido>Selecione as seguintes entradas, se necessário:Fornecimento ilimitadoRevisão de faturas baseada na entrada de mercadoriasNenhum faturamento automático de entrada de mercadoriasObrigatoriedade de confirmação da ordemControle de confirmação | Dados de remessa e quantidade são adicionados. |  |
| 8 | Inserir dados da condição | Na seção Condições, selecione Criar. Insira os seguintes dados:Válido desde: <Data de início da validade>Montante: <Montante>Unidade de preço: <Unidade de determinação do preço>Válido até: <Data de fim da validade>Moeda: <moeda>Clique em Aplicar. | Dados de condição são adicionados. |  |
| 9 | Inserir dados de referência (opcional) | Opcionalmente, você pode inserir dados de referência. | Os dados de referência são adicionados. |  |
| 10 | Salvar os dados | Clique em Criar. | Um registro info para compras é salvo. |  |

### Modificações em massa do registro info para compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Neste procedimento, você aplica modificações a vários registros info para compras selecionados em massa.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Modificações em massa registros info p/compras(F2667). | O app é aberto. |  |
| 3 | Pesquisar por Registros info para compras | Para pesquisar por registros info para compras, insira os seguintes valores para os filtros:Fornecedor: <ID do fornecedor>Grupo de compradores: por exemplo, 001Centro: <ID do centro>Clique em Ir. | Os resultados da pesquisa exibem os detalhes dos respectivos critérios de filtragem.Por padrão, todos os registros info para compras são selecionados para a operação de modificação em massa. |  |
| 4 | Selecionar Registros info para compras | Marque a caixa de seleção Registros info para compras na guia Registro info para compras e organização de compras.Clique em Edição em massa. |  |  |
| 5 | Definir novos valores | Insira novos valores nas seguintes entradas:Na seção Dados gerais:Nº material forn.Grupo mercs forn.Na seção Dados da organização de compras:Grupo de compradoresQuantidade mínima da ordemClique em Aplicar modificações em massa.É exibida uma caixa de diálogo para confirmar modificações em massa.Na tela Aplicar modificações em massa , clique em Aplicar.É exibida uma caixa de diálogo com o ID job.Clique em Exibir lista de jobs. | Novos valores são aplicados aos registros info para compras selecionados. |  |
| 6 | Verificar jobs de aplicação | Insira os critérios de pesquisa e clique em Ir.A página Jobs de aplicação é exibida, contendo a lista dos IDs de job para todos os registros info de compras.Clique emLog para verificar o sucesso dos registros info de compras selecionados. |  |  |

### Modificações de preço em massa para registro info para compras

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Neste procedimento, o app Modificação de preço- registros info(MEKP) é usado para a atualização em massa de preços para registros info.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Comprador. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Modificação de preço- registros info(MEKP). | O app é aberto. |  |
| 3 | Inserir dados iniciais | Efetue as seguintes entradas e clique em Executar:Organização de compras: <ID da organização de compras>Fornecedor: <ID do fornecedor>Material: <ID do Material>Registros info sem material: <em branco>Execução de teste: <em branco>Vá para a seção Modificar tipo de condição ou preço bruto e efetue as seguintes entradas:Tipo de condição: <ID do tipo de condição>, por exemplo, PPR0Montante fixo: <montante fixo>, por exemplo, 10Sinal: <Sinal>, por exemplo, +Preço bruto: <em branco>Linhas da escala: <X>Vá para a seção Condições válida e efetue as seguintes entradas:Em: <data atual>Ou De<em branco>Até <em branco> | Novos valores são atualizados para os registros info para compras. |  |
| 4 | Verificar alterções de registros info para compras | Na tela modificação de preço para registros info do fornecedor <XXXX> verifique os registros Antigo e Novo e confirme as alterações. | A modificação de preço dos registros info para compras são salvas. |  |
| 5 | Finalizar | Clique em Encerrar. |  |  |

## Anexo

### Recursos relevantes

Aqui estão listadas algumas funcionalidades de aplicação importantes relacionadas a registros info para compras que não estão cobertas nos procedimentos de teste acima.

| Área funcional | Função | Informações detalhadas | Comentário |
| --- | --- | --- | --- |
| Registros info para compras | Apps relacionados a registros info | WebGUI: Excluir registros info para compras (ME15)WebGUI: Exibir registros info para compras por fornecedor (ME1L)WebGUI: Atualizar modificações de registros info para compras (ME14)WebGUI: Atualizar condições de compra (MEKA)WebGUI: Atualizar perfil de arredondamento (OWD1) |  |

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
- related-to :: [[10-procurement/create-purchasing-info-record-mds-bhd-master-data-script-563]]
- related-to :: [[10-procurement/einkaufsinfosatz-anlegen-sds-bhd-stammdatenskript-562]]
- related-to :: [[10-procurement/mds-bhd-565]]
- related-to :: [[10-procurement/mds-bhd-567]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BHD_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 30,266 chars in the whole document
