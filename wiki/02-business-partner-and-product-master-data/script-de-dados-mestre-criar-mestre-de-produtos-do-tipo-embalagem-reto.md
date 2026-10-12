---
id: 02-business-partner-and-product-master-data/script-de-dados-mestre-criar-mestre-de-produtos-do-tipo-embalagem-reto
title: "Script de dados mestre - Criar mestre de produtos do tipo \"Embalagem retornável\" (MDS 65B) (65B_S4CLD2608_Master_Data_PT_XX)"
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (65B): test procedures to create a returnable-packaging (LEIH) product master via MM01 or F1602."
cluster: 02-business-partner-and-product-master-data
tags: [kb/business-partner-and-product-master-data, topic/product-master-packaging]
aliases: [65B_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product Master: Packaging and Returnable Packaging", product master data, returnable packaging, basic data, sales data, mrp planning data, storage location data, accounting data, material types, numbering ranges]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-500
topic: 02-business-partner-and-product-master-data/product-master-packaging
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar mestre de produtos do tipo "Embalagem retornável" (MDS 65B) (65B_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product Master: Packaging and Returnable Packaging** in Business Partner and Product Master Data. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar mestre de produtos do tipo "Embalagem retornável" – MDS (65B) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893876)

[2 Pré-requisitos 3](#_Toc233893877)

[2.1 Acesso ao sistema 3](#_Toc233893878)

[2.2 Funções 3](#_Toc233893879)

[2.3 Unidades organizacionais necessárias 4](#_Toc233893880)

[2.4 Dados mestre obrigatórios e opcionais 4](#_Toc233893881)

[2.5 Parâmetros principais para a criação de dados 5](#_Toc233893882)

[2.5.1 Tipo de material e intervalos de numeração 5](#_Toc233893883)

[2.5.2 Setor industrial 5](#_Toc233893884)

[3 Tabela de síntese 6](#_Toc233893885)

[4 Procedimentos de teste 7](#_Toc233893886)

[4.1 Criar dados mestre de materiais (produto) - dados básicos 7](#_Toc233893887)

[4.2 Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA) 10](#_Toc233893888)

[4.3 Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro) 14](#_Toc233893889)

[4.4 Criar dados mestre de materiais (produto) - dados do depósito 16](#_Toc233893890)

[4.5 Criar dados mestre de materiais (produto) – Dados contábeis 19](#_Toc233893891)

## Objetivo

O mestre de materiais ou produto contém informações sobre todos os materiais físicos armazenados e vendidos.

O mestre de materiais contém informações como o número único de material, nome, tipo de material, unidade de medida, descrições, peso e dimensões. Essas informações de material são usadas e armazenadas em transações como ordens do cliente, remessas, pedidos ou movimentos de mercadorias.

Visto que todas as informações de um material são armazenadas centralmente, as informações do mestre de materiais são organizadas em diferentes visões. Por exemplo, vendas, armazenamento e contabilidade.

Algumas informações em cada material são específicas a determinadas unidades organizacionais. Por exemplo, uma descrição de vendas é específica a uma unidade de vendas (conhecida como área de vendas), um planejador MRP é específico a um certo local (conhecido como centro), ou algumas informações podem ser específicas de um depósito.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece a você o URL para acessar os vários apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Especialista em dados mestre - Dados do produto | SAP_BR_PRODMASTER_SPECIALIST | Dados mestre - produtos / Governança de produto | SAP_BR_PRODMASTER_SPECIALIST / SAP_CMD_SPT_PR_GOV_PC |  |

### Unidades organizacionais necessárias

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Dados básicos | Independente de unidades organizacionais | Descrição do material (texto breve),, Número do material, Grupo de materiais, Unidade de medida básica, etc. | Os dados básicos só existem uma vez para um registro de dados mestre de materiais. | N/A |
| Dados de vendas | Centro, organização de vendas, canal de distribuição | Dados de imposto, Grupo de categorias de item, Grupo de transporte, Grupo de carregamento, etc. | Os dados de venda podem existir para todas as organizações de vendas de sua estrutura empresarial nas quais o registro mestre de materiais seja utilizado. | Centro:____________Organização de vendas:__________Canal de distribuição:__________ |
| Dados MRP/de planejamento | Centro, depósito | Tipo de MRP, Planejador MRP, Prazo de entrega previsto, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados do depósito | Centro, depósito | Centro de lucro, etc. | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de materiais.Os dados do depósito (contexto de planejamento) são opcionais com base na necessidade de efetuar o planejamento específico do depósito. | Centro:____________Depósito:__________ |
| Dados contábeis | Área de avaliação(=Centro) | Preço por unidade, Controle de preço, etc. | Os dados da área de avaliação podem existir para cada ID do centro da sua estrutura empresarial para a qual é utilizado o registro mestre de materiais. Cada centro representa uma área de avaliação (por exemplo, preço de avaliação diferente de um material em centros diferentes). | Centro:____________Tipo de avaliação:__________ |

### Dados mestre obrigatórios e opcionais

Os registros de dados mestre de materiais podem fazer referência a outros dados mestre. A tabela seguinte fornece uma síntese dos objetos de dados mestre opcionais e obrigatórios a serem utilizados em um registro de dados mestre de materiais.

|  |
| --- |
| Nota Os campos específicos do Brasil são necessários para obter um cálculo de imposto adequado.Verifique Nota Fiscal Brasil - JD0 no capítulo Definir campos específicos do BR para dados mestre para dados mestre de materiais. |

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| Centro de lucro |  | Obrigatório | A atribuição de um centro de lucro a um mestre de materiais (produtos) é necessária para os processos de avaliação corretos. |

### Parâmetros principais para a criação de dados

Nesta seção descrevemos alguns parâmetros básicos que influenciam o comportamento de um registro mestre e que são sempre necessários para criar um registro de dados mestre de materiais.

#### Tipo de material e intervalos de numeração

Com a ajuda de tipos de material, o sistema determina que segmentos de dados (visões) podem ser atualizados ou que campos são obrigatórios ou opcionais. Com base em tipos de material, o sistema também determina os intervalos de numeração para materiais. No conteúdo padrão SAP, todos os tipos de material utilizam a mesma definição de intervalo de numeração.

| Intervalo de numeração | Intervalo/ID do parceiro de negócios | Comentários |
| --- | --- | --- |
| Alfanumérico externo | A – ZZZZZZZZ | Este intervalo deve iniciar com um caractere. Em geral, o ID não deve ter mais de 40 caracteres. |
| Numérico interno | 1 – 99999999 | Este intervalo é utilizado se o sistema tiver que atribuir automaticamente um valor numérico a um material. |

#### Setor industrial

O conteúdo padrão fornece apenas um setor industrial M. Atualmente, ele é visível apenas no SAP GUI.

## Tabela de síntese

Este item de escopo consiste de várias etapas de processo listadas na seguinte tabela:

Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.

Você pode encontrar todos os outros apps não incluídos na página inicial usando a barra de pesquisa.

Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps.

| Etapa de processo | Função empresarial | Transação / App | Resultados previstos |
| --- | --- | --- | --- |
| [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7 | Especialista em dados mestre - Dados do produto | Criar material(MM01) / Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados básicos criados. |
| [Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA)](#unique_12) [página ] 10 | Especialista em dados mestre - Dados do produto | Criar material(MM01) / Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados de vendas criados. |
| [Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)](#unique_13) [página ] 14 | Especialista em dados mestre - Dados do produto | Criar material(MM01) / Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados MRP/de planejamento criados. |
| [Criar dados mestre de materiais (produto) - dados do depósito](#unique_14) [página ] 16 | Especialista em dados mestre - Dados do produto | Criar material(MM01) / Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados do depósito criados. |
| [Criar dados mestre de materiais (produto) – Dados contábeis](#unique_15) [página ] 19 | Especialista em dados mestre - Dados do produto | Criar material(MM01) / Administrar dados mestre do produto(F1602) | Dados mestre de materiais – Dados contábeis (dados da área de avaliação) criados. |

## Procedimentos de teste

Esta seção descreve procedimentos para cada segmento ou etapa de processo que faz parte deste registro mestre.

### Criar dados mestre de materiais (produto) - dados básicos

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 3 | Inserir dados básicos de material | Na tela Criar material (1ª tela), faça o seguinte:Material: <número do material>Setor industrial: engenharia mecânicaNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Embalagem retornávelClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 4 | Clicar em visões | Na janela Selecionar visões, selecione as visões seguintes e clique em Continuar:Dados básicos 1Dados básicos 2 | A tela Criar material... (embalagem retornável) é exibida. |  |
| 5 | Inserir dados básicos | Na guia Dados básicos 1, insira uma descrição do material (texto breve). |  |  |
| 6 | Inserir dados básicos | Na guia Dados básicos 1, na seção Dados gerais, insira as descrições para o seguinte:Unidade de medida básicaGrupo de materiaisGrpCtgsItemGer.: LEIH |  |  |
| 7 | Inserir dados básicos | Na seção Dimensões/EANs insira o seguinte:Peso brutoUnidade de pesoPeso líquidoPressione Enter. | A guia Dados básicos 2 é exibida. |  |
| 8 | Preencher dados básicos | Não são necessárias entradas para Dados básicos 2. |  |  |
| 9 | Salvar os dados | No canto inferior direito da tela, clique em Salvar para salvar seus dados. | É exibida a tela Criar material (1ª tela).Os dados básicos são criados e salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento a seguir, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | A tela Administrar dados mestre de produto é exibida. |  |
| 3 | Selecionar Criar novo mestre de produtos | Na tela Administrar dados mestre do produto, na seção Produtos, clique em Criar. | A tela Criar registro de dados mestre é exibida. |  |
| 4 | Inserir dados para campos obrigatórios | Na tela Criar registro de dados mestre, efetue as seguintes entradas:Número do produto: por exemplo, Z …Nota Você insere qualquer ID alfanumérico externo e esse ID deve iniciar com um caracteres alfanumérico ou, se você não fornecer nenhuma entrada, o sistema atribui automaticamente um ID numérico.Para mais informações sobre o número do produto, consulte a seção anterior Tipo de material e intervalos de números.Tipo de produto: LEIHGrupo de produtos: por exemplo, L006Unidade básica: por exemplo, Unid.Descrição: <qualquer descrição> |  |  |
| 5 | Clicar em OK | Clique em OK. |  |  |
| 6 | Inserir dados básicos | Vá para Administrar dados mestre de produto > Informações gerais > Dados básicos, e efetue as seguintes entradas:Setor de atividade: por exemplo, 00 |  |  |
| 7 | Clicar em Adicionar (+) | Vá para Administrar mestre de produtos > Informações gerais > Descrições, e clique em Criar. | A descrição no idioma padrão (por exemplo, inglês) já se encontra preenchida. |  |
| 8 | Inserir dados de descrição | Na visão Descrições, efetue as seguintes entradas:Idioma: por exemplo, AlemãoDescrição do produto: <sua descrição> |  |  |
| 9 | Inserir dados de data do peso | Na seção Peso (se não for exibido, clique em Exibir mais), insira o seguinte:Peso bruto: por exemplo, 2Unidade de peso: por exemplo, kgPeso líquido: por exemplo, 1Nota Se a seção Peso não for exibida, clique em Exibir mais.Quando os campos Peso bruto, Unidade de peso, ou Peso líquido não fornecer um campo de entrada, atualize ou recarregue a página da Web. Depois de atualizar ou recarregar, os campos estarão disponíveis para entrada. |  |  |
| 10 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de materiais (produto) - dados de vendas (dados do IVA)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve completar a seção anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, antes de continuar com esta seção.

Inicie o procedimento assim que salvar as entradas de dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Clique em Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: engenharia mecânicaNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: LEIH Embalagem retornávelClique em Selecionar visões. | A tela Selecionar visões é exibida. |  |
| 3 | Clicar em visões | Na tela Selecionar de visões, clique em Vendas: Dados organizacionais de vendas 1, Vendas: Dados organizacionais de vendas 2 e Vendas: Dados gerais/do centro e clique em Continuar. | A tela Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Níveis organizacionais, na seção Níveis organizacionais, insira as descrições para o seguinte:CentroOrganização de vendasCanal de distribuiçãoClique em Continuar.Nota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | A tela Criar material... (embalagem retornável) é exibida. |  |
| 5 | Inserir dados de vendas | Na tela Criar material... (embalagem retornável), na guia Vendas: organização de vendas 1, na seção Dados gerais, efetue as seguintes entradas:Unidade de medida básicaCentro fornecedor |  |  |
| 6 | Inserir dados de vendas | Na tela Criar material... (embalagem retornável), na guia Vendas: organização de vendas 1, na seção Dados fiscais, efetue as seguintes entradas:Classificação fiscal: 1Nota O valor inserido indica que o material é (geralmente) totalmente tributável.Somente para o Brasil: na seção Dados fiscais, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: 1Pressione Enter. | A guia seguinte, Vendas: organização de vendas 2 é exibida. |  |
| 7 | Inserir dados de vendas | Na guia Vendas: organização de vendas 2, na seção Critérios de agrupamento, efetue as seguintes entradas:Grupo estat.materialGrupo de categorias de item: CB02Grp.ctg.item geral LEIHMat.grp.class.cont. Y2Pressione Enter. | A guia seguinte, Vendas: geral/centro é exibida. |  |
| 8 | Inserir dados de vendas | Na guia Vendas: gerais/centro, na seção Dados gerais, insira os seguintes dados:Verificação de disponibilidade: SR |  |  |
| 9 | Inserir dados de vendas | Na guia Vendas: gerais/centro, na seção Dados de expedição (tempos em dias), insira os seguintes dados:Grp. transf.: <0001>Grp.carregamento: <0001> |  |  |
| 10 | Inserir dados de vendas | Na guia Vendas: gerais/centro, na seção Parâmetros gerais de centro, insira os seguintes dados:Centro de lucro |  |  |
| 11 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento a seguir, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que o levará até a tela Produto.Selecione Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar as cadeias de distribuição | Na tela Produto, clique na guia Cadeias de distribuição. | A guia Cadeias de distribuição é exibida. |  |
| 4 | Clicar em Adicionar (+) | Na guia Cadeias de distribuição, clique em Criar. | Cadeias de distribuição é exibido no modo de edição. |  |
| 5 | Inserir dados de cadeias de distribuição | Na tela Cadeias de distribuição, efetue as seguintes entradas:Vá para Informações gerais > Dados gerais:Organização de vendas: <nº org.vendas>Nota O valor da unidade organizacional é determinado pelo que é oferecido nas entradas possíveis.Canal de distribuição: por exemplo, 10Centro fornecedor: <número do centro>Na seção Critérios de agrupamento:Grupo de categorias de item: por exemplo, CB02Grupo de classificações contábeis: por exemplo, Y2 Mercadorias retornáveisNa seção IVA:País: <código do país>Categoria de imposto: por exemplo, TTX1:Classificação fiscal: por exemplo, insira 1 para material ou 2 para serviços. Exemplo de Classificação fiscal: 1 Imposto total ao utilizar a condição de imposto UTXJ para EUA.Nota A classificação fiscal depende dos requisitos específicos do país. A classificação fiscal no mestre de materiais e nas tabelas mestre de clientes determinam as entradas da porcentagem.Somente para o Brasil: Na seção Classificação fiscal, efetue as seguintes entradas:País: BRCategoria de imposto: IBRXClassificação fiscal: 1 |  |  |
| 6 | Retornar à visão principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com esta seção.

Inicie o procedimento assim que salvar as entradas de Dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: engenharia mecânicaNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Embalagem retornávelClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Clicar em visões | Na tela Selecionar visões, selecione MRP 1, MRP 2, MRP 3e MRP 4 e clique em Continuar. | A tela Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Efetue as seguintes entradas na tela Níveis organizacionais, na seção Níveis organizacionais:Centro: <número do centro>Depósito: <número do depósito>Clique em Continuar.Nota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | A tela Criar material... (embalagem retornável) é exibida. |  |
| 5 | Inserir dados MRP/de planejamento | Na tela Criar material... (embalagem retornável), na guia MRP 1, na seção Procedimento MRP, efetue as seguintes entradas:Tipo de MRP: NDPlanejador MRP: <001>Pressione Enter. | A guia seguinte, MRP 2 é exibida. |  |
| 6 | Inserir dados MRP/de planejamento | Na tela Criar material... (Embalagem retornável), na guia MRP 2, na seção Planejamento, efetue a seguinte entrada:Prazo de entrega Hora: por exemplo, 10Na seção Suprimento, efetue a seguinte entrada:Tipo de suprimento: FPressione Enter. | A guia seguinte, MRP 3 é exibida. |  |
| 7 | Inserir dados MRP/de planejamento | Na tela Criar material... (embalagem retornável), na guia MRP 3, na seção Verificação de disponibilidade, efetue a seguinte entrada:Verificação de disponibilidade: por exemplo, SRPressione Enter. | A guia seguinte, MRP 4 é exibida. |  |
| 8 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento a seguir, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que o levará até a tela Produto.Selecione Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique na guia Centros. | A guia Centros é exibida. |  |
| 4 | Clicar em Adicionar (+) | Na guia Centros, clique em Criar. | A tela Centros é exibida no modo de edição. |  |
| 5 | Inserir centros - dados gerais | Vá para Informações gerais > Dados gerais, e efetue as seguintes entradas:Centro: nº do centro, por exemplo, 1010Centro de lucro: por exemplo, YB111Na seção Vendas, efetue a seguinte entrada:Grupo de carregamento, por exemplo, 0001 |  |  |
| 6 | Inserir centros - dados MRP | Vá para Dados MRP > Dados MRP e efetue as seguintes entradas:Verificação de disponibilidade:: por exemplo, SRTipo de MRP: por exemplo, NDPlanejador MRP: por exemplo, 001 |  |  |
| 7 | Inserir centros - dados de suprimento | Vá para Dados MRP > Suprimento, e efetue a seguinte entrada:Prazo de entrega planejado: por exemplo, 10 |  |  |
| 8 | Retornar à visão principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de materiais (produto) - dados do depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com esta seção.

Inicie o procedimento assim que salvar as entradas de Dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: engenharia mecânicaNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Embalagem retornávelClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Clicar em visões | Na tela Selecionar visões, marque o seguinte:Dados gerais do centro/armazenamento 1Dados gerais do centro/armazenamento 2Clique em Continuar. | A tela Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Efetue as seguintes entradas na tela Níveis organizacionais, na seção Níveis organizacionais:Centro: por exemplo, <número do centro>Depósito: <número do depósito>Clique em Continuar.Nota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | A tela Criar material... (embalagem retornável) é exibida. |  |
| 5 | Inserir dados do depósito | Para a guia Dds.cen./armazmto 1 nenhuma entrada é necessária. |  |  |
| 6 | Confirmar entradas | Para a guia Dds.cen./armazmto 2 nenhuma entrada é necessária. |  |  |
| 7 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento a seguir, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que o levará até a tela Produto.Selecione Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados de centros | Na tela Produto, clique na guia Centros.Nota Se não houver registro de dados da planta, siga as etapas da seção anterior, [Criar dados mestre de materiais (produto) - dados MRP/de planejamento (dados do centro)](#unique_13) [página ] 14. | A guia Centros é exibida. |  |
| 4 | Selecionar detalhes do centro | Na guia Centros, use o ícone de seta para selecionar os dados de centro criados na etapa anterior. | A tela Centro é exibida. |  |
| 5 | Navegar para o centro: Depósito | Na tela Centro, vá para Depósitos > Depósitos. |  |  |
| 6 | Clicar em Adicionar (+) | Na guia Depósitos, na seção Depósitos, clique em Criar. | A visão Centro – Depósitos é exibida. |  |
| 7 | Inserir centro: Dados do depósito | Na tela Centro – Depósitos, efetue a seguinte entrada:Depósito: <número do depósito> |  |  |
| 8 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 9 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

### Criar dados mestre de materiais (produto) – Dados contábeis

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O seguinte procedimento disponibiliza instruções para criar dados mestre do material (produto). Os apps disponíveis dependem da sua função atribuída, por isso são fornecidas duas opções.

Pré-requisito

Você deve concluir o procedimento anterior, [Criar dados mestre de materiais (produto) - dados básicos](#unique_11) [página ] 7, para prosseguir com esta seção.

Inicie o procedimento assim que salvar as entradas de Dados básicos, como descrito no procedimento anterior.

Procedimento: Opção 1 – Criar material

Utilize o seguinte procedimento, caso seu acesso de usuário ofereça o app Criar material(MM01).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Criar material(MM01). | É exibido Criar material (1ª tela). |  |
| 2 | Inserir dados básicos de material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Setor industrial: engenharia mecânicaNota Se o campo de entrada Setor industrial estiver oculto, nenhuma entrada é necessária. Quando o setor industrial não é oferecido para entrada, o campo fica esmaecido.Tipo de material: Embalagem retornávelClique em Seleção de visões. | A tela Selecionar visões é exibida. |  |
| 3 | Clicar em visões | Na tela Selecionar visões, marque o seguinte:Contabilidade 1Contabilidade 2Clique em Continuar. | A tela Níveis organizacionais é exibida. |  |
| 4 | Inserir dados dos níveis organizacionais | Na tela Níveis organizacionais, na seção Níveis organizacionais, efetue a seguinte entrada:Centro: <número do centro>Clique em Continuar.Nota São exibidas informações na parte inferior da tela: O material já existe e será ampliado. | A tela Criar material... (embalagem retornável) é exibida. |  |
| 5 | Inserir dados contábeis | Na tela Criar material... (embalagem retornável), na guia Contabilidade 1, na seção Avaliação atual, efetue as seguintes entradas:Classe de avaliação: por exemplo, 3050Preço móvel: por exemplo, 5Controle de preço:: por exemplo, VPressione Enter.Nota A classe de avaliação não é obrigatória para o tipo de produto LEH. Você pode defini-la como vazia via app Modificar material(MM02). | É exibida a guia seguinte Contabilidade 2. |  |
| 6 | Confirmar entradas | Na guia Contabilidade 2, nenhuma entrada é necessária. |  |  |
| 7 | Salvar os dados | Na parte inferior da tela, clique em Salvar. | Os dados estão salvos. |  |

Procedimento: Opção 2 – Administrar dados mestre de produto

Use o procedimento a seguir, caso seu acesso de usuário ofereça o app Administrar dados mestre do produto(F1602).

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Acessar o app SAP Fiori | Abra Administrar dados mestre do produto(F1602). | O app é aberto e vários campos de pesquisa são exibidos. |  |
| 2 | Procurar e abrir o produto para edição | Procure o produto criado anteriormente, inserindo o número do produto no campo de pesquisa Produto.Selecione o produto da lista que o levará até a tela Produto.Selecione Editar. | O produto é exibido no modo de edição (os campos estão disponíveis para entrada). |  |
| 3 | Selecionar dados da área de avaliação | Na tela Produto, clique na guia Áreas de avaliação. | A guia Áreas de avaliação é exibida. |  |
| 4 | Selecione Create | Na guia Áreas de avaliação, na seção Áreas de avaliação, clique em Criar. | A tela Área de avaliação é exibida no modo de edição. |  |
| 5 | Inserir dados da área de avaliação atual | Na guia Informações gerais, na seção Dados gerais, efetue as seguintes entradas:Área de avaliação: por exemplo, 1010Classe de avaliação: por exemplo, 3050Na seção Período atual, efetue as seguintes entradas:Preço do estoque: por exemplo, 5Controle do preço: por exemplo, preço médio móvel/preço interno periódico (V) |  |  |
| 6 | Retornar à tela principal | Clique em Aplicar para voltar à tela Produto. | A tela Produto é exibida. |  |
| 7 | Salvar os dados | Clique em Salvar. | O objeto é salvo. |  |

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
- related-to :: [[02-business-partner-and-product-master-data/master-data-script-create-product-master-of-type-returnable-packaging]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-499]]
- related-to :: [[02-business-partner-and-product-master-data/mds-65b-501]]
- related-to :: [[02-business-partner-and-product-master-data/script-de-datos-maestros-crear-maestro-de-productos-de-tipo-embalaje-e]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/65B_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 38,047 chars in the whole document
