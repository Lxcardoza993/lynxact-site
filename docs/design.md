# LynxAct 官网设计文档

> 2026-08-05 · 目的：Microsoft for Startups 申请的企业身份门面（也服务 GOAI 等外部审核场景）

## 定位

以 **LynxAct 体育 AI 视频分析**为申请主体（用户拍板 2026-08-05）——真实资产最强：lynxact-coach / lynxmove-oss 公开仓、GOAI 参赛背书、创始人爱丁堡体育硕士背景。

## 决策记录

| 决策 | 结论 | 理由 |
|------|------|------|
| 域名 | act.lynxflow.co | 裸域被 ailynx 工具集占用；qzz.io 免费域名审核可信度低；不买新域名 |
| 部署 | CF Pages 项目 lynxact-site，wrangler 直接部署 | 用户 wrangler 工作流成熟；Git 集成可后补 |
| GitHub 门面 | 组织 github.com/lynxact（名字可用） | 公司气质；转移后旧 URL 自动 301 |
| 内容原则 | 零造假 | 全部数据来自真实 spike（98.7% Stanford40、0.62–1.25m 标定、62 技术卡、95.7% 帧≥8人） |

## 结构

- `index.html` 单页长滚动：Hero / Products(3层) / Technology(数据带+pipeline) / Demo / Open Source / Company / Footer
- `privacy.html` 独立隐私政策页
- `_headers` 安全头（HSTS+CSP+XFO+nosniff+Referrer/Permissions-Policy）
- 深色球场主题：#0b0f0e 底 + #00e676 荧光绿 + SVG 球场线条背景；Inter/JetBrains Mono

## 已知待办

- 组织建好后：转移 lynxact-coach/lynxmove-oss/lynxact-site → 官网 GitHub 链接升级为组织 URL 重新部署
- Email Routing founder@lynxflow.co → Gmail：CF token 无 Email Routing 写权限，需 dashboard 手动
- GOAI 提交材料（8/16 前）里的仓库链接在转移后需更新为新 URL
