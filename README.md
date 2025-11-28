# AI 翻译服务系统

## 项目简介

AI 翻译服务系统是一个基于人工智能技术的多语言翻译工具。该系统能够将文本自动翻译成指定的目标语言，提供高质量、符合目标语言习惯的翻译结果。系统同时支持命令行交互和 RESTful API 两种使用方式，方便灵活集成到各种应用场景中。

## 功能特点

- **智能翻译**：基于先进的 AI 模型，提供高质量的翻译服务
- **多语言支持**：支持多种语言之间的互译
- **双模式运行**：提供命令行版本和 API 服务两种使用方式
- **RESTful API**：提供标准的 API 接口，便于集成到其他系统
- **CORS 支持**：支持跨域访问，方便前端应用调用
- **Docker 部署**：提供 Docker 和 Docker Compose 配置，简化部署流程
- **健康检查**：内置健康检查接口，便于监控服务状态

## 项目结构

```
.
├── api.py                  # FastAPI后端服务
├── translator.py           # 翻译核心逻辑（含命令行版本）
├── config/                 # 配置文件目录
│   └── translate_prompt.md # AI提示词模板
├── requirements.txt        # Python依赖包列表
├── Dockerfile              # Docker镜像构建文件
└── docker-compose.yml      # Docker Compose配置
```

## 环境要求

- Python 3.12+
- OpenAI API 兼容接口及密钥

## 安装步骤

1. 克隆项目代码：
   ```bash
   git clone https://github.com/zhiheng-yu/translator
   cd translator
   ```

2. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置API密钥：
   系统会自动从环境变量中读取API密钥和基础URL，请确保设置以下环境变量：
   ```bash
   export OPENAI_API_KEY="your-api-key"
   export OPENAI_BASE_URL="your-openai-api-compatible-url"  # 可选，默认为 https://api.openai.com/v1
   export OPENAI_MODEL="gpt-4o-mini"  # 可选，默认为 gpt-4o-mini
   ```

## 使用方法

### 命令行版本

直接运行翻译器进行交互式翻译：

```bash
python translator.py
```

然后按提示输入目标语言和需要翻译的文本。

### 启动 API 服务

```bash
python api.py
```

默认监听端口为 6003。

### Docker 部署

使用 Docker Compose 快速启动服务：

```bash
# 创建 .env 文件并配置环境变量
cp .env.example .env

# 构建镜像
docker build -t translator .

# 启动服务
docker-compose up -d
```

### API 接口说明

[翻译助手接口文档-Apifox](https://s.apifox.cn/a2dfbdce-fafc-4e7f-9ad0-c9e3efa6f56d)

## 配置说明

### AI 提示词模板 (`config/translate_prompt.md`)

定义了 AI 翻译代理的角色和行为规则。模板中的 `{{dst_lang}}` 占位符会在运行时被替换为实际的目标语言。

## 技术栈

- **Agno**: AI Agent 开发框架，用于构建智能代理
- **FastAPI**: 现代化的 Python Web 框架，提供高性能的 API 服务
- **OpenAI SDK**: 用于调用 OpenAI 兼容的 AI 模型 API
- **Uvicorn**: 轻量级 ASGI 服务器
- **Docker**: 容器化部署方案

## 注意事项

1. 请确保 API 密钥和基础 URL 配置正确
2. 默认使用 `gpt-4o-mini` 模型，可通过环境变量 `OPENAI_MODEL` 自定义
3. 在生产环境中，建议限制 CORS 允许的具体域名
4. 翻译质量取决于所使用的 AI 模型
5. 长文本翻译可能需要较长处理时间
