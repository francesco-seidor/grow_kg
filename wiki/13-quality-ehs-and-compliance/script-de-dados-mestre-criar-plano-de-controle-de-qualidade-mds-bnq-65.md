---
id: 13-quality-ehs-and-compliance/script-de-dados-mestre-criar-plano-de-controle-de-qualidade-mds-bnq-65
title: Script de dados mestre - Criar plano de controle de qualidade - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (BNQ): prerequisites and step-by-step Fiori test procedures to create quality inspection plans."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/inspection-plans]
aliases: [BNQ_S4CLD2608_Master_Data_PT_XX]
keywords: [Quality Inspection Plans, inspection plans, inspection plan management, code groups and selected sets, master inspection characteristics, sampling plans, copy inspection plans, defect code groups, inspection methods, class characteristics]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_PT_XX.docx]
confidence: low
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-656
topic: 13-quality-ehs-and-compliance/inspection-plans
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar plano de controle de qualidade - MDS (BNQ) (BNQ_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Quality Inspection Plans** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar plano de controle de qualidade – MDS (BNQ) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 3](#_Toc233894105)

[2 Pré-requisitos 4](#_Toc233894106)

[2.1 Acesso ao sistema 4](#_Toc233894107)

[2.2 Funções 4](#_Toc233894108)

[2.3 Unidades organizacionais necessárias 4](#_Toc233894109)

[2.4 Dados mestre obrigatórios e opcionais 5](#_Toc233894110)

[2.5 Condições empresariais 6](#_Toc233894111)

[2.6 Parâmetros principais para a criação de dados 6](#_Toc233894112)

[2.6.1 Intervalos de numeração 6](#_Toc233894113)

[3 Tabela de síntese 7](#_Toc233894114)

[4 Procedimentos de teste 8](#_Toc233894115)

[4.1 Atributos de característica – Editar grupos de códigos para conjuntos selecionados 8](#_Toc233894116)

[4.2 Editar conjuntos selecionados para atributos de característica 9](#_Toc233894117)

[4.3 Editar grupos de códigos para defeitos (opcional) 10](#_Toc233894118)

[4.4 Criar método de controle (opcional) 11](#_Toc233894119)

[4.5 Criar características mestre de controle (opcional) 13](#_Toc233894120)

[4.6 Criar característica mestre de controle com referência à característica de classe (opcional) 17](#_Toc233894121)

[4.7 Criar plano de amostragem (opcional) 18](#_Toc233894122)

[4.8 Criar processo de amostragem (opcional) 22](#_Toc233894123)

[4.9 Criar Regra de controle dinâmico (opcional) 23](#_Toc233894124)

[4.10 Criar plano de controle 25](#_Toc233894125)

[4.11 Administrar planos de controle 27](#_Toc233894126)

[4.12 Copiar de planos de controle existentes 31](#_Toc233894127)

[4.13 Exibir lotes de controle em aberto 33](#_Toc233894128)

## Objetivo

Caso a qualidade do material deva ser controlada, um os pré-requisitos é que um plano de controle esteja disponível. Por exemplo, talvez seja necessário efetuar um controle durante o processo de entrada de mercadorias do fornecedor ou da ordem de produção. O plano de controle deve conter alguns detalhes sobre as características a serem inspecionadas, como devem ser controladas e, por exemplo, quantas amostras devem ser verificadas.

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
| Planejador da qualidade | SAP_BR_QUALITY_PLANNER | Planejamento de qualidade | SAP_BR_QUALITY_PLANNER |  |
| Técnico de qualidade | SAP_BR_QUALITY_TECHNICIAN | Controle de qualidade | SAP_BR_QUALITY_TECHNICIAN |  |

### Unidades organizacionais necessárias

Alguns segmentos de dados mestre são dependentes das unidades organizacionais do centro. A tabela abaixo oferece uma síntese destes diferentes segmentos de dados e de suas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser utilizada |
| --- | --- | --- | --- | --- |
| Conjuntos selecionados para atributos de característica - Processar conjuntos selecionados | Centro | Conjunto selecionado, etc. | Os conjuntos selecionados combinam diferentes grupos de códigos e códigos no nível do centro, que são úteis para certas aplicações | Centro: |
| Criar método de controle | Centro | Método de controle | O método de controle pode ser utilizado em um plano de controle |  |
| Criar características do plano de controle | Centro | Características mestre de controle, atribuição do conjunto selecionado, etc. | As características mestre de controle podem ser utilizadas em um plano de controle. | Centro: |
| Criar plano de controle | Centro | Atribuição a um número de material, utilização, status, centro de trabalho, etc. | Os dados do centro estão atribuídos a todos os IDs de centro de sua estrutura empresarial para um plano de controle | Centro: |

### Dados mestre obrigatórios e opcionais

A tabela seguinte oferece uma síntese de objetos de dados mestre opcionais e obrigatórios a serem usados em um registro de dados do plano de controle de qualidade.

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Grupo de códigos/Conjunto selecionado – para Atributo de característica |  | Obrigatório | Grupo de códigos/Conjunto selecionado para atributo de característica deve ser criado antes de você criar um plano de controle. |
| Grupo de códigos – para defeitos |  | Opcional | Grupo de códigos – para defeitos deve ser criado antes de você criar um plano de controle. |
| Métodos de controle |  | Opcional | Os métodos de controle podem ser criados antes de você criar um plano de controle. |
| Características mestre de controle |  | Opcional | As características mestre de controle devem ser criadas antes de você criar um plano de controle. |
| Plano de amostragem |  | Opcional | O plano de amostragem define um conjunto de instruções da amostra que pode ser criado antes de você criar um plano de controle. |
| Processo de amostragem |  | Opcional | O processo de amostragem define regras que especificam o modo como o sistema calcula o tamanho da amostra e o processo pode ser criado antes de você criar um plano de controle. |
| Regra de controle dinâmico |  | Opcional | A regra de controle dinâmico contém a definição das etapas de controle e a condição para o controle da etapa de controle. Uma regra de controle dinâmico pode ser criada antes de você criar um plano de controle. |

### Condições empresariais

Antes que este item de escopo possa ser testado, cumpra as seguintes condições empresariais.

| Item do escopo | Condição empresarial |
| --- | --- |
| BNY - Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS | O mestre de materiais deve ser criado antes da criação de um plano de controle. |
| 2ZW - Criar dados mestre de administração de lotes – MDS (opcional) | Se os resultados de controle deverem ser transferidos para a classe de lote quando a decisão de utilização for tomada, assegure que estejam preenchidos os pré-requisitos a seguir. Além disso, considere que uma característica de classe tem de ser atribuída a uma característica mestre de controle (ver a seção deste documento):A característica da classe deve existir.A classe do lote (tipo 023) deve existir.A característica de classe tem de ser atribuída ao tipo de classe 023.O material tem de ser processado em lotes e a classe de lote foi atribuída ao mestre de materiais na visão de classificação.Nota Se a decisão de utilização e o respectivo índice de qualidade deverem ser transferidos para a classificação de lotes, as características de classe LOBM_UDCODE e LOBM_QSCORE, respectivamente, devem ser atribuídas à classe de lote. Observe que não é necessário ligar estas características a uma característica mestre de controle neste caso. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para se criar um plano de controle.

#### Intervalos de numeração

Os intervalos de numeração a seguir são definidos para planos de controle e para funcionalidade dependente, relacionada:

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Numeração externa | 50000000 a 59999999 | Este intervalo destina-se ao plano de controle. |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Atributos de característica – Editar grupos de códigos para conjuntos selecionados](#unique_11) [página ] 8 | Planejador da qualidade | Processar grupos de códigos(QS41) | Códigos e grupos de códigos de atributos de característica são criados |
| [Editar conjuntos selecionados para atributos de característica](#unique_12) [página ] 9 | Planejador da qualidade | Processar conjuntos selecionados(QS51) | O conjunto selecionado para atributos de característica é criado. |
| [Editar grupos de códigos para defeitos (opcional)](#unique_13) [página ] 10 | Planejador da qualidade | Processar grupos de códigos(QS41) | Os grupos de códigos são criados. |
| [Criar método de controle (opcional)](#unique_14) [página ] 11 | Planejador da qualidade | Criar método de controle(QS31) | O método de controle é criado. |
| [Criar características mestre de controle (opcional)](#unique_15) [página ] 13 | Planejador da qualidade | Criar característica mestre de controle(QS21) | As características mestre de controle são criadas. |
| [Criar característica mestre de controle com referência à característica de classe (opcional)](#unique_16) [página ] 17 | Planejador da qualidade | Criar característica mestre de controle(QS21) | A característica mestre de controle quantitativa com referência à característica de classe é criada. |
| [Criar plano de amostragem (opcional)](#unique_17) [página ] 18 | Planejador da qualidade | Criar plano de amostragem(QDP1) | O plano de amostragem é criado. |
| [Criar processo de amostragem (opcional)](#unique_18) [página ] 22 | Planejador da qualidade | Criar processo de amostragem(QDV1) | O Procedimento de amostra é criado. |
| [Criar Regra de controle dinâmico (opcional)](#unique_19) [página ] 23 | Planejador da qualidade | Criar regra de controle dinâmico(QDR1) | A regra de controle dinâmico é criada. |
| [Criar plano de controle](#unique_20) [página ] 25 | Planejador da qualidade | Criar plano de controle(QP01) | O plano de controle é criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Atributos de característica – Editar grupos de códigos para conjuntos selecionados

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Atributos da característica refere-se a um catálogo padrão de administração de qualidade (QM) que define estados possíveis de atributos controlados. Os códigos são agrupados em códigos de grupos, de forma a definir uma estrutura hierárquica.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Processar grupos de códigos(QS41). | Editar catálogo: 1ª tela é exibida. |  |
| 3 | Inserir catálogo | Em Editar catálogo: 1ª tela, efetue as seguintes entradas:Catálogo: por exemplo, 1Grupo de códigos: *Selecione Continuar. | A visão Modificar visão "Atualizar grupos de códigos": tela de síntese é exibida. |  |
| 4 | Atualizar grupos de códigos | Selecione um grupo de códigos, por exemplo SUPERFÍCIE e clique duas vezes em Códigos na estrutura de diálogo. | É exibido Modificar visão “Grupo de códigos": tela de síntese é exibida. |  |
| 5 | Criar códigos | Na visão Modificar síntese da visão “Códigos”, selecione Novas entradas e efetue as seguintes entradas:código: por exemplo, 0010, 0020, etc.Texto breve para código: <Insira sua descrição> |  |  |
| 6 | Salvar os dados | Clique em Salvar. | Os dados são salvos. |  |

### Editar conjuntos selecionados para atributos de característica

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Os conjuntos selecionados combinam diferentes grupos de códigos e códigos no nível do centro. Estes conjuntos selecionados são úteis para determinados cenários, como a caracterização de possíveis resultados da análise para um certo atributo de produto (por exemplo, propriedades da superfície).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Processar conjuntos selecionados(QS51). | O app é aberto. |  |
| 3 | Inserir catálogo/centro/conjunto selecionado | Em Editar conjunto selecionado: 1ª tela, efetue as seguintes entradas:Catálogo: 1Centro: <código do centro>Conjunto selecionado: *Pressione Enter. | A tela Modificar visão "Conjuntos selecionados": síntese é exibida. |  |
| 4 | Atualizar conjuntos selecionados | Selecione um Conjunto selecionado, por exemplo SMOOTH e clique duas vezes em Códigos de conjunto selecionado na Estrutura de diálogo. | A visão Modificar visão "Códigos de conjunto selecionado": síntese é exibida. |  |
| 5 | Criar códigos de conjunto selecionado | Na tela Modificar visão "Códigos de conjunto selecionado": Síntese, selecione Entradas novas e efetue as seguintes entradas:Grupo de códigos: <valor do grupo de códigos>código: <valor do código>Código de avaliação: ou Aceito (OK) ou Rejeitado (não OK)Classe de defeitos: Defeito principal |  |  |
| 6 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

### Editar grupos de códigos para defeitos (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Use grupos de códigos para categorizar ou classificar possíveis defeitos de qualidade.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Processar grupos de códigos(QS41). | Editar catálogo: visão inicial será exibido. |  |
| 3 | Inserir dados iniciais | Efetue as seguintes entradas:Catálogo: por exemplo, 9Grupo de códigos, porr exemplo, DEF-SURFSelecione Continuar. | A visão Modificar visão "Atualizar grupos de códigos": síntese é exibida. |  |
| 4 | Atualizar grupos de códigos | Na área de Atualizar grupos de códigos, efetue as seguintes entradas:Texto breve: por exemplo, Defeitos de superfície | Assegure-se de que o Status do grupo de códigos seja Liberado. |  |
| 5 | Atualizar códigos de grupos de códigos | Na área Atualizar grupos de códigos, selecione um item que você tenha criado.Navegue para Códigos na área Estrutura de diálogo e clique duas vezes em "Códigos". | Modificar visão "Códigos": síntese é exibida. |  |
| 6 | Atualizar códigos de grupos de códigos | Na visão de Modificar visão "Códigos": síntese, selecione Novas entradas.Efetue as seguintes entradas:Código: por exemplo, 0010Texto breve para código: por exemplo, Problema de superfícieClasse de defeitos: por exemplo, Defeito principalPara salvar os seus dados, clique em Salvar. | Os grupos de códigos são atualizados. |  |

### Criar método de controle (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar método de controle

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | SelecioneCriar método de controle(QS31). | Criar método de controle: 1ª tela é exibida. |  |
| 3 | Inserir dados iniciais | Efetue as seguintes entradas:Centro: <Código do centro>Método Método: por exemplo, SUPERFÍCIEInício da validade: Por exemplo, <data atual>Selecione Método de controle. | Criar método de controle: dados gerais é exibida. |  |
| 4 | Inserir dados gerais | Efetue as seguintes entradas:Status: LiberadoTexto breve: por exemplo, SuperfícieCampo de pesquisa: por exemplo, Superfície |  |  |
| 5 | Inserir texto descritivo | Selecione Criar texto descritivo ao lado do campo Texto breve e insira o texto descritivo, por exemplo:Favor controlar a superfície cuidadosamente, especialmente quanto à aspereza, e se há riscos ou arranhões.Selecione Voltar. |  |  |
| 6 | Salvar dados | Para salvar os seus dados, clique em Salvar |  |  |
| 7 | Acessar o app SAP Fiori | Selecione Modificar método de controle. | Modificar versão do método de controle: 1ª tela é exibido |  |
| 8 | Inserir dados iniciais | Efetue as seguintes entradas:Centro: <Código do centro>Método Método: por exemplo, SUPERFÍCIESelecione Método de controle. | A visão Modificar versão do método de controle: dados gerais é exibida. |  |
| 9 | Selecionar um documento a ser anexado | Selecione Documentos de Informações gerais |  |  |
| 10 | Criar anexo para documento | Selecione Criar documento.Na caixa de diálogo Modificar versão do método de controle: dados gerais, selecione Continuar/Enter sem inserir dados.Confirme a mensagem de upload do arquivo clicando em OK e selecione um arquivo do seu sistema de arquivos com um clique duplo.Selecione Transferir para navegar de volta à tela Modificar versão de método de controle: dados gerais. |  |  |
| 11 | Salvar dados | Para salvar os seus dados, clique em Salvar. |  |  |

### Criar características mestre de controle (opcional)

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar característica mestre de controle(QS21). | Criar características mestre de controle: visão inicial é exibida. |  |
| 3 | Inserir dados do centro | Em Criar característica mestre de controle: Visão inicial, efetue as seguintes entradas:Centro: <Código do centro>Caract.mestre ctrl.: <valor>, por exemplo, YQUALI01Início da validade: <data atual>Selecione Característica mestre de controle | A visão Criar características mestre de controle: dados gerais é exibida. |  |
| 4 | Inserir dados gerais para característica qualitativa | Em Criar característica mestre de controle: dados gerais, efetue as seguintes entradas:Caract.qualitativa: marcadoTexto breve: por exemplo, SuperfícieCampo de pesquisa: por exemplo, SuperfícieStatus: Selecione Liberado e Característica de referênciaPressione Enter. | É exibida uma nova janela, Editar código de controle de característica.Característica de referênciaSe você usar a característica mestre de controle em um plano de controle, uma referência é primeiramente criada para esta característica. Porém, você pode cancelar esta referência e modificar os dados individualmente, por exemplo, tolerâncias. Configurações opcionais são fornecidas nas etapas seguintes.Modelo de cópia completoSe você usar a característica mestre de controle em um plano de controle, a referência para esta característica é cancelada. Você pode modificar imediatamente os dados, por exemplo, tolerâncias. Somente depois você poderá usar esta característica mestre de controle como modelo de cópia.Modelo de cópia incompletoSe você usar a característica mestre de controle em um plano de controle, ela só poderá ser usada em um modelo de cópia. Este tipo de característica mestre de controle não pode ser usado em uma especificação do material. |  |
| 5 | Editar códigos de controle para características qualitativas | Na visão Editar códigos de controle de característica, marque as seguintes opções:Atributo caract.Processo de amostragemRegistro compact.Caract.necessáriaSelecione Continuar para marcar outras opçõesEscopo fixoNenhuma documentaçãoSelecione Continuar para sair da edição. | A visão Editar códigos de controle de característica é exibida. |  |
| 6 | Atribuir catálogos de controle | A partir da caixa de diálogo Catálogo de controle atribuído, selecione um valor para o campo GrC/CjtoSel., por exemplo, MACIO.Selecione Continuar. | Retorne à visão Criar característica mestre de controle: dados gerais.Nota O centro é automaticamente atualizado ao selecionar Macio nas entradas possíveis. |  |
| 7 | Método de controle atribuído (opcional) | Selecione Métodos de controle e a visão Métodos de controle atribuídos é exibida.Efetue as seguintes entradas:Método: SuperfícieCentro: <Código do centro>Selecione Continuar. | Retorne à visão Criar característica mestre de controle: dados gerais. |  |
| 8 | Salvar os dados | Clique em Salvar | Os dados são salvos |  |
| 9 | Criar característica mestre de controle quantitativa | No launchpad do SAP Fiori, abra a visão Criar característica mestre de controle: dados iniciais e efetue as seguintes entradas:Centro: <Código do centro>Caract.mestre ctrl.: por exemplo, YQUANT01Início da validade: <data atual>e selecione Característica mestre de controle | A visão Criar característica mestre de controle: dados gerais é exibida. |  |
| 10 | Inserir dados gerais para característica quantitativa | Em Criar características mestre de controle: dados gerais, efetue as seguintes entradas:Caract.quantitativa: marcadoTexto breve: por exemplo, comprimentoCampo de pesquisa: por exemplo, comprimentoStatus: 2 LiberadoSelecione Liberado e Característica de referênciaPressione Enter | A janela Editar códigos de controle de característica é exibida.Características de referênciaSe você usar a característica mestre de controle em uma lista de tarefas ou especificação do material, uma referência é primeiramente criada para esta característica. Porém, você pode cancelar esta referência e modificar os dados individualmente, por exemplo, para tolerâncias.Modelo de cópia completoSe você usar a característica mestre de controle em uma lista de tarefas, ela só poderá ser usada em um modelo de cópia. Este tipo de característica mestre de controle não pode ser usado em uma especificação do material.Modelo de cópia incompletoSe você usar a característica mestre de controle em uma lista de tarefas, ela só poderá ser usada em um modelo de cópia. Este tipo de característica mestre de controle não pode ser usado em uma especificação do material. |  |
| 11 | Editar códigos de controle para características quantitativas | Em Editar códigos de controle de característica, marque as seguintes opções:Limite espec.inferiorLimite espec.superiorProcesso de amostragemRegistro compact.Caract.necessáriaSelecione Continua e marque as seguintes opções adicionais:Escopo fixoNenhuma documentaçãoReg.valores medidosDocs.modificação RRSelecione Avançar. |  |  |
| 12 | Inserir valor fixado | Na visão Chaves de tolerância, efetue a seguinte entrada:Valor fixado: por exemplo, 150e selecione Continuar |  |  |
| 13 | Inserir dados quantitativos | Na visão Dados quantitativos, efetue as seguintes entradas:Casas decimais: por exemplo, 2UM: por exemplo, cmLimite inferior: por exemplo, 100Limite superior: por exemplo, 200Selecione Avançar. |  |  |
| 14 | Salvar os dados | Clique em Salvar. | Os dados são salvos. |  |
| 15 | Ativar registro de defeitos para uma característica mestre de controle existente (opcional) | Abra o app Modificar característica mestre de controle(QS23) e, em seguida, a característica mestre de controle que você quer modificar.Selecione Códigos de controle.Na caixa de diálogo Editar códigos de controle de característica, ative a opção Registro de defeitos na seção Confirmação de resultados e selecione Continuar.Selecione novamente Continuar. |  |  |
| 16 | Atribuir catálogos de controle (opcional) | Em Informações gerais, selecione o botão Catálogos. | A caixa de diálogo Catálogos de controle atribuídos aparece. |  |
| 17 | Atualizar códigos de defeito para rejeição (opcional) | Nos Códigos de defeito para rejeição da caixa de diálogo Catálogos de controle atribuídos, procure e insira o grupo de códigos/código para violação dos limites geral, superior e inferior de violação de limite, respectivamente.Selecione Continuar. |  |  |
| 18 | Salvar os dados | Clique em Salvar. | Os dados são salvos |  |

### Criar característica mestre de controle com referência à característica de classe (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

A ligação entre as características mestre de controle e as características da classe permite a transferência automática dos resultados de controle para a classificação de lotes, desde que você execute um controle com uma lista de tarefas. As características da classe do lote são automaticamente avaliadas no encerramento do controle, na base dos resultados de controle.

Se você inserir uma característica de classe e ligá-la a uma característica mestre de controle, certos códigos de controle e valores desta característica de classe são transferidos para a característica mestre de controle.

A ligação entre as características mestre de controle e as características de classe permite que você transfira resultados de um controle de qualidade para a classificação de lotes.

|  |
| --- |
| Nota Você só pode ter uma relação de 1:1 entre uma característica de classe e uma característica mestre de controle (ou seja, você não pode referenciar a mesma característica de classe em várias características mestre de controle). A classe de característica é definida no nível do mandante e a característica mestre de controle é definida no nível de centro. Por isso, se você quiser usar avaliação do lote para vários centros, é obrigatório definir características de classe específicas do centro e ligá-las à respectiva característica mestre de controle no nível de centro. |

Pré-requisitos

Os pré-requisitos devem ser atendidos para a ligação de característica mestre de controle à característica de classe. Consulte o capítulo Condições empresariais sobre 2ZW.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Comentários de resultado esperados | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar característica mestre de controle(QS21). | A visão Criar característica mestre de controle: 1ª tela é exibida. |  |
| 3 | Inserir dados do centro | Na tela Criar característica mestre de controle: Inicial, efetue as seguintes entradas:Centro: Código do centroCaract.mestre ctrl.: <valor>Início da validade: <data atual>Característica de classe: valorSelecione Característica mestre de controle. | A visão Criar característica mestre de controle: dados gerais é exibida. |  |
| 4 | Executar etapas 10-14 no capítulo anterior | Nota A característica mestre de controle tem de ser uma característica de referência.Alguns dados são copiados da característica da classe para a característica mestre de controle. Além disso, dependendo das configurações da característica de classe, alguns códigos de controle da característica mestre de controle não pode ser modificados. | A característica mestre de controle quantitativa com referência à característica de classe é criada. |  |
| 5 | Verificar características do lote após controle de qualidade (opcional) | Criar lote de controle manualmente ou através de movimento de mercadorias, executar controle de qualidade e tomar decisão de utilização.Para revisar características do lote, efetue login no launchpad do SAP Fiori como Técnico de qualidade e acesse o app SAP Fiori Administrar lotes(F2462) ou Batch Information Cockpit(BMBC), e verifique as características em Classificação. | Os dados do controle de qualidade foram transferidos para a característica do lote. |  |

### Criar plano de amostragem (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Você pode criar, opcionalmente, um plano de amostragem. Um plano de amostragem é um conjunto de instruções de amostra. Um plano de amostragem define a quantidade de amostras a serem controladas (tamanho da amostra) como uma função do tamanho do lote. Também podem ser definidos critérios para aceitar ou rejeitar uma amostra (por exemplo, com base no grau de controle atual). O grau de controle define se um controle normal, reduzido ou intensificado é executado, de forma que um planejador da qualidade possa adaptar flexivelmente os recursos de controle à situação de qualidade atual (por exemplo, menos controles, tamanho menor da amostra ou critérios mais altos de aceitação, se a situação de qualidade atual for boa).

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Criar plano de amostragem(QDP1). | A caixa de diálogo Criar plano de amostragem: visão inicial é exibida. |  |
| 3 | Inserir nome do plano de amostragem da amostra | Insira um nome do plano de amostragem da amostra.Plano de amostragem: por exemplo, QM2Selecione Continuar. | A caixa de diálogo Criar plano de amostragem: dados de cabeçalho é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as entradas seguintes ou selecionadas:Plano de amostragem: por exemplo, Plano de amostragem para gravidades (atributo)Parâmetros de avaliação: por exemplo, Controle de atributosTabela de amostras para: por exemplo, Grau de controle.Selecione Continuar. | A caixa de diálogo Criar plano de amostragem: parâmetros é exibida. |  |
| 5 | Inserir grau de controle Parâmetros | Na caixa de diálogo Criar plano de amostragem: parâmetros, efetue a seguinte pesquisa e entradas:Grau de controle: por exemplo, 002(controle reduzido)Dica O grau de controle define se é executado um controle normal, reduzido ou intensificado. Um planejador de qualidade pode adaptar flexivelmente os recursos de controle, tais como menos controles, tamanhos menores de amostra ou critérios mais altos de aceitação, se a situação de qualidade atual for boa.e selecione Selecionar | A visão Criar plano de amostragem: tabela de amostras é exibida. |  |
| 6 | Criar instruções da amostra | Na tabela Instruções de amostra, efetue as seguintes entradas.Tamanho do lote: por exemplo, 10.Tamanho de amostra: por exemplo, 1.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 100.Tamanho de amostra: por exemplo, 2.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 1000.Tamanho de amostra: por exemplo, 5.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 10000000000.Tamanho de amostra: por exemplo, 50.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1. | Foi criada uma instrução da amostra.Aceitação nº N: Número mais alto de unidades não conformes ou defeitos tolerados, de forma que o lote ou o atributo possa ser aceito.Rejeição nº N: Número mais baixo de unidades não conformes ou defeitos resultando em uma rejeição do lote ou do atributo.Lembrete Se o número de unidades não conformes ou defeitos se situar entre os limites de aceitação e rejeição, o sistema define a instrução da amostra seguinte. |  |
| 7 | Criar outra tabela | Na visão Criar plano de amostragem: tabela de amostras, selecione Outra tabela (ou pressione shift + F5). | A caixa de diálogo Criar plano de amostragem: parâmetros é exibida. |  |
| 8 | Inserir grau de controle Parâmetros | Na caixa de diálogo Criar plano de amostragem: parâmetros, efetue as seguintes entradas:Grau de controle: por exemplo, 004 (controle normal)e clique em Selecionar | A visão Criar plano de amostragem: tabela de amostras é exibida. |  |
| 9 | Criar instruções da amostra | Na tabela Instruções de amostra, efetue as seguintes entradas.Tamanho do lote: por exemplo, 10.Tamanho de amostra: por exemplo, 1.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 100.Tamanho de amostra: por exemplo, 5.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 1000.Tamanho de amostra: por exemplo, 10.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 10000000000.Tamanho de amostra: por exemplo, 100.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1. | Em seguida, a instrução da amostra é criada. |  |
| 10 | Criar outra tabela | Na visão Criar plano de amostragem: Na visão Tabela de amostras, selecione Outra tabela (ou pressione shift + F5). | A caixa de diálogo Criar plano de amostragem: parâmetros é exibida. |  |
| 11 | Inserir grau de controle Parâmetros | Na caixa de diálogo Criar plano de amostragem: parâmetros, efetue as seguintes entradas:Grau de controle: por exemplo, 006 (controle intensificado)e clique em Selecionar | A visão Criar plano de amostragem: tabela de amostras é exibida. |  |
| 12 | Criar instruções da amostra | Na tabela Instruções de amostra, efetue as seguintes entradas.Tamanho do lote: por exemplo, 10.Tamanho de amostra: por exemplo, 2.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 100.Tamanho de amostra: por exemplo, 10.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 1000.Tamanho de amostra: por exemplo, 25.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1.Tamanho do lote: por exemplo, 10000000000.Tamanho de amostra: por exemplo, 200.Aceitação nº1: por exemplo, 0.Rejeição nº1: por exemplo, 1. | Em seguida, a instrução da amostra é criada. |  |
| 13 | Salvar dados | Para salvar os seus dados, clique em Salvar. | O plano de amostragem é criado. |  |

### Criar processo de amostragem (opcional)

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Selecione Criar processo de amostragem(QDV1). | A tela Criar processo de amostragem: 1ª tela é exibida. |  |
| 3 | Inserir nome do processo de amostragem | Insira um nome do processo de amostragem, por exemplo, YPERCIN1.Selecione Continuar. | Aparece uma nova janela. |  |
| 4 | Inserir dados do processo de amostragem | Insira dados para o processo de amostragem:insira uma descrição, por exemplo, 10% controle sem pontos de controleTipo de amostra: por exemplo, Amostra percentualModo de avaliação: por exemplo, avaliação de acordo com código atrib.caract.Pontos de controle: por exemplo, Sem pontos de controleCódigo de utilização: Deixe o campo Utilização bloqueada em branco.Selecione Continuar. | A regra de determinação é definida.Nota Para usar Planos de amostragem, é necessário selecionar Usar plano de amostragem no campo Tipo de amostra. Em seguida, você atribui o plano de amostragem que você criou no processo anterior. |  |
| 5 | Atualizar instrução da amostra | Selecione Amostra e insira em seguida os seguintes dados:Tamanho como % do lote: por exemplo, 10Selecione Continuar.Clique em Salvar. | Os dados são salvos. |  |

### Criar Regra de controle dinâmico (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

Criar regra de controle dinâmico.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar regra de controle dinâmico(QDR1). | A tela Criar regra de controle dinâmico: 1ª tela é exibida. |  |
| 3 | Inserir nome para regra de controle dinâmico | Insira um nome para a regra de controle, por exemplo, QM1 | A tela Criar regra de controle dinâmico: dados de cabeçalho é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetuar as seguintes entradas:Texto breve: por exemplo, Controle/SkipPara decisão de utilização: marcadoReinicializar período (dias): por exemplo, 90Selecionar Tela seguinte | A tela Criar regra de controle dinâmico: etapas de controle é exibida. |  |
| 5 | Inserir dados para etapa de controle 10 | Efetue as entradas abaixo na primeira linha:Etapa: 10GrauCtrl.: 2Ctrl.inicial Etapa: marcadoTexto breve: Controle inicial |  |  |
| 6 | Inserir dados para etapa de controle 20 | Efetue as entradas abaixo na segunda linha:Etapa: 20GrauCtrl.: deixar em brancoSkip: marcadoTexto breve: Skip |  |  |
| 7 | Inserir dados para etapa de controle 30 | Efetue as entradas abaixo na terceira linha:Etapa: 30GrauCtrl.: 4Texto breve: por exemplo, <Controle normal> |  |  |
| 8 | Atualizar modificação da etapa de controle 10 | Selecione Etapa de controle 10 e em seguida Modificação da etapa.Na tela Criar modificação da etapa, efetue as seguintes entradas:OKNº de controles: 1Novo ctrl. Etapa: 20Não OKRejeições: 1Novo ctrl. Etapa: 30 | As entradas são refletidas na tabela. |  |
| 9 | Atualizar modificação da etapa de controle 20 (Skip) | Selecione Etapa de controle 20 e em seguida Modificação da etapa.Na tela Criar modificação da etapa, efetue as seguintes entradas:OKNº de skips: 1Duração máx.skip: 90Novo ctrl. Etapa: 30Não OKRejeições: 1Novo ctrl. Etapa: 30 | As entradas são refletidas na tabela. |  |
| 10 | Atualizar modificação da etapa de controle 30 | Selecione Etapa de controle 30 e em seguida Modificação da etapa.Na tela Criar modificação da etapa, efetue as seguintes entradas:OKNº de controles: 1Novo ctrl. Etapa: 20Não OKRejeições: 1Novo ctrl. Etapa: 30 | As entradas são refletidas na tabela. |  |
| 11 | Salvar os dados | Salve os dados. |  |  |

### Criar plano de controle

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | É exibida a página Início. |  |
| 2 | Acessar o app SAP Fiori | Abra o bloco Criar plano de controle(QP01). | Criar plano de controle (visão inicial) é exibido. |  |
| 3 | Inserir dados | Em Criar plano de controle (visão inicial), efetue as seguintes entradas:Material: <Seu número de material>, por exemplo QM001Centro: <Código do centro>Data fixada: por exemplo, hojeSelecione Avançar. | A visão Criar plano de controle: detalhes do cabeçalho é exibida quando não houver nenhum plano disponível para a combinação material/centro.Nota Se houver um plano disponível, selecione um grupo da caixa de diálogo e Criar plano de controle: síntese da lista de tarefas é exibido. Selecione Novas entradas para criar um novo plano de controle. |  |
| 4 | Atualizar detalhes do cabeçalho | Criar plano de controle (detalhes do cabeçalho) aparece. Insira os dados seguintes:Utilização: Selecione na lista de entradas possíveis para fins de utilização, por exemplo, 5 Entrada de mercadoriasStatus: A partir da lista de entradas possíveis, selecione por exemplo 4 Liberado (geral)Tamanho do lote: entre 1 e 99.999, por exemplo, 999 unNível controle dinâmico (opcional): 1 Controle dinâmico no nível do loteNota Estes dados só são necessários se você usar Regras de controle dinâmico.Regra de controle dinâmico (opcional): <Seus dados>Nota Estes dados só são necessários se você usar Regras de controle dinâmico.Critérios de controle dinâmico (opcional): por exemplo, Fornecedor e ProdutorNota Estes dados só são necessários se você usar Regras de controle dinâmico.Selecione Operações. | A tela Criar plano de controle: síntese de operações é exibida. |  |
| 5 | Inserir dados da operação (síntese) | Na visão Criar plano de controle: síntese de operações, insira o seguinte:Nº da operação: por exemplo, 0010Centro de trabalho: Selecione um centro de trabalho, por exemplo, QMLABSChave de controle: Selecione uma chave de controle, por exemplo, QM01Descrição: Insira uma descrição.Marque a partida individual de operação e selecione Operação.Nota Se o botão Operação não estiver disponível, selecione Mais > Operação | Criar plano de controle: detalhes da operação aparece.Nota A chave de controle influencia o planejamento e o processamento da operação de controle, por exemplo, se é ou não necessário atualizar características de controle para uma operação de controle. |  |
| 6 | Dados da operação (detalhes) | Na visão Criar plano de controle: detalhes da operação, role para verificar Visão de registro: ‘valores individuais e resultado compactado (visão default)’Selecione Voltar para retornar à visão Síntese de operações. |  |  |
| 7 | Inserir características de controle | Marque a linha de operação e selecione o botão Característica de controle.Atribua Características mestre de controle, por exemplo, uma característica mestre de controle relacionada à qualidade, como YQUALI01 para uma característica qualitativa; ou uma relacionada à quantidade, como YQUANTI01 para uma característica quantitativa.Atribua Procedimento de amostra (opcionalmente), para usar em combinação com as características a serem controladas.Atribuir Regra de controle dinâmico (opcional): por exemplo, QMINota A modificação dinâmica pode ser atribuída no nível do cabeçalho ou no nível da característica de controle.Pressione Enter. | As informações detalhadas são exibidas. |  |
| 8 | Salvar os dados | Clique em Salvar. | Os dados são salvos. |  |

### Administrar planos de controle

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Procedimento

| Nº da etapa de teste | Nº da etapa de teste / Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar planos de controle(F3788). | O app é aberto. |  |
| 3 | Filtrar dados | Em Administrar planos de controle (visão inicial), efetue as seguintes entradas:Material: <Material> (adaptando os filtros na seção Versão do plano de controle)Centro: <código do centro>Status do plano: <status global>, por exemplo, 4 Liberado (geral)Selecione Ir. | A lista de planos de inspeção aparece cumprindo os critérios de seleção. |  |
| 4 | Selecionar plano de controle | Selecione a entrada relevante e navegue selecionando o > no lado direito da linha selecionada. | Você navega para o Plano de controle relevante. |  |
| 5 | Modificar data fixada | No app Administrar planos de controle(F3788), selecione Modificar data fixada. É exibida uma caixa de diálogo e você pode atualizar a Data fixada inserindo a data a partir da qual a alteração deve ser válida:Data fixada: <Data>Nota A data fixada só é considerada para objetos criados e excluídos (por exemplo, operações de controle), mas não podem ser consideradas para alterações. As alterações no objeto existente podem aparecer imediatamente. | A data da pesquisa é alterada. |  |
| 6 | Atualizar dados gerais | A tela Administrar planos de controle é exibida com os campos Geral, Atribuição de material, Operações, Anexos e Dados administrativos. Efetue as seguintes entradas para atualizar os dados gerais (clique em Editar para alterar as entradas):Centro: Selecione na lista de entradas possíveis se ainda não tiver sido inserido.Descrição do plano de controle: Altere a descrição.Utilização: Selecione na lista de entradas possíveis para fins de utilização, por exemplo, 5 Entrada de mercadoriasStatus global: Selecione na lista de entradas possíveis, por exemplo, 4 Liberado (geral)Tamanho do lote: entre 1 e 99.999, por exemplo, 999 unPonto de controle (opcional): Insira 101 relacionado ao tempo, se você deseja criar pontos de controle com base no tempo.Nota Os dados a seguir só são necessários se você usar Regras de controle dinâmico.Nível controle dinâmico (opcional): 1 Controle dinâmico no nível do loteNota Em Regras de controle dinâmico, pode ser decidido em que nível uma dinamização é relevante.Regra de controle dinâmico (opcional): <seus dados>Nota Os dados a seguir só são necessários se você usar Regras de controle dinâmico.Critérios de controle dinâmico (opcional): por exemplo, Fornecedor e Produtor | Os dados gerais do plano de controle são atualizados. |  |
| 7 | Atualizar atribuição de material | Atualize as informações de Atribuição de material em Administrar planos de controle (selecione Adicionar para adicionar entradas):Material: <material>Centro: <código do centro>Fornecedor (opcional): <número do fornecedor>Cliente (opcional): <número do cliente>Nota Outros critérios podem ser exibidos por Configurações. | As informações de atribuição de material de plano de controle são atualizadas. |  |
| 8 | Atualizar operações | Atualize as informações de Operações em Administrar planos de controle (selecione Criar para criar entradas):Descrição da operação: <descrição>Centro: <código do centro>Quantidade básica: <quantidade>Unidade de medida: <unidade>Nota Outros critérios podem ser exibidos por Configurações.Navegue para os detalhes de operação clicando em > no lado direito da linha selecionada. | As informações da operação do plano de controle são atualizadas e você navega para o item. |  |
| 9 | Atualizar operação (síntese) | Atualize os Dados gerais na tela Operação:Nº da operação: <número indicado pelo sistema>Chave de controle: <fornecido pelo sistema>Centro: <código do centro>Descrição da operação: <descrição>Centro de trabalho (opcional) Selecione um centro de trabalho, por exemplo, QMLABSQuantidade básica: <quantidade>Unidade de medida: <unidade>Conversão de unidades de medida de cabeçalho para operaçãoNota Outros critérios podem ser exibidos por Configurações de ponto de controle. | Os dados gerais da operação são atualizados. |  |
| 10 | Atualizar operação (características) | Vá para Características na tela Operação. Selecione Atribuir características para copiar informações da característica mestre de controle ou selecione Adicionar para adicionar uma nova característica ou características mestre de controle.Nota Mesmo depois de clicar em Adicionar, é possível adicionar uma referência a uma característica mestre de controle posteriormente.Efetue as seguintes entradas:Descrição: <descrição breve>Características mestre de controle (opcional): <características mestre de controle>Código de controle: <Códigos de controle>Nota Outros critérios podem ser exibidos por Configurações de ponto de controle.Navegue para os detalhes da característica clicando em > no lado direito. | A informação da característica de operação é atualizada e você navega para a característica. |  |
| 11 | Atualizar característica | Os detalhes da característica são exibidos e podem ser atualizados. Os seguintes dados podem ser relevantes para a atualização:Nota Dependendo das configurações para Código de controle na etapa anterior, podem ser exibidos diferentes campos.Descrição: <descrição breve>Ponderação de característica (opcional): Selecione na lista de entradas possíveis, por exemplo, <Ponderação>Método de controle, versão, centro (opcional): Selecione na lista de entradas possíveis, por exemplo, <Método de controle>Campos de informação (opcional): <Mais informações>Conjunto selecionado, centro: selecione na lista de entradas possíveis, por exemplo, <características qualitativas do conjunto selecionado>Modificação dinâmica para a característica (opcional): Selecione na lista de entradas possíveis, por exemplo, <Outra característica>Regra de controle dinâmico (opcional): Selecione na lista de entradas possíveis, por exemplo, <Regra de controle dinâmico>Nota A regra de controle dinâmico só é exibida se for uma modificação dinâmica estiver no nível de característica.Você pode encontrar outros dados administrativos na área relevante.Volte para Operações. | As informações da característica são atualizadas e você navega para a tela Operações. |  |
| 12 | Verificar operações de dados administrativos | A tela Operações é exibida e pode ser atualizada.Você pode encontrar outros dados administrativos na área relevante.Volte para Plano de controle. | Os dados administrativos estão disponíveis e você navega para a tela Plano de controle. |  |
| 13 | Adicionar anexos ao plano de controle | O Plano de controle é exibido e os Anexos podem ser atualizados.Clique em Adicionar para criar um URL com descrição.Clique em Carregar para inserir um documento do sistema de arquivos local.Você pode encontrar outros dados administrativos na área relevante.Volte para Plano de controle. | Os dados administrativos estão disponíveis e você navega para a tela Plano de controle. |  |
| 14 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

### Copiar de planos de controle existentes

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador da qualidade | A página Início é exibida. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar planos de controle(F3788). | Administrar planos de controle (visão inicial) é exibida. |  |
| 3 | Na visão inicial Filtrar dados | Em Administrar planos de controle (visão inicial), efetue as seguintes entradas:Material: <material>, adaptando os filtros na seção Versão do plano de controle.Centro: <código do centro>Status do plano: <status global>, por exemplo, 4 Liberado (geral)Clique em Ir. | A Lista de planos de inspeção aparece cumprindo os critérios de seleção. |  |
| 4 | Na visão filtrada, selecione Planos de controle | Selecione a entrada relevante e navegue selecionando o > no lado direito da linha selecionada. | O plano de controle relevante foi inserido. |  |
| 5 | Copiar de Plano existente (início) | Administrar planos de controle é exibida Clique em Copiar de planos existentes.Na caixa de diálogo Copiar de planos existentes, insira potencialmente alguns dados ou clique em OK:Centro: <código do centro>, selecione a partir das entradas possíveis.Grupo e contador de grupos: <identificador do plano>, selecione a partir das entradas possíveis.Status global: <status>, a partir da lista de entradas possíveis, selecione por exemplo 4 Liberado (geral)Data de início de validade: selecione a partir da lista de entradas possíveisNota Outros critérios podem ser exibidos mediante Adaptar filtros | Cópia de painel lateral dos planos existentes é exibida. |  |
| 6 | Copiar de plano existente (cópia) | Em Copiar de planos existentes do lado dos planos, os planos de acordo com os filtros selecionados anteriormente são exibidos. Ao usar o > diante de cada linha, os objetos dos planos podem ser comprimidos:Plano > Materiais > OperaçõesEm Materiais um material pode ser selecionado e, clicando em Copiar, a entrada selecionada é copiada para o plano de controle atual.Em Operações uma ou várias operações podem ser selecionadas e clicando em Copiar transferido para o plano de controle.Operação > CaracterísticasEm Características atribuídas a operações individuais, uma ou várias características podem ser selecionadas e transferidas para uma operação de uso livre, clicando em Copiar. Também é possível marcar uma operação e uma ou várias características correspondentes para copiar a operação, incluindo somente as características marcadasNota Para copiar de planos existentes, também é possível na síntese Operação e característica no app Administrar planos de controle. | Cópia de painel lateral dos planos existentes é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | Seus dados estão salvos. |  |

### Exibir lotes de controle em aberto

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O lote de controle é usado para registrar os resultados da operação de controle. Nesta etapa opcional, as referências são verificadas e o tamanho da amostra usado para controle de qualidade é revisado. A instrução para retirada de amostra pode ser impressa.

Pré-requisito

O lote de controle é criado.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Aprovada / Reprovada / Comentário |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Técnico de qualidade | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar lotes de controle(F2343). | A tela Administrar lotes de controle é exibida. |  |
| 3 | Inserir Campos de filtro | Efetue entradas de filtro e clique em Ir | Se as referências relevantes (p.ex. Pedido de compra ou ordem de produção) não são exibidas nos Filtros, clique em Adaptar filtros. Na caixa de diálogo Adaptar filtros, procure Suprimento ou Produção e clique em Mais filtros. Selecione o documento relevante e clique em OK. Clique em Ir. |  |
| 4 | Selecionar lote de controle | Na lista de lote de controle, selecione o lote de controle que você criou anteriormente. | O lote de controle é exibido. |  |
| 5 | Imprimir instrução para retirada de amostra | Clique em Imprimir instrução para retirada de amostra.Selecione um item de saída para impressão, duplicado potencialmente um e, em seguida, clique em Enviar saída.Nota Se a impressão já tiver sido gerada para um lote de controle, o diálogo Detalhes de saída exibe uma lista de itens de saída impressos anteriormente. | A caixa de diálogo Detalhes de saída é exibida, mostrando uma lista de itens de saída com canais de impressão e de e-mail configurados. Um documento PDF que contém a instrução para retirada de amostra é acionada e é enviado para a aplicação Atualizar filas de impressão para impressão. |  |
| 6 | E-mail Instrução para retirada de amostra | Clique em Imprimir instrução para retirada de amostra.Selecione um item de saída para E-mail e, em seguida Enviar saída. | Um e-mail com o PDF é enviado para os destinatários previstos. |  |

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
> Flagged while digesting this document, not verified: Quantitative characteristic step text on 'modelo de cópia completo' vs 'incompleto' is near-identical for both, and differs from the qualitative description; possible text inconsistency

> [!warning] Conflict
> Flagged while digesting this document, not verified: Test-case metadata (ID, dates, executor) is left as template placeholders

## Connections
- part-of :: [[_cluster]]
- related-to :: [[13-quality-ehs-and-compliance/master-data-script-create-quality-inspection-plan-mds-bnq-653]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-655]]
- related-to :: [[13-quality-ehs-and-compliance/sap-s-4hana-cloud-public-edition-mds-bnq-657]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-creacion-de-plan-de-inspeccion-de-calidad-mds]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNQ_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 62,005 chars in the whole document
