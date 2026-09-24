# GPMH · design para pessoas e IAs

**Pacote 1.1.0-rc1 · design system 1.3.0-rc1 · 24/09/2026 · em revisão.**

Uma base de design compartilhada para posts, carrosséis, apresentações, impressos, landing pages, sites e movimento. Reúne identidade, concepção de imagem, hierarquia, execução e revisão sem depender do histórico de uma conversa.

## Baixar tudo

**[Baixar o pacote completo — GPMH-DESIGN-CLIENTE.zip](https://github.com/luisbezerragrowth/design-gpmh/releases/download/v1.1.0-rc1/GPMH-DESIGN-CLIENTE.zip)**

Esse é o download para a equipe: manual HTML, fontes, logos, grafismos, referências, modelos, módulos e instruções para as IAs. Extraia o ZIP e comece pelo README. As fontes e condições dos ativos estão documentadas no pacote.

Para importar somente a skill: **[GPMH-DESIGN-SKILL-COMPLETA.zip](https://github.com/luisbezerragrowth/design-gpmh/releases/download/v1.1.0-rc1/GPMH-DESIGN-SKILL-COMPLETA.zip)**.

Os downloads ficam na [release 1.1.0-rc1](https://github.com/luisbezerragrowth/design-gpmh/releases/tag/v1.1.0-rc1), com acesso público, sem login ou convite. O botão “Code → Download ZIP” do GitHub baixa o código-fonte sem o kit; para receber tudo, use o link **pacote completo** acima. Acesso público não concede licença de uso ou redistribuição dos ativos.

## Começar

| Quem vai usar | Entrada |
|---|---|
| Cliente / direção | `MANUAL-GPMH.html`, incluído no pacote cliente |
| Designer | `GPMH-DESIGN-SYSTEM-KIT.zip`, incluído no pacote cliente |
| IA com acesso à pasta | [LEIA-PRIMEIRO-IA.md](LEIA-PRIMEIRO-IA.md) |
| IA por anexo / chat | [GPMH-IA-UNIVERSAL.md](GPMH-IA-UNIVERSAL.md) + ativos pertinentes |
| Instruções persistentes do projeto | [INSTRUCOES-PROJETO.md](INSTRUCOES-PROJETO.md) |
| Instalação por ferramenta | [COMPATIBILIDADE.md](COMPATIBILIDADE.md) |

Cursor, Codex e Claude Code têm adaptadores que apontam para a mesma pasta `gpmh-design/`. Lovable, Manus e outras IAs podem consumir o documento único. O pacote não presume que anexar um ZIP fará a ferramenta ler todos os arquivos: confira a leitura e os ativos antes de produzir.

## Pedido de início

```text
Use a base GPMH deste projeto. Leia LEIA-PRIMEIRO-IA.md e as referências pertinentes; se só tiver anexos, leia GPMH-IA-UNIVERSAL.md. Confirme brevemente a versão lida e os ativos disponíveis. Depois crie [formato] para [objetivo/público], usando [copy e CTA]. Preserve a identidade, proponha uma ideia visual específica e revise o resultado renderizado. Não invente os dados ou arquivos que faltarem.
```

Em Claude Code, também pode usar `/gpmh-design`. Em Codex, selecionar `gpmh-design` no menu de skills disponível na interface. As instruções de projeto funcionam mesmo sem invocação por menu, desde que carregadas pelo ambiente.

## Estrutura

```text
LEIA-PRIMEIRO-IA.md        entrada comum
GPMH-IA-UNIVERSAL.md      documento gerado, pronto para anexo
INSTRUCOES-PROJETO.md     resumo para conhecimento do projeto
AGENTS.md / CLAUDE.md     entradas de projeto
.cursor/rules/           adaptador Cursor
.agents/skills/          adaptador Codex
.claude/skills/           adaptador Claude Code
gpmh-design/             única fonte de regras, tokens e recursos
  SKILL.md
  references/
  assets/brand-kit/      kit incluído nos pacotes completos da release
tools/                   anexação e geração dos pacotes
qa/                      verificação reproduzível e resultados locais
```

## Crivo de design

“Não parecer IA” aqui significa decisões específicas, composição bem acabada e revisão: PP Neue Corp, Cerise correto, margens reais, escala consistente, rostos livres, logos íntegros e metáforas relacionadas à mensagem. Nada de serifa, microeyebrow, tracking exagerado, texto essencial minúsculo ou cards por hábito. Consulte o [crivo](gpmh-design/references/crivo-de-design.md).

A IA deve distinguir referência de aprovação e fato de suposição. O processo exige inspeção; um arquivo de regras não garante qualidade sozinho nem impede todo erro.

## Distribuir

- **GPMH-DESIGN-CLIENTE.zip:** manual, kit, núcleo completo e todos os adaptadores, na mesma raiz após extrair.
- **GPMH-DESIGN-SKILL-COMPLETA.zip:** pasta portátil `gpmh-design/` com SKILL.md, referências e ativos; útil para importação de skill.
- **GPMH-DESIGN-SKILL-GITHUB.zip:** código-fonte do repositório, sem kit comercial e sem fontes. Repositório: `design-gpmh`.

Fonte compartilhada: [luisbezerragrowth/design-gpmh](https://github.com/luisbezerragrowth/design-gpmh), com acesso público por solicitação de Luis em 24/09/2026. Nenhum envio ao cliente foi realizado. Guia de passagem: [ENTREGA-CLIENTE.md](ENTREGA-CLIENTE.md). Condições dos ativos: [DISTRIBUICAO.md](DISTRIBUICAO.md).

## Abrir o repositório

O clone para leitura não exige conta no GitHub:

```sh
git clone https://github.com/luisbezerragrowth/design-gpmh.git
cd design-gpmh
```

Abra essa pasta no editor e siga [COMPATIBILIDADE.md](COMPATIBILIDADE.md). As regras, tokens e módulos estão versionados. Quem clonar a fonte pode baixar o pacote completo na release e anexar o kit de produção à sua cópia, conforme abaixo.

## Anexar o kit ao clone

Dentro do pacote completo baixado na release está `GPMH-DESIGN-SYSTEM-KIT.zip`. Na raiz do clone, execute com Python 3:

```sh
python3 tools/attach_brand_kit.py /caminho/para/GPMH-DESIGN-SYSTEM-KIT.zip
```

O script confere versão e estrutura e grava em `gpmh-design/assets/brand-kit/`, ignorado pelo Git. Recusa sobrescrita. Preserve a versão anterior antes de atualizar. A existência dos arquivos não concede licença de fonte.

## Manter uma única versão

Edite a fonte `gpmh-design/`, não o documento agregado. Depois execute:

```sh
python3 tools/build_context.py
python3 qa/check_distribution.py
```

O verificador usa Python 3 e Ruby/Psych para validar YAML. O uso da skill e a leitura dos arquivos não exigem esses runtimes. Os relatórios distinguem estrutura validada de execução em cada produto. A documentação oficial dos adaptadores e os limites dos testes estão em [COMPATIBILIDADE.md](COMPATIBILIDADE.md).

Para gerar os ZIPs: `python3 tools/build_handoff.py --manual /caminho/MANUAL.html --kit /caminho/KIT.zip --out /pasta/de/entrega`. O gerador atualiza também o arquivo único. Não executa upload.

Mudanças de regra devem registrar status e versão. A consolidação continua em revisão; promoção a referência oficial exige decisão explícita. Não usar este repositório de instruções como site de apresentação.
