from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from translate_agent import OpenAIAgent


app = FastAPI(
    title="AI Translate API",
    description="基于 AI 的翻译服务",
    version="1.0.0"
)

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该限制具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求模型
class TranslateRequest(BaseModel):
    text: str
    dst_lang: str = "English"  # 目标语言，默认为英语

# 响应模型
class TranslateResponse(BaseModel):
    success: bool
    content: str

# 健康检查端点
@app.get("/")
def root():
    return {"message": "AI Translate API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AI Translate API"}

# 生成会议纪要（同步接口）
@app.post("/api/translate", response_model=TranslateResponse)
def create_translate(request: TranslateRequest):
    """同步翻译"""
    try:
        # 验证输入
        if not request.text or not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="翻译内容不能为空"
            )

        # 初始化 AI 代理
        agent = OpenAIAgent(dst_lang=request.dst_lang)

        # 直接调用翻译
        result = agent.translate(request.text)

        # 返回结果
        return TranslateResponse(
            success=True,
            content=result,
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"翻译时发生错误: {str(e)}"
        )

# 获取支持的模型信息
@app.get("/api/models")
def get_models():
    return {
        "models": [
            {
                "name": "qwen3-30b-a3b-instruct-2507",
                "description": "通义千问3-30B 指令模型"
            }
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6003)
