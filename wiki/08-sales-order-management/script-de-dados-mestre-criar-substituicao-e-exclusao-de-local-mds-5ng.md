---
id: 08-sales-order-management/script-de-dados-mestre-criar-substituicao-e-exclusao-de-local-mds-5ng
title: Script de dados mestre - Criar substituição e exclusão de local (MDS 5NG) (5NG_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP S/4HANA Cloud Public Edition 2608 master data script (5NG): test steps to create plant and storage location substitutions and exclusions via Fiori apps."
cluster: 08-sales-order-management
tags: [kb/sales-order-management, topic/product-and-location-substitution]
aliases: [5NG_S4CLD2608_Master_Data_PT_XX]
keywords: ["Product, Plant and Storage Location Substitution", plant substitution, plant exclusion, storage location substitution, storage location exclusion, master data scripts, substitution reasons, substitution groups, substitution controls, organizational units]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-476
topic: 08-sales-order-management/product-and-location-substitution
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre - Criar substituição e exclusão de local (MDS 5NG) (5NG_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Product, Plant and Storage Location Substitution** in Sales Order Management. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar substituição e exclusão de local – MDS (5NG) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893875)

[2 Pré-requisitos 3](#_Toc233893876)

[2.1 Acesso ao sistema 3](#_Toc233893877)

[2.2 Funções 3](#_Toc233893878)

[2.3 Unidades organizacionais necessárias 3](#_Toc233893879)

[2.4 Dados mestre obrigatórios 4](#_Toc233893880)

[2.5 Etapas preliminares para substituição de centro 4](#_Toc233893881)

[2.5.1 Criar motivo para substituição de centro (opcional) 4](#_Toc233893882)

[2.5.2 Criar grupo para substituição de centro (opcional) 5](#_Toc233893883)

[2.5.3 Criar controle para substituição de centro (opcional) 7](#_Toc233893884)

[2.6 Etapas preliminares para substituição de depósito 8](#_Toc233893885)

[2.6.1 Criar motivo para substituição de depósito (opcional) 8](#_Toc233893886)

[2.6.2 Criar grupo para substituição de depósito (opcional) 9](#_Toc233893887)

[2.6.3 Criar controle para substituição de depósito (opcional) 11](#_Toc233893888)

[3 Tabela de síntese 13](#_Toc233893889)

[4 Procedimentos de teste 14](#_Toc233893890)

[4.1 Substituição de centro 14](#_Toc233893891)

[4.1.1 Criar substituição de centro 14](#_Toc233893892)

[4.1.2 Criar exclusão de centro 15](#_Toc233893893)

[4.2 Substituição de depósito 17](#_Toc233893894)

[4.2.1 Criar substituição de depósito 17](#_Toc233893895)

[4.2.2 Criar exclusão de depósito 18](#_Toc233893896)

## Objetivo

Neste documento, você encontrará informações sobre como criar dados mestre de substituição e exclusão de localização para o sistema SAP S/4HANA Cloud Public Edition.

Os tipos de localização Centro e Depósito são suportados para substituição e exclusão.

Substituição de centro é uma técnica usada para substituir um centro por outro. Uma substituição de centro pode ser criada por vários motivos. Por exemplo:

- O centro de origem está em manutenção
- O centro de origem está em zona de contenção
- O estoque do produto não está disponível no centro de origem

A exclusão do centro permite que os clientes excluam um centro de se tornar um substituto. Por exemplo, a exclusão de centro pode ser criada para um centro temporariamente desativado.

A substituição de depósito é uma técnica usada para substituir um depósito por outro no mesmo centro. Uma substituição de depósito pode ser criada por vários motivos. Por exemplo:

- O depósito de origem não está disponível
- O estoque do produto não está disponível no depósito de origem no centro

Exclusão do depósito permite que os clientes excluam um depósito de se tornar um substituto.

## Pré-requisitos

Esta seção resume todos os pré-requisitos necessários para conduzir o teste em termos de sistemas, usuários, dados mestre, dados organizacionais, outros dados de teste e condições empresariais.

### Acesso ao sistema

| sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece a você o URL para acessar os vários apps atribuídos a sua função. |

### Funções

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) | Efetuar login |
| --- | --- | --- | --- | --- |
| Administrador de cumprimento de ordens | SAP_BR_ORDER_FULFILLMNT_MNGR | Administração de cumprimento da ordem | SAP_BR_ORDER_FULFILLMNT_MNGR |  |

### Unidades organizacionais necessárias

A estrutura organizacional reflete a estrutura da sua empresa.

Os substitutos do centro podem ser dependentes de unidades organizacionais (organização de vendas e canal de distribuição) da empresa. Também pode ser independente da unidade organizacional.

Os substitutos de depósito podem ser dependente das unidade organizacional (centro) da empresa. É sempre dependente da unidade organizacional.

A tabela a seguir fornece uma síntese das unidades organizacionais relevantes.

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Substituição e exclusão de centro | Organização de vendas |  | A organização de vendas não é obrigatória na substituição/exclusão de centro. A substituição/exclusão de centro pode ocorrer sem restrição da organização de vendas. | Organização de vendas:____________ |
| Substituição e exclusão de centro | Canal de distribuição |  | O canal de distribuição não é obrigatório na substituição/exclusão de centro. A substituição/exclusão de centro pode ocorrer sem restrição de canal de distribuição. | Canal de distribuição:____________ |
| Substituição e exclusão de depósito | Centro |  | O centro é obrigatório em substituição/exclusão de depósito. A substituição/exclusão de depósito não pode ocorrer sem o centro. | Centro: 1010 |

### Dados mestre obrigatórios

| Objeto de dados mestre | Usado no segmento de dados | Obrigatório/opcional | Comentários |
| --- | --- | --- | --- |
| NA | NA | NA | NA |

### Etapas preliminares para substituição de centro

#### Criar motivo para substituição de centro (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de motivo para a substituição/exclusão de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar motivos da substituição - Unidades gerenciais(F5313). | A tela Administrar motivos de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar motivos de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar motivos de substituição – Criar unidades gerenciais é exibida. |  |
| 4 | Inserir um motivo | Efetue a seguinte entrada na seção Cabeçalho:Categoria da unidade gerencial: <centro>Motivo: <insira o novo código do motivo para substituição de centro, por exemplo, NEW_PLANT> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Motivo criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição do motivo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o motivo, por exemplo, EN inglês>Descrição do motivo: <insira texto para descrever o motivo, por exemplo, Novo centro disponível> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição criada. |  |

#### Criar grupo para substituição de centro (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de grupos para substituição/exclusão de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar grupos de substituição - Unidades gerenciais(F5311). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar grupos de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar grupos de substituição – Criar unidades gerenciais é exibida. |  |
| 4 | Inserir grupo | Efetue as seguintes entradas na seção Cabeçalho:Categoria da unidade gerencial: <centro>Grupo: <Insira o novo grupo de substituição, por exemplo, SOUTH_REGION> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Grupo criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição do grupo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <Insira o idioma aplicável para o grupo, por exemplo, EN inglês>Descrição do grupo: <insira texto para descrever o grupo, por exemplo, Centros disponíveis na região sul> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição do grupo criada. |  |
| 9 | Selecionar Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar grupos de substituição – Unidades gerenciais é exibida. |  |
| 10 | Ativar dados do grupo | Clique em Definir como ativo. | A mensagem do sistema mostra que O status foi modificado. |  |

#### Criar controle para substituição de centro (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de controle para controles de substituição/exclusão de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Unidades gerenciais(F5312). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar controles de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar controles de substituição – Criar unidades gerenciais é exibida. |  |
| 4 | Inserir controle | Efetue a seguinte entrada na seção Cabeçalho:Categoria da unidade gerencial: <centro>Controle: <insira o novo controle para substituição, por exemplo, REGION> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Controle criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o controle, por exemplo, EN inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, para uma região> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição de controle criada. |  |
| 9 | Selecionar Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 10 | Grupos atribuídos | Na seção Grupos atribuídos, clique em Atribuir. | A tela Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, clique em Grupo<SOUTH_REGION>Clique em Atribuir. | A mensagem do sistema mostra Os grupos foram atribuídos. |  |

### Etapas preliminares para substituição de depósito

#### Criar motivo para substituição de depósito (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de motivo para a substituição/exclusão de depósito. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar motivos da substituição - Unidades gerenciais(F5313). | A tela Administrar motivos de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar motivos de substituição – Unidades gerenciais, clique em Criar. | A tela Motivo é exibida. |  |
| 4 | Inserir um motivo | Na seção Cabeçalho, efetue a entrada a seguir.Tipo de localização: <depósito>Motivo: <insira o novo código do motivo para substituição do depósito, por exemplo, NEW_SLOC> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Motivo criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Descrição do motivo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o motivo, por exemplo, EN inglês>Descrição do motivo: <insira texto para descrever o motivo, por exemplo, Novo depósito disponível> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição criada. |  |

#### Criar grupo para substituição de depósito (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de grupos para substituição/exclusão de depósitos. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar grupos de substituição - Unidades gerenciais(F5311). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar controles de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar grupos de substituição – Criar unidades gerenciais é exibida. |  |
| 4 | Inserir grupo | Efetue as seguintes entradas na seção Cabeçalho:Categoria da unidade gerencial: <depósito>Grupo: <insira o novo grupo de substituição, por exemplo, COLD_STORAGE> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Grupo criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição do grupo é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o grupo, por exemplo, EN inglês>Descrição do grupo: <insira texto para descrever o grupo, por exemplo, Depósito para itens de armazenamento frio> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição do grupo criada. |  |
| 9 | Selecionar Voltar | Na seção Título, clique em < (Voltar). | A tela Administrar grupos de substituição – Unidades gerenciais é exibida. |  |
| 10 | Ativar dados do grupo | Clique em Definir como ativo. | A mensagem do sistema mostra que O status foi modificado. |  |

#### Criar controle para substituição de depósito (opcional)

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de controle para controles de substituição/exclusão de depósito. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar controles de substituição - Unidades gerenciais(F5312). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na tela Administrar controles de substituição – Unidades gerenciais, clique em Criar. | A tela Administrar controles de substituição – Criar unidades gerenciais é exibida. |  |
| 4 | Inserir controle | Efetue a seguinte entrada na seção Cabeçalho:Categoria da unidade gerencial: <depósito>Controle: <insira o novo controle para substituição, por exemplo, STORAGE_TYPE> |  |  |
| 5 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Controle criado. |  |
| 6 | Clicar em Criar | Na seção Descrição, clique em Criar. | A tela Criar descrição de controle é exibida. |  |
| 7 | Inserir dados de descrição | Na seção Descrição, efetue as seguintes entradas:Código de idioma: <insira o idioma aplicável para o controle, por exemplo, EN inglês>Descrição do controle: <insira o texto para descrever o controle, por exemplo, para categoria da unidade gerencial> |  |  |
| 8 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Descrição de controle criada. |  |
| 9 | Selecionar Voltar | Na seção Título, selecione < (Voltar). | A tela Administrar controles de substituição – Unidades gerenciais é exibida. |  |
| 10 | Grupos atribuídos | Na seção Grupos atribuídos, clique em Atribuir. | A tela Atribuir grupos ao controle é exibida. |  |
| 11 | Seleciona grupo | Na caixa de diálogo Atribuir grupos ao controle, pesquise e clique em Grupo.Por exemplo, clique em Grupo<COLD_STORAGE>Clique em Atribuir. | A mensagem do sistema mostra Os grupos foram atribuídos. |  |

## Tabela de síntese

Este item de escopo é composto pelo processo de segmentos fornecido na tabela abaixo.

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Segmento | Função empresarial | App/Transação | Resultados previstos |
| --- | --- | --- | --- |
| [Criar substituição de centro](#unique_14) [página ] 14 | Administrador de cumprimento de ordens | Administrar substituições - Unidades gerenciais(F5314) | O registro de substituição de centro é criado. |
| [Criar exclusão de centro](#unique_15) [página ] 15 | Administrador de cumprimento de ordens | Administrar exclusões - Unidades gerenciais(F5315) | O registro de exclusão de centro é criado. |
| [Criar substituição de depósito](#unique_16) [página ] 17 | Administrador de cumprimento de ordens | Administrar substituições - Unidades gerenciais(F5314) | O registro de substituição de depósito é criado. |
| [Criar exclusão de depósito](#unique_17) [página ] 18 | Administrador de cumprimento de ordens | Administrar exclusões - Unidades gerenciais(F5315) | O registro de exclusão de depósito é criado. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Substituição de centro

#### Criar substituição de centro

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para criar substituição de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar substituições - Unidades gerenciais(F5314). | A tela Administrar substituições – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na visão Administrar substituições – Unidades gerenciais, na seção Centro, clique em Criar. | O layout de coluna flexível Administrar substituições – Unidades gerenciais é exibido com a tela Criar. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Centro: <insira o centro que exige um substituto>Centro substituto: <insira o substituto>Organização de vendas: <número da organização de vendas>Canal de distribuição: <número do canal de distribuição>Os dados do centro e do centro substituto são obrigatórios para criar uma substituição. |  |  |
| 5 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <insira o motivo para a criação do substituto. por exemplo, NEW_PLANT>Grupo: <insira o grupo de substituição. por exemplo, SOUTH_REGION>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 6 | Criar dados | Clique em Criar. | A mensagem do sistema exibe Substituição criada. |  |
| 7 | Ativar dados de substituição de centro | Clique em Definir como ativo. | A mensagem do sistema exibe Status alterado. |  |
| 8 | Exibir gráfico | Clique em Visualizar gráfico | A tela Exibir gráfico de rede de centros é exibida. |  |

#### Criar exclusão de centro

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação da exclusão de centro. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar exclusões - Unidades gerenciais(F5315). | A tela Administrar exclusões – Unidades gerenciais é exibida. |  |
| 3 | Clicar em Criar | Na visão Administrar exclusões – Unidades gerenciais (centro), clique em Criar. | A tela Exclusão de centro é exibida. |  |
| 4 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Centro: <insira o centro que deve ser excluído da substituição>Organização de vendas: <número da organização de vendas>Canal de distribuição: <número do canal de distribuição>O centro é obrigatório para criar uma exclusão. |  |  |
| 5 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <Insira o motivo da exclusão do centro>Grupo: <insira o grupo aplicável para exclusão do centro>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 6 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Exclusão criada. |  |
| 7 | Ativar dados de exclusão de centro | Clique em Definir como ativo. | A mensagem do sistema exibe Status alterado. |  |

### Substituição de depósito

#### Criar substituição de depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação da substituição de depósito. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar substituições - Unidades gerenciais(F5314). | A tela Administrar substituições – Unidades gerenciais é exibida. |  |
| 3 | Selecionar depósito | Na tela Administrar substituições – Unidades gerenciais, clique em Depósito. | A tela Administrar substituições – Unidades gerenciais (Depósito) é exibida. |  |
| 4 | Clicar em Criar | Na guia Depósito, clique em Criar. | O layout de coluna flexível Administrar substituições – Unidades gerenciais é exibido com a tela Criar. |  |
| 5 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Centro: <número do centro>Depósito: <insira o depósito que exige um substituto>Depósito substituto: <insira o substituto>Dados do centro e do depósito substituto são obrigatórios para criar uma substituição, enquanto o depósito é opcional. O centro é selecionado por padrão quando Depósito é selecionado. |  |  |
| 6 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <insira o motivo para a criação do substituto. por exemplo, NEW_SLOC>Grupo: <insira o grupo de substituição. por exemplo, COLD_STORAGE>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 7 | Criar dados | Clique em Criar. | A mensagem do sistema exibe Substituição criada. |  |
| 8 | Ativar dados de substituição de depósito | Clique em Definir como ativo. | A mensagem do sistema exibe Status alterado. |  |
| 9 | Exibir gráfico | Clique em Visualizar gráfico. | A tela Exibir gráfico de rede de depósito é exibida. |  |

#### Criar exclusão de depósito

Administração de teste

Projeto de cliente: Preencha as partes específicas do projeto.

|  |  |  |  |
| --- | --- | --- | --- |
| ID do caso de teste | <X.XX> | Data de testes: |  |
| Nome do executante de teste: |  | Duração: |  |
| Funções empresariais: |  | Responsabilidade: | <Confirme o provedor de serviços, cliente ou fornecedor de serviço comum e cliente> |

Objetivo

O procedimento a seguir fornece instruções para a criação de exclusão de depósito. Os apps disponíveis dependem de sua função atribuída.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Administrador de cumprimento de ordens. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Administrar exclusões - Unidades gerenciais(F5315). | A tela Administrar exclusões – Unidades gerenciais é exibida. |  |
| 3 | Selecionar depósito | Na visão Administrar exclusões – Unidades gerenciais, clique em Depósito. | A tela Administrar exclusões – Unidades gerenciais (Depósito) é exibida. |  |
| 4 | Clicar em Criar | Na visão Administrar exclusões – Unidades gerenciais (Depósito), clique em Criar. | A tela Administrar exclusões – Criar unidades gerenciais é exibida. |  |
| 5 | Inserir dados de cabeçalho | Efetue as seguintes entradas na seção Cabeçalho:Centro: <número do centro>Depósito: <insira o depósito que deve ser excluído da substituição>O centro e o depósito são obrigatórios para exclusão. |  |  |
| 6 | Inserir dados de informações gerais | Na seção Informações gerais, efetue as seguintes entradas:Motivo: <insira o motivo de exclusão do depósito>Grupo: <insira o grupo aplicável à exclusão do depósito>Válido desde: <insira a data e hora de início da validade>Válido até: <insira a data e a hora do fim da validade>Fuso horário: <insira o fuso horário aplicável à validade>As entradas acima são opcionais. |  |  |
| 7 | Criar dados | Clique em Criar. | A mensagem do sistema mostra Exclusão criada. |  |
| 8 | Ativar dados de exclusão de depósito | Clique em Definir como ativo. | A mensagem do sistema exibe Status alterado. |  |

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
- related-to :: [[08-sales-order-management/lokationsersetzung-und-ausschluss-anlegen-sds-5ng-472]]
- related-to :: [[08-sales-order-management/master-data-script-create-location-substitution-and-exclusion-mds-5ng]]
- related-to :: [[08-sales-order-management/mds-5ng-475]]
- related-to :: [[08-sales-order-management/mds-5ng-477]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/5NG_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 32,595 chars in the whole document
