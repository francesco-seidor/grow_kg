---
id: 14-maintenance-service-and-projects/script-de-dados-mestre-criar-dados-mestre-de-manutencao-de-centro-para
title: "Script de dados mestre: Criar dados mestre de manutenção de centro para serviço - MDS (3U3) (3U3_S4CLD2608_Master_Data_PT_XX)"
description: Portuguese (machine-translated) master data script 3U3 for creating functional location and equipment master data for service in S/4HANA Cloud Public Edition.
cluster: 14-maintenance-service-and-projects
tags: [kb/maintenance-service-and-projects, topic/service-technical-objects-and-boms]
aliases: [3U3_S4CLD2608_Master_Data_PT_XX]
keywords: [Technical Objects and BOMs for Service, functional location, equipment master data, master data scripts, technical objects, warranty, maintenance planner role, service orders, 3U3]
sources: [raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_PT_XX.docx]
confidence: high
status: active
kind: verbatim
doc_id: sap-best-practices-for-sap-s4hana-cloud-public-edition-2608-374
topic: 14-maintenance-service-and-projects/service-technical-objects-and-boms
language: PT
part: 1/1
created: 2026-10-12
updated: 2026-10-12
---

# Script de dados mestre: Criar dados mestre de manutenção de centro para serviço - MDS (3U3) (3U3_S4CLD2608_Master_Data_PT_XX)

*Verbatim text of `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_PT_XX.docx`, extracted with `mammoth`. Grouped under **Technical Objects and BOMs for Service** in Maintenance, Service and Projects. Nothing below the rule has been rewritten; headings are shifted one level down.*

---

|  |  |
| --- | --- |
| <!-- image omitted: unnamed --> | Script de dados mestreSAP S/4HANA Cloud Public Edition - 02-07-26 |
|  | Criar dados mestre de manutenção de centro para serviço – MDS (3U3) **<!-- image omitted: SAP Logo -->** |
|  | PUBLIC |

Índice

