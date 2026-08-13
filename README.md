# LynxAct — Official Website

Source code of [lynxact.lxlynx.com](https://lynxact.lxlynx.com), the official site of **LynxAct**, an AI-powered sports video intelligence product line built by **LynxFlow AI**.

## What is LynxAct?

LynxAct turns match footage into tactical insight:

- **Tactical Annotation** — VLM-assisted pre-annotation with human expert review
- **AI Coach Agent** — LLM agent producing natural-language tactical reports ([lynxact-coach](https://github.com/Lxcardoza993/lynxact-coach))
- **Player Tracking** — open pipeline extracting 2D pitch coordinates from broadcast footage ([lynxmove-oss](https://github.com/Lxcardoza993/lynxmove-oss))

## Stack

Pure static HTML/CSS/JS — no build step. Deployed on Cloudflare Pages.

```
index.html      # single-page site
privacy.html    # privacy policy
css/style.css   # dark pitch theme
js/main.js      # nav state + scroll reveal
assets/         # demo media
```

## Local preview

```bash
python3 -m http.server 8917
# open http://localhost:8917
```

## Deploy

```bash
npx wrangler pages deploy . --project-name=lynxact-site
```

---

## 中文简介

本仓库是 LynxAct 官网（lynxact.lxlynx.com）的源码。LynxAct 是 LynxFlow AI 旗下的体育视频智能分析产品线：技战术标注、AI 教练 Agent、球员追踪。纯静态站，Cloudflare Pages 部署。

## License

Website content © 2026 LynxFlow AI. Code is MIT-licensed — see [LICENSE](LICENSE).
