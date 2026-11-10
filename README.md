# Bambu Casas · Site interativo (protótipo v1)

Abra `index.html` em um servidor web (GitHub Pages). Páginas por âncora:
#inicio · #como (Como consigo ter uma casa?) · #casas (Qual é a minha casa?) · #casa-ipe · #casa-jatoba

- `pano/`  panorâmicas 360° (6144×3072) — `thumb/` miniaturas do tour
- `img/` + `imgthumb/` imagens das galerias (book só de imagens)
- `inst/` institucional (equipe, obras reais, estrutura, logos) — PROVISÓRIOS, recortados dos slides antigos: trocar pelos originais com o mesmo nome
- `book/` PDFs completos dos books (botão "Baixar o book")
- `lib/` Pannellum 2.5.7 (MIT)
- `index.src.html` + `build_site.py` geram o `index.html` (ícones, QR codes e links de WhatsApp)

Planta no tour: posição dos pontos em HOUSES[...].scenes (x,y em % da planta).
