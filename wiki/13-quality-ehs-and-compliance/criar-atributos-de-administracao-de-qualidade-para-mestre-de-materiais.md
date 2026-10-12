---
id: 13-quality-ehs-and-compliance/criar-atributos-de-administracao-de-qualidade-para-mestre-de-materiais
title: Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS (BNY) (BNY_S4CLD2608_Master_Data_PT_XX)
description: "Portuguese SAP master data script BNY for creating quality management attributes in the material/product master (MM01), with test steps."
cluster: 13-quality-ehs-and-compliance
tags: [kb/quality-ehs-and-compliance, topic/qm-material-master-attributes]
aliases: [BNY_S4CLD2608_Master_Data_PT_XX]
keywords: [Quality Management View of the Material Master, quality management, material master, inspection types, automatic usage decision, plant data, master data scripts, BNY]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-692
topic: 13-quality-ehs-and-compliance/qm-material-master-attributes
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS (BNY) (BNY_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Quality Management View of the Material Master** in Quality, EHS and Compliance. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar atributos de administração de qualidade para mestre de materiais/produtos – MDS (BNY) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233894156)

[2 Pré-requisitos 3](#_Toc233894157)

[2.1 Acesso ao sistema 3](#_Toc233894158)

[2.2 Funções 3](#_Toc233894159)

[2.3 Unidades organizacionais necessárias 3](#_Toc233894160)

[3 Tabela de síntese 5](#_Toc233894161)

[4 Procedimentos de teste 6](#_Toc233894162)

[4.1 Atributos da administração de qualidade para material 6](#_Toc233894163)

## Objetivo

Se a qualidade do material deve ser controlada, o pré-requisito é que a visão da administração de qualidade no mestre de material seja atualizada para o respectivo centro.

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

### Unidades organizacionais necessárias

Nessa seção você descreve e explica todas as unidades organizacionais relevantes para a criação de registros de dados mestre.

Alguns segmentos dos dados mestre de cliente são dependentes das unidades organizacionais da empresa. Os dados gerais (centrais) não dependem de uma unidade organizacional ou da empresa. A seguinte tabela oferece uma síntese destes segmentos de dados diferentes e das respectivas unidades organizacionais relevantes:

| Segmento de dados | Depende de | Exemplos de campo | Comentários | Unidade organizacional a ser usada |
| --- | --- | --- | --- | --- |
| Administração de qualidade | Centro |  | Os dados do centro podem existir para cada ID do centro da sua estrutura empresarial para a qual é usado o registro mestre de cliente. | Centro: |

## Tabela de síntese

Este item de escopo é composto por várias etapas de processo listadas na seguinte tabela:

|  |
| --- |
| Nota Caso o administrador do sistema tenha ativado áreas e páginas no launchpad do SAP Fiori, a página inicial só conterá os apps essenciais para executar as tarefas típicas de uma função empresarial.Você pode encontrar todos os outros apps (pesquisáveis) não incluídos na página inicial usando a barra de pesquisa ([2434549](https://me.sap.com/notes/2434549)).Se você pretende personalizar a página inicial e incluir os apps ocultos, navegue para o seu perfil do usuário e clique em Buscador de apps. |

| Etapa de processo | Função empresarial | Transação / App | Resultados esperados |
| --- | --- | --- | --- |
| [Atributos da administração de qualidade para material](#unique_7) [página ] 6 | Especialista em dados mestre - Dados do produto | Criar material(MM01) | Dados mestre de materiais – Dados da administração de qualidade criados. |

## Procedimentos de teste

Esta seção descreve os procedimentos de teste para cada etapa de processo que pertence a este item de escopo.

### Atributos da administração de qualidade para material

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
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Especialista em dados mestre - Dados do produto. | O launchpad do SAP Fiori é exibido. |  |
| 2 | Acessar o app SAP Fiori | Abra Criar material(MM01). | O app é aberto. |  |
| 3 | Inserir dados do material | Na tela Criar material (1ª tela), efetue as seguintes entradas:Material: <número do material>Tipo de material: Produtos comercializáveisPressione Enter. | A tela Selecionar visões é exibida. |  |
| 4 | Selecionar a visão Administração de qualidade | Na tela Seleção de visões, selecione a visão Administração de qualidade e Níveis org. | Uma nova tela é exibida para entrada de dados organizacionais. |  |
| 5 | Inserir dados dos níveis organizacionais | Na tela Unidades organizacionais, na seção Níveis organizacionais, efetue a seguinte entrada e selecione Continuar:Centro: <código do centro> | A tela Criar material...(Produtos comercializáveis) é exibida. |  |
| 6 | Inserir dados da administração de qualidade | Na tela Criar material <XXX> (Produtos comercializáveis), guia Administração de qualidade, insira a descrição do material.Descr.: <inserir a descrição>Na seção Dados gerais, guia Administração de qualidade, efetue a seguinte entrada:Unidade de medida básica: <unidade de medida>:Selecione Config. Controle. Na caixa de diálogo exibida, clique em Criar tipos de controle e efetue as seguintes entradas:Tipo ctrl.: por exemplo, 01.Tipo de controle preferido: XAtivo: XSelecionar Det. tipo ctrl. para ver os detalhes.Verifique se os seguintes campos estão marcados com X:Lançar em estoque em controle de qualidadeControle com lista de tarefasAtribuição automáticaCtrl.caracts.Clique em Continuar. |  |  |
| 7 | Ativar/Desativar decisão de utilização automática (opcional) | Marque ou desmarque DU automática para ativar ou desativar a decisão de utilização automática para esta combinação de material e tipo de controle.Nota Uma decisão de utilização automática após o registro dos resultados pode ser efetuada para lotes de controle com resultados de controle positivos. Para ativar esse processo, seu sistema precisa estar configurado adequadamente no app Administrar sua solução(F1241). Verifique [SAP Help](https://help.sap.com/viewer/DRAFT/84dbf30eedb4450983dc3d1c81b71996/1811.500/en-US/746b66d98e504e238eca043bae05ecb8.html) para obter mais informações e pré-requisitos técnicos. |  |  |
| 8 | Inserir dados de suprimento (opcional) | Para opcionalmente usar um registro de informação de qualidade do material, efetue as entradas a seguir na guia Administração de qualidade, seção Dados de suprimento:QM – Suprimento ativo: XChave de controle QM: por exemplo, 0001. |  |  |
| 9 | Salvar os dados | Clique em Salvar. | Os dados estão salvos. |  |

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
- related-to :: [[13-quality-ehs-and-compliance/create-quality-management-attributes-for-material-product-master-mds-b]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-691]]
- related-to :: [[13-quality-ehs-and-compliance/mds-bny-693]]
- related-to :: [[13-quality-ehs-and-compliance/script-de-datos-maestros-crear-atributos-de-gestion-de-calidad-para-ma]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/BNY_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,159 chars in the whole document
