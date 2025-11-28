from fastapi import FastAPI, HTTPException, Form
from fastapi.middleware.cors import CORSMiddleware

from translator import translate


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

# 健康检查端点
@app.get("/")
def root():
    return {"message": "AI Translate API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AI Translate API"}

# 翻译接口
@app.post("/api/translate")
def create_translate(text: str = Form(...), dst_lang: str = Form("English")):
    """同步翻译"""
    try:
        # 验证输入
        if not text or not text.strip():
            raise HTTPException(
                status_code=400,
                detail="翻译内容不能为空"
            )

        # 直接调用翻译
        translation_result = translate(text, dst_lang)

        # 返回结果
        return {"content": translation_result}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"翻译时发生错误: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6003)