[1 Objetivo 2](#_Toc233893701)

[2 Pré-requisitos 3](#_Toc233893702)

[2.1 Acesso ao sistema 3](#_Toc233893703)

[2.2 Funções 3](#_Toc233893704)

[3 Procedimentos 4](#_Toc233893705)

[3.1 Criar dados mestre de local de instalação 4](#_Toc233893706)

[3.2 Criar dados mestre de equipamento 5](#_Toc233893707)

## Objetivo

Neste documento, você encontra uma descrição sobre como criar um local de instalação e registros de dados mestre de equipamento para seu sistema SAP S/4HANA. A descrição inclui os segmentos de dados que são relevantes para os dados mestre para trabalhar em um ambiente de sistema "normal". O leitor aprende principalmente que campos e segmentos de dados precisam ser normalmente preenchidos com valores de entrada. Os campos que não são relevantes para o escopo do fornecimento de conteúdo do S/4HANA, por SAP Best Practices, não são descritos neste documento, apesar de eles poderem aparecer na IU.

O local de instalação e os registros mestre de equipamento que são criados como descrito aqui podem ser utilizados em ordens de serviço, confirmações de serviço e contrato de prestação de serviços.

## Pré-requisitos

### Acesso ao sistema

| Sistema | Detalhes |
| --- | --- |
| Sistema | Acessível via launchpad do SAP Fiori. O administrador do sistema fornece o URL para acessar os diversos apps atribuídos à sua função. |

### Funções

Criar funções empresariais usando os seguintes modelos de função empresarial fornecidos pela SAP e atribuir os mesmos aos usuários de teste individuais.

Como alternativa, se disponível, você pode usar as seguintes áreas fornecidas pela SAP. Você cria um espaço com páginas contendo apps predefinidos essenciais e o atribui à função empresarial. Em seguida, você atribui essa função empresarial a seus usuários individuais.

Para mais informações, consulte Como criar uma função empresarial a partir de um modelo na [assistência do produto](https://help.sap.com/docs/SAP_S4HANA_CLOUD/53e36b5493804bcdb3f6f14de8b487dd/ec310a8b669a45ca898dc4dd91d97de2.html) para SAP S/4HANA Cloud Public Edition.

| Nome (modelo de função) | ID (modelo de função) | Nome (área do launchpad) | ID (área do launchpad) |
| --- | --- | --- | --- |
| Planejador de manutenção | SAP_BR_MAINTENANCE_PLANNER | Planejamento de manutenção | SAP_BR_MAINTENANCE_PLANNER |

## Procedimentos

### Criar dados mestre de local de instalação

Objetivo

Nesta etapa de teste, você atualiza uma estrutura do local de instalação que consiste em um nível mais alto do local de instalação e dois locais de instalação subordinados.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no Launchpad do SAP Fiori como Planejador de manutenção. |  |  |
| 2 | Abrir o app | Na seção Objeto técnico, selecione o bloco Criar objeto técnico. |  |  |
| 3 | Criar local de instalação | Na tela Criar objeto técnico, selecione o Tipo de objeto técnico: Local de instalação.Na próxima tela, atualize as seguintes entradas:Tipo de objeto técnico: Local de instalaçãoCódigo de estrutura: YBPM (código de estrutura para melhor prática)Objeto técnico: <insira um identificador, por exemplo> ZZ01Categoria de objeto técnico: S (unidade gerencial do cliente)Selecione Continuar. |  |  |
| 4 | Atualizar dados gerais | Na tela Criar objeto técnico: ZZ01, na seção Dados gerais, atualize as seguintes entradas:Descrição: <por exemplo, Edifício A>Opcionalmente, atualize outros dados gerais, em seguida, navegue para a seção Dados da unidade gerencial. |  |  |
| 5 | Atualizar dados da unidade gerencial | Na seção Dados da unidade gerencial, atualize as seguintes entradas:Centro de manutenção: <atualize um centro relevante, por exemplo, 1710 para EUA>Nota os objetos técnicos que pertencem à mesma estrutura devem ter o mesmo centro atribuído. Como alternativa, você pode deixar a informação sobre o centro em branco para todos os objetos técnicos.Opcionalmente, atualize outros detalhes, tais como informações de endereço. |  |  |
| 6 | Salvar local de instalação | Opcionalmente, você pode atualizar informações adicionais como, por exemplo, informações do parceiro, etc., na seção Dados organizacionais.Clique em Salvar.Em seguida, navegue de volta para a tela Página inicial. |  |  |
| 7 | Criar local de instalação subordinado | Para atualizar uma estrutura do local de instalação, proceda como descrito nas etapas acima e atualize os seguintes locais de instalação:Objeto técnico: ZZ01-001Descrição: 1º pavimentoObjeto técnico: ZZ01-002Descrição: 2º pavimento |  |  |
| 8 | Revisar objeto técnico no Asset Viewer | Na Página inicial, selecione o bloco Exibir objeto técnico.Na tela Exibir objeto técnico, atualize o Objeto técnico relevante, por exemplo, ZZ01, em seguida, selecione Continuar.Para revisar a estrutura do local de instalação e os detalhes por objeto técnico, selecione Você também pode: Exibir objeto técnico no Asset Viewer. |  |  |

### Criar dados mestre de equipamento

Objetivo

Nesta etapa de teste, você atualiza um registro para um equipamento que está montado em um local de instalação.

Procedimento

| Nº da etapa de teste | Nome da etapa de teste | Instrução | Resultado esperado | Comentários |
| --- | --- | --- | --- | --- |
| 1 | Efetuar login | Efetue login no launchpad do SAP Fiori como Planejador de manutenção. |  |  |
| 2 | Abrir o app | Abrir Criar objeto técnico. |  |  |
| 3 | Criar equipamento | Na tela Criar objeto técnico, selecione o Tipo de objeto técnico: Equipamento.Na próxima tela, atualize as seguintes entradas:Tipo de objeto técnico: EquipamentoObjeto técnico: <vazio>Válido desde: <data de hoje>Categoria de objeto técnico: S (equipamento do cliente)Clique em Continuar. |  |  |
| 4 | Atualizar dados gerais | Na tela Criar objeto técnico: <ID do equipamento>, na seção Dados gerais, atualize as seguintes entradas:Descrição: <por exemplo, Impressora A1>(Opcional) Garantia do cliente: Início/fim da garantia(Opcional) Garantia do fornecedor: Início/fim da garantiaNota O processo de conserto em oficina (item de escopo 3XK) suporta e integra garantias baseadas em datas (período de garantia). No conserto em oficina, você pode utilizar os tipos de garantia do cliente e do fornecedor.Você precisa inserir a data de início e a data do fim da garantia nos dados mestre do equipamento. Se você tiver inserido a data do fim para a garantia do cliente e/ou do fornecedor de um equipamento, o sistema verifica se a data do fim da garantia é anterior à data de criação do conserto em oficina.Um ícone indica se a data de criação do conserto em oficina está dentro do período de garantia.Opcionalmente, atualize outros dados gerais como informações do fabricante, número do modelo, etc., em seguida, navegue para a seção Dados da unidade gerencial. |  |  |
| 5 | Atribuir material e número de série | Clique em Funções adicionais > Mostrar dados de número de série:Efetue as seguintes entradas e pressione Enter:Material: TG20 |  |  |
| 6 | Atualizar dados da unidade gerencial | Na seção Dados da unidade gerencial, atualize as seguintes entradas:Centro de manutenção: <atualize um centro relevante, por exemplo, 1710 para EUA>Nota os objetos técnicos que pertencem à mesma estrutura devem ter o mesmo centro atribuído. Como alternativa, você pode deixar a informação sobre o centro em branco para todos os objetos técnicos.Opcionalmente, atualize outros detalhes, tais como informações de endereço ou de sala. |  |  |
| 7 | Salvar equipamento | Opcionalmente, você pode atualizar informações adicionais, como informações do parceiro etc., na seção Dados organizacionais.Clique em Salvar. |  |  |
| 8 | Montar equipamento no local de instalação | Na tela Modificar objeto técnico: <ID do equipamento>, navegue para a seção Estrutura.Selecione Modificar estrutura: Montar.Na caixa de diálogo Modificar local de montagem, atualize as seguintes entradas:Objeto técnico superior: ZZ01-001Posição: <deixar em branco>Data/hora de montagem: <mantenha a proposta do sistema>Clique em OK.Clique em Salvar. |  |  |

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
- related-to :: [[14-maintenance-service-and-projects/instandhaltungs-stammdaten-fur-service-anlegen-sds-3u3-370]]
- related-to :: [[14-maintenance-service-and-projects/master-data-script-create-plant-maintenance-master-data-for-service-md]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-373]]
- related-to :: [[14-maintenance-service-and-projects/mds-3u3-375]]

## Sources
- `raw_assets/SAP_Best_Practices_for_SAP_S4HANA_Cloud_Public_Edition_2608_AE_SAPCUSTOMER (1)/S4C/Library/Others/2608_Master_Data_Scripts/3U3_S4CLD2608_Master_Data_PT_XX.docx` — full document · extracted with `mammoth` · 10,949 chars in the whole document
