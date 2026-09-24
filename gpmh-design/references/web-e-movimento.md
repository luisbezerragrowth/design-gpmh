# Web e movimento

## Layout

Aplicar os [tokens](../assets/design-tokens.json). Container compartilhado 76 rem; gutter clamp(1.25rem,4vw,4rem). Logo do header, hero e footer usam a mesma referência de alinhamento. Largura e altura se adaptam ao conteúdo; rem/clamp/grid/flex, sem impedir zoom. Pixel fixo é aceitável para pequenos detalhes gráficos, não como sistema de tamanho da página inteira.

PP Neue Corp 500 corrente e 750 em ênfase. Corpo de 18–20 px equivalentes, apoio de 16–18; H1 geral de 40–80 e H2 36–64 na raiz de 16 px, com escala fluida. Não aplicar fontes enormes a todo apoio. Para uma campanha de download, uma LP curta pode ter 3 seções se o briefing pedir: mensagem/prova, valor do material e captura. Em outros objetivos, escolher as seções pela oferta real e pelo CTA solicitado; não inventar um material para preencher a estrutura.

Big numbers devem ser identificáveis logo de cara quando forem a prova central, com unidade e significado corretos. Logos editoriais identificam a publicação; não inventar parceria. CTA conduz ao formulário/produto real. No benchmark, Typebot é a integração escolhida, mas IDs/host pertencem ao briefing de cada campanha; não duplicar uma captura de produção para qualquer página.

Componha alternância orientada ao conteúdo. Centralizar blocos pode criar unidade sem alinhar tudo ao mesmo eixo. Preserve texto, foco e alvos de toque. Formulário com rótulos, estados e retorno compreensível.

## Vocabulário e uso dos efeitos

| Efeito | Função | Condição de qualidade |
|---|---|---|
| Vídeo ambiente em loop | Vento, folhas, nuvens plausíveis | Playsinline, muted, poster; sem salto visível na emenda |
| Parallax | Profundidade entre planos | Amplitude comedida; não cobrir leitura; desligar quando reduzido |
| Transformação por rolagem (scroll-driven morph) | Relacionar ideias enquanto o texto muda | Sequência contínua e reversível; scroll nativo livre |
| Perspectiva/reação ao ponteiro | Dar volume e resposta | Não capturar toque necessário à navegação |
| Entrada de conteúdo (reveal) | Orientar chegada de uma seção | Texto disponível sem JavaScript; sem demora artificial para ler |
| Microinteração | Mostrar hover, foco, clique e estado | Também operar por toque e teclado |
| Rede ambiente discreta | Continuar uma narrativa visual | Opacidade baixa, abaixo de conteúdo/fotos, sem claims científicos |

## Receita disponível: cérebro→lâmpada→cérebro→conexões

O motor, CSS, poster e licença também estão versionados em `assets/motion/`, sem fontes comerciais. Caminhos que começam por `assets/` nesta referência são relativos à raiz da skill. A página de demonstração e a integração completa vêm no kit.

No kit: `assets/brand-kit/modules/demo.html`, script WebGL e guia BRAIN-SCULPTURE. Ler a API antes de integrar, preservar licença HRA. Um único canvas decorativo acompanha 3 cenas em fluxo normal. Forma, posição, escala e expansão dependem da rolagem; textos não ficam presos. Desktop alterna lados; mobile protege a área de texto acima da forma.

Comportamentos verificados na integração 1.3 (escopo no relatório de QA do kit): entrada por hash sincronizada depois das fontes; snap ao retomar ou saltar muito; chegada vertical suave em telas curtas; layout idêntico com movimento ligado/desligado para não deslocar a leitura; rede sob conteúdo e fotografias. Não copiar só o efeito e descartar esses comportamentos.

Limites do módulo:18k/9k/6.5k partículas, rede 240/150/108 nós; teto 30 fps; DPR 1.75/1.5. São orçamentos, não promessa de desempenho universal. Pausar fora de uso/aba oculta; liberar recursos. Canvas sem capturar links/toque; reduzir movimento e respeitar economia de dados. WebGL ausente mantém poster e leitura.

Não tornar esse cérebro a abertura obrigatória de toda LP. O componente pode apoiar outra mensagem só quando existir relação; a criatividade inclui uma nova ideia visual.

## Verificação

Testar desktop, tablet, 320/390 px, horizontal, texto 200%, CTA/foco, scroll nos dois sentidos, entrada direta por link e modo sem movimento. Examinar imagens de pessoas em cada recorte. Rodar mais de um ciclo de vídeo. Informar quais motores/aparelhos foram de fato usados; viewport de iPhone não equivale a Safari/iPhone físico. Fazer render visual além de testes de código.
