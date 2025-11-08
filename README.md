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
├── main.py                 # 命令行版本主程序
├── translate_agent.py      # AI代理核心逻辑
├── config/                 # 配置文件目录
│   └── translate_prompt.md # AI提示词模板
├── requirements.txt        # Python依赖包列表
├── test_curl.sh            # API测试脚本
├── Dockerfile              # Docker镜像构建文件
└── docker-compose.yml      # Docker Compose配置
```

## 环境要求

- Python 3.8+
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
   ```

## 使用方法

### 方式一：命令行模式

运行命令行交互程序：

```bash
python main.py
```

程序会提示你输入目标语言和需要翻译的文本，输入 `/q` 退出程序。

### 方式二：API 服务

#### 启动 API 服务

```bash
python api.py
```

默认监听端口为 6003。

#### Docker 部署

使用 Docker Compose 快速启动服务：

```bash
# 创建 .env 文件并配置环境变量
echo "OPENAI_API_KEY=your-api-key" > .env
echo "OPENAI_BASE_URL=your-base-url" >> .env

# 启动服务
docker-compose up -d
```

或使用 Docker 直接构建和运行：

```bash
# 构建镜像
docker build -t ai-translator .

# 运行容器
docker run -d -p 6003:6003 \
  -e OPENAI_API_KEY="your-api-key" \
  -e OPENAI_BASE_URL="your-base-url" \
  ai-translator
```

### API 接口说明

#### 1. 健康检查
```
GET /
```
返回示例：
```json
{
  "message": "AI Translate API is running"
}
```

#### 2. 健康状态检查
```
GET /health
```
返回示例：
```json
{
  "status": "healthy",
  "service": "AI Translate API"
}
```

#### 3. 获取支持的模型信息
```
GET /api/models
```

#### 4. 翻译文本
```
POST /api/translate
```
请求体：
```json
{
  "text": "需要翻译的文本",
  "dst_lang": "English"
}
```
响应示例：
```json
{
  "success": true,
  "content": "翻译结果"
}
```

参数说明：
- `text` (必填): 需要翻译的文本内容
- `dst_lang` (可选): 目标语言，默认为 "English"

### 测试脚本

项目提供了 cURL 测试脚本，可直接运行进行功能测试：

```bash
chmod +x test_curl.sh
./test_curl.sh
```

测试脚本包含以下测试用例：
1. 根路径访问测试
2. 健康检查测试
3. 模型信息获取测试
4. 中文翻译为英文测试
5. 英文翻译为中文测试
6. 空内容错误测试
7. 长文本翻译测试

## 配置说明

### AI 提示词模板 (`config/translate_prompt.md`)

定义了 AI 翻译代理的角色和行为规则。模板中的 `{{dst_lang}}` 占位符会在运行时被替换为实际的目标语言。

## 使用示例

### 命令行示例

```bash
$ python main.py
选择翻译的目标语言: English
输入需要翻译的文本: 你好，世界！
Hello, World!
输入需要翻译的文本: /q
```

### API 调用示例

使用 cURL：
```bash
curl -X POST "http://localhost:6003/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "你好，世界！",
    "dst_lang": "English"
  }'
```

使用 Python requests：
```python
import requests

response = requests.post(
    "http://localhost:6003/api/translate",
    json={
        "text": "你好，世界！",
        "dst_lang": "English"
    }
)
print(response.json())
```

## 技术栈

- **FastAPI**: 现代化的 Python Web 框架，提供高性能的 API 服务
- **OpenAI SDK**: 用于调用 OpenAI 兼容的 AI 模型 API
- **Uvicorn**: 轻量级 ASGI 服务器
- **Docker**: 容器化部署方案

## 注意事项

1. 请确保 API 密钥和基础 URL 配置正确
2. 在生产环境中，建议限制 CORS 允许的具体域名
3. 翻译质量取决于所使用的 AI 模型
4. 长文本翻译可能需要较长处理时间
